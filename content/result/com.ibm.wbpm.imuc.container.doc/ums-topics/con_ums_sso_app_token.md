# Using long-lived access tokens

## Understanding app tokens

App tokens were introduced to support enforcing multi-factor authentication (MFA) for command
line clients. Because Liberty does not support MFA natively, it is expected that authentication is
delegated further to an existing identity provider that supports MFA. Therefore, the client should
use the browser-based implicit flow to obtain an initial
access\_token, which is then exchanged for an app\_token that has a
much longer validity.

## Design considerations for the custom app

1 The custom application must register with UMS SSO, specifying the implicit grant\_type and token response\_type . For clarity and convenience, in the following examples, the UMSadmin credentials are stored in the environment variables umsuser andumspassword and localhost:9443 are used for the UMS host and port:
    1. Create a new file named json.txt with content similar to the following,
substituting your values where
necessary:{
  "scope": "openid",
  "preauthorized\_scope": "openid",
  "introspect\_tokens": true,
  "response\_types": ["token"],
  "grant\_types": ["implicit"],
  "redirect\_uris": [ "http://192.168.99.100:8080", "myapp://token" ],
  "appTokenAllowed": true  
}
    2. Run the following
commands:umsuser=umsadmin
umspassword=passw0rd
curl -k -s -X POST -H "Content-Type:application/json" -u "$umsuser:$umspassword" -d @json.txt "https://localhost:9443/oidc/endpoint/ums/registration"Example
response:{
    "client\_id\_issued\_at": 1572602365,
    "registration\_client\_uri": "https://localhost:9443/oidc/endpoint/ums/registration/1657e00324474d8b9fbe637b0883515d",
    "client\_secret\_expires\_at": 0,
    "token\_endpoint\_auth\_method": "client\_secret\_basic",
    "scope": "openid",
    "grant\_types": ["implicit"],
    "response\_types": ["token"],
    "application\_type": "web",
    "preauthorized\_scope": "openid",
    "introspect\_tokens": true,
    "resource\_ids": [],
    "proofKeyForCodeExchange": false,
    "publicClient": false,
    "appPasswordAllowed": false,
    "appTokenAllowed": true,
    "hash\_itr": 0,
    "hash\_len": 0,
    "client\_id": "1657e00324474d8b9fbe637b0883515d",
    "client\_secret": "5a8pw7rQWN3VeKGcfvsIs039zHHrmiliprDAVKlLvbK9yrnhHgOulvKpbLgN",
    "client\_name": "1657e00324474d8b9fbe637b0883515d",
    "redirect\_uris": ["http://192.168.99.100:8080", "myapp://token"],
    "allow\_regexp\_redirects": false
}
    3. Note the values for client\_id and client\_secret. For
demonstration purposes, you might store them in environment
variables:clientid=1657e00324474d8b9fbe637b0883515d
clientsecret=5a8pw7rQWN3VeKGcfvsIs039zHHrmiliprDAVKlLvbK9yrnhHgOulvKpbLgN
2 The app obtains a short-lived access token. If UMS is not configured to delegate authenticationfurther, we can use basic authorization, forexample:curl -k -s -v -u "$umsuser:$umspassword" 'https://localhost:9443/oidc/endpoint/ums/authorize?response\_type=token&client\_id=$clientid&scope=openid&state=none&redirect\_uri=myapp://token' Where The 302 redirect response will contain an HTTP response header location that is pointing tothe registered and requested location (myapp://token) with an appended fragment that includes amongother things your access\_token , forexample: location: myapp://token#scope=openid&access\_token=C87wJE2Mst7DEdBJMfV9Rw6I8RUlZ9bilITmZqhK&token\_type=Bearer&expires\_in=7199&state=none Theshort-lived access\_token isC87wJE2Mst7DEdBJMfV9Rw6I8RUlZ9bilITmZqhK expires in 7199 seconds.

```
curl -k -s -v -u "$umsuser:$umspassword" 'https://localhost:9443/oidc/endpoint/ums/authorize?response\_type=token&client\_id=$clientid&scope=openid&state=none&redirect\_uri=myapp://token'
```

- response\_type=token indicates that the app wants an access token (not an id
token).
- client\_id=$clientid identifies itself so that the authorization server can
verify that the redirect\_uri is in the preregistered whitelist and that it can include the client\_id
in the token information.
- scope=openid is required.
- state=none is a short-cut in this example. You can use this parameter to help
re-establishing the context, for example, if the browser app had saved some parameters in HTML5
session storage or to make sure that the client actually sent the user to the authorization
server.
- redirect\_uri the URI to come back to after the user authenticated and gave
consent (depending on scopes).

The 302 redirect response will contain an HTTP response header location that is pointing to
the registered and requested location (myapp://token) with an appended fragment that includes among
other things your access\_token, for
example:

```
location: myapp://token#scope=openid&access\_token=C87wJE2Mst7DEdBJMfV9Rw6I8RUlZ9bilITmZqhK&token\_type=Bearer&expires\_in=7199&state=none
```

3. Exchange the access\_token for long-lived app\_token by using
the access token to call the UMS app-tokens endpoint. For
example:curl -k -X POST -u "$clientid:$clientsecret" -d "app\_name=myapp" -H "Accept: application/json" -H "access\_token: $accesstoken" "https://localhost:9443/oidc/endpoint/ums/app-tokens"The
response contains the app-token:
GGONoU7vG9uJ6jJQOwKO7nBouq9sB08WHiOLzv0qBO{
    "app\_token": "GGONoU7vG9uJ6jJQOwKO7nBouq9sB08WHiOLzv0qBO",
    "app\_id": "Lk088OmmPgwAmglhR4skWd4OzKmYT4nprrR4xR3e",
    "created\_at": "1572603852658",
    "expires\_at": "1580379852658"
}For
demonstration purposes, you might store the token in an environment
variable:apptoken=GGONoU7vG9uJ6jJQOwKO7nBouq9sB08WHiOLzv0qBOTip: You can set the following lifetimes and limits for app tokens and app passwords in the custom
resource file: 
ums\_configuration.oauth.app\_token\_lifetime
The lifetime of app tokens. The default is 366d.
ums\_configuration.oauth.app\_password\_lifetime
The lifetime of app passwords. The default is 366d.
ums\_configuration.oauth.app\_token\_or\_password\_limit
The maximum number of app tokens or app passwords per client. The default is 100.
4. Use the app\_token just like any other access\_token to invoke
an API. for
example:curl -k -s -H "Authorization: Bearer $apptoken" https://sample-host/rest/bpm/wle/v1/user/current