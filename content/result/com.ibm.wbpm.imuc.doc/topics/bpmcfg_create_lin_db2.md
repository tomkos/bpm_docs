# Creating profiles, network deployment environments and database
tables using the BPMConfig command

## Before you begin

Before you create a deployment environment using the
BPMConfig command-line utility, you may need to manually create all of the
databases that are specified in the properties file. Although the BPMConfig
command can create the database schema and tables, it cannot create the databases. The databases
must be created before the tables are created (and before the servers are started). Depending on the
value that is set for the bpm.de.deferSchemaCreation property, the database
schema and tables can be created when the BPMConfig command is run or they can be
created after the command is run. Information about the
bpm.de.deferSchemaCreation property is found in the About this task
section.

## About this task

- Creates any local profiles specified in the
configuration properties file that do not already exist.
- Creates the deployment manager node based on the values in the
deployment manager properties file and starts the deployment manager.
- For each node specified in the configuration properties file,
creates a managed node based on the specified values.
- Federates each managed node and adds the node to the deployment
environment.
- Generates the deployment environment.
- If the properties file that is used has the parameter bpm.de.deferSchemaCreation set
to false, then the database tables are also created
when you run the command.
- If the bpm.de.deferSchemaCreation property
in the configuration properties file is set to true,
then only the scripts for creating the database tables are generated.
In this case, the database tables need to be created separately using
these scripts, and the bootstrapProcessServerData bootstrap
utility will need to be run manually to load the Process database
with system information.Tip: If you run the BPMConfig command
to generate the database scripts instead of creating the actual tables,
you can pass along these scripts to your database administrator to
review and run the scripts.

## Procedure

To create the deployment environment for the first time,
complete the following steps:Note: The value of the
deployment environment type must be Process Center (PC) (for Workflow Center) or Process Server (PS)
(for Workflow Server).

1. If you previously ran the BPMConfig command
with the -create -sqlfiles -outputDir parameters
to generate the database scripts that are used to create your databases,
you should already have a properties file.
Verify that the value of the bpm.de.deferSchemaCreation property has been
set, and then go to step 5 and complete the
remaining steps.
However, if you do not yet have a
customized properties file that contains the configuration settings
for your profiles, deployment environment, and databases, complete
all of the following steps.
2. On the computer where you want to
create the deployment environment, locate the appropriate sample properties
file: BPM\_Home/BPM/samples/config.
3 Find the sample properties file that most closely represents your targetdeployment environment and make a copy of this file. For each of the different product configurations, there is a differentfolder containing sample configuration files. For example, for configuring anAdvanced , AdvancedOnly , or Standard deploymentenvironment, there is an advanced , advancedonly , orstandard folder containing a set of sample configuration properties files. For configuring case management to use an externalContent Platform Engine , there is anexternalcpe folder . Forconfiguring case management to use an external IBM® ContentNavigator , there is anexternalicn folder. Within each folder, there is a set of files that arespecific to the different database types and configuration environments. The sample files are namedaccording to the following format:de\_type [-environment\_type ]-topology -database\_type [-suffix ] ,where: For example, the sample configuration properties file forconfiguring Advanced deployment environments with Workflow Server in a single cluster topology using a DB2database is called Advanced-PS-SingleCluster-DB2.properties .
    - de\_type can be set to Advanced,
AdvancedOnly, or Standard.Restriction: IBM Business Automation
Workflow Enterprise Service Bus
supports only the AdvancedOnly deployment environment.
    - environment\_type can be set to PS for Workflow Server or PC for Workflow Center. This variable is not used if
de\_type is AdvancedOnly.
    - topology can be set to SingleCluster or
ThreeClusters.
    - database\_type can be set to DB2, DB2zOS,
Oracle, or SQLServer.
    - suffix can be set to -WinAuth for an
SQL Server database.
4. Modify your version
of the properties file so that the values correspond to your own configuration. 
When modifying the sample properties file,
use the guidance provided within the file for specifying values. 
When you are configuring a Workflow Server
environment to use Workflow Center remotely, you must change the default value for the
psProcessCenterHostname property from local host to a valid
host name. If you are configuring an offline Workflow Server and the value for
bpm.de.psOffline is set to true, then you do not need to specify a value for the
psProcessCenterHostname property. Note: Your modified properties file must use
UTF-8 encoding. 

Do not add any custom properties to this
file when you perform your modifications or the BPMConfig command will fail when
it is run.
If you need to use a backslash character (\) in
your properties file, you must use an escape backslash before it; for example,
bpm.dmgr.installPath=c:\\IBM\\BPM\_V23.0.2.
If
you are configuring a three-cluster setup that is based on the Advanced or AdvancedOnly template,
and you want your deployment environment to include the optional Business
Process Archive Manager, include the properties file entries that
are described in Configuring Business Process Archive Manager.
For more information about the available properties,
read the comments in the sample files, or see the BPMConfig command-line utility and the
sample property file descriptions in Configuration properties for the BPMConfig command.
5. Run the BPMConfig command
on the computer that has the deployment manager, passing it the name
of the properties file you created. For
example:install\_root/bin/BPMConfig -create -de my\_environment.properties Tip: You can also use the BPMConfig command
to add cluster members by running the following command syntax:BPMConfig -create -clusterMembers properties\_file
6. Start the deployment manager. For example: To start the node and
manager on the same machine at the same time, use the below BPMConfig command.  
BPMConfig -start <properties file>
Run the BPMConfig command on each computer that has one or more
managed nodes, passing it the name of the same properties file.The managed node
profiles are created and federated into the deployment manager cell. Only one node profile can be
federated to the deployment manager at a time. Ensure that you are running only one
BPMConfig command at a time.Note: For each node that is to be configured on a
different machine from the deployment manager, check the soap port of the deployment manager and
update the value of bpm.dmgr.soapPort in the properties file before running
BPMConfig on the node.

Note: For each cluster member in the properties file,
BPMConfig adds http and https ports to the
virtual hosts list. Check the virtual hosts list after running BPMConfig to make
sure that the assigned ports are acceptable.
7. Optional: If you plan to
use applications with advanced content or that have been imported
into IBM Integration Designer and you are adding more than one deployment
environments to the cell, provide a way to distinguish between the
advanced content in these business level applications across the deployment
environments. For information, see the step that describes
how to set the AdvancedDeploymentDEScoped property
in Isolating deployment environments.

## What to do next

If you ran BPMConfig with the
deferSchemaCreation set to true, then you must create
your database tables and if your environment includes the ProcessServer
component, you must also load the Process database. To create the database, run the SQL scripts that
are generated by the BPMConfig command. To load the Process database, run the
bootstrapProcessServerData utility. For more information see the related task
link for running the generated scripts for creating database tables. After you have created your
deployment environment and your database tables, you can start the deployment manager, node agents,
and clusters by running the BPMconfig command with the
-start action from the deployment manager computer. If you are
creating an Advanced or AdvancedOnly deployment
environment, the deployment manager and node agents need to be restarted for the cell scoped
configuration to take effect. This is only required for the first deployment environment with
Advanced or AdvancedOnly capabilities.