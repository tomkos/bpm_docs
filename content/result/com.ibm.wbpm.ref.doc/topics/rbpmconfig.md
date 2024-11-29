# BPMConfig command-line utility

## Syntax

```
BPMConfig [flags]

Deployment environment orchestration commands:
-create Create profiles, deployment environment configuration, database tables, or the SQL scripts for creating the required database tables.
-delete Delete profiles, deployment environments, and cluster members.

Configuration updating commands:
-update Update configuration including custom context root, data source, custom JDBC paths, virtual host, and network directory.

Deployment environment migration commands:
-upgrade Upgrade an existing Standard deployment environment to an Advanced deployment environment.
-migrate Migrate from an older product or version.

Deployment environment operation commands:
-export Export configuration properties from an existing deployment environment to an output configuration directory.
-validate Validate that the specified configuration properties file can be used to create a deployment environment.
-start Start the deployment environment.
-stop Stop the deployment environment.

Other commands:
-help Get help about any command.
```

## Description

You can use the BPMConfig command to create an Business Automation Workflow
deployment environment, instead of using the Deployment Environment wizard (see
Configuring a network deployment environment using the Deployment Environment wizard) in the WebSphere administrative console. You can also use the
BPMConfig command to create profiles for the deployment manager and managed
nodes, instead of using the Profile Management Tool or the manageprofiles
utility.

To supplement the BPMConfig command, an IBM Business Automation
Workflow Configuration editor
is provided that enables you to graphically edit a configuration properties file that is exported
from your source environment that uses the BPMConfig -export command. After you
modify the exported properties file in the editor, you can use the BPMConfig
-create command to create a new deployment environment that is based on the modified file.
Information about the IBM Business Automation
Workflow Configuration editor
is found in the topic Configuring your environment with the IBM Business Automation Workflow Configuration editor.

- Create new WebSphere® Application
Server profiles by using the command instead of creating them through the WebSphere Application
Server Profile
Management Tool
- Generate the SQL scripts that you can later use to create your database tables
- Add nodes or cluster members to an existing deployment environment
- Create a custom context root for the entire deployment environment or just for the Process
Portal component
- Update the configuration in the deployment environment, such as the
performance tuning properties, data source, or virtual host
- Upgrade a Standard
deployment environment to an Advanced
deployment environment
- Validate the configuration:
    - Validate the configuration status of an existing deployment environment
    - Test whether connections to the databases can be successfully established
    - Test the configuration settings in an existing configuration properties file
- Start and stop the deployment environment
- Export configuration properties and data:

- Export configuration properties of the deployment environment
- Export database information for performance analysis purposes
- Export system data for performance analysis purposes
- Migrate to a new environment based on the previous environment
- Delete one or more of the following entities:

- Profiles
- Deployment environments
- Nodes in deployment environments
- Cluster members
- Enable or disable content object support
- Display usage information for a specified parameter

```
install\_root/BPM/samples/config
```

If an error occurs while running the BPMConfig command, the command ends with
an error message that should help you diagnose and resolve the problem. Any messages that are
related to the running of the BPMConfig command are recorded in the following
file (where install\_root is the installation location of IBM Business Process
Manager):

Before V19.0.0.2:
install\_root/logs/config/BPMConfig\_time\_stamp.log

From V19.0.0.2:
install\_root/logs/config/BPMConfig\_action\_name\_profile\_name\_deployment\_environment\_name\_time\_stamp.log

Where action\_name is one of create, update,
upgrade, export, migrate,
validate, start, or stop. If the particular
BPMConfig action is associated with a profile name,
profile\_name, deployment environment name,
deployment\_environment\_name, or both, that information is also part of the file
name. For example, the output file for the command BPMConfig.sh -export Dmgr -de
De1PC would have the following output file name:
BPMConfig\_export\_Dmgr\_De1PC\_[timestamp].log. But if there are errors in the
command parameters, such as the action name, profile name, or deployment environment name, the
BPMConfig output log file has the following file name:
BPMConfig\_time\_stamp.log

```
WARNING: Could not open/create prefs root node Software\JavaSoft\Prefs at root 0x80000002
Windows RegCreateKeyEx(...) returned error code 5.
```

