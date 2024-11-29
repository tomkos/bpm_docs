# Creating and configuring the test environment profile using BPMConfig

## Before you begin

You must have installed IBM Integration
Designer and the
test environment silently using the command line or response file.

Ensure that the DB2 command line environment can be successfully invoked by running
db2cmd from the command prompt. This should open a DB2 command line interface.

Regardless of whether you are an administrative or non-administrative user or a root or non-root
user, you must be authorized to create and drop databases. The Typical installation from the product
launchpad validates this authority. To obtain the required authority for creating and dropping
databases, add the user to the DB2ADMNS group. For more information about how to
add a user to the group, see Adding your user ID to the DB2ADMNS and DB2USERS user groups (Windows).

## About this task

- Creates a standalone profile for the IBM Workflow
Server test environment
- Configures the test environment profile

## Procedure

To create and configure the profile for the IBM Workflow
Server test environment, complete the following
steps:

1. On the system where you want to create the test environment profile, locate the sample
properties file Advanced-PS-Standalone-DB2.properties at the following path:
extract\_directory\launchpad\content\samples\config\iid

Note: Ensure that the schema, table space, and database directory for the Case database have been
created in advance and the values are consistent with the values defined in this property file.
2. Create a copy of the above sample properties file.
3. Modify your version of the properties file so that the values correspond to your own
configuration.
To create the test environment profile for IBM
Integration Designer, clear out or update the default
variable values assigned to the required properties.
Table 1. BPMConfig command properties that must be set. 
The following table lists the properties and the values that you must set:

Configuration properties
Values to set

bpm.de.psProcessCenterHostname
bpm.de.psProcessCenterPort

The Workflow Server test
environment is an offline server configuration. Clear the default values
@PS\_PC\_HOSTNAME@ and @PS\_PC\_PORT@ specified for the host name and
port number.

bpm.de.authenticationAlias.1.name=
    DeAdminAlias
bpm.de.authenticationAlias.1.user
bpm.de.authenticationAlias.1.password

Retain the default value DeAdminAlias for authentication
alias for the test environment administrator. See Business Automation Workflow security roles for more
information about the roles.If you change the value for
bpm.de.authenticationAlias.1.alias from the default
DeAdminAlias, you must update it everywhere that references that alias, for
example bpm.de.roleMapping.#.alias
Specify custom user name and password for
the authentication alias for the test environment administrator.

bpm.de.authenticationAlias.2.name=
    ProcessCenterUserAlias
bpm.de.authenticationAlias.2.user
bpm.de.authenticationAlias.2.password

The Workflow Server test
environment is an offline server configuration. Clear the default values specified for the user name
and password for the ProcessCenterUserAlias authentication alias.

bpm.de.authenticationAlias.3.name=
    BPM\_DB\_ALIAS
bpm.de.authenticationAlias.3.user
bpm.de.authenticationAlias.3.password

Retain the default value BPM\_DB\_ALIAS for authentication
alias for the database instance. Specify custom user name and password for the authentication
alias for the database user.

bpm.cell.authenticationAlias.1.name=
    CellAdminAlias
bpm.cell.authenticationAlias.1.user
bpm.cell.authenticationAlias.1.password

Retain the default value CellAdminAlias for authentication
alias for the cell. See Business Automation Workflow security roles for more information about the
roles.Specify custom user name and password for the authentication alias for the cell
administrator.

bpm.de.node.1.hostname
bpm.de.node.1.installPath
bpm.de.node.1.profileName

Update the default value @INSTALL\_HOSTNAME@ to specify the
host name of the computer where the product is installed. Update the default value
@INSTALL\_PATH@ to specify the installation path of the test
environment.
Update the default value @SERVER\_PROFILE\_NAME@ for the profile
name to qbpmps.

bpm.de.db.1.hostname
bpm.de.db.1.portNumber
bpm.de.db.1.schema

Update the default value @DB\_HOSTNAME@ to specify the host
name of the database.Update the default value @DB\_PORTNUMBER@ to specify the
port number of the DB2 service.
Update the default value @DB\_SCHEMA@ to
specify the user name for the DB2 database in CAPITAL letters.

bpm.de.db.1.databaseName
bpm.de.db.2.databaseName
bpm.de.db.3.databaseName
bpm.de.db.4.databaseName 
bpm.de.db.5.databaseName 
bpm.de.db.6.databaseName

Update the default value @CMN\_DB\_NAME@ for the Common
database to QCMNDB.Update the default value @PS\_DB\_NAME@ for
the Process database to QBPMDB.
Update the default value
@PDW\_DB\_NAME@ for the Performance Data Warehouse
database to QPDWDB.
Update the default value @CASE\_DB\_NAME@
for the IBM Content
Navigator database, Design
Object Store database, and Target Object Store database to QCPEDB. 

bpm.de.db.3.databaseDataDirectoryPath
bpm.de.db.4.databaseDataDirectoryPath
bpm.de.db.5.databaseDataDirectoryPath

Update the directory path where certain database content will be stored for
the IBM Content
Navigator
(ICN), design object store (DOS), and target object store (TOS) databases. Use an existing empty
directory on the database server; for example, <IID install root>\\ECMDBs. Use
the same directory for all three databases and make sure the directory exists.

For more information about the BPMConfig command properties, read the
comments in the sample files, or see the sample property file descriptions in Configuration properties for the BPMConfig command.
4. Add the property bpm.de.createDatabase in the properties file and set its
value set to true.
5. Run the BPMConfig command passing it the name of the properties file you
created.
For exampleBPM\_home\bin\BPMConfig -create -de
my\_environment.properties

## What to do next

Create a copy of the updated properties file, rename this copied version to
Standalone.properties, and place this file at the location
<WTE\_HOME>/properties/wte. This ensures that the
Server Reset feature in Integration Designer
functions properly.

After you have created test environment profile, you can start the test profile by running the
BPMconfig command with the -start action.