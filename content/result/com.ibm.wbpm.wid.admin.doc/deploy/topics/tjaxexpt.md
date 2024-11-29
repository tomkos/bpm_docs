<!-- image -->

# Adding JAX-RPC handlers for web service exports

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web services export.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4. Select the Web Services Exports node.
5. Click Add and select Web Service Export. A Web Service Export node is added
beneath Web Services Exports.
6. Set the Name field of the Web Service
Export node to your web service export. For example, receiveWebServiceCallFromClient.
7. Select the Web Service Export node.
8. Click Add and select JAX-RPC Handlers. A JAX-RPC Handlers and a JAX-RPC Handler
node are added under Web Service Export.
9. Select the JAX-RPC Handler node.
10. In the Display name field, type
the name that you want to assign to the display. For example, WSExportHandler.
11. In the Handler name field, type
the name that you want to assign to the new JAX-RPC handler. For example, WSExportHandler.
12. Beside the Handler class field,
click Browse and select your handler class.
For example, com.ibm.test.li536.rpc.WSExportHandler.
13. In the Description field, type a
description for the new JAX-RPC handler. For example, JAX-RPC
handler for the receiveWebServiceCallFromClient export.
14. Add Initial Parameter, SOAP Header, and SOAP Role nodes
as needed under the JAX-RPC Handler node.
15. Press Ctrl-S to save your changes
and then close the module deployment editor.
16. If your server is already running in the Servers view,
click the Build Activities tab to open the
Build Activities view and then click Update Running Servers.