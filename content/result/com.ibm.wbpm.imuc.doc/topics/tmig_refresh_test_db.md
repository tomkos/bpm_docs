# Testing the upgrade by using production database data

## About this task

- Isolate the test environment from Workflow Server or Workflow Center because
the test environment could conflict with them.
- Modify your applications and configure or block network connections
to external resources used by the current production system to prevent
the test applications from conflicting with production applications.
- Avoid changing the host name, because a changed host name could
affect applications that rely on it.
- Because you are copying the database, make sure that both the
new Business Automation Workflow test
server and the database server are configured for the same time zone
as the existing ones.
- If you need full access to instance data, make sure that the user
registry contains all the same users and groups. Having the same DeAdmin
and CellAdmin users is especially important.

## Procedure

1. Export the configuration from the Business Automation Workflow source
deployment environment by using the following command: BPMConfig –export –profile profile\_name -de de\_name -outputDir output\_directoryIf
there is only one deployment environment in the WebSphere cell, omit
the -de option.Important: Specify a different
output directory for each deployment environment. When a cell has
multiple deployment environments, a unique output directory is required
for each deployment environment.
The configuration files are
placed in the output directory that you specify.
Table 1. Configuration files for each deployment
environment

Sample name
Description

DE\_name.properties
This properties file contains the configuration properties from your source
environment. You use this file when you configure the target environment. For more information about
the configuration properties, see the topic Configuration properties for the BPMConfig command.

fileRegistry.xml
If you use a file-based user registry, the user registry file is copied from
the source environment to be added to the target environment.

ltpa.jceks
If you use LTPA, the LTPA key file is copied from the source environment to be
added to the target environment.

ldap\_additional\_properties.xml
If you use a federated repository and an unencrypted LDAP connection in the
source environment, user-defined additional properties of the LDAP server are copied from the source
environment to the output directory, where they are later used automatically to create the target
environment.Restriction: If you extend the federated repository to use a custom login
property (such as userPrincipalName) in addition to the default
uid property in the source environment, LDAP is not configured for the target
environment, with the following warning: CWMCB0600W: LDAP could not be configured! You may
configure LDAP separately after BPMConfig has terminated successfully. If you see this
warning, manually configure LDAP with the login properties you want to use after the migration is
complete.

ProcessServer\_100SourceCustomMerged.xml and
PDW\_100SourceCustomMerged.xml
If you have XML configuration properties files, they are copied from the
source environment. The exported configuration files are merged and renamed to
101CustomMigrated.xml in the target environment.

Application-config-bpc.xml and
resources-bpc.xml
If you have Business Process Choreographer that are configured in the source
environment, the configuration files are copied from the source environment to the output directory,
where they are later used automatically to create the target environment.

Support-config-bpc.xml
If you have Business Process Choreographer Archive Manager configured on the
support cluster in the source environment, the configuration is copied from the source environment
to the output directory, where it is later used automatically to create the target
environment.

Copy the output
directory to the computer where you want to create the new deployment
environment.
2. Install Business Automation Workflow on the
environment where you are going to test the upgrade. The version must
match the version of the environment that you are cloning the database
from.
3 If you are testing upgrade for an Advanced orAdvancedOnly deployment environment, you must extract the advancedapplications and service integration bus (SIB) messages; otherwise,you can skip this step.
    1. Update the source\_install\_root/util/migration/resources/migration.properties file
to point to your source environment. Update the following
properties:admin.username=admin
admin.password=admin

bpm.home=E:/bpm85
profile.name=DmgrProfile

source.application.cluster.name=
source.support.cluster.name=
source.messaging.cluster.name=
    2. To keep the SIB messages in the cloned database consistent
with the SIB messages that you will extract in the next step, run
the BPMManageApplications command to prevent the
automatic starting of applications and schedulers.  BPMManageApplications -autoStart false -source -propertiesFile migration\_properties\_fileStop
the environment, back up the databases, and restart the environment
before you continue.If you are testing and do not care about the
gap between the SIB messages in the database and the extracted SIB
messages, manually create an empty file named app\_cluster\_name.BPMManageApplications.false.success in
the dmgr\_profile/logs folder to skip this step.
    3. Run the BPMExtractSourceInformation command
to extract the advanced applications and SIB messages and create a
snapshot in the specified folder.  BPMExtractSourceInformation -backupFolder folder\_path  -propertiesFile migration\_properties\_file
4 Back up and clone your existing databases. Normally,you back up databases while the server is offline, but you can backup the databases online for testing purposes only.

