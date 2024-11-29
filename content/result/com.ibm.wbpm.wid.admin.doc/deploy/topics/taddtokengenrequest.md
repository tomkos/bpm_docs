<!-- image -->

# Creating a token generator for the request message

## Before you begin

## About this task

## Procedure

1 If the module deployment editor is closed, open it by completingthe following steps:
    1. In the Business Integration view,
select the module that contains your web services import.
    2. Right-click the selected module and select Open Deployment Editor. The module deployment editor
opens.
2. Click the Design tab.
3. Select the Web Services Imports node.
4. Click Add and select Web Services Client Binding Configurations. The Web Services
Client Binding Configurations node is added under Web Services Imports
and the Component Scoped Reference node is added under the Web Services
Client Binding Configurations node.
5. Select the Component Scoped Reference node.
6. Click Add and select Service Reference. The Select a Web Service Import window
appears.
7. In the window, select your web service import. For example,
sendWebServiceCallToServer.
8. Select the Port Qualified Name Binding node that was added.
9. Click Add and select Security Request Generator Binding Configuration. The
Security Request Generator Binding Configuration node is added under
Port Qualified Name Binding.
10. Select the Security Request Generator Binding
Configuration node.
11. Click Add button and select Token Generator. A Token Generator node is added under
Security Request Generator Binding Configuration.
12. Select the Token Generator node.
13. In the Token generator name field,
type a name for the new token generator. For example, basicAuthToken.
14. In the Token generator class field,
ensure that the following token generator class is selected: com.ibm.wsspi.wssecurity.token.UsernameTokenGenerator.
15. Select the Part Reference node under
the Token Generator node.
16. In the Security token field, select basicAuth. This is the name of the security token that
you created earlier under the import extensions of the module deployment
editor.
17. Select the Token Generator node,
then press Add and select Use Value
Type. The Select a Token Type window appears.
18. In the window, select Username Token. The Use Value Type node is added under Token Generator.
19. Select the Callback Handler node
under the Token Generator node.
20. In the Callback handler class drop-down
list, ensure that the following callback handler class is selected: com.ibm.wsspi.wssecurity.auth.callback.NonPromptCallbackHandler. You use the call back handler to manually specify a user ID and
password in the token generator configuration.
21. In the User ID and Password fields under the Basic Authentication subsection,
specify the user ID and password for the client. For example, if you
are using the default security settings of IBM® Integration
Designer, you would type admin as both the user ID
and password.  Tip: You can also set your user
ID and password to match the user ID and password of Business Automation Workflow.
22. Press Ctrl-S to save your changes.

## What to do next