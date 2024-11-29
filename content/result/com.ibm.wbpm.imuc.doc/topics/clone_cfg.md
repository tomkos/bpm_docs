# Creating a new deployment environment based on an existing configuration

## About this task

After you export the configuration properties, use the IBM Business Automation
Workflow Configuration editor to update the exported
properties to match your requirements. For example, you can update the database information to use a
new set of databases, update the LDAP server to use the testing server, and update performance
tuning properties to match the new environment. After you modify the properties file in the editor,
you can use the BPMConfig -create command to create a new deployment environment
that is a partial copy of the existing deployment environment, based on the modified file.

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

The databases and customer applications are not replicated to the new environment. For
instructions to replicate the complete environment, see Migrating IBM Business Automation Workflow to new hardware.

## Procedure

To create the new deployment environment, complete the following steps:

1 Run the BPMConfig –export commandto extract the configuration data from the Business Automation Workflow deploymentenvironment. For example: If there is only one deployment environment in the WebSpherecell, you can omit the -de option.Important: Specifya different output directory for each deployment environment. In thecase where a cell has multiple deployment environments, a unique outputdirectory is required for each deployment environment. The configuration files are placed in the output directory that you specify.Table 1. Configuration files for each deploymentenvironment Sample name Description DE\_name .properties This properties file contains the configuration properties from your sourceenvironment. You use this file when you configure the target environment. For more information aboutthe configuration properties, see the topic Configuration properties for the BPMConfig command . fileRegistry.xml If you use a file-based user registry, the user registry file is copied fromthe source environment to be added to the target environment. ltpa.jceks If you use LTPA, the LTPA key file is copied from the source environment to beadded to the target environment. ldap\_additional\_properties.xml If you use a federated repository and an unencrypted LDAP connection in thesource environment, user-defined additional properties of the LDAP server are copied from the sourceenvironment to the output directory, where they are later used automatically to create the targetenvironment.Restriction: If you extend the federated repository to use a custom loginproperty (such as userPrincipalName ) in addition to the defaultuid property in the source environment, LDAP is not configured for the targetenvironment, with the following warning: CWMCB0600W: LDAP could not be configured! You mayconfigure LDAP separately after BPMConfig has terminated successfully. If you see thiswarning, manually configure LDAP with the login properties you want to use after the migration iscomplete. ProcessServer\_100SourceCustomMerged.xml andPDW\_100SourceCustomMerged.xml If you have XML configuration properties files, they are copied from thesource environment. The exported configuration files are merged and renamed to101CustomMigrated.xml in the target environment. Application-config-bpc.xml andresources-bpc.xml If you have Business Process Choreographer that are configured in the sourceenvironment, the configuration files are copied from the source environment to the output directory,where they are later used automatically to create the target environment. Support-config-bpc.xml If you have Business Process Choreographer Archive Manager configured on thesupport cluster in the source environment, the configuration is copied from the source environmentto the output directory, where it is later used automatically to create the targetenvironment.
    - BPMConfig.sh -export -profile
DmgrProfile -de DeploymentEnvironment1 -outputDir /home/user\_name/DE1ConfigFolder
    - BPMConfig.bat -export -profile
DmgrProfile -de DeploymentEnvironment1 -outputDir C:\DE1ConfigFolder

| Sample name                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DE\_name.properties                                                        | This properties file contains the configuration properties from your source environment. You use this file when you configure the target environment. For more information about the configuration properties, see the topic Configuration properties for the BPMConfig command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| fileRegistry.xml                                                          | If you use a file-based user registry, the user registry file is copied from the source environment to be added to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ltpa.jceks                                                                | If you use LTPA, the LTPA key file is copied from the source environment to be added to the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ldap\_additional\_properties.xml                                            | If you use a federated repository and an unencrypted LDAP connection in the source environment, user-defined additional properties of the LDAP server are copied from the source environment to the output directory, where they are later used automatically to create the target environment.Restriction: If you extend the federated repository to use a custom login property (such as userPrincipalName) in addition to the default uid property in the source environment, LDAP is not configured for the target environment, with the following warning: CWMCB0600W: LDAP could not be configured! You may configure LDAP separately after BPMConfig has terminated successfully. If you see this warning, manually configure LDAP with the login properties you want to use after the migration is complete. |
| ProcessServer\_100SourceCustomMerged.xml and PDW\_100SourceCustomMerged.xml | If you have XML configuration properties files, they are copied from the source environment. The exported configuration files are merged and renamed to 101CustomMigrated.xml in the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Application-config-bpc.xml and resources-bpc.xml                          | If you have Business Process Choreographer that are configured in the source environment, the configuration files are copied from the source environment to the output directory, where they are later used automatically to create the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Support-config-bpc.xml                                                    | If you have Business Process Choreographer Archive Manager configured on the support cluster in the source environment, the configuration is copied from the source environment to the output directory, where it is later used automatically to create the target environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

2 Use the Business Automation Workflow Configuration editor to update the exportedproperties to match your requirements for the new deployment environment. Important: Tip: In addition to the configuration exported by the BPMConfig–export command, you can use the exportWASConfig.py script toexport customized WebSphere® ApplicationServer configuration,including data sources, authentication aliases, and Secure Sockets Layer (SSL) settings, from yoursource environment. You can refer to this configuration to update the target environment manually oruse the importWASConfig.py script to import the configuration automatically afterthe target environment is configured.

- Make sure that the database information for each component points to a new database schema,
because database schemas must not be shared between deployment environments.
- Make sure that you use a unique cell name for the new deployment environment, because duplicate
cell names can cause conflicts.
3. Save the updated properties file, keeping it in the same
output directory. Copy the output directory to the computer where
you want to create the new deployment environment.
4. Install Business Automation Workflow on the computer where you
want to create the new deployment environment.
5. Create the empty databases for your new Business Automation Workflow deployment environment, as described in the
appropriate topic for your product edition, operating system, and database type. 
For example, when creating an Business Automation Workflow
environment with DB2 databases on Linux, follow the steps in Creating Db2 databases in a network deployment environment on Linux.
6. Validate that all database connections are correctly configured. 
BPMConfig -validate -db output\_directory/updated\_properties\_file
7. Create the new deployment environment. BPMConfig -create -de output\_directory/updated\_properties\_file
In the following example, the exported DE1.properties file
and all the other files from table 1 are in the current directory.BPMConfig -create -de DE1.properties
In
the following example, the exported DE2.properties file
and all the other files from table 1 are in the  /usr/joe/De2CfgBackup directory.BPMConfig -create -de /usr/joe/De2CfgBackup/DE2.properties
8. If you set the bpm.de.deferSchemaCreation property to
true, create the database schemas manually using the generated scripts and
run the bootstrapProcessServerData command.
9 Complete other configuration customization. You might need to do other customization on the cloned environment to make it consistent withthe source. For example:

- Copy customized data sources or authentication aliases.
- Copy business space customization.
- Copy other services that the Business Automation Workflow system needs to integrate
with.

## Results

## Related tasks

- Testing the IBM Business Automation Workflow upgrade
- Migrating IBM Business Automation Workflow to new hardware

## Related information

- Configuring your environment with the IBM Business Automation Workflow Configuration editor
- BPMConfig command-line utility
- exportWASConfig.py script
- importWASConfig.py script