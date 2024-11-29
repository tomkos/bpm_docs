# Completing configuration for Business Space

If you customized the Business Space component in the source environment,
you must perform some additional tasks for the Business Space component after you migrate to the new
version of IBM Business Automation Workflow, before you start your clusters
and use Heritage Process Portal.

Figure 1. Sample environment after the target is
started. The source environment is not running. The target can read
from the databases.

<!-- image -->

<!-- image -->

## Procedure

1. If there are custom widgets in the source environment, you must
migrate your custom widgets used in Heritage Process Portal spaces to work in the
new version of IBM Business Automation Workflow. 
See Migrating custom widgets.
2. Configure the REST endpoints for widgets if they are not present in
the target environment.  See Widget support for BPDs, BPEL processes, and human tasks and
Configuring the Business Space component and registering REST endpoints on the administrative console.
3. If you modified the Business Space Ajax proxy
in the source environment, make the same changes in the target environment.
See Configuring the Business Space Ajax proxy.
4 If you modified the mashups configurationin the source environment, make the same changes in the target environment:
    1 Copy the ConfigService.properties filefrom the previous version into an empty folder on your system. The file is in one of the following locations:
        - (cluster) deployment\_manager\_profile\BusinessSpace\cluster\_name\mm.runtime.prof\config\ConfigService.properties
        - (stand-alone) profile\_name\BusinessSpace\node\_name\server\_name\mm.runtime.prof\config\ConfigService.properties
2 Run the updatePropertyConfig command.using the wsadmin scripting client. Important: Thevalue for the propertyFileName parameter mustbe the full path to the file, and all backslashes must be double,as shown in the following examples.
    - For a cluster:
        - The following example uses Jython:AdminTask.updatePropertyConfig('[-clusterName cluster\_name -propertyFileName
 "c:\\temp\\BPM\\config\\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
        - The following example uses Jacl:$AdminTask updatePropertyConfig {-clusterName cluster\_name -propertyFileName
 "c:\\temp\\BPM\\config\\ConfigService.properties" -prefix "Mashups\_"}
$AdminConfig save
- For a stand-alone server:
    - The following example uses Jython:AdminTask.updatePropertyConfig('[-serverName server\_name -nodeName node\_name 
-propertyFileName "c:\\temp\\BPM\\config\\ConfigService.properties" -prefix "Mashups\_"]')
AdminConfig.save()
    - The following example uses Jacl:$AdminTask updatePropertyConfig {-serverName server\_name -nodeName node\_name
 -propertyFileName "c:\\temp\\BPM\\config\\ConfigService.properties" -prefix "Mashups\_"}
$AdminConfig save
5. To avoid problems, do not add the Module Administration
and Module Assembly widgets to the same page.

## Related information

- Migrating custom widgets