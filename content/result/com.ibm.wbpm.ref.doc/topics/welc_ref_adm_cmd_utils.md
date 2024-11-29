# Command-line utilities

- BPMConfig command-line utility

The BPMConfig command is used to create, update, upgrade, or delete an IBM® Business Automation Workflow deployment environment. It can also be used to create the database scripts and profiles, start and stop the deployment environment, export or migrate the configuration properties of the deployment environment, export database information and system data for performance analysis, and validate the deployment environment configuration. The BPMConfig command - line utility is located in the WAS\_INSTALL/bin directory.
- BPMCreateDatabaseUpgradeUtilities command-line utility (deprecated)

Use the BPMCreateDatabaseUpgradeUtilities command-line utility to create an archive file that contains all of the commands and their prerequisites that need to be invoked on the database system where the database upgrade is to be performed.
- BPMCreateRemoteMigrationUtilities command-line utility

Use the BPMCreateRemoteMigrationUtilities command-line utility to create an archive file containing all the commands and their prerequisites that need to be run on the source environment. These commands with prerequisites can be used to extract or manage the configuration for migration.
- BPMEnablePostInstaller command-line utility

 Traditional: 
Use the BPMEnablePostInstaller command-line utility to run the post-installation scripts after swinging the profiles. Use this command only if your environment is configured for swinging profiles and you have already completed the rest of the upgrading steps. This command is supported only on Linux.
- BPMExtractSourceInformation command-line utility

Use the BPMExtractSourceInformation command-line utility to export the service integration bus (SIB) messages and advanced Business Automation Workflow applications during migration. This command is needed only if you are migrating from IBM BPM Advanced.
- BPMGenerateUpgradeSchemaScripts command-line utility

Use the BPMGenerateUpgradeSchemaScripts command-line utility to generate SQL scripts and upgradeSchema scripts for a database that must be upgraded manually during a version-to-version migration or a refresh pack upgrade.
- BPMManageApplications command-line utility

Use the BPMManageApplications command-line utility to make sure that no new events or processes are entering the system during migration when you are migrating from IBM BPM Advanced.
- BPMMigrate command-line utility

Use the BPMMigrate command-line utility to import the migration snapshot from your previous version to your new version. The migration snapshot is taken using the BPMExtractSourceInformation command and includes the service integration bus (SIB) messages and advanced Business Automation Workflow applications. The BPMMigrate command is only needed if you are migrating from IBM BPM Advanced.
- BPMMigrationPreValidation command-line utility

Use the BPMMigrationPreValidation command-line utility to check for migration readiness. This command makes sure that your source environment is in the correct state for migration. It also makes you aware of changes that you will have to make after migration.
- BPMMigrationStatus command-line utility

Use the BPMMigrationStatus command-line utility to display the status of the migrations that have been executed on the system.
- BPMQueryDeploymentConfiguration command-line utility

Use the BPMQueryDeploymentConfiguration command-line utility to extract the deployment configuration from the source profile and generate an XML file. This information is needed specifically for updating WebSphere Adapters during runtime migration.
- createDatabase.sh script

Use the createDatabase.sh script to create your IBM Business Automation Workflow database objects in a DB2® for z/OS® subsystem. This script also includes a parameter that can be used to create the databases. You can run createDatabase.sh from UNIX System Services.
- DBUpgrade command-line utility

Use the DBUpgrade command-line utility to upgrade previous versions of database schemas and data to the current version of Business Automation Workflow.
- esAdmin command-line utility

Use the esAdmin command to list, unlock, or delete active and queued locks.
- eventbucket command-line utility

Use the eventbucket command-line utility to display or change the event database bucket configuration.
- eventpurge command-line utility

Use the eventpurge command-line utility to delete events from the event database. You can delete all events from the event database, or you can limit the deletion to events meeting certain criteria.
- genMapper command-line utility

Use the genMapper command-line utility to generate a component that bridges as Service Component Architecture (SCA) reference to a Java interface.
- installProcessAppPackage command-line utility (deprecated)

Use the installProcessAppPackage command-line utility to install an extracted installation package on an offline server.
- manageprofiles command-line utility

The manageprofiles command-line utility creates a profile, which is the set of files that define the runtime environment for a deployment manager, a managed node, or a stand-alone server.
- MeteringAgent command-line utility

Use the MeteringAgent command-line utility to start a thread that analyzes the audit log files from the WebSphere® Application Server Auditing Facility, collects license compliance records, and sends the information to the IBM FileNet® System Manager. Concurrent user metrics are required for the Concurrent User license option, and you can also record and monitor activity metrics.
- MeteringConfig command-line utility

Use the MeteringConfig command-line utility to enable or disable WebSphere Application Server security auditing and the ability to generate the audit logs used to capture concurrent user metrics and number of activities. Concurrent user metrics are used to monitor usage for the IBM Business Automation Workflow Concurrent User license option.
- migrateBSpaceData command-line utility

Use the migrateBSpaceData command-line utility to migrate the Business Space data.
- retrieveProcessAppPackage command-line utility (deprecated)

Use the retrieveProcessAppPackage command-line utility to extract an installation package before installing it on an offline server.
- serviceDeploy command-line utility

Use the serviceDeploy command to package Service Component Architecture (SCA) compliant modules as Java™ applications that can be installed on a server. The command is useful when performing batch installs through wsadmin.
- tuneBPM command-line utility (removed)

Use the tuneBPM command-line utility to apply the properties specified in the performanceTuning.properties file to the existing deployment environment. You can define and edit any of the properties in the file and then run the tuneBPM command to apply them.
- upgradeSchema command-line utility

Use the upgradeSchema command-line utility to upgrade the database schema.