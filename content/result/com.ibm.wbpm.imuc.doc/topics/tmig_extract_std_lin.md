# Migrating the configuration from the source environment

Migrate the configuration
information from your source environment so that you can start with
the same configuration when you create your target environment. Later,
you will use the IBM BPM Configuration editor to configure the environment
that you want.

Figure 1. Sample environment after the new version is installed on the target and BPMConfig -migrate is
run. The output folder is being copied to the target environment. The source environment is running
and transferring data to and from its databases. The target has been created but does not contain a
deployment environment.

<!-- image -->

<!-- image -->

## Before you begin

If the source
environment is a network deployment environment, ensure that the deployment
manager, nodes, and deployment environment have been started. If the
source environment is a stand-alone environment, ensure that the stand-alone
server has been started.

## About this task

Run the BPMConfig -migrate command
to export the configuration information from the source environment
and generate the properties file. You will later configure your new
environment with the IBM BPM Configuration editor. The changes that
you make in the editor are saved to the properties file and used to
create the target environment that you want.

## Procedure

For each deployment environment in your
source environment, or for your stand-alone source environment, complete
the following steps:

1. If you modified any of the 100Custom.xml files, make sure
that the 100Custom.xml files on the managed node are in sync with the
100Custom.xml files on the deployment manager. If the files are different,
manually copy the 100Custom.xml files from the node profile to the deployment
manager profile.

You must perform this step because the BPMConfig -migrate command reads the
100Custom.xml file from the deployment manager profile only. The command
exports the 100Custom.xml files from the deployment manager profile to the
snapshot folder. 

 All customized .xml files in the /config folder are
merged, and PDW\_100SourceCustomMerged.xml and
ProcessServer\_100SourceCustomMerged.xml files are created in the output
directory that you chose. The XML files are merged in a sequence where those starting with a letter
of the alphabet are merged before those that start with numbers, which are merged in numeric order.
For more information about which files are merged and the sequence that is used, see the comments in
100SourceCustomMerged.xml.
If you modified any configuration files under the /config/system folder,
such as 99Local.xml or 00Static.xml, directly on the
source environment, the customization in these files will not be migrated, and you must apply the
same customization to the target at post migration.
2 Migrate the configuration informationfrom your source environment and generate the properties file. You are prompted for some information about the target environment youwant, such as the topology, whether to use multiple buses, and the number of nodes. Alternatively,you can run this command silently by specifying the -responseFileresponse\_file parameter. where: For example:BPMConfig.sh -migrate -wasHome /opt/BPM751Std/ -profile Dmgr01 -de PSDE -outputDir /home/user\_name/751configuration After the command finishes successfully, you see information similarto the followinginformation:Logging to file path\_to\_log\_file .Initializing context for export...You are using BPMConfig to migrate from product version to IBM BPM 8.6.0.0.Choose the topology for the target environment:1. Single Cluster2. Three ClustersInput option number: 2Specify the number of nodes for the target environment: 1Choose the bus option for the target environment:1. Single Bus2. Multiple BusesInput option number: 1Exporting security information...Exporting data source information...Exporting WebSphere Lombardi XML information...Exporting performance tuning parameters...The command completed successfully.
    - Network deployment source environment:
        - If you installed the new version of the product on the same computer as the source environment,
run the following command in the target
environment:install\_root\_new\_version/bin/BPMConfig -migrate -wasHome source\_installation\_directory -profile profile\_name [-de deployment\_environment\_name] [-useRecommendedSettings] -outputDir path\_to\_configuration\_folder
        - If you installed the new version of the product on a different computer and copied the migration
files to the source environment, run the following command in the source environment on the computer
where the deployment manager is
deployed:remote\_migration\_utility/bin/BPMConfig -migrate -wasHome source\_installation\_directory -profile profile\_name [-de deployment\_environment\_name] [-useRecommendedSettings] -outputDir path\_to\_configuration\_folder
- Stand-alone source environment:
    - If you installed the new version of the product on the same computer as the source environment,
run the following command in the target
environment:install\_root\_new\_version/bin/BPMConfig -migrate -wasHome source\_installation\_directory -profile profile\_name [-useRecommendedSettings] -outputDir path\_to\_configuration\_folder
    - If you installed the new version of the product on a different computer and copied the migration
files to the source environment, run the following command in the source environment on the computer
where the stand-alone server is
deployed:remote\_migration\_utility/bin/BPMConfig -migrate -wasHome source\_installation\_directory -profile profile\_name [-useRecommendedSettings] -outputDir path\_to\_configuration\_folder

- source\_installation\_directory is the full path to the previous installation
in the source environment.
- profile\_name is the name of the deployment manager or stand-alone
profile.
- deployment\_environment\_name specifies the name of the deployment environment,which you can find in the administrative console. This name is required if you are migrating morethan one deployment environment. If you are migrating only one deployment environment, you can omitthe name. Do not use deployment\_environment\_name if you are migrating from astand-alone environment. In Business Automation Workflow 8.5.0.0 or later, you canuse only the following characters in a deployment environment name: If you migrate a pre-8.5.0.0 deployment environment to Business Automation Workflow 8.5.0.0 or later, youmust ensure that the name of the new deployment environment only uses permitted characters. Althoughyou can export a pre-8.5.0.0 deployment environment that has unpermitted characters in the name, youwill need to rename the deployment environment when you use the BPMConfig commandto create the new deployment environment. If the new deployment environment name containsunpermitted characters, you may receive an error message that is similar to the following message:message:com.ibm.bpm.config.model.ConfigModelFactory validateConfigModel CWMCB0368E: bpm.de.name has an invalid value invalid\_value
    - a - z
    - A - Z
    - 0 - 9
    - ! ( ) - . ? [ ] \_ ` ~ \ /

```
message:com.ibm.bpm.config.model.ConfigModelFactory validateConfigModel
 CWMCB0368E:  bpm.de.name has an invalid value invalid\_value
