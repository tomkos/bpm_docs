<!-- image -->

# Creating a required security token for the request message

## Before you begin

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web services export.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4. Select the Web Services Exports node.
5. Click Add and select Web Services Security Extensions. The Web Services Security
Extensions node is added under the Web Services Exports node.
6. Select the Web Services Security Extensions node.
7. Click Add and select Web Service Description Extension. The Select a Web Service
Export window appears.
8. In the window, select your web service export, for example,
receiveWebServiceCallFromClient.
9. Select the Port Component Binding node that was added.
10. Click Add and select Server Service Configuration. The Server Service Configuration
node is added under Port Component Binding.
11. Select the Server Service Configuration node.
12. Click Add and select Request Consumer Service Configuration Details. The Request
Consumer Service Configuration Details node is added under Server
Service Configuration.
13. Select the Request Consumer Service Configuration
Details node.
14. Click Add and select Required Security Token. The Select a Token Type window
appears.
15. In the window, select Username Token. A Required Security Token node is added under Request Consumer
Service Configuration Details.
16. Select the Required Security Token node.
17. In the Name field, type a name for
the new required security token. For example, reqUNToken.
18. Leave the Namespace URI field blank.
No URI value is required for a username token.
19. In the Usage type drop-down list,
select Required. The Required usage type will
cause a SOAP fault to be thrown whenever a required security token
is not included in the import's request message.
20. Press Ctrl-S to save your changes.

## What to do next