This
warning occurs because a non-administrative user does not have write
permissions on the Windows registry. The java.util.prefs.WindowsPreferences
utility attempts to save information in HKEY\_LOCAL\_MACHINE\Software\JavaSoft\Prefs instead
of under HKEY\_CURRENT\_USER\Software\JavaSoft\Prefs.
To prevent the warning from being issued in the future, log into Windows
as the administrator and create the key HKEY\_LOCAL\_MACHINE\Software\JavaSoft\Prefs.

## Parameters

If you run BPMConfig -create -de
properties\_file, you must run the command on the computer that has the
deployment manager profile and then run it on each computer that has a managed node. Both the
deployment environment and the profiles are created in a cell for those profiles that match the
values for the installPath and hostName properties that
are specified  in the configuration properties file and that do not yet exist. When you run the
command, the scripts to create the database tables are automatically created. Depending on the value
that you set for the bpm.de.deferSchemaCreation property in the properties
file, the database tables may be created and the Process database that is loaded with system
information. If you are migrating and Business Process Choreographer was configured in your source
environment, the configuration properties files were automatically exported when BPMConfig
-migrate was run and they are used to automatically re-create the Business Process
Choreographer configuration in the new environment. When you have finished creating the new
environment, you may need to perform some Business Process Choreographer post-migration tasks, which
are described in the topic "Moving your custom configuration to the target environment."

If you run the
BPMConfig
-create command with the -profile option, the only profiles
that are created are those profiles that are specified in the configuration properties file that do
not exist. If -create -de was already run and one or more profiles already
exist, the BPMConfig command reports the existing profile names in a message and
continues to configure the deployment environment. When you create a new profile, by default, the
new node is federated when it is created. If you want to create the profile without federating the
node, specify the -federateLater option with the -create
-profile action. Although the -create -profile action creates one or
more Business Automation Workflow profiles,
it does not configure the deployment environment. This is useful if you want to use the Deployment
Environment wizard in the administrative console to configure the deployment environment. You can
create the Business Automation Workflow
deployment manager profile and managed node profile first by using the -create
-profile action and then start the administrative console to configure your deployment
environment.

To add one or more cluster members to an existing deployment environment, run the command
BPMConfig -create -clusterMembers properties\_file. Run the
command on the deployment manager node. If you have remote custom nodes, you must run the
syncNode command on the remote nodes to obtain the latest configuration file
changes.

Before you run the command, you must add the properties of the cluster members to the
configuration properties file. The names of the added members must be different from the names of
existing members on the same node. Also increment the index of the cluster members.

You can add the cluster member properties to the properties file by using one of the following
approaches:

- If a configuration properties file was used to generate the deployment environment, you can edit
the file and add the cluster member properties, then run the command to add the cluster members to
the existing deployment environment.
- If the Deployment Environment wizard was used to generate the deployment environment, you can
export the configuration properties file by using the BPMConfig -export command
and add the cluster member properties to the file, then run the command to add the cluster members
to the existing deployment environment.

Before you run the command to add the cluster members, ensure that the deployment manager is
running and also ensure that the local node agent is stopped.

Use the -update parameter to configure a custom context root for a deployment
environment. Alternatively, you can use the -update
parameter to update data source information for the deployment environment. The specified
custom context root is used as a prefix to the default Business Automation Workflow context roots. Create the
deployment environment before you run the command. Stop the deployment
manager, node agents, and all running servers before you run the command. Run the command from
the <install\_root>\bin directory in the Windows environment.

You can also use the -update parameter with the
jdbc\_driver\_path value to configure custom JDBC paths. This command updates the
JDBC driver path variables. On a stand-alone server, run the command to configure the server. In a
network deployment environment, run the command to configure the deployment manager and run it again
for each managed node.

The -profile profile\_name value identifies the deployment
manager profile. It is suggested that you create a backup copy of the profile before running the
-update parameter. The -de DE\_name value
identifies the deployment environment name. You can omit the -de option if there is
only one deployment environment in the WebSphere cell. The -component
component\_name value identifies the component, and the values (with
respect to a custom context root) are ProcessPortal,
CaseManager, and ContentNavigator. If
-component component\_name is not specified, the context root is
updated for all components.

