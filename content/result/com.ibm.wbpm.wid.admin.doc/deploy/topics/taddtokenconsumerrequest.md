<!-- image -->

# Creating a token consumer for the request message

## About this task

## Procedure

1 If the module deployment editor is closed, open it by completingthe following steps:
    1. In the Business Integration view,
select the module that contains your web services export.
    2. Right-click the selected module and select Open Deployment Editor. The module deployment editor
opens.
2. Click the Design tab.
3. Select the Web Services Exports node.
4. Click Add and select Web Services Binding Configurations. The Web Services
Binding Configurations node is added immediately after Web Service Exports.
5. Select the Web Services Binding Configurations node.
6. Click Add and select Web Service Description Binding. The Select a Web Service
Export window appears.
7. In the window, select your web service export. For example,
receiveWebServiceCallFromClient.
8. Select the Port Component Binding node that was added.
9. Click Add and select Request Consumer Binding Configuration Details. The Request
Consumer Binding Configuration Details node is added under Port Component
Binding.
10. Select the Request Consumer Binding Configuration
Details node.
11. Click Add and select Token Consumer. A Token Consumer node is added under
Request Consumer Binding Configuration Details.
12. Select the Token Consumer node.
13. In the Token consumer name field,
type a name for the new token consumer. For example, con\_UNtcon.
14. In the Token consumer class field,
ensure that the com.ibm.wsspi.wssecurity.token.UsernameTokenConsumer class is selected.
15. Select the Token Consumer node.
16. Click Add and select Part Reference. The Part Reference node is added under
Token Consumer.
17. In the Security token field, select
the security token that you created under the extensions. For example,
reqUNToken.
18. Select the Token Consumer node.
19. Click Add and select Use Value Type. The Select a Token Type window appears.
20. In the window, select Username Token. A Use Value Type node is added under Token Consumer.
21. Select the Token Consumer node.
22. Click Add and select Use jaas.config to have the security token in the import's
request message validated. The Use jaas.config node is added under
Token Consumer.
23. In the jaas.config name field, type system.wssecurity.UsernameToken. This is the default
JAAS configuration name for username tokens and it causes a username
token to be validated with a user name and password.
24. Press Ctrl-S to save your changes.

## What to do next