```

- -useRecommendedSettings is an optional parameter to add if you want to use the
recommended values for the performance tuning properties after migration, instead of using the
values from the source environment. For performance tuning properties, such as the JVM heap size or
thread pool configuration, the command compares the source value with the recommended value. If the
source value is smaller, the recommended value is added to the properties file instead.
- path\_to\_configuration\_folder is the full path to the folder where you want to
put the configuration files. Tip: If you are running this command more than once because
you have more than one deployment environment, remember to specify different output
folders.

```
BPMConfig.sh -migrate -wasHome /opt/BPM751Std/ -profile Dmgr01 -de PSDE -outputDir /home/user\_name/751configuration
```

```
Logging to file path\_to\_log\_file.

Initializing context for export...
You are using BPMConfig to migrate from product version to IBM BPM 8.6.0.0.

Choose the topology for the target environment:
1. Single Cluster
2. Three Clusters
Input option number: 2

Specify the number of nodes for the target environment: 1

Choose the bus option for the target environment:
1. Single Bus
2. Multiple Buses
Input option number: 1

Exporting security information...
Exporting data source information...
Exporting WebSphere Lombardi XML information...
Exporting performance tuning parameters...

The command completed successfully.
```

3 If your target environment is on a different computer from your sourceenvironment, copy the output folder to the target environment. The output folder contains files similar to the following files:Table 1. Files for migration Sample name Description DE1-Standard-PC-ThreeClusters-DB2.properties The properties file containing the configuration information from your sourceenvironment. You will use this file when you configure the target environment. You can see a list ofthe properties in the Configuration properties for the BPMConfig command topic. fileRegistry.xml If you use a file-based user registry, the user registry file is copied fromthe source environment to be migrated to the target environment. ldap\_additional\_properties.xml If you use a federated repository and an unencrypted LDAP connection in thesource environment, user-defined additional properties of the LDAP server are copied from the sourceenvironment to be migrated to the target environment. PDW\_100SourceCustomMerged.xml andProcessServer\_100SourceCustomMerged.xml If you have XML configuration properties files, they are copied from thesource environment to be migrated to the target environment. Important:

| Sample name                                                               | Description                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DE1-Standard-PC-ThreeClusters-DB2.properties                              | The properties file containing the configuration information from your source environment. You will use this file when you configure the target environment. You can see a list of the properties in the Configuration properties for the BPMConfig command topic. |
| fileRegistry.xml                                                          | If you use a file-based user registry, the user registry file is copied from the source environment to be migrated to the target environment.                                                                                                                      |
| ldap\_additional\_properties.xml                                            | If you use a federated repository and an unencrypted LDAP connection in the source environment, user-defined additional properties of the LDAP server are copied from the source environment to be migrated to the target environment.                             |
| PDW\_100SourceCustomMerged.xml and ProcessServer\_100SourceCustomMerged.xml | If you have XML configuration properties files, they are copied from the source environment to be migrated to the target environment.                                                                                                                              |

- Keep the same cell name, cell administrator, deployment environment
administrator, database schema names, and database user names.
- Make sure that bpm.de.deferSchemaCreation is set to true in the properties
file.
- Use the same LDAP server as the source environment, because missing users and
groups in the LDAP server could cause problems with running instances after migration.
- In the properties file that contains the configuration information from your
source environment, look for endpoint information that contains the load balancing information from
the source configuration. Make sure that the host name and ports will be reused for the target
environment. For example, if a web server or a load-balancing server is configured in the source
environment, you will see the following lines in the properties
file:bpm.de.processServer.processAdminPrefix=https://mzwin7-bpm1/ProcessAdmin
bpm.de.processServer.teamworksWebAppPrefix=https://mzwin7-bpm1/teamworks
bpm.de.processServer.clientLink=https://mzwin7-bpm1/teamworks
bpm.de.processServer.commonPortalPrefix=https://mzwin7-bpm1/portalIf
you are using a different web server for the target environment, modify the host name and ports in
these lines. The migration code does not use the changes made directly in the
99local.xml file. If you have not used the 100custom.xml
file to override the default values, you will not see these lines in the properties file and you can
configure the endpoints after the target environment is configured. See Customizing IBM BPM to work with a web server.
- Some XML security configuration properties are moved to the WebSphere® Application
Server configuration files automatically. These
properties are exported to the properties file and will be moved to the WebSphere Application
Server configuration files when you run
BPMConfig -create. Refer to Security configuration properties for a list of
the properties that have been moved.

## Results

## What to do next

Not all Business Automation Workflow
configuration information is automatically migrated to the target environment. Review Completing configuration for IBM Business Automation Workflow carefully and export other configuration as required. In addition
to the configuration exported by the BPMConfig –migrate command, you can use the
exportWASConfig.py script to export customized WebSphere Application
Server configuration, including data sources,
authentication aliases, and JDBC and JMS providers, from your source environment. You can refer to
this configuration to update the target environment manually or use the
importWASConfig.py script to import the configuration automatically after the
target environment is configured.

## Related information

- Completing configuration for IBM Business Automation Workflow
- BPMConfig command-line utility
- Configuration properties for the BPMConfig command
- exportWASConfig.py script