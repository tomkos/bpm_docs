<!-- image -->

# Adding JAX-RPC handlers for web service imports

## About this task

## Procedure

1. In the Business Integration view,
select the module that contains your web services import.
2. Right-click the selected module and select Open
Deployment Editor. The module deployment editor opens.
3. Click the Design tab.
4. Select the Web Services Imports node.
5. Click Add and select Web Services Import. A web service import node is added
under Web Services Imports.
6. Set the Name field of the web service
import node to your web service import, for example, sendWebServiceCallToServer.
7. Select the Web Service Import node.
8. Click Add and select JAX-RPC Handlers. A JAX-RPC Handlers and a JAX-RPC Handler
node are added under Web Service Import.
9. Select the JAX-RPC Handler node.
10. In the Display name field, type
the name that you want to assign to the display. For example, WSImportHandler.
11. In the Description field, type a
description for the new JAX-RPC handler. For example, JAX-RPC
handler for the sendWebServiceCallToServer import.
12. In the Handler name field, type
the name that you want to assign to the new JAX-RPC handler. For example, WSImportHandler.
13. Beside the Handler class field,
click Browse and select your handler class.
For example, com.ibm.test.li536.rpc.WSImportHandler.
14. Click OK to close the New Handler
window.
15. Add Initial Parameter and SOAP Header nodes as needed under
the JAX-RPC Handler node.
16. Press Ctrl-S to save your changes
and then close the module deployment editor.
17. If your server is already running in the Servers view,
click the Build Activities tab to open the
Build Activities view and then click Update Running Servers.