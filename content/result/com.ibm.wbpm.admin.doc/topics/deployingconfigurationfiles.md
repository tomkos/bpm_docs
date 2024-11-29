# Deploying a 100Custom.xml file to a deployment environment

## Before you begin

Create a 100Custom.xml file with the required changes. For more
information, see The 100Custom.xml file and configuration.

## Procedure

1. Determine the server\_type configuration scope to which you want to deploy
changes. The XML file contains changes to one of the three server types: process-server,
process-center, and performance-data-warehouse. This information is used to determine the path for
your 100Custom.xml file. For 3-cluster environments, the application cluster is
used for changes to the process-server and process-center server types. The support cluster is used
for changes to the performance-data-warehouse server type.
2 Use the updateBPMConfig command to automatically deploy changes to the100Custom.xml files. Alternatively, you can manually place the100Custom.xml files on the stand-alone server or the deployment manager. If you want to place your 100Custom.xml files in a stand-alone serverenvironment, place them in the following location: standalone\_profile\_root \config\cells\cell\_name \nodes\node\_name \servers\server\_name \server\_type \config\ If you want to place your 100Custom.xml files on the deployment manager,place them in the following locations (in the config directory of thedeployment manager profile): Note: Ensure that you are editing the 100Custom.xml configuration files in thedeployment manager profile. If you edit these configuration files in a managed node profile, thechanges will be lost in the next node synchronization. Also, if you are replacing an existing fileand need a backup, ensure that you modify the file extension as all files with a.xml file extension loads. For example, use the .bak fileextension instead of .xml .

If you want to place your 100Custom.xml files in a stand-alone server
environment, place them in the following location:

```
standalone\_profile\_root\config\cells\cell\_name\nodes\node\_name\servers\server\_name\server\_type\config\
```

If you want to place your 100Custom.xml files on the deployment manager,
place them in the following locations (in the config directory of the
deployment manager profile):

    - For each cluster
member:dmgr\_profile\_root\config\cells\cell\_name\nodes\node\_name\servers\cluster\_member\_name\server\_type\config\
    - For the appropriate
cluster:dmgr\_profile\_root\config\cells\cell\_name\clusters\cluster\_name\server\_type\config\Note: 
The cluster files are used during the creation of new cluster members and for certain administrative
commands that are running in local mode.
3. Synchronize the changes with the nodes or restart the node agents. After you confirm that all
the changes are synchronized with the nodes, restart the deployment environment to enable the
changes to take effect.
4. Review the TeamWorksConfiguration.running.xml file to confirm that the
changes are applied properly.