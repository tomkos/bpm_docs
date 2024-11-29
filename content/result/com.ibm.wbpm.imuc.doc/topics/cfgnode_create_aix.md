# Creating the deployment environment using the configureNode
command

You can use the configureNode command
to create a typical network deployment environment. The goal of this
command is to provide a ready-to-use environment. The only parameters
that can be customized are provided in a properties file.

## Before you begin

- Make sure that the username and schema exist before the configuration
is done. The schema value should be the default schema for the user
chosen.
- If connections to the database will be made by the current Windows
user that the server is running under, the SQL Server must have Windows
authentication mode or SQL Server and Windows
 Authentication mode enabled, as specified through Microsoft
SQL Server Management Studio.

## About this task

The configureNode command
uses default ports to create the deployment manager. You cannot customize
the ports using this command. The parameters listed in the sample
files are the only parameters that can be customized. Make sure that
no other profiles that are configured with default ports are started
on the same machine.

- A single cell environment
- The environment contains the number of cluster members that you
specify in the properties file
- The environment uses the Remote Messaging, Remote Support, andWeb topology pattern, which includes the following four clusters:
    - Messaging infrastructure cluster
    - Supporting infrastructure cluster
    - Application deployment target cluster
    - Web application cluster

- Creates the deployment manager node based on the values in the
deployment manager properties file and starts the deployment manager.
- Creates the deployment environment definition.
- Creates a custom node based on the values in the custom node properties
file.
- Federates the node and adds the node to the deployment environment.
- Generates the deployment environment.
- Creates the database tables. (You must already have created the databases. See Before you
begin for instructions.)
- Runs the bootstrap utility to load the Workflow Server database
with system information.
- Configures Business Space and Heritage Process Portal (deprecated)on the
web application cluster.

## Procedure

To create the deployment environment
for the first time, complete the following steps:

1. On the machine where you want to
create the deployment environment, locate the sample properties file: install\_root/util/ndUtils/samples/.
2. Copy the sample files and modify
the files to reflect your environment.
For example, for a deployment manager for IBM® BPM Advanced for Process
Server, choose the sample\_adv\_pc\_dmgr.properties file.
For each database that you want to
create, copy the database parameters section and specify the database
name, user name, password, and schema name. The Workflow Server database,
Performance Data Warehouse database, and Common database are required,
and they must have different names. For IBM BPM Advanced, the
Business Process Choreographer database is also required.
For
more information about the available properties, read the comments
in the sample files, or see the configureNode command
reference and the examples.Restriction: The parameters
listed in the sample files are the only parameters that can be customized.
3 Run the configureNode command,passing it the names of the two files you created. The custom nodefile is optional, but if you do not include it, only the deploymentmanager is created. For example: Note: If you receive the Failed to performSecurity setting update error, check to ensure that the globalIP address has not been appended to 127.0.0.1 localhost inthe hosts file. For example: 127.0.0.1 localhost example.ibm.com .
    - install\_root/util/ndUtils/configureNode.sh
-dmgr\_response my\_dmgr\_response\_file.properties -response node01\_response\_file.properties

## Results

You now have a deployment manager, a custom node, and a deployment
environment that use the Remote Messaging, Remote Support, and Web topology pattern.

Messages are recorded in the file
install\_root/logs/config/configureNode.log.

## Related information

- Topologies of a network deployment environment
- configureNode command-line utility
- Removing a managed node profile from a deployment environment
- Database privileges
- Configuring a proxy server for Process Portal