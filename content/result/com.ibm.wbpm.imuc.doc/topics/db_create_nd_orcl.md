# Creating users for Oracle databases

You can create the users for Oracle databases
either before or after you run the BPMConfig command with the -create
-de parameters to create profiles and configure your deployment environment.
Create the cell-scoped user, the deployment environment-level user, the
Process database user, the Performance Data Warehouse user, and the three users for the Content
database: design object store user, target object store user, and IBM® Content
Navigator user.
The Process, Performance Data Warehouse, and Content users are not needed
for an AdvancedOnly
deployment environment.

- If the property is set to false, database tables are automatically created
when you run the BPMConfig command to create the profiles and deployment
environment. Therefore, the database users must exist before you run the
BPMConfig command.
- If the property is set to true, database table creation is deferred when
you run the BPMConfig command to create the profiles and deployment
environment. Therefore, you can create the database users either before or after running the
command. You might find it useful to create the database users after running the
BPMConfig command because you can use the set of populated scripts, which the
command generates, to create the database users and database tables at a time that you choose.
- If your PostgreSQL DB
server uses Certificate Authentication, you must set
bpm.de.deferSchemaCreation property to true in
bpmconfig.properties. You cannot run BPMConfig -validate -db
bpmconfig.properties to validate database connections. There is no place in
bpmconfig.properties to specify the location of certificates, hence the
BPMConfig command cannot be used to connect directly to PostgreSQL DB with client
authentication.

## Before you begin

Before
you create any users for Oracle databases, see the topic Configuring XA transactions for Oracle in a network environment on AIX or Linux.

- Design object store (DOS)
- Target object store (TOS)
- IBM Content
Navigator (ICN)

| Tuning item      |   Minimum memory for initial settings (MB) |
|------------------|--------------------------------------------|
| Buffer cache     |                                       2048 |
| Shared pool size |                                       1024 |

Recommendations for database table space
settings:

On Oracle, IBM Business Automation
Workflow stores
large objects (LOBs) with the SECUREFILE option. For SECUREFILE, it
is recommended to use a table space with the AUTOALLOCATE option. If
you use UNIFORM SIZE extents, ensure that the UNIFORM SIZE is big
enough. Given the default block size of 8K, specify a UNIFORM SIZE
of at least 120K. Business Automation Workflow does
not explicitly prescribe the table space options; it relies on the
default Oracle settings (such as AUTOALLOCATE) to automatically manage
extents.

For new Business Automation Workflow installations,
create table spaces with the AUTOALLOCATE option.

For migrations, if you use table spaces with
a UNIFORM SIZE less than 120K, create new table spaces with the AUTOALLOCATE
option and make it the default table space for Business Automation Workflow database
schema users.

## About this task

The default database names are BPMDB for the Process database, PDWDB for the
Performance Data Warehouse database, CMNDB for the Common database, and CPEDB for the Content
database.  In the case of an Advanced
deployment environment or AdvancedOnly
deployment environment, the Common database has two parts: one is
scoped to the cell and the other is scoped to the deployment environment. Both parts can be defined
to use CMNDB (which is the default) or they can use separate databases. For details about databases
and schemas, see Planning the number of databases.

- Creating users for the databases before creating the profiles and configuring the deployment environment
- Creating users for the databases after creating the profiles and configuring the deployment environment

## Related information

- Troubleshooting Oracle transaction recovery messages

## Creating users for the databases before creating the profiles
and configuring the deployment environment

To generate the database scripts that can be
used by the BPMConfig command to create the users and configure your databases,
you can run BPMConfig with the -create -sqlfiles parameters,
and additionally include the -outputDir parameter to specify a location for the
generated scripts. When you run the BPMConfig command with these parameters, it
generates the database scripts without configuring your environment.

### Before you begin

- Information about the database configuration that you are designing.This might be a document that describes the general purpose of thedatabase configuration supplied by the database administrator or solutionarchitect. Alternatively, it might be a description of required parametersand properties. This information must include:
    - The location of the databases
    - The user ID and password for authenticating to the database
- Information about how IBM Business Automation Workflow and
its components have been installed, the database software used, and
the properties required by that type of database.
- An understanding of the profiles that you plan to create, specifically,
the functional relationship between the profile types and the databases.
- Information about the topology pattern to be implemented, and
an understanding of how the database design fits into the pattern
that you plan to use.

### Procedure

1. On the computer where you installed IBM Business Automation Workflow, navigate to the following directory where
the sample configuration properties files are stored: 
install\_root/BPM/samples/config
2 Find the sample properties file that most closely represents your target deployment environmentand make a copy of this file. For each of the different product configurations, there is adifferent folder containing sample properties files. For example, for configuring an Advanced,AdvancedOnly, or Standard deployment environment, there is an advanced ,advancedonly , or standard folder containing a set ofsample properties files. Within each folder, there is a set of files that are specific to thedifferent database types and configuration environments. The sample properties files are namedaccording to the following format:de\_type [-environment\_type ]-topology -Oracle , where: For example, the sample configuration properties file forconfiguring an Advanced deployment environment with Workflow Center and a single cluster topology using an Oracledatabase is named Advanced-PC-SingleCluster-Oracle.properties .
    - de\_type can be set to
Advanced, AdvancedOnly, or
Standard.
    - environment\_type can be set to PS for Workflow Server or PC for Workflow Center. This variable is
not used if de\_type is AdvancedOnly.
    - topology can be set to