The TargetObjectStore value
has been replaced with CaseManager.

- The -component
ContentNavigator option is used only for embedded IBM Content
Navigator.
- In V18.0.0.1 (only), when the -contextRootPrefix option is specified, IBM Business Automation
Workflow applications are handled
differently than case applications. For example, if the option value was set to
/abc, the Process Center application context root would be changed from
/ProcessCenter to /abc/ProcessCenter.
However, the Case Builder application would be changed from
/CaseBuilder to /abcCaseBuilder without
the forward slash character (/) between
abc and CaseBuilder.

Do your process applications use inbound web services, the web API, or the REST API? All URLs
exposed by IBM Business Process Manager contain the newly configured context root; therefore, this
change affects client applications that are using the previous context root as an endpoint. Update
your client applications to use the new custom context root.

Any previously installed Process Designer must be downloaded and installed again because Process
Designer must use the new context root configuration.

Case management configuration must be updated with the new context root. Start the Case
configuration tool and run all tasks. To enable IBM
FileNet® Process Designer in Case Builder, see Configuring IBM Business Automation Workflow to use the stand-alone IBM FileNet Process Designer.

Update the web server plug-in. The web modules are updated in the product
applications when you run the BPMConfig -update -contextRootPrefix command. If the
product applications are mapped to a web server, the plugin-cfg.xml file for
the web server must be updated with the new context roots. Any web server plug-ins might need to be
propagated (or generated and propagated). For more information, see the topic Plug-ins configuration in the WebSphere Application Server product
information.

Clear your browser cache before you start the user interfaces. After running the
BPMConfig command, run the syncNode command on each node to
obtain the latest configuration file changes.

If you specify -update -profile profile\_name -de
DE\_name -virtualHost virtual\_host\_name, the web
modules of the Business Automation Workflow
applications in the specified deployment environment are mapped to the specified virtual host. If
you have more than one deployment environment in your cell, you can either use context root prefixes
to differentiate between the multiple deployment environments or you can use the BPMConfig
-update -virtualHost command to configure another virtual host.

If you specify -update -profile profile\_name -de
DE\_name -caseConfigure, the command collects the case management
configuration parameters and configures the case data sources for the upgrade path.

You can run this command silently by specifying the
-responseFile response\_file parameter. See the Sample case configuration response files.

If you specify -update -profile profile\_name -de
DE\_name -networkDirectory networkDirectory -component
component\_name, you can update the network directory for the IBM Content
Navigator or the
IBM Case
Manager. The
-component parameter is required and the supported values are CaseManager and ContentNavigator.

If you specify -update -dataSource properties\_file, the
database name, database server name, and database server port are all updated for the deployment
environment. For Oracle databases, the database URL is also updated. However, the associated user
authentication and schema are not updated. As a result, you must ensure that the database that you
are updating has the same user and schema as those configured in the current deployment
environment.

You can also use the -performanceTuning option with the
-update parameter to update performance tuning properties for the deployment
environment specified in the configuration properties file. If you specify
-performanceTuning properties\_file, all performance tuning
properties in the configuration properties file are updated. For the list of performance tuning
properties that can be edited, see Configuration properties for the BPMConfig command.

If you specify -update -profile
profile\_name -enableContentObjectSupport true|false, you can enable or
disable content object support in IBM Business Automation
Workflow. By default, internal
Content Platform Engine 5.5.3 or later
is used with IBM Business Automation
Workflow
(such as used with IBM Business Automation
Workflow 19.0.0.2 and later), and content object support is enabled.

If an internal Content Platform Engine is used, you can enable
content object support by using the -enableContentObjectSupport parameter. You
can also use the same parameter to disable content object support regardless of the internal
Content Platform Engine version. See the
example in the Examples section below.

```
BPMConfig.sh -upgrade -de properties\_file
```

The upgrade is based on the properties that are found in the
specified configuration properties file. You probably need to edit the properties in the file before
you run the command. Sample configuration properties files that can be edited and used to upgrade a
deployment environment are found in the following
location:

install\_root/BPM/samples/config/upgradede