1. Use your database utility to back up each of your source
databases, and restore them to another database instance or schema.
Clone each of the Business Automation Workflow databases.
2. Manually drop the existing messaging engine tables in
the cloned messaging database before you start the target deployment
environment.  Tip:  The messaging engine table
names use the SIB prefix.
5 Create the cloned environment using the exported configurationfiles.

1 Use the Business Automation Workflow Configurationeditor to update the exported properties file. Make sure that it pointsto the cloned databases instead of the source databases. Updatethe following database properties: Make other updates if required.Notes:
    - hostname
    - port
    - database name
    - password
    - Keep the same cell name, cell administrator, deployment environment
administrator, environment type, database schema names, and database
user names.
    - Keep the same application cluster name if you are cloning an Advanced
or AdvancedOnly deployment environment.
    - Make sure that bpm.de.deferSchemaCreation is
set to true in the properties file.
    - If possible, use the same LDAP server as the source environment.
    - If the Business Automation Workflow system
is integrated with other services, you must reconfigure that part
of the environment after the deployment environment is created and
point to the test environment for those services.
2. Run the following command to validate that all database
connections are correctly configured.   BPMConfig -validate -db output\_directory/updated\_properties\_file
3. Run the following command to create the cloned environment
on the test computer.  BPMConfig –create –de output\_directory/updated\_properties\_file
6 If you are testing upgrade for an Advanced or AdvancedOnlydeployment environment, you must deploy the advanced applicationsand SIB messages that you extracted in step 3 ; otherwise, you can skipthis step.

1. Update the following properties in the target\_install\_root/util/migration/resources/migration.properties file
to point to your target environment:  admin.username=admin
admin.password=admin

bpm.home=E:/bpm
profile.name=DmgrProfile

source.application.cluster.name=
source.support.cluster.name=
source.messaging.cluster.name=
# Use the properties file that you used to create the deployment environment
target.config.property.file= Important: Make
sure that you keep the source (not target) cluster names for the source.*.cluster.name properties.
2. Run the BPMManageApplications command
to disable the automatic starting of applications and schedulers.
 BPMManageApplications -autoStart false -target -propertiesFile migration\_properties\_file
3. Add a deployment\_environment\_name.DBUpgrade.success file
in the deployment\_manager\_profile/logs folder
to skip the check for upgrading the database, because the database
version is the same as in the cloned deployment environment and does
not need to be upgraded.
4. Start the environment.
5 In the backup folder that was generated when you ranthe BPMExtractSourceInformation command, open the snapshot\_folder /cell\_name /Applications folderand remove all Business Automation Workflow systemapplications that should not be deployed to the target again whenthe BPMMigrate command runs:
    - Business.Rules.Manager
    - IBM\_BPM\_DocStoreAdmin
    - IBM\_BPM\_DocumentStore
    - IBM\_BPM\_WebPD
    - RemoteAL61
    - HTM\_PredefinedTaskMsg
    - HTM\_PredefinedTasks
6. Run the BPMMigrate command to deploy
applications, import SIB messages, and re-create scheduler tasks:
 BPMMigrate -backupFolder folder\_path  -propertiesFile migration\_properties\_file
7. Run the BPMManageApplications command
again to enable the automatic starting of applications and schedulers:
 BPMManageApplications -autoStart true -target -propertiesFile migration\_properties\_file
8. Restart the servers.
7 Complete other configuration customization on the cloned environment to make itconsistent with the source, for example:

- Copy customized data sources or authentication aliases. Tip: If you are upgrading
from V8.5.6 or later, you can use the exportWASConfig.py script to export
customized WebSphere® Application
Server
configuration, including data sources, authentication aliases, and Secure Sockets Layer (SSL)
settings, from your source environment. Refer to this configuration to update the target environment
manually or use the importWASConfig.py script to import the configuration
automatically after the target environment is configured. If exportWASConfig.py
and importWASConfig.py do not work for your version, manually export the
configuration from the source and import it to the target Business Automation Workflow environment by using the
administrative console or the wsadmin command.
- Copy the business space customization.
- Copy other services that the Business Automation Workflow system must integrate
with.
8. Review the SystemOut.log startup
files for each server in the environment. Ensure that the environment
is starting successfully and showing behavior similar to the existing
environment.
9. Using the upgrading documentation, test the upgrading procedures
against your cloned environment to check the success of the database
upgrades and profile upgrades. If you find problems, debug them in
the test environment.

## Results

## Related information

- BPMConfig command-line utility
- Configuration properties for the BPMConfig command
- BPMExtractSourceInformation command-line utility
- BPMManageApplications command-line utility
- BPMMigrate command-line utility