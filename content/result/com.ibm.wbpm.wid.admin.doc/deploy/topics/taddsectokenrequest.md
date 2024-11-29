<!-- image -->

# Creating a security token for the request message

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web services import.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4. Select the Web Services Imports node.
5. Click Add and select Web Services Client Security Extensions and click OK. The Web Services Client Security Extensions node
is added under Web Services Imports. The Component Scoped Reference
node is added under the Web Services Client Security Extensions node.
6. Select the Component Scoped Reference node.
7. Click Add and select Service Reference. The Select a Web Service Import window
appears.
8. In the window, select your web service import. For example,
sendWebServiceCallToServer.
9. Select the Port Qualified Name Binding node that was added.
10. Click Add and select Client Service Configuration. The Client Service Configuration
node is added under Port Qualified Name Binding.
11. Select the Client Service Configuration node.
12. Click Add and select Request Generator Configuration. The Request Generator
Configuration node is added under Client Service Configuration.
13. Select the Request Generator Configuration node.
14. Click Add and select Security Token. The Select a Token Type window appears.
15. In the window, select Username Token. A Security Token node is added under Request Generator Configuration.
16. Select the Security Token node.
17. In the Name field, type a name for
the new security token. For example, basicAuth.
18. Leave the URI field blank. No URI
value is required for a username token.
19. Press Ctrl-S to save your changes.

## What to do next