If you
added a supported customization to your Standard
deployment environment, such as a context root prefix or
an update to the virtual host mapping, the same customization is automatically applied to the Advanced
deployment environment during the upgrade. For example, if
you set the bpm.de.contextRootPrefix property and the
bpm.de.virtualHost property in your Standard
deployment environment properties file, the context root
and virtual host mapping of all web modules are automatically updated for the advanced capabilities
when the environment is upgraded.

When you choose the databases that you want to use in the
new Advanced
deployment environment, you can use your existing
Business Automation Workflow databases or you
can specify new databases and buses for the advanced capabilities of the environment. Scripts are
provided to generate the resources that are required to support the databases and buses. For
example, if you set the bpm.de.deferSchemaCreation property to
false, all of the tables that are required for the advanced environment
capabilities are generated automatically in your databases.

```
BPMConfig.sh -upgrade -de properties\_file -component BPCArchive
BPMConfig.sh -upgrade -de properties\_file -component EmbeddedECM
```

First
update the configuration properties file. For instructions, see the topics Configuring Business Process Archive Manager and Configuring the BPM document store for Db2 on z/OS. After you run the command,
synchronize the nodes so that the managed nodes obtain the latest configuration properties file
changes.

```
BPMConfig -upgrade -profile dmgr\_profile\_name
```

Exports configuration properties from an existing deployment environment to an output
configuration directory. Also optionally exports database information and/or system data for
performance analysis purposes.

```
BPMConfig.sh -export -profile profile\_name [-de DE\_name] [-outputDir configuration\_directory]
```

```
BPMConfig.sh -export -profile profile\_name [-de DE\_name] [-db [properties\_file]] [-system properties\_file] [-outputDir configuration\_directory]
```

- You can only use the -system option to export system data on machines that are
running the Linux or AIX operating systems. You cannot use the -system option
to export system data on machines that are running the Windows operating system.
- If you are specifying both the -db option and the -system
option, the -db option must be specified first in the command syntax.
- An input configuration properties file is optional for the -db option and
required for the -system option. However, the two options use the same input file,
which contains properties that enable you to export database information and system data. If you
specify both the -db option and -system option in the command
syntax, you must not specify an input file for the -db option and only specify an
input file for the -system option. (You can change properties for both the
-db and -system options in the input file that you specify with
the -system option.) A sample input properties file named
PerformanceAnalysis.properties is provided for you to copy and customize. It is
located in the following directory (where install\_root is the installation
location of Business Automation Workflow):install\_root/BPM/samples/config/performanceanalysis/

For more detailed information about using the -db and -system
options to export database information and system data for performance analysis purposes, see the
topics Using the BPMConfig command to export database information for performance analysis and Using the BPMConfig command to export system data for performance analysis.

- Modify the properties with the IBM Business Automation
Workflow Configuration editor
and then create another deployment environment on a different Business Automation Workflow installation that is
similar to the exported deployment environment (a clone with modifications).
- Compare the configuration of the exported deployment environment with another deployment
environment that you also exported.
- Extend the existing deployment environment with more cluster members by running the command
BPMConfig -create clusterMembers properties\_file.

- Cell and deployment environment
- Deployment manager and managed node
- Cluster and cluster member
- Data source and JDBC provider information
- Authentication alias and role mapping
- LDAP
- Deployment environment and Process Portal context root prefix (if set in the current deployment
environment)
- Business Process Choreographer customization
- Additional performance tuning configuration properties

The output directory contains configuration files similar to the files in the following table. To
reflect the requirements of your new deployment environment, make updates to the exported
configuration properties file listed in the first row of the table. No updates are needed to the
other files listed in the table, but ensure that those files are kept together in the same directory
for future reference.

