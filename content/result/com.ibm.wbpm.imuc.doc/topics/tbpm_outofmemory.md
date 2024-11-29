# Recovering from an out of memory exception while installing  desktop Process Designer
(deprecated)

## Procedure

If you encounter an out of memory exception after clicking Download Process Designer from
the Workflow Center,
follow these steps to resolve the problem.

1. Restart the Workflow Center.
2. In the Administrative console, set a web container custom
property by selecting Servers > Server Types > WebSphere application
servers > server\_name > Web Container Settings > Web container > Custom Properties.
3. Define the property com.ibm.ws.webcontainer.channelwritetype and
set the value to sync.
4. Save your changes.
5. Stop, then restart, the Workflow Center.
6. Again, click Download Process Designer from
the Workflow Center.

## Results