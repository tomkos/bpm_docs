# Configuring authentication for a REST API 3.0 service

## About this task

Add authentication to your component by completing the following steps.

## Procedure

1. Log in to the WebSphere administrative Console with admin
credentials.
2. Go to Security > Global security > Java Authentication and
Authorization Service > J2C authentication data.
3 Add an authentication alias for either Basic orAPIKey authentication: Make sure to include valid credentials:
    - For APIKey authentication : provide the API key name in the
UserID field and the API key in the Password
field.
    - For Basic authentication : provide the username at the
UserID section and the password in the Password
section.
4 Go to the advanced configuration section in theProperties view of the REST Outbound Component toconfigure the REST outbound component:

1. Go to the Security tab, select Authentication
Type, and choose the authentication type (Basic or
APIKey).
2. Enter manually the authentication alias set in step 3, or add it from your IBM Workflow
Server.
5. Optional: You can configure the authentication alias for each bound method
from the Method Bindings tab in the Properties view of
the Security section.