| Sample name                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DE\_name.properties                                                        | This properties file contains the configuration properties from your source environment. You use this file when you configure the target environment. For more information about the configuration properties, see the topic Configuration properties for the BPMConfig command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| fileRegistry.xml                                                          | If you use a file-based user registry, the user registry file is copied from the source environment to be added to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ltpa.jceks                                                                | If you use LTPA, the LTPA key file is copied from the source environment to be added to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ldap\_additional\_properties.xml                                            | If you use a federated repository and an unencrypted LDAP connection in the source environment, user-defined additional properties of the LDAP server are copied from the source environment to the output directory, where they are later used automatically to create the target environment.Restriction: If you extend the federated repository to use a custom login property (such as userPrincipalName) in addition to the default uid property in the source environment, LDAP is not configured for the target environment, with the following warning: CWMCB0600W: LDAP could not be configured! You may configure LDAP separately after BPMConfig has terminated successfully. If you see this warning, manually configure LDAP with the login properties you want to use after the migration is complete. |
| ProcessServer\_100SourceCustomMerged.xml and PDW\_100SourceCustomMerged.xml | If you have XML configuration properties files, they are copied from the source environment. The exported configuration files are merged and renamed to 101CustomMigrated.xml in the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Application-config-bpc.xml and resources-bpc.xml                          | If you have Business Process Choreographer that are configured in the source environment, the configuration files are copied from the source environment to the output directory, where they are later used automatically to create the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Support-config-bpc.xml                                                    | If you have Business Process Choreographer Archive Manager configured on the support cluster in the source environment, the configuration is copied from the source environment to the output directory, where it is later used automatically to create the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

- The -wasHome option specifies the full path to the installation directory for
the previous installation in the source environment. For example:
opt/BPMInstall/BMP751Adv or E:\BPMInstall\WPS700 or
C:\IBM\Lombardi72\AppServer.
- The -profile option specifies the name of the deployment manager or stand-alone
profile.
- The -de option specifies the name of the deployment environment, which you can
find in the administrative console. This option is required if you are migrating more than one
deployment environment. If you are migrating only one deployment environment, you can omit this
option. Do not use this option if you are migrating from a stand-alone environment.

```
# Deployment environment type for the target environment. Value is Advanced, Standard or AdvancedOnly
target.deType=Advanced
# Topology for the target environment(number of cluster). Value is 1 or 3
target.clusterNumber=3
# Node number for the target environment. Value is a number, such as 2.
target.nodeNumber=2
# Bus option for the target environment for 3-cluster topology. Value is true or false
target.isSingleBus=false
```

- If you are migrating from a stand-alone environment, you must migrate the performance tuning
properties manually.
- If the source environment is a network deployment environment, BPMConfig
-migrate adds a default cluster member in the properties file for each migrated cluster.
However, it does not migrate existing cluster members; you must add them in the properties file
manually.

| Sample name                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DE1-Advanced-PS-ThreeClusters-DB2-MultiBus.properties                     | This properties file contains the configuration information from your source environment. You use this file when you configure the target environment. For information about the properties, see the reference topic about properties that are migrated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| fileRegistry.xml                                                          | If you use a file-based user registry, the user registry file is copied from the source environment to be migrated to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ltpa.jceks                                                                | If you use LTPA, the LTPA key file is copied from the source environment to be migrated to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ldap\_additional\_properties.xml                                            | If you use a federated repository and an unencrypted LDAP connection in the source environment, user-defined additional properties of the LDAP server are copied from the source environment to be migrated to the target environment.Restriction: If you extend the federated repository to use a custom login property (such as userPrincipalName) in addition to the default uid property in the source environment, LDAP is not configured for the target environment, with the following warning: CWMCB0600W: LDAP could not be configured! You may configure LDAP separately after BPMConfig has terminated successfully. If you see this warning, manually configure LDAP with the login properties you want to use after the migration is complete. |
| ProcessServer\_100SourceCustomMerged.xml and PDW\_100SourceCustomMerged.xml | If you have XML configuration properties files, they are copied from the source environment to be migrated to the target environment. The exported configuration files are merged and renamed to 101CustomMigrated.xml in the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Application-config-bpc.xml and resources-bpc.xml                          | If you have Business Process Choreographer that are configured in the source environment, the configuration files are copied from the source environment to be migrated to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Support-config-bpc.xml                                                    | If you have Business Process Choreographer Archive Manager configured on the support cluster in the source environment, the configuration is copied from the source environment to be migrated to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

If you specify -validate properties\_file, the command
validates that the specified configuration properties file can be used to create a deployment
environment.

If you specify -validate -db
properties\_file, the command validates that connections to the databases
can be successfully established by using the specified user names and passwords. It does not
validate the contents of the databases, such as the schema.

