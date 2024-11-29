# How a custom command line application obtains an access token from UMS SSO

## Understanding the Resource Owner Password Credential flow

In the Resource Owner Password Credentials flow, resource owner credentials, such as username and
password, are used directly to obtain an access\_token. The custom command line
application therefore initially needs to obtain credentials from the resource owner (the end user).
It can then invoke UMS SSO, authenticate as a registered client application and exchange the user's
username and password combination for an access\_token. This flow can also be used
with client types other than command line, but this is the most typical usage scenario.

## Design considerations for the custom command line application

1 The custom command line application must register with UMS SSO as an OIDC Relying Party, for example:curl -v -k -s -X POST -H "Content-Type:application/json" -u "umsadmin:passw0rd " -d @- "https://<ums-host>/oidc/endpoint/ums/registration" <<+++{ "scope": "openid", "preauthorized\_scope": "openid", "introspect\_tokens": true, "client\_id": "customApp ", "client\_secret": "passw0rd", "client\_name": "customApp ", "grant\_types": ["password"], "response\_types": [ "token"]}+++ Where

```
curl -v -k -s -X POST -H "Content-Type:application/json" -u "umsadmin:passw0rd" -d @- "https://<ums-host>/oidc/endpoint/ums/registration" <<+++
{
  "scope": "openid",
  "preauthorized\_scope": "openid",
  "introspect\_tokens": true,
  "client\_id": "customApp",
  "client\_secret": "passw0rd",
  "client\_name": "customApp",
  "grant\_types": ["password"],
  "response\_types": [ "token"]
}
+++
```

    - passw0rd is an example client\_secret to authenticate as the
custom command line application to UMS - make sure that you use a much stronger secret
    - customApp  is a human-readable identifier for your custom
command line application
    - grant\_types must be set to “password”
    - response\_types must be set to “token”
2 Then the app can obtain an access token. Forexample:curl -k -X POST -u "customApp :passw0rd " -d "grant\_type=password&scope=openid&username=user\_name &password=user\_password " "https://ums-host /oidc/endpoint/ums/token" Where The response contains the access token, access\_token , forexample:{ "access\_token": "uEsdnucnBtjt8llTYQDqKHxcPF7a06YLX1IbzQH8", "token\_type": "Bearer", "expires\_in": 7199, "scope": "openid"}

```
curl -k -X POST -u "customApp:passw0rd" -d "grant\_type=password&scope=openid&username=user\_name&password=user\_password" "https://ums-host/oidc/endpoint/ums/token"
```

- option -u "customApp:passw0rd" is used by
the client to authenticate with UMS, it is the combination of the values for
client\_id and client\_secret that you registered in the previous
step.
- grant\_type must be set to "password".
- user\_name and
user\_password are the credentials of the resource owner user
name for whom the access token is being requested.
- ums-host is the hostname of the UMS server.

```
{
  "access\_token": "uEsdnucnBtjt8llTYQDqKHxcPF7a06YLX1IbzQH8",
  "token\_type": "Bearer",
  "expires\_in": 7199,
  "scope": "openid"
}
```

3. The custom command line application uses the access\_token in the authorization
header of the request to invoke the OAuth 2.0 protected REST API. For
example:curl -k -s -H "Authorization: Bearer $access\_token" https://my.server:9443/rest/bpm/wle/v1/user/current