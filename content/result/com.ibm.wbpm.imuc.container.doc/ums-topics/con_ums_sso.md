# Invoking OAuth 2.0 protected APIs

The following topics describe how different types of applications can use appropriate OAuth 2.0
authorization flows to obtain an access token.

- How a custom command line application obtains an access token from UMS SSO

 Containers: 
Because a custom command line application cannot redirect a user to a browser UI for authentication, such applications can use the Resource Owner Password Credentials flow to obtain an access token from User Management Service (UMS) single sign-on (SSO) that can be used to invoke an OAuth 2.0 protected REST API.
- How a browser or mobile application obtains an access token from UMS

 Containers: 
A browser or mobile application can use the Implicit flow to obtain an access token from User Management Service (UMS) single-sign-on (SSO) that can be used to invoke an OAuth 2.0 protected REST API.
- How a Liberty-based application obtains an access token from UMS SSO

 Containers: 
A Liberty-based application can use the Authorization Code flow to act as an OIDC Relying Party (RP) to delegate authentication to UMS single sign-on (SSO), which acts as an OIDC Offering Party (OP).
- Using long-lived access tokens

 Containers: 
If it is inconvenient for your programmatic clients that the User Management Service (UMS) access\_token tokens have a default validity of two hours, you can exchange an access\_token for an app\_token that is valid for 366 days.