EmbeddedECMDb must use the same schema name as the database username. Otherwise,
running the BPMConfig -validate command in a working Business Automation Workflow or IBM Business Process
Manager environment of V8.5.5 or later gives you the following error: CWMCB0239E: The
database schema value BPMECM2S for component EmbeddedECM should be the same as the database user
name BPMSAND.

If you specify -validate -profile profile\_name [-de
DE\_name] [-outputDir output\_directory] (where the
-de option is optional when there is only one deployment environment in the
WebSphere cell), a status report is generated for the specified deployment environment. The status
report lists the components that are configured in the deployment environment and displays the
status of each component and its associated resources. The report also displays the status of key
security roles and the runtime status of Workflow Center, Workflow Server, and Performance Data
Warehouse. The name of the generated status report is
ConfigValidationReport\_DE\_name.html, where
DE\_name is the name of the deployment environment. For example,
ConfigValidationReport\_De1.html. If you specify an output directory, the status
report is generated into a directory that is named html that is appended to the
output directory. For example, if you specify E:/Output as the output
directory, the status report is generated into E:/Output/html. If you do not
specify an output directory, the status report is generated into an html
directory that is appended to the directory where you ran the BPMConfig command.
For example, install\_root/bin/html.

If you specify -validate -performanceTuning properties\_file,
the command validates all performance tuning parameters in the configuration properties file, such
as the JVM heap size and thread pool configuration. If the value in the file is different from the
recommended value, you see a warning message. For example, if the recommended value for the JVM
maximum heap size is 2048, but the value in the configuration properties file is 1024, the following
warning message is shown: The parameter 'maximumHeapSize' for Dmgr value [2014] is less than
the target default value [2048]. For the list of performance tuning properties that can be
edited, see Configuration properties for the BPMConfig command.

With secure LDAP configured, running the BPMConfig -validate command to verify
that the exported configuration properties file gives  you the following error: CWMCB0345E:
LDAP protocol ldaps: is not supported. You can safely ignore this error.

```
outputDir\cells\PCCell1\clusters\SingleCluster\performance-data-warehouse\TeamWorksConfiguration.running.xml
outputDir\cells\PCCell1\clusters\SingleCluster\performance-data-warehouse\TeamWorksConfiguration.system.xml
outputDir\cells\PCCell1\clusters\SingleCluster\process-center\TeamWorksConfiguration.running.xml
outputDir\cells\PCCell1\clusters\SingleCluster\process-center\TeamWorksConfiguration.system.xml
outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\performance-data-warehouse\TeamWorksConfiguration.running.xml
outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\performance-data-warehouse\TeamWorksConfiguration.system.xml
outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\process-center\TeamWorksConfiguration.system.xml
outputDir\cells\PCCell1\nodes\Node1\servers\SingleClusterMember1\performance-data-warehouse\TeamWorksConfiguration.system.xml
```

Starts the deployment environment. You can run the command by specifying the deployment manager
profile name and the deployment environment name or you can run the command with a configuration
properties file. If you run the command by specifying the deployment manager profile name, you can
omit the -de option if there is only one deployment environment in the WebSphere
cell.

The command must be run on the deployment manager machine after all remote node agents have been
manually started. The -start parameter uses the deployment manager profile to
start multiple elements of the deployment environment, including the deployment manager, any local
node agents, and the cluster members.

The -delete parameter is used to delete profiles, deployment environments, and
cluster members.

