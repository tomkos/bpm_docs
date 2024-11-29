<!-- image -->

# Creating a caller part for the request message

## Before you begin

## About this task

## Procedure

1 If the module deployment editor is closed, open it by completingthe following steps:
    1. In the Business Integration view,
select the module that contains your web services export.
    2. Right-click the selected module and select Open Deployment Editor. The module deployment editor
opens.
2. Click the Design tab.
3. Select the node for your export. For example, receiveWebServiceCallFromClient
has a ServerInterfaceExport1\_ServerInterfaceHttpService web service
description extension, and a receiveWebServiceCallFromClient\_ServerInterfaceHttpPort
port component binding.
4. Select the Web Services Exports node.
5. Click Add and select Web Services Security Extensions. The Web Services Security
Extensions node is added under the Web Services Exports node.
6. Select the Web Services Security Extensions node.
7. Click Add and select Web Service Description Extension. The Select a Web Service
Export window appears.
8. In the window, select your web service export. For example,
receiveWebServiceCallFromClient.
9. Select the Port Component Binding node that was added.
10. Click Add and select Server Service Configuration. The Server Service Configuration
node is added under Port Component Binding.
11. Select the Server Service Configuration node.
12. Click Add and select Request Consumer Service Configuration Details. The Request
Consumer Service Configuration Details node is added under Server
Service Configuration. (For example, receiveWebServiceCallFromClient has a ServerInterfaceExport1\_ServerInterfaceHttpService web service description extension and a receiveWebServiceCallFromClient\_ServerInterfaceHttpPort port component binding.)
13. Select the Request Consumer Service Configuration
Details node.
14. Click Add and select Caller Part. The Select a Token Type window appears.
15. In the window, select Username Token. A Caller Part node is added under Request Consumer Service Configuration
Details.
16. In the Name field, type a name for
the new caller part. For example, basicAuth.
17. Press Ctrl-S to save your changes.

## What to do next