SingleCluster or ThreeClusters.
3 Edit the copied propertiesfile and update the values as required to reflect your profile, deployment environment, and databaseconfiguration. When modifying the sample properties file, use the guidance provided within the file forspecifying values.Tip: You should use this sameproperties file later when you run the BPMConfig command to create your profilesand deployment environment. Additional considerations: For more information about the available properties, see the BPMConfig command-line utility topic and the descriptions in the Configuration properties for the BPMConfig command topic.

- Your modified properties file must use UTF-8 encoding.
- If you want to automatically create your database tables when you
run the BPMConfig command later to create profiles and configure your deployment
environment, set the bpm.de.deferSchemaCreation property to
false.
- Do not add any custom properties to this file when you perform
your modifications or the BPMConfig command will fail when it is run.
- If you need to use a backslash character (\) in your properties file,
for instance when specifying path names or passwords, you must use an escape backslash before it.
For example: bpm.dmgr.installPath=c:\\IBM\\BPM85.
- If
you are configuring a three-cluster setup that is based on the Advanced or AdvancedOnly template,
and you want your deployment environment to include the optional Business Process Archive Manager,
include the properties file entries that are described in the topic Configuring Business Process Archive Manager.

For more information about the available properties, see the BPMConfig command-line utility topic and the descriptions in the Configuration properties for the BPMConfig command topic.

4 Run the BPMConfig commandon the computer where IBM Business Automation Workflow is installed,passing it the name of the properties file that you created. Forexample:install\_root /bin/BPMConfig -create -sqlfiles /directory\_path /my\_environment.properties -outputDir /my\_bpmscripts\_dir Inthis syntax,directory\_path /my\_environment .properties is the location and name of your customized properties file, andmy\_bpmscripts\_dir is the directory where you want togenerate the database scripts. The generated scripts include a set of files namedcreateUser.sql , which can be used to create the users for the databases. ThecreateUser.sql files are generated into the following default locations: The number of subdirectories that are generated is dependenton the deployment environment type and the number of database users that were defined in theproperties file. Note: Thesescripts are overwritten if you run the BPMConfig command again.

```
install\_root/bin/BPMConfig -create -sqlfiles /directory\_path/my\_environment.properties -outputDir /my\_bpmscripts\_dir
```

In
this syntax,
directory\_path/my\_environment.properties
is the location and name of your customized properties file, and
my\_bpmscripts\_dir is the directory where you want to
generate the database scripts.

- my\_bpmscripts\_dir/dbscripts/cell\_name/Oracle/oracle\_instance\_name/cell\_user
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/CMN\_user
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/PS\_user
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/PDW\_user
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/DOS\_user
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/TOS\_user
- my\_bpmscripts\_dir/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/ICN\_user
5. For each createUser.sql file
that was generated, run the following command on your local or remote database server: 
  sqlplus oracle\_user\_ID/oracle\_password@oracle\_instance\_name @createUser.sql schema\_user\_password

Note: Although you can specify the schema user password shown in the command syntax, you can
alternatively edit the createUser.sql script and replace the parameter
&1 with the schema user password and then run the script without specifying any
parameter.
6. Manually create the table spaces for the Content database by running the
createUserTablespace\_ECM.sql script that is in each of the
DOS\_user and
TOS\_user folders. Also run the
createUser.sql script and the
createTablespace\_Advanced.sql,
createTablespace\_Standard.sql, or
createTablespace\_Express.sql script that is in the
ICN\_user folder.

Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should be
replaced manually.

## Creating users for the databases after creating the profiles
and configuring the deployment environment

When you run the BPMConfig
command with the -create -de parameters to create the profiles and configure
the network deployment environment, database scripts are generated that are populated with the
values from the properties file that you specified. You can use some of these scripts to create the
users for the databases if you chose to defer the creation of the database tables.

### Before you begin

You must
have already run the BPMConfig command to create
the profiles and configure the network deployment environment.

### Procedure

1 On the computer where you created the deployment manager profile, navigate to one or moreof the following default subdirectories where the SQL database scripts were generated: These directories contain the createUser.sql scripts that you can use tocreate the users for the databases. The number of subdirectories that are generated is dependent on the deployment environmenttype and the number of database users that were defined in the properties file.
    - dmgr\_profile\_root/dbscripts/cell\_name/Oracle/oracle\_instance\_name/cell\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/CMN\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/PS\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/PDW\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/DOS\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/TOS\_user
    - dmgr\_profile\_root/dbscripts/cell\_name.deployment\_environment\_name/Oracle/oracle\_instance\_name/ICN\_user

These directories contain the createUser.sql scripts that you can use to
create the users for the databases.

The number of subdirectories that are generated is dependent on the deployment environment
type and the number of database users that were defined in the properties file.

2. For each createUser.sql file
that was generated, run the following command on your local or remote database server: 
  sqlplus oracle\_user\_ID/oracle\_password@oracle\_instance\_name @createUser.sql schema\_user\_password

Note: Although you can specify the schema user password shown in the command syntax, you can
alternatively edit the createUser.sql script and replace the parameter
&1 with the schema user password and then run the script without specifying any
parameter.
3. Manually create the table spaces for the Content database by running the
createUserTablespace\_ECM.sql script that is in each of the
DOS\_user and
TOS\_user folders. Also run the
createUser.sql script and the
createTablespace\_Advanced.sql,
createTablespace\_Standard.sql, or
createTablespace\_Express.sql script that is in the
ICN\_user folder.

Tip: In some Content database scripts, there is a @DB\_DIR@ variable that should be
replaced manually.