- To delete all Business Automation Workflow profiles at once, when your environment is on a single computer, run the following command:
BPMConfig -delete -profiles properties\_file
The
deployment manager must be running, and BPMConfig must be run on the computer
with the profiles that you want to delete. This command deletes all profiles in the configuration
properties file on the installation where you run the command, including the deployment manager
profile. If you want to delete only one or more managed node profiles, see Removing a managed node profile from a deployment
environment instead.
It is suggested that you create a backup copy of the profiles
before running the -delete parameter. 
Note: When you run this command, it is
possible that some files under the profile root directory will not be deleted because they are
locked. Check the profile root directory, and if it still exists, you should recursively delete
it.
- To delete a deployment environment, run the following command (where
profile\_name is the name of the deployment manager):
BPMConfig -delete -profile profile\_name -de
DE\_name
The command to delete a deployment environment must be run
on the deployment manager machine.
When the command is used to delete a deployment
environment, it deletes the resources (such as clusters and applications) that were configured when
the deployment environment was created by the BPMConfig command or the Deployment
Environment wizard. The command also deletes the buses that are used by the deployment
environment.
The command retains the author alias and users that are used by the deployment
environment. It also retains the database for the deployment environment as well as the DB scripts
(which are in the directory
profile\_root/dbscripts/cell\_name.DE\_name).
The
BPMConfig command runs in disconnected (local) mode and it does not have access
to IBM BPM databases. Before you run the BPMConfig command to delete the
deployment environment, ensure that there are no long-running tasks and then uninstall the
applications HTM\_PredefinedTasks\_V8000\_cluster\_name and
HTM\_PredefinedTaskMsg\_V8000\_cluster\_name (where
cluster\_name is the name of the application cluster for the
deployment environment). To uninstall the applications, you can use the WebSphere administrative
console or you can use an administrative command and script, as described in the topic Deploying BPEL process and human task applications and its subtopics.
If there are resources that you or other users have
manually configured in the deployment environment, you must delete the resources
manually.
After running the BPMConfig command, you must run the
syncNode command to obtain the latest configuration file changes.
Note: After
you have run this command, you will need to manually delete the following directories on each
managed node that hosted application cluster members of the deleted Business Automation Workflow deployment
environment:managed\_node\_profile/BusinessSpace/application\_cluster\_name
managed\_node\_profile/SearchIndex/task/application\_cluster\_name
managed\_node\_profile/FileNet/application\_cluster\_name
- To remove a managed node from a deployment environment, run the following command (where
node\_name is the name of the managed node and
profile\_name is the name of the deployment manager profile):
BPMConfig -delete -profile profile\_name -de DE\_name
-node node\_name
After running the BPMConfig
command, you must run the syncNode command to obtain the latest configuration
file changes.
This command deletes all cluster members on a node but will not compromise the
functions of the Business Automation Workflow
deployment environment. At least one cluster member will always remain in every cluster of the
deployment environment.Note: After you have run this command, you will need to manually delete the
following directories:
managed\_node\_profile/BusinessSpace/application\_cluster\_name
managed\_node\_profile/SearchIndex/task/application\_cluster\_name
managed\_node\_profile/FileNet/application\_cluster\_name

For
the full procedure, see Removing a managed node profile
from a deployment environment.
- To delete an individual cluster member, run the following command (where
cluster\_member\_name is the name of the target cluster member and
profile\_name is the name of the deployment manager profile):
BPMConfig -delete -profile profile\_name -de DE\_name
-node node\_name -clusterMember
cluster\_member\_name
You need to run the command only on the
deployment manager node. If you have remote custom nodes, you must run the
syncNode command on the remote nodes to obtain the latest configuration file
changes. Before you run the syncNode command, ensure that the deployment manager
is running and also ensure that the local node agent is stopped. If you have local custom nodes that
are on the same machine as the deployment manager node, there is no need to run the
syncNode command because it is automatically invoked for local nodes when the
BPMConfig command is run.
Note: After you have run this command, you will need
to manually delete the following directories (if the deleted application cluster member was the last
one on the managed
node):managed\_node\_profile/BusinessSpace/application\_cluster\_name
managed\_node\_profile/SearchIndex/task/application\_cluster\_name
managed\_node\_profile/FileNet/application\_cluster\_name
- If you do
not want to be prompted to confirm that you want to delete the specified resources, append the
-acceptDeletionPrompt option to the end of the command syntax.

Displays usage information for the specified parameter name. If you specify the
-help parameter by itself without a parameter name, it returns usage information
for the BPMConfig command. If you specify the -help parameter
with a parameter name (such as the -create parameter), it displays usage
information for the specified parameter. For example: -help create.

The BPMConfig command uses a configuration properties file that contains the
properties that are used by the command, as well as usage information about the properties and their
defaults.

To create your own properties file, make a copy of one of the sample configuration properties
files that are found in the product-specific directories in the following parent directory:

install\_root/BPM/samples/config

When you specify the properties file to use, you can specify either an
absolute path or a path relative to the current directory.

```
FATAL ERROR:  'java.lang.NullPointerException'
           :null
```

