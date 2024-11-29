# Creating profiles, network deployment environments and database
tables using the BPMConfig command

## Before you begin

You must have installed the product. You must
also have created all the users that you specify in the properties
file.

## About this task

- Creates any local profiles specified in the configuration properties file that
do not already exist.
- Creates the deployment manager node based on the values in the deployment manager properties
file and starts the deployment manager.
- For each node specified in the configuration properties file, creates a managed node based on
the specified values.
- Federates each managed node and adds the node to the deployment environment.
- Generates the deployment environment.
- Generates the scripts that you can use to create the database
tables.

## Procedure

To create the deployment environment for the first time,
complete the following steps:Note: The value of the
deployment environment type must be Process Center (PC) (for Workflow Center) or Process Server (PS)
(for Workflow Server).

1. On the computer where you want to
create the deployment environment, locate the appropriate sample properties
file: BPM\_Home\BPM\samples\config.
2 Find the sample properties file that most closely represents your target deployment environmentand make a copy of this file. For each of the different product configurations, there is a differentfolder containing sample configuration files. For example, for configuring anAdvanced , AdvancedOnly , or Standard deploymentenvironment, there is an advanced , advancedonly , orstandard folder containing a set of sample configuration properties files. For configuring case management to use an externalContent Platform Engine , there is anexternalcpe folder . Forconfiguring case management to use an external IBM® ContentNavigator , there is anexternalicn folder. Within each folder, there is a set of files that arespecific to the different database types and configuration environments. The sample files are namedaccording to the following format:de\_type [-environment\_type ]-topology -database\_type [-suffix ] ,where: For example, the sample configuration properties file for configuringAdvanced deployment environments with Process Server in a single cluster topologyusing a DB2 for z/OS database is calledAdvanced-PS-SingleCluster-DB2zOS.properties .
    - de\_type can be set to Advanced,
AdvancedOnly, or Standard.Restriction:
IBM Business Automation
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
3 Modify your version of theproperties file so that the values correspond to your own configuration. When modifying the sample properties file, use the guidanceprovided within the file for specifying values. Whenyou are configuring a Workflow Server environment to use Workflow Center remotely, you must change the default value for the psProcessCenterHostname propertyfrom local host to a valid host name. If youare configuring an offline Workflow Server and the value for bpm.de.psOffline isset to true, then you do not need to specify a value for the psProcessCenterHostname property. Note: Yourmodified properties file must use UTF-8 encoding. Additionalnotes for database configuration: Do not add any customproperties to this file when you perform your modifications or the BPMConfig willfail when it is run. For more information about the availableproperties, read the comments in the sample files, or see the BPMConfig command-line utility and thesample property file descriptions in Configuration properties for the BPMConfig command .

When
you are configuring a Workflow Server environment to use Workflow Center
remotely, you must change the default value for the psProcessCenterHostname property
from local host to a valid host name. If you
are configuring an offline Workflow Server  and the value for  bpm.de.psOffline is
set to true, then you do not need to specify a value for the psProcessCenterHostname property.

- By default, the bpm.de.deferSchemaCreation property
in the sample configuration properties file for DB2 for z/OS is set
to true. Do not change this setting, because, for
a z/OS database, you cannot create the database objects at the same
time that the database scripts are generated. After the BPMConfig command
completes, you can run the database scripts to manually create the
database objects at a time that you choose. When bpm.de.deferSchemaCreation is
set to true, the bootstrap utility, which loads the
Process database with system information, also must be run manually.
- Work with your DB2 for z/OS database administrator to establish
good naming conventions for DB2 components such as database names,
storage group names, schema qualifiers, and VSAM catalog names (VCATs).

Do not add any custom
properties to this file when you perform your modifications or the BPMConfig will
fail when it is run.

For more information about the available
properties, read the comments in the sample files, or see the BPMConfig command-line utility and the
sample property file descriptions in Configuration properties for the BPMConfig command.

4 Runthe BPMConfig command on the computer that hasthe deployment manager, passing it the name of the properties fileyou created. BPM\_home \bin\BPMConfig -create -de my\_environment.properties The database SQL scripts are generated in the DMGR\_PROFILE/dbscripts folderby default. These subdirectories also contain a createDatabase.sh script,which you can use to run the database scripts to create the DB2 forz/OS database tables. Note: For eachcluster member in the properties file, BPMConfig adds http and https portsto the virtual hosts list. Check the virtual hosts list after running BPMConfig tomake sure that the assigned ports are acceptable.

```
BPM\_home\bin\BPMConfig -create -de my\_environment.properties
```

- The database scripts that can be used to create the cell-scoped
database are generated in DMGR\_PROFILE\dbscripts\cell\_name\DB2zOS\cell\_database\_name.
- The database scripts that can be used to create the cluster-scoped
database are generated in DMGR\_PROFILE\dbscripts\de\_name\DB2zOS\cluster\_database\_name.
5. Use FTP to transfer all the generated database scripts
to the z/OS system that contains the installation of DB2. Transfer
the createDatabase.sh script as an ASCII text file,
and transfer the database schema files in binary mode.
6. Optional: If you plan to
use applications with advanced content or that have been imported
into IBM Integration Designer and you are adding more than one deployment
environments to the cell, provide a way to distinguish between the
advanced content in these business level applications across the deployment
environments. For information, see the step that describes
how to set the AdvancedDeploymentDEScoped property
in Isolating deployment environments.

## What to do next

After you have created
your deployment environment and your database tables, you can start
the deployment manager, node agents, and clusters by running the BPMconfig command
with the -start action from the deployment manager
computer. If you are creating an Advanced or AdvancedOnly deployment
environment, the deployment manager and node agents need to be restarted
for the cell scoped configuration to take affect. This is only required
for the first deployment environment with Advanced or AdvancedOnly 
capabilities.

## Related information

- Creating and configuring Db2 for z/OS databases after network deployment profile creation on Windows