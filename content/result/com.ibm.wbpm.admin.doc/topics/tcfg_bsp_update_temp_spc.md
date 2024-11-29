# Heritage Process Portal or
dashboard theme fails to load

## About this task

## Procedure

- If IBM® Business Automation Workflow isconfigured in a cluster, perform the following steps:
    1 Identify the custom profile for oobLoadedStatusproperties file:
        1. In deployment manager profile, open the deployment\_manager\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties file.
        2. Look for the name of cell, node and server in the com.ibm.mashups.directory.templates or com.ibm.mashups.directory.spaces properties. For
example, in com.ibm.mashups.directory.templates = config/cells/Cell01/nodes/Node01/servers/Server1/mm/templates,
you can locate the custom profile by the Cell01 cell
name and the Node01 node name.
        3. Use the name of cell, node and server to locate the custom profile.
2. In the custom profile, open the custom\_profile\_root\BusinessSpace\cluster\_name\mm.runtime.prof\public\oobLoadedStatus.properties file
and update the importTemplates.txt or importSpaces.txt properties:
importTemplates.txt=true
importSpaces.txt=trueIf you have created the Business
Space database after it was deleted, or if you need to reload the
theme for any other reason, also update the following property:importThemes.txt=true
3 Resynchronize the custom profile.
    1. Open the administrative console and click System
administration > Nodes.
    2. Click Full Resynchronize.
4. Restart the cluster.
- If IBM Business Automation Workflow isconfigured in a managed server, perform the following steps:

1. In the custom profile where the managed server is located,
open the custom\_profile\_root\BusinessSpace\node\_name\server\_name\mm.runtime.prof\public\oobLoadedStatus.properties file
and update the importTemplates.txt or importSpaces.txt properties:
importTemplates.txt=true
importSpaces.txt=trueIf you have created the Business
Space database after it was deleted, or if you need to reload the
theme for any other reason, also update the following property:importThemes.txt=true
2 Resynchronize the custom profile.
    1. Open the administrative console and click System
administration > Nodes.
    2. Click Full Resynchronize.
3. Restart the server.