## Examples

```
BPMConfig -create -de myenvironment.properties
```

```
BPMConfig -create -profile myenvironment.properties
```

```
BPMConfig -create -sqlfiles myenvironment.properties -outputDir /MyBPMScriptDir
```

```
BPMConfig -create -clusterMembers myenvironment.properties
```

```
BPMConfig -update -profile mydeploymentmgrprofilename -de mydeploymentenvname -contextRootPrefix /mycorporation
```

```
BPMConfig -update -profile mydeploymentmgrprofilename -de mydeploymentenvname -component ProcessPortal -contextRootPrefix /mycorporationprocessportal
```

```
BPMConfig -update -dataSource myenvironment.properties
```

```
BPMConfig -update -profile DmgrProfile -de De1 -virtualHost virhost1
```

```
BPMConfig -update -profile Dmgr01 -node Dmgr01 -jdbcDriverPath E:\temp\jdbcdrivers\Oracle
BPMConfig -update -profile Dmgr01 -node Node01 -jdbcDriverPath E:\temp\jdbcdrivers\Oracle
BPMConfig -update -profile Dmgr01 -node Node02 -jdbcDriverPath /root/temp/jdbcdrivers/Oracle
```

```
BPMConfig -update -profile profile\_name -enableContentObjectSupport true
```

```
BPMConfig -update -profile profile\_name -enableContentObjectSupport false -clientDownloadServiceHostname CPE\_server\_hostname -clientDownloadServicePort 9443
```

```
BPMConfig -upgrade -de myenvironment.properties
```

```
BPMConfig -validate myenvironment.properties
```

```
BPMConfig -validate -db myenvironment.properties
```

```
BPMConfig -validate -profile DmgrProfile -de De1 -outputDir E:/Output
```

```
BPMConfig -start -profile DmgrProfile -de De1
```

```
BPMConfig -start myenvironment.properties
```

```
BPMConfig -stop -profile DmgrProfile -de De1 -username DmgrAdmin -password mypassword
```

```
BPMConfig -stop myenvironment.properties
```

```
BPMConfig -export -profile DmgrProfile -de De1 -outputDir E:\ConfigExport
```

```
BPMConfig.sh -export -profile DmgrProfile -de De1 -db -system /home/user/performanceAnalysis.properties -outputDir /home/user/ConfigExport
```

```
BPMConfig -migrate -wasHome E:\BPM751Adv -profile DmgrProfile -de De1 -outputDir E:\ConfigExport
```

```
BPMConfig -migrate -wasHome /opt/BPM751Adv/ -profile DmgrProfile -de DE1 -outputDir /home/user\_name/751configuration -responseFile /home/user\_name/bpm\_response.txt
```

```
BPMConfig -delete -profiles myenvironment.properties
```

```
BPMConfig -delete -profile DmgrProfile -de De1
```

```
BPMConfig -delete -profile DmgrProfile -de De1 -node Node1
```

```
BPMConfig -delete -profile DmgrProfile -de De1 -node Node1 -clusterMember Server1
```

```
BPMConfig -help
```

```
BPMConfig -help create
```

- Configuration properties for the BPMConfig command

The BPMConfig command uses a properties file to configure your environment according to the settings that you specify. Before you begin your configuration, select a sample file that most closely resembles the configuration that you want, copy the file, and customize it to suit your own environment. This topic provides descriptions for the properties in the sample properties files. It also provides descriptions for many properties that are not contained in the sample properties files but that can be manually added to the files.
- Sample configuration properties files for the BPMConfig command

Your Business Automation Workflow installation includes several sample configuration files that are provided as a starting point for your configuration. These sample files are composed of common properties and settings for different Business Automation Workflow environments. Before you begin your configuration, select a sample file that most closely resembles the configuration that you want, copy the file, and customize it to suit your own environment. The BPMConfig command will use the properties file to configure your environment according to the settings that you specify.
- Sample case configuration response files for the BPMConfig command

You can use a sample response file to collect the case management parameters and configure the case data sources for the upgrade path, using the BPMConfig -update -profile profile\_name -de DE\_name -caseConfigure command. The following sample files for Db2, Oracle, and SQL Server are provided as a starting point.