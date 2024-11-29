<!-- image -->

# Configuring Business Process Archive Manager

## About this task

You
can configure the Business Process Archive Manager only on the support
cluster of a three-cluster topology of an Advanced or AdvancedOnly deployment
environment. When you configure the Business Process Archive Manager,
a Business Process Archive Explorer is also configured.

## Procedure

1 If you are updating your deployment environment to addthe Business Process Archive Manager, ensure that the configurationproperties file correctly reflects the topology of the IBM BPM deploymentenvironment by exporting the configuration properties file using the BPMConfig command. The configuration properties file is named deployment\_environment .properties (where deployment\_environment isthe name of the deployment environment). The file is located in theoutput directory that you specify when you run the command.Note: Ifthere is only one deployment environment in the WebSphere cell, youcan omit the -de option.
    - On Microsoft Windows operating systems, run the following BPMConfig.bat command:install\_root\bin\BPMConfig.bat -export -profile deployment\_manager\_profile\_name [-de deployment\_environment\_name] -outputDir path\_to\_configuration\_files
    - On Linux and UNIX-based operating systems, run the following BPMConfig.sh command:install\_root/bin/BPMConfig.sh -export -profile deployment\_manager\_profile\_name [-de deployment\_environment\_name] -outputDir path\_to\_configuration\_files
2 Open your deployment environment properties file in aneditor. Tip: For more informationabout possible keys and values for the BPCArchive component,see the appropriate properties file.

- install\_root/BPM/samples/config/advanced/Advanced-PC-ThreeClusters-DB2.properties
- install\_root\BPM\samples\config\advanced\Advanced-PC-ThreeClusters-DB2.properties
3. Add the archive database to the support cluster. For
example,  if cluster 3 is the support cluster, add an entry that is
similar to the following example:bpm.de.cluster.3.db=PerformanceDb,ArchiveDb
4. Add the definition of the archive database. For
example, for a DB2 database named BPARCDB,
if the next free database index is 5, add entries
that are similar to the following example.bpm.de.db.5.name=ArchiveDb
bpm.de.db.5.dbCapabilities=BPCArchive
bpm.de.db.5.type=DB2
bpm.de.db.5.hostname=localhost
bpm.de.db.5.portNumber=50000
bpm.de.db.5.databaseName=BPARCDB
bpm.de.db.5.schema=db2admin
bpm.de.db.5.roleMapping.1.name=DbUser
bpm.de.db.5.roleMapping.1.alias=BPM\_DB\_ALIAS
bpm.de.db.5.roleMapping.2.name=DbUserXAR
bpm.de.db.5.roleMapping.2.alias=BPM\_DB\_ALIASTip: Because
the purpose of the Business Process Archive Manager is to reduce the
size of the runtime database, make sure that BPARCDB is
a separate database from the database that Business Process Choreographer
uses.
5 Create or update the deployment environment.

- If you are creating your deployment environment for the first
time, after you make all your changes and update the properties file,
run the BPMConfig -create command. For example:BPMConfig -create -de DE1.properties
- If you are updating your deployment environment to add theBusiness Process Archive Manager, complete the following steps.
    1. Run the BPMConfig -upgrade -component BPCArchive command.
You must run the command on the deployment manager node. The following
example shows how to run the command:BPMConfig -upgrade -de DE1.properties -component BPCArchiveAfter
you run the command, synchronize the nodes so that the managed nodes
obtain the latest configuration file changes.
    2 Run the database script.
        1. The database script is in dmgr\_profile\_root/dbscripts\_upgrade.
The script is named createSchema\_Advanced.sql.
        2. Copy the script to your database machine and run the script. For
example:db2 -tf createSchema\_Advanced.sql
3. Restart the deployment environment.

## Results