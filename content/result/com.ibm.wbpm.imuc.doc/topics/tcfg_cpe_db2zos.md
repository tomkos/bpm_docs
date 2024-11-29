# Configuring IBM Business Automation
Workflow case management for
Db2 for z/OS

## About this task

First, you export the properties file using the BPMConfig -export -profile
command and append the case management related attributes. Then you use the BPMConfig
-upgrade -de -component command to configure case management and generate the corresponding
database scripts. Finally, you use the db2 command to run the auto-generated SQL
files on your Db2 database machine. The detailed configuration steps follow.

Because the BPMConfig command is necessary for this configuration, see BPMConfig command-line utility to learn more about this command.

## Procedure

After you create the deployment environment, complete the following
steps:

1 Export the configuration properties file using the BPMConfig command. Ensure that the configuration properties file correctly reflects the topology of the IBM Business AutomationWorkflow deployment environment. The configuration properties file is nameddeployment\_environment .properties (wheredeployment\_environment is the name of the deploymentenvironment). The file is located in the output directory that you specify when you run the command.If there is only one deployment environment in the WebSphere cell, you can omit the-de option.
    - On Microsoft Windows operating systems, run the following BPMConfig.bat
command:install\_root\bin\BPMConfig.bat -export -profile deployment\_manager\_profile\_name [-de deployment\_environment\_name] -outputDir path\_to\_configuration\_files
    - On Linux and UNIX-based operating systems, run the following BPMConfig.sh
command:install\_root/bin/BPMConfig.sh -export -profile deployment\_manager\_profile\_name [-de deployment\_environment\_name] -outputDir path\_to\_configuration\_files
2. Open the deployment environment properties file that you just exported in an editor. Make sure
that you replace the values wherever you see "TO\_BE\_REPLACED" in the file.
3 Specify the case management components on the application cluster. There are differences depending on whether you use an external ECM system instead of theembedded ECM.

- If you are using the embedded ECM system:
    - In a Single Cluster topology, add entries that are similar to those in the following
example, where cluster 1 has both application and support capabilities and the next component index
number is
2:bpm.de.cluster.1.capability.1.component.2.name=EmbeddedECM
bpm.de.cluster.1.capability.1.component.3.name=CMIS
bpm.de.cluster.1.capability.1.component.4.name=ContentNavigator
bpm.de.cluster.1.capability.1.component.5.name=CaseManager
bpm.de.cluster.1.capability.3.component.1.name=DocumentStoreAdmin
    - In a Three Cluster topology, add entries that are similar to those in the following
example, where cluster 1 has application capability and the next available component index number is
2, and where cluster 3 has support capability and the next available component index number is
1:bpm.de.cluster.1.capability.1.component.2.name=EmbeddedECM
bpm.de.cluster.1.capability.1.component.3.name=CMIS
bpm.de.cluster.1.capability.1.component.4.name=ContentNavigator
bpm.de.cluster.1.capability.1.component.5.name=CaseManager
bpm.de.cluster.3.capability.1.component.1.name=DocumentStoreAdmin
- If you are using an external ECM system, the updates are the same for a Single Cluster or
Three Cluster topology. Add entries that are similar to those in the following
example:bpm.de.useExternalCPE=true

bpm.de.cluster.1.capability.1.component.2.name=CMIS
bpm.de.cluster.1.capability.1.component.3.name=ContentNavigator
bpm.de.cluster.1.capability.1.component.4.name=CaseManager
4 Add the related database definitions to the application cluster that uses the same clusterindex as in the previous step. Modify the entry in the exporteddeployment\_environment.properties file to add the corresponding database names asshown in the following examples. The database names are IcnDb for the IBM ContentNavigator , DosDb for theDesign Object Store, and TosDb for the Target Object Store.

- If you are using an embedded ECM
system:bpm.de.cluster.1.db=SharedDb,PerformanceDb,EmbeddedEcmDb,IcnDb,TosDb,DosDb
- If you are using an external ECM
system:bpm.de.cluster.1.db=SharedDb,PerformanceDb,IcnDb
5 Add the detailed definitions of the case management related databases, based on your localDb2 for z/OS database. For an embedded ECMsystem, add the properties for EmbeddedEcmDb , IcnDb ,TosDb , and DosDb . For an external ECM system, add only theproperties for IcnDb .

- If you are using an embedded ECM system:
    - For the EmbeddedEcmDb database, add entries similar to those in the following example, where the
Db2 for z/OS database is named ECMDBLH and
the next free database index is 4: Important: The schema name of the EmbeddedEcmDb
should be set to the same value as  bpm.de.authenticationAlias.2.user in the
exported properties
file.
bpm.de.db.4.name=EmbeddedEcmDb
bpm.de.db.4.dbCapabilities=EmbeddedECM
bpm.de.db.4.type=DB2zOS
bpm.de.db.4.hostname=9.125.72.29
bpm.de.db.4.portNumber=480
bpm.de.db.4.connectionLocation=LOCDB11
bpm.de.db.4.databaseName=ECMDBLH
bpm.de.db.4.schema=TUSER03
bpm.de.db.4.vcat=DC12
bpm.de.db.4.bptable4k=BP1
bpm.de.db.4.bptable8k=BP8K0
bpm.de.db.4.bptable16k=BP16K0
bpm.de.db.4.bptable32k=BP32K1
bpm.de.db.4.bpindex=BP2
bpm.de.db.4.bplob4k=BP3
bpm.de.db.4.volumes='*'
bpm.de.db.4.stogrp=ECMCT
bpm.de.db.4.roleMapping.1.name=DbUser
bpm.de.db.4.roleMapping.1.alias=BPM\_DB\_ALIAS
bpm.de.db.4.roleMapping.2.name=DbUserXAR
bpm.de.db.4.roleMapping.2.alias=BPM\_DB\_ALIAS
    - For the IcnDb database, add entries similar to those in the following example, where the
Db2 for z/OS database is named ICNDBLH and
the next free database index is
5:bpm.de.db.5.name=IcnDb
bpm.de.db.5.dbCapabilities=ContentNavigator
bpm.de.db.5.type=DB2zOS
bpm.de.db.5.hostname=9.125.72.29
bpm.de.db.5.portNumber=480
bpm.de.db.5.connectionLocation=LOCDB11
bpm.de.db.5.databaseName=ICNDBLH
bpm.de.db.5.schema=ICNLH
bpm.de.db.5.vcat=DC12
bpm.de.db.5.bptable4k=BP0
bpm.de.db.5.bptable8k=BP8K0
bpm.de.db.5.bptable16k=BP16K0
bpm.de.db.5.bptable32k=BP32K
bpm.de.db.5.bpindex=BP2
bpm.de.db.5.bplob4k=BP3
bpm.de.db.5.volumes='*'
bpm.de.db.5.stogrp=ICNCT
bpm.de.db.5.roleMapping.1.name=DbUser
bpm.de.db.5.roleMapping.1.alias=BPM\_DB\_ALIAS
bpm.de.db.5.roleMapping.2.name=DbUserXAR
bpm.de.db.5.roleMapping.2.alias=BPM\_DB\_ALIAS
    - For the TosDb database, add entries similar to those in the following example, where the
Db2 for z/OS database is named TOSDBLH, and
the next free database index is 6:
bpm.de.db.6.name=TosDb
bpm.de.db.6.dbCapabilities=TargetObjectStore
bpm.de.db.6.type=DB2zOS
bpm.de.db.6.hostname=9.125.72.29
bpm.de.db.6.portNumber=480
bpm.de.db.6.connectionLocation=LOCDB11
bpm.de.db.6.databaseName=TOSDBLH
bpm.de.db.6.schema=TOSLH
bpm.de.db.6.vcat=DC12
bpm.de.db.6.bptable4k=BP1
bpm.de.db.6.bptable8k=BP8K0
bpm.de.db.6.bptable16k=BP16K0
bpm.de.db.6.bptable32k=BP32K1
bpm.de.db.6.bpindex=BP2
bpm.de.db.6.bplob4k=BP3
bpm.de.db.6.volumes='*'
bpm.de.db.6.stogrp=TOSCTLH
bpm.de.db.6.roleMapping.1.name=DbUser
bpm.de.db.6.roleMapping.1.alias=BPM\_DB\_ALIAS
bpm.de.db.6.roleMapping.2.name=DbUserXAR
bpm.de.db.6.roleMapping.2.alias=BPM\_DB\_ALIAS
    - For the DosDb database, add entries similar to those in the following example, where the
Db2 for z/OS database is named DOSDBLH, and
the next free database index is 7:
bpm.de.db.7.name=DosDb
bpm.de.db.7.dbCapabilities=DesignObjectStore
bpm.de.db.7.type=DB2zOS
bpm.de.db.7.hostname=9.125.72.29
bpm.de.db.7.portNumber=480
bpm.de.db.7.connectionLocation=LOCDB11
bpm.de.db.7.databaseName=DOSDBLH
bpm.de.db.7.schema=DOSLH
bpm.de.db.7.vcat=DC12
bpm.de.db.7.bptable4k=BP1
bpm.de.db.7.bptable8k=BP8K0
bpm.de.db.7.bptable16k=BP16K0
bpm.de.db.7.bptable32k=BP32K1
bpm.de.db.7.bpindex=BP2
bpm.de.db.7.bplob4k=BP3
bpm.de.db.7.volumes='*'
bpm.de.db.7.stogrp=DOSCTLH
bpm.de.db.7.roleMapping.1.name=DbUser
bpm.de.db.7.roleMapping.1.alias=BPM\_DB\_ALIAS
bpm.de.db.7.roleMapping.2.name=DbUserXAR
bpm.de.db.7.roleMapping.2.alias=BPM\_DB\_ALIAS
- If you are using an external ECM system:

- For the IcnDb database, add entries similar to those in the following example, where the
Db2 for z/OS database is named ICNDBLH and
the next free database index is
4:bpm.de.db.4.name=IcnDb
bpm.de.db.4.dbCapabilities=ContentNavigator
bpm.de.db.4.type=DB2zOS
bpm.de.db.4.hostname=9.125.72.29
bpm.de.db.4.portNumber=480
bpm.de.db.4.connectionLocation=LOCDB11
bpm.de.db.4.databaseName=ICNDBLH
bpm.de.db.4.schema=ICNLH
bpm.de.db.4.vcat=DC12
bpm.de.db.4.bptable4k=BP0
bpm.de.db.4.bptable8k=BP8K0
bpm.de.db.4.bptable16k=BP16K0
bpm.de.db.4.bptable32k=BP32K
bpm.de.db.4.bpindex=BP2
bpm.de.db.4.bplob4k=BP3
bpm.de.db.4.volumes='*'
bpm.de.db.4.stogrp=ICNCT
bpm.de.db.4.roleMapping.1.name=DbUser
bpm.de.db.4.roleMapping.1.alias=BPM\_DB\_ALIAS
bpm.de.db.4.roleMapping.2.name=DbUserXAR
bpm.de.db.4.roleMapping.2.alias=BPM\_DB\_ALIAS
6. Add the Case Manager properties to the exported
deployment\_environment.properties file, and modify them based on
your environment settings.
For example:###########################
# Case Manager Properties #
###########################
# The network directory shared among multiple process servers in the deployment environment.
bpm.de.caseManager.networkSharedDirectory=${WAS\_INSTALL\_ROOT}/CaseManagement/properties
bpm.de.caseManager.formsType=eForms only
bpm.de.caseManager.ibmFormsDirectory=
bpm.de.caseManager.ibmFormsRenderApp=autoDetect
bpm.de.caseManager.ibmFormsTranslatorURL=http://localhost:8085/translator
bpm.de.caseManager.enableVCS=false
bpm.de.caseManager.vcsSandboxPath=
bpm.de.caseManager.vcsAdditionalParameters=
bpm.de.caseManager.vcsHeartbeatInterval=60
bpm.de.caseManager.vcsCommitTimeout=120
bpm.de.caseManager.vcsDeliverTimeout=600
7. On the deployment manager computer, validate that all database connections are correctly
configured by running the  BPMConfig -validate command. 
Use the following
syntax:install\_root/bin/BPMConfig -validate -db configuration\_properties\_filewhere
configuration\_properties\_file is the full path and name of your
deployment\_environment.properties file.  The command uses
the database properties and the database-related authentication alias properties (including
passwords) from the configuration properties file. If necessary, you can update these database
properties in the file.
8. Stop the IBM Business Automation Workflow environment, including
the deployment environment, node agent, and deployment manager.
9. Upgrade the deployment environment to add the Case Manager component, by running the following
command on the deployment manager. 
BPMConfig -upgrade -de DE1.properties -component CaseManager
After you run the command, the nodes are synchronized so that the managed nodes obtain the latest
configuration file changes.
10 Create the database objects for the upgraded databases by running the database scriptsgenerated indeployment\_manager\_profile /dbscripts\_upgrade/cell\_name .deployment\_environment\_name /DB2zOS/upgrade\_database\_name subdirectories on the IBM Business AutomationWorkflow system. Each upgrade\_database\_name subdirectory contains oneor more of these files, which you must run in the following order:

1. createDatabase.sql
2. createTablespace\_Advanced.sql
3. createSchema\_Advanced.sql
11. Restart the deployment environment.
12. If you are using an external ECM, follow the instructions in Configuring an existing external Content Platform Engine.
13. Run the createObjectStoreForContent command to create the design object store,
target object store, and other necessary items in the embedded Content Platform
Engine. If you have trouble, see createObjectStoreForContent fails to run.
14. See Configuring your system for case management for further instructions.