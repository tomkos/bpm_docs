# How a Liberty-based application obtains an access token from UMS SSO

## Understanding the Authorization code flow

1. The user’s browser has attempted to access a protected resource on the RP and is redirected to
the OP (UMS SSO), including values for client\_id and redirect\_url
as registered.
2. The user authenticates.
3. The OP redirects back to the RP, including an authorization code.
4. The RP sends the authorization code and client credentials using a back-channel
communication.
5. The OP responds with id\_token, refresh\_token,
access\_token.

## Design Considerations for the custom app

1 Register the Liberty server as an OIDC client with UMS SSO. For example:curl -k -s -X POST -H "Content-Type:application/json" -u "umsadmin:passw0rd" -d @- "https://ums-host/oidc/endpoint/ums/registration" <<+++ | jq '.'{ "scope": "openid profile", "preauthorized\_scope": "openid profile", "introspect\_tokens": true, "client\_id": "liberty", "client\_secret": "liberty-secret", "client\_name": "liberty", "redirect\_uris": [ "https://liberty-host:10001/oidcclient/redirect/umsClient" ]}+++ Where Note: If you omit the optional client\_id and client\_secret parameters, random values are generated and returned in the registration response.

```
curl -k -s -X POST -H "Content-Type:application/json" -u "umsadmin:passw0rd" -d @- "https://ums-host/oidc/endpoint/ums/registration" <<+++ | jq '.'
{
   "scope": "openid profile",
   "preauthorized\_scope": "openid profile",
   "introspect\_tokens": true,
   "client\_id": "liberty",
   "client\_secret": "liberty-secret",
   "client\_name": "liberty",
   "redirect\_uris": [
      "https://liberty-host:10001/oidcclient/redirect/umsClient"
   ]
}
+++
```

    - -u "umsadmin:passw0rd": The user and password used by the client to
authenticate with UMS SSO.
    - Optional: "client\_id": "liberty" corresponds to the configuration in the
server.xml configuration file.
    - Optional: "client\_secret": "liberty-secret" corresponds to the configuration in
the server.xml configuration file.
    - "redirect\_uris" are the URIs to which the user (and the authorization code) are
redirected upon successful authentication. This must match one of the redirect URIs that were
specified when the custom application registered with UMS SSO.
    - "scope": "openid profile" are the scopes that are represented by the access
token, access\_token, that is included in the final response to the authentication
request. The openid scope is required to complete the flow. The
profile scope should allow calling the UserInfo endpoint.
Additional scopes are possible and depend on the application(s) where the token will be used.
2. Extend the Liberty server configuration in
wlp/usr/servers/server\_Name/server.xml to configure your UMS
host name and port number. Choose a clientId and a clientSecret
and add them to the
configuration.<variable name="ums\_prefix" value="https://<ums-host>" />

<openidConnectClient id="umsClient"
  authorizationEndpointUrl="${ums\_prefix}/oidc/endpoint/ums/authorize"
  clientId="liberty"
  clientSecret="liberty-secret"
  tokenEndpointUrl="${ums\_prefix}/oidc/endpoint/ums/token"
  validationEndpointUrl="${ums\_prefix}/oidc/endpoint/ums/introspect"
  validationEndpointUrl="${ums\_prefix}/oidc/endpoint/ums/userinfo"
  userInfoEndpointEnabled="true"
  userInfoEndpointUrl="${ums\_prefix}/oidc/endpoint/ums/userinfo"
  validationMethod="userinfo"
  inboundPropagation="supported"
  signatureAlgorithm="RS256"
  jwkEndpointUrl="${ums\_prefix}/oidc/endpoint/ums/jwk">
</openidConnectClient>
3 When an end user attempts to access a protected resource on the RP without having an establishedauthenticated session, the RP redirects the user's browser to the UMS authorization endpointhttps://ums-host/oidc/endpoint/ums/authorize?response\_type=code&client\_id=liberty&state=001558899960297TBjhvTZSn&redirect\_uri=https%3A%2F%2Fliberty-host%3A10001%2Foidcclient%2Fredirect%2FumsClient&scope=openid+profile .In the Authorization flow, the request to handle delegated authentication contains the following parameters:

- response\_type=code indicates the authorization code flow.
- client\_id=liberty corresponds to the configuration in the
server.xmlconfiguration file.
- state=random\_number a nonce that the RP can use later to
validate that an invocation belongs to a flow that it triggered.
- redirect\_uri specifies the URI to which the user (and the authorization code)
are redirected upon successful authentication. This must match one of the redirect URIs that were
specified when the custom application registered with UMS.
- scope=openid+profile specify the scopes that are represented by the access
token, access\_token, that is included in the final response to the authentication
request. The openid scope is required to complete the flow. The
profile scope should allow calling the UserInfo endpoint.
Additional scopes are possible and depend on the application(s) where the token will be used.
4. The request returns an authorization code. The Liberty server application can call the UMS SSO
token endpoint to exchange the authorization code for access\_token,
refresh\_token, and  id\_token.UMS SSO provides all three tokens
if the token endpoint is invoked with a valid recent authorization code and a matching
client\_id and client\_secret for the client that requested
authentication.
5 The Liberty server application can now establish an authenticated session based on theinformation in the id\_token . Several configurations are possible:

- The default is to use all information from the id\_token to create a security
context.
- Use just the user name from the id\_token and create a security context with
information that is found in the locally configured user registry for that user name.
- Perform some sort of identity mapping. For example, the id\_token might contain
an email address that represents the user, but the RP creates a security context for the employee
serial number, which might be contained in some other claim of the id\_token.