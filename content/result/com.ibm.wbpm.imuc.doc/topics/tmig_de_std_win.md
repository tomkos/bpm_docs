# Configuring IBM Business Automation Workflow 24.x

After you install IBM Business Automation
Workflow
24.x and use the
IBM Business Automation
Workflow
Configuration editor to modify the properties file that is used to configure the new topology, run
the BPMConfig -create command to create the profiles and network deployment
environment. The BPMConfig command is required for migration.

Figure 1. Sample environment after 24.x is configured on
the target. The source environment is running and transferring data to and from its databases. The
target is not running but contains a deployment environment. The deployment environment has three
clusters and is configured across two nodes.

<!-- image -->

<!-- image -->

## About this task

- Creates the deployment manager node based on the values
in the deployment manager properties file and starts the deployment
manager.
- For each node specified in the configuration properties
file, creates a managed node based on the specified values.
- Federates each managed node and adds the node to the
deployment environment.
- Generates the deployment environment.
- Creates any profiles specified in the configuration
properties file that do not already exist.
- Migrates configuration data, such as XML configuration
properties files and fileRegistry.xml.
- Generates SQL scripts for upgrading and creating the
databases.

## Procedure

For each deployment environment in your
target environment, complete the following steps:

1. Make sure that you are using the properties
file that you generated with the
BPMConfig -migrate command to configure your target
environment. You can check either in the IBM Business Automation
Workflow Configuration
editor or in the properties file itself. The properties with the bpm.de.sourceInfo
prefix are taken from your source environment and are correct if you
are using the correct properties file.

Table 1. 

Property
Editor
Name in properties file

Source version, such as 7.5.1.0
Check the title at the top
bpm.de.sourceInfo.versionInfo

Product, such as Express
Check the title at the top
bpm.de.sourceInfo.productType

Workflow Server customization file, such as
ProcessServer\_100SourceCustomMerged.xml
Check the end of the Summary page
bpm.de.sourceInfo.psCustomFile

Performance Data Warehouse customization file,
such as
PDW\_100SourceCustomMerged.xml
Check the end of the Summary page
bpm.de.sourceInfo.pdwCustomFile
2 Oracle and SQL Serverdatabase JDBC drivers that previously came with Business Automation Workflow havebeen removed. If you were using these default drivers, or driverslocated in the${WAS\_INSTALL\_ROOT}/jdbcdrivers/Oracle or${WAS\_INSTALL\_ROOT}/jdbcdrivers/SQLServer directories,you must reconfigure your JDBC drivers before migrating.
    1. If you have not already done so, on the Business Automation Workflow deployment
manager and every managed node machine, create a custom directory
for your JDBC driver and copy the required JDBC driver JAR file into
it.  For example, you could create the following custom
directory:temp/jdbcdrivers/Oracle
    2. Set the JDBC driver path (the bpm.dmgr.jdbcDriverPath property)
for your deployment manager and all nodes, or for your stand-alone
server, to point to the directory where your JDBC driver is installed.
3. If you are migrating from IBM Business Process Manager
Express,
set bpm.de.deferSchemaCreation to true.
4. Optional: If you are using a DB2
for z/OS database and migrating to Business Automation Workflow, you
can enable the optional component Business Automation Workflow document
store for DB2 for z/OS on your target environment. For
instructions, see Configuring the BPM document store for Db2 on z/OS.
5 Run the BPMConfig commandwith the -create -de option and the propertiesfile that you just edited. The command creates the deployment managerprofile and generates the deployment environment. Use the following syntax:install\_root \bin\BPMConfig -create -de path\_to\_properties\_file Tip: If you run BPMConfig -validate -performanceTuningproperties\_file before running the -create command,the command validates all performance tuning parameters in the propertiesfile. Creating the deployment environment takes some time.After the deployment environment is created, the command generatesSQL scripts for upgrading and creating the databases and puts theminto the correct directories for you, as well as updating the securityproperties and moving the properties that were exported from the XMLcustomization files to the WebSphere® ApplicationServer configurationfiles. You can follow the progress of the command by reading the output,which includes the following actions: Note: If you see an error about invalid characters in a username or password, change them to valid characters. Refer to the listof valid characters in the table in Business Automation Workflow security roles . Afterall actions are completed, you see a message that the command completedsuccessfully.

```
install\_root\bin\BPMConfig -create -de path\_to\_properties\_file
```

- Creating the deployment manager profile
- Starting the deployment manager
- Creating the managed node profiles
- Federating the managed nodes
- Generating SQL files for upgrading the databases
- Performing security configuration
- Creating clusters
- Creating cluster members
- Synchronizing the nodes
- Stopping the deployment manager

After
all actions are completed, you see a message that the command completed
successfully.

6 If one or more managed nodes are ondifferent computers from the deployment manager, complete the followingsteps:

1. Start the deployment manager.
2. Check the soap port of the deployment manager and update
the value of
bpm.dmgr.soapPort in the properties file.
3. On each of the other computers that has one or more
managed nodes, run the
BPMConfig command, passing it the name of the properties
file. The managed node profiles are created and federated
into the deployment manager cell.
For each cluster member in the properties file, BPMConfig adds
http and https ports to the virtual
hosts list. Check the virtual hosts list to make sure that the assigned
ports are acceptable.
4. Stop the deployment manager after you have configured
the target environment.

## What to do next

Do not start the
new deployment environment until after you have upgraded the databases.

## Related information

- BPMConfig command-line utility
- Configuration properties for the BPMConfig command
- exportWASConfig.py script