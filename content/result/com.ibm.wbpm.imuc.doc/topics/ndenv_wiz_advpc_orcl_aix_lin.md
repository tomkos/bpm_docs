# Creating the Advanced Workflow Center deployment environment

Create a Workflow Center deployment environment to store, run and
administer process applications and toolkits that are developed in Process Designer and Integration Designer. You can create more than one deployment
environment in the same cell using the Deployment Environment wizard. However,
you can create only one Workflow Center-based
deployment environment in a single cell.

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

- Make sure that the user name and schema name are exactly the same.
The user specified should exist in the database before generating
the environment.
- Process and Performance Data Warehouse can use the same database instance, but should use
different users.

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
Type section, select Advanced Workflow Center. Features
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
8 Required: On the ConfigureDatabases page, select Oracle , configure the database parametersfor data sources of the deployment environment, click Test connection , andafter the connection succeeds click Next to go to theSummary page. On this page, define the database information for the components that are included in thisdeployment environment. Where possible, the wizard supplies default information for the parameters,but change those values to match the values that you defined when you planned the environment. Important: The databases specified in this panel must already exist. Deployment environmentconfiguration never creates a database. For more information, see the section about creatingdatabases. Attention: The default schema names that are displayedon this page might conflict with your site naming convention or might conflict with existingschemas. As such, it is likely that you will need to change the schema name. Pay close attention tothe values specified to avoid potential naming conflicts.Also ensure that you have completed thefollowing items: You can edit all key parameters, such as the database name, whether or not to create tables, thedata source runtime user name, and the password for the deployment environment. You can select whichdatabase to use for the given component. Tip: Steps that cannot be completed through theDeployment Environment wizard, and which need to be completed manually, arelisted on the Deferred Configuration page. You can view this page after you have created yourdeployment environment. To view this administrative console page, click Servers > Deployment Environments > Deployment environment name > Deployment Environment Configuration > AdditionalProperties > Deferred Configuration .

- Shared parameters
    - Server: Type a server name where the database is located.
    - Port: Type the port number to connect to the database.
    - Instance name: Type the instance name for the Oracle database.
    - Create Tables: Select to create the required tables.Note: If this option
is selected, ensure that the user has sufficient rights to access the database and create
tables.
- cellDB Note: The cellDB option is only visible whenyou create the first Advanced deployment environment . Afterthis, every Advanced deployment environment that you createshares the cellDB of the first environment.

- User name: Type a user name for the cell database.
- Password: Type the password for the cell database user.
- Confirm password: Type to confirm the password for the cell database
user.
- Common database

- User name: Type a user name for the common database that is used for
CommonDB components, Business Space, Business Process Choreographer, and
Messaging.
- Password: Type the password for the common database user.
- Confirm password: Type to confirm the password for the common database
user.
- Process database

- User name: Type a user name for the Process database.
- Password: Type the password for the Process database user.
- Confirm password: Type to confirm the password for the Process database
user.
- Performance Data Warehouse database

- User name: Type a user name for the Performance Data Warehouse
database.
- Password: Type the password for the Performance Data Warehouse database
user.
- Confirm password: Type to confirm the password for the Performance Data
Warehouse database user.
- Select the databases that you want to separate from the Common database.

- Messaging : Select this option to create a separate messaging engine database.
    - User name: Type a user name for the messaging engine database.
    - Password: Type the password for the messaging engine database user.
    - Confirm password: Type to confirm the password for the messaging engine
database user.
- Business Process Choreographer : Select this option to create a separateBusiness Process Choreographer database.

- User name: Type a user name for the Business Process Choreographer
database.
- Password: Type the password for the Business Process Choreographer
database user.
- Confirm password: Type to confirm the password for the Business Process
Choreographer database user.
- Case management

- Check Use an external Content Platform Engine to use an external Content
Platform Engine rather than the embedded Content Platform Engine. If you check this box, you can't
fill in user names and passwords for the design object store and target object store databases.
- Check Use an external Content Navigator to use an external IBM® Content
Navigator rather than
the embedded IBM Content
Navigator. If you
check this box, you can't fill in user names and passwords for the IBM Content
Navigator
database.
- Design object store database

- User name: Type a user name for the design object store database.
- Password: Type the password for the design object store database
user.
- Confirm password: Type to confirm the password for the design object
store database user.
- Target object store database

- User name: Type a user name for the target object store database.
- Password: Type the password for the target object store database
user.
- Confirm password: Type to confirm the password for the target object
store database user.
- IBM ContentNavigator configuration database

- User name: Type a user name for the IBM Content
Navigator
database.
- Password: Type the password for the IBM Content
Navigator database
user.
- Confirm password: Type to confirm the password for the IBM Content
Navigator database
user.
- Network shared directory: Specify the location of the network shared
directory, which is used to store IBM Content
Navigator plug-ins and
resources, including pages, help system contents, widget package, and translation resources. For a
single-node cluster, specify a location in the local file system. In a three-cluster environment,
you can do the same, or specify a virtual or shared drive. The network shared directory must be
visible to and writable by all nodes, so make sure it is mapped to all server nodes in the
cluster.

- Make sure that the user name and the schema name are exactly the same. The user specified should
exist in the database before generating the environment.
- Process and Performance Data Warehouse can use the same database instance, but should use
different users.

You can edit all key parameters, such as the database name, whether or not to create tables, the
data source runtime user name, and the password for the deployment environment. You can select which
database to use for the given component.

9 Verify that the information on the Summary page is correct and perform the following substeps:

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
10. If you have postponed the Workflow Server database table
creation by clearing the create table option on the Database page, create the tables and load the
database with system information by running the bootstrapProcessServerData
command.

Important: This command must be run before starting any cluster members.
11 Restart the following resources after you have completed your configurations in the orderspecified here. For the steps to restart a resource, see Starting and stopping your environment . For Advanced deployment environment or AdvancedOnly deployment environment , the deployment manager andnode agents need to be restarted for the cell scoped configuration to take affect. This is onlyrequired for the first deployment environment that you create.

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