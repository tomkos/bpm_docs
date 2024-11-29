# Creating the Standard Workflow Server
deployment environment (deprecated)

## Before you begin

- Install the product
- Create the deployment manager profile and the associated nodes
- Ensure that the databases specified in the Database Configuration panel of the
Deployment Environment wizard are already created. The deployment environment
configuration never creates a database. For more information, see the section about creating
databases.
- Make sure that you start all the local and remote nodes that you
want to add in the deployment environment.
- When you create a 3-cluster deployment environment using the DeploymentEnvironment wizard, the process might take a lot of timeto complete. In that case, you can perform one of the following stepsto create the 3-cluster environment:
    - Increase the transaction timeout value using the Deployment Manager
and re-create the deployment environment. For more information, see Preventing timeout and out-of-memory exceptions during installation or deployment.
    - Do not create tables during the Deployment Environment creation.
After creating the environment, create the databases, tables, and
then run the bootstrap command.
- If you are using the Deployment Environment wizard, you can enable
deployment manager trace for details about the deployment creation.
To enable trace for a single run and till the deployment manager restarts,
log in to the administrative console, go to Troubleshooting > Logs and trace > deployment\_manager\_name > Change log detail levels > Runtime, add com.ibm.bpm.config.*=all to the Change
log detail levels text area, and save the changes.

Because the procedure for creating
deployment environments using the Deployment Environment wizard
includes steps for selecting patterns and features, you should read
and understand the information about patterns and features documented
in the planning section.

## About this task

This
task describes the procedure for creating a deployment environment
that is based on a specific pattern and uses the Deployment
Environment wizard. When you complete the configuration,
the database scripts that you can use to configure the databases are
generated.

- Process and Performance Data Warehouse should not use the same database.

## Procedure

Complete the following steps to create the deployment environment.

1. From the administrative console, navigate to the Deployment
Environments page by clicking Servers > Deployment Environments.
2 Launch the Deployment Environment wizard byclicking New on the Deployment Environments page. TheCreate new deployment environment page is displayed. Note: The database provides isolation of internal groups, such as administrators. If the database isshared by two deployment environments, one administrators group is shared between them. When such asituation occurs, both administrators are able to login as administrator for each of the deploymentenvironment.
    1. Enter a unique name for the deployment environment in the Deployment
environment name field.
    2. Enter a user name for the deployment environment administrator in the
Deployment environment administrator user name field.

Note: It is recommended to use a different administrator for each deployment environment and also
the cell administrator.
    3. Enter a password for the deployment environment administrator in the
Password field.
    4. Reconfirm the password in the Confirm password field.
    5. In the Dmgr's JDBC driver folder field, specify the JDBC driver path for
the deployment manager. This folder must contain the JAR files for the JDBC drivers for your
database. 
For DB2, the default value is ${WAS\_INSTALL\_ROOT}/jdbcdrivers/DB2. For
Oracle and SQL Server, there is no default and you must specify a value.
    6. In the Context root prefix field, you can either accept the default
blank (empty) value or you can specify a context root prefix for all web modules in this
environment. If set, the context root prefix must start with a forward slash character (/).
    7. Optional: In the Virtual host list, select a
virtual host to map to all web modules of the Business Automation Workflow applications in the
deployment environment. The default selection is (none).
3. From the Business Automation Workflow Deployment Environment
Type section, select Standard Workflow Server. Features
represent the runtime processing capabilities of your deployment environment.
4 From the Select the deployment environmentpattern section, select a pattern for the deployment environment and clickNext to display the Select Nodes page. The availablepatterns are:

- Single Cluster: The application deployment target includes the messaging
infrastructure and supporting applications.
- Application, Remote Messaging, Remote Support: A separate cluster each
for application deployment, remote messaging, and remote support.
5. On the Select Nodes page, select the nodes that
you want to include in this deployment environment, then click Next to
display the Define Clusters page. 
Select nodes that have the required capabilities for the environment you selected on the IBM BPM
Deployment Environment Features section.
In the JDBC Driver Path field for each node, specify the JDBC driver path
for the deployment manager. This folder must contain the JAR files for the JDBC drivers for your
database. For DB2, the default value is ${WAS\_INSTALL\_ROOT}/jdbcdrivers/DB2.
For Oracle and SQL Server, there is no default and you must specify a value.
Select at least one node for the deployment environment. For high-availability and failover
environments, select at least two nodes. For scalability, you can add more nodes.
6. On the Define Clusters page, assign the
required number of clusters for each node and click Next to display the
Customize Cluster Name and Ports page.

By default one cluster member is assigned on each node for each function. You change the number
by replacing the number in each column. If you are unfamiliar with the different cluster roles and
functions provided by each type of cluster, see Topology types and deployment environment
patterns.

A 0 (zero) value for a node means that the node does not contribute to the selected function,
based on features that you have selected.
7. On the Customize Cluster Name and Ports
page, customize the cluster names or cluster member names for the cluster type. You can use the
default values provided, or customize the cluster details, and click
Next.

Note: You can specify the starting port for the cluster members. The system generates default values
for cluster member names and the starting port. Ensure that the starting port numbers you specify
are at least 20 ports apart. Port numbers are reserved and assigned to each node for the cluster
members using the port number that is specified. If you specify an initial port when you create the
deployment environment, that same initial port specified would be assigned to the cluster member.
For example, if the port number for the first cluster member is 2000, it would use the port numbers
2000, 2001, 2002, and so on. The port number of the second cluster member would be 2020 and the port
numbers would be 2020, 2021, 2022, and so on. The port number of the third cluster member would be
2040. 
If there is already a node on that physical system then there may be port conflicts and
these must be resolved manually by changing the port values.
If you use additional servers
with unique ports, WebSphere® Application
Server
does not automatically configure the virtual host for the server. Specifically, WebSphere Application
Server does not automatically
add the host alias ports to a virtual host. However, you can use the administrative console to add a
new host alias for each of the ports that are used by the new server. For more information, see the
WebSphere Application
Server documentation about
configuring virtual hosts.
8 On the Configure Workflow Server page, set the valuesfor the Workflow Center configuration and click Next .

- Environment nameEnter an environment name
of the Workflow Server.

An environment name is the name by which this server or cluster will be known to a Workflow Center user.
- Environment typeFrom the pull-down
list, select the environment type for the Workflow Server you are configuring.

The environment type refers to how the Workflow Server is used. For example,
in what capacity will the Workflow Server be used -
development, test, staging, or production. Load testing might be done on
a test server, while a staging environment type might be used as a temporary location to host
changes before putting those changes into production. You might specify
Staging as the environment type if the Workflow Server you are configuring,
will be accessed and used to review content and new functionality.
There are four types of
environments available for selection:

Development
Select Development if the server will serve in a development
capacity.
Test
Select Test if the server you are configuring will be used as a testing
environment.
Staging
Select Staging if the server will serve as a staging platform to be used
as a preproduction server.
Production
Select Production  if the server will serve in a production
capacity.
- Use server offlineIndicate whether the
server you are configuring is an offline server. 
An offline server is a Workflow Server that is not connected
to Workflow Center.
Offline servers can still be used when deploying snapshots of process applications.
However the method for deploying process applications to an offline Workflow Server differs from the
method for deploying process applications to an online Workflow Server.
- ProtocolSelect either
http:// or https:// as the connection protocol to
Workflow Center.
- Host name or virtual host in a load-balanced
environmentType the host or virtual host that this Workflow Server needs to communicate
with Workflow Center. Use a
fully qualified host name. In an environment with a load balancer or proxy server between the
Workflow Server and the
Workflow Center services,
make sure that what you designate here matches the URL for accessing Workflow Center. Note: Ensure that you specify the host name instead of
localhost for the server name when you configure the Workflow Server. This is required when you are using the
Process Designer remotely.
- PortType the port number of Workflow Center. In an environment
with a load balancer or proxy server between Workflow Server and Workflow Center, make sure that what
you designate here matches the URL for accessing Workflow Center.
- User nameType a valid user name that exists
on Workflow Center. Workflow Server will connect to
Workflow Center as this user.
- PasswordType the password for the user.
- Confirm passwordType to confirm the
password for the user.
9 Required: On the ConfigureDatabases page, select DB2 , configure the database parameters fordata sources of the deployment environment, click Test connection , and afterthe connection succeeds click Next to go to the Summary page. On this page, define the following database information for the components that are included inthis deployment environment. Where possible, the wizard supplies default information for theparameters, but change those values to match the values that you defined when you planned theenvironment. Important: The databases specified in this panel must already exist.Deployment environment configuration never creates a database. For more information, see the sectionabout creating databases. Attention: Process and Performance Data Warehouse should not use the same database.You can clear the Create Tables check box if you want to create the tablesmanually instead of the configuration creating it automatically. The scripts to create tables aregenerated in the BPM\_Install \profiles\DmgrProfile\dbscripts\ folder. You can run the scripts from the dbscripts folder and do not need togenerate scripts using the BPMConfig command. You can edit all key parameters, such as the database name, whether or not to create tables andthe data source runtime user name for the deployment environment. You can select which database touse for the given component. Tip: Steps that cannot be completed through theDeployment Environment wizard, and which need to be completed manually, arelisted on the Deferred Configuration page. You can view this page after you have created yourdeployment environment. To view this administrative console page, click Servers > Deployment Environments > Deployment environment name > Deployment Environment Configuration > AdditionalProperties > Deferred Configuration .

- Shared parameters
    - User name: Type the user name to connect to the database.
    - Password: Type the password for the user name.
    - Confirm password: Type to confirm the password for the user name.
    - Server: Type a server name where the database is located.
    - Port: Type the port number to connect to the database.
    - Create Tables: Select to create the required tables.Note: If this option
is selected, ensure that the user has sufficient rights to access the database and create
tables.
- Common database

- Name: Type a name for the common database that is used for CommonDB
components, Business Space, Business Process Choreographer, and
Messaging.
- Process database

- Name: Type a name for the Process database.
- Performance Data Warehouse database

- Name: Type a name for the Performance Data Warehouse database.
- Select the databases that you want to separate from the Common database.

- Messaging : Select this option to create a separate messaging engine database.
    - Name: Type a name for the messaging engine database.
- Case management

- Check Use an external Content Platform Engine to use an external Content
Platform Engine rather than the embedded Content Platform Engine. If you check this box, you can't
fill in the schema names for the Design Object Store and Target Object Store.
- Check Use an external Content Navigator to use an external IBM® Content
Navigator rather than
the embedded IBM Content
Navigator. If you
check this box, you can't fill in the schema name for the IBM Content
Navigator
database.
- Content database

- Name: Type a name for the content database that is used for the design
object store, target object store (including Case Analyzer and case history), and IBM Content
Navigator.
- Design Object Store database schema name: Type a name for the design
object store schema.
- Target Object Store database schema name: Type a name for the target
object store schema.
- IBM Content
Navigator database
schema name: Type a name for the IBM Content
Navigator database
schema.
- Network shared directory: Specify the location of the network shared
directory, which is used to store IBM Content
Navigator plug-ins and
resources, including pages, help system contents, widget package, and translation resources. For a
single-node cluster, specify a location in the local file system. In a three-cluster environment,
you can do the same, or specify a virtual or shared drive. The network shared directory must be
visible to and writable by all nodes, so make sure it is mapped to all server nodes in the
cluster.

You can clear the Create Tables check box if you want to create the tables
manually instead of the configuration creating it automatically. The scripts to create tables are
generated in the BPM\_Install\profiles\DmgrProfile\dbscripts\
folder. You can run the scripts from the dbscripts folder and do not need to
generate scripts using the BPMConfig command.

You can edit all key parameters, such as the database name, whether or not to create tables and
the data source runtime user name for the deployment environment. You can select which database to
use for the given component.

10 Verify that the information on the Summary page is correct and perform the following substeps:

1. Optional: If you want to exit without generating the configuration, click
Cancel.
2. Optional: 
If you want to save the environment configuration to configure a similar deployment
environment, click Export for Scripting.
3. If you are satisfied with the deployment environment configuration, click
Generate Deployment Environment to save and complete the configuration of the
deployment environment. This will also generate a properties file in the
BPM\_Install\_Root/logs/config folder on the deployment
manager machine with a timestamp in the file name,
bpmconfig-de\_name-timestamp.properties. Save this file for
future reference or for troubleshooting any issues.
11. If you have postponed the Process database table creation
by clearing the create table option on the Database page, create the
tables and load the database with system information by running the bootstrapProcessServerData command.
The bootstrap code runs automatically if the Process database table
creation is selected on the Database page wizard.
12 Restart the following resources after you have completed your configurations in the orderspecified here. For the steps to restart a resource, see Starting and stopping your environment . For Advanced deployment environment or AdvancedOnly deployment environment , the deployment manager andnode agents need to be restarted for the cell scoped configuration to take affect. This is onlyrequired for the first deployment environment that you create.

1. Stop the deployment environment.
2. Stop the node agent.
3. Stop the deployment manager.
4. Start the deployment manager.
5. Start the node agent.
6. Start the deployment environment.

## Results

When the configuration completes, you can examine
the configuration files to view the changes.

## What to do next

## Related information

- Business Automation Workflow security roles
- Creating Db2 databases in a network deployment environment on Windows