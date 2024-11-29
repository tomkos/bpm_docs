# Checking for migration readiness

Before you migrate, run a command
to find potential issues in the source environment that must be fixed
before you can migrate. The command also makes you aware of changes
to make after you migrate.

Figure 1. Sample environment after 24.x is installed on the target. The source environment is
running and transferring data to and from its databases. The target has been created but does not
contain a deployment environment.

<!-- image -->

<!-- image -->

## Before you begin

If the source environment is
a network deployment environment, ensure that the deployment manager,
nodes, and deployment environment have been started. If the source
environment is a stand-alone environment, ensure that the stand-alone
server has been started.

Before
migrating, use the failed event manager to find and manage failed
events. Make sure that all failed events are deleted or resubmitted
before the migration. After migration, failed events from the source
environment cannot be handled again.

## About this task

The BPMMigrationPreValidation command
validates your applications, data sources, and messaging engines.
It generates a report that shows the current status of your source
environment. You can see the changes that you must make so that migration
can proceed smoothly, as well as the changes that you must make after
migration.

## Procedure

1 Copy the migration.properties samplefile and rename it to source\_migration.properties .Update the file with the configuration information for the sourceenvironment. Check all the properties and edit themif required, following the instructions in the sample file. If you are migrating multiple deployment environments,you must use a different source migration properties file for eachone where you assign values to the following parameters: These cluster name parameters must have different values betweendeployment environments. However, within the same migration propertiesfile, the values can be the same. If you are migrating from a stand-alone environment,leave the cluster name parameters empty. If you are migrating from a single cluster environment,enter a value for the application cluster name, for example: If you are migrating from a network deploymentenvironment, input the names of the clusters that exist in your sourceenvironment, for example: In addition, you must specify values for thefollowing parameters in each file: For admin.username and admin.password ,use the WebSphere primary administrative user name. You can find theprimary administrative user name in the administrative console bygoing to Users and Groups > Administrativeuser roles . The bpm.home parameter is the installationroot of your source product. Make sure that the file separators areforward slashes (/). Use the full path. Do not use the tilde character(˜) to stand for the home directory. For example: bpm.home =/opt/IBM/BPM
    - If you installed the new version of the product on the same computer
as the source environment, the sample file is in install\_root\_24.0.0.0/util/migration/resources/migration.properties.
    - If you installed the new version of the product on a different
computer and copied the migration files to the source environment,
the sample file is in
remote\_migration\_utility/util/migration/resources/migration.properties.
    - source.application.cluster.name
    - source.messaging.cluster.name
    - source.support.cluster.name
    - source.web.cluster.name

If you are migrating from a stand-alone environment,
leave the cluster name parameters empty.

    - source.application.cluster.name=SingleCluster
    - source.messaging.cluster.name=
    - source.support.cluster.name=
    - source.web.cluster.name=
    - source.application.cluster.name=ApplicationCluster
    - source.messaging.cluster.name=MessagingCluster
    - source.support.cluster.name=SupportCluster
    - source.web.cluster.name=
    - admin.username
    - admin.password
    - bpm.home
    - profile.name

For admin.username and admin.password,
use the WebSphere primary administrative user name. You can find the
primary administrative user name in the administrative console by
going to Users and Groups > Administrative
user roles.

The bpm.home parameter is the installation
root of your source product. Make sure that the file separators are
forward slashes (/). Use the full path. Do not use the tilde character
(˜) to stand for the home directory.  For example:

```
bpm.home=/opt/IBM/BPM
```

2 Optional: Update other configurationfiles in theinstall\_root\_ 24.0.0.0 \util\migration\resources directory,following the instructions in the files. Do not update any of the other files.

- Update the soap.client.props file to change
the
com.ibm.SOAP.requestTimeout property if the SOAP
invocation is timing out at the current setting.
- Update the ssl.client.props file to change
the keystore and truststore.
- Update the logging.properties file to set
the default logging level to FINEST if you need to capture more detail
in the log.
3 Run the command to check for migration readiness. where: For example:BPMMigrationPreValidation.sh -propertiesFile /opt/BPM/util/migration/resources/source\_migration.properties -reportDir /BPM751\_precheck\_report This command finds potential issuesin the source environment that must be fixed before you can migrate,and also makes you aware of changes that you must make after you migrate.The command performs the following checks: The command displays each validationrule as it runs. After all the validation rules are finished, yousee a message similar to the following message:Generating the report for migration prevalidation...Migration prevalidation was completed. You can review the report in: /BPM\_precheck\_report

- If you installed the new version of the product on the same computer
as the source environment, run the following command in the target
environment. The properties in the
source\_migration\_properties\_file must point to
the source environment.install\_root\_24.0.0.0/bin/BPMMigrationPreValidation.sh -propertiesFile source\_migration\_properties\_file -reportDir path\_to\_report\_package

- If you installed the new version of the product on a different
computer and copied the migration files to the source environment,
run the following command in the source environment on the computer
where the deployment manager or stand-alone server is deployed. The
properties in the source\_migration\_properties\_file must
point to the source environment.remote\_migration\_utility/bin/BPMMigrationPreValidation.sh -propertiesFile source\_migration\_properties\_file -reportDir path\_to\_report\_package

- source\_migration\_properties\_file is the full
path to the migration properties file in which you specified the configuration
information for the source environment (the file that you updated
in Step 1).
- path\_to\_report\_package is the full path to
the directory where the validation report will be stored

```
BPMMigrationPreValidation.sh -propertiesFile /opt/BPM/util/migration/resources/source\_migration.properties -reportDir /BPM751\_precheck\_report
```

- Profile validation:
    - Validates that the source product and version is supported
for migration
    - Validates the status of IBM Business Process Manager
 applications
    - Validates the connection status of all IBM BPM data sources
    - Validates the status of IBM BPM messaging
engines
    - Performs the following checks:
        - Whether any existing service integration bus (SIB) message is
in a transaction
        - Whether too many SIB messages are stuck in a queue
        - Whether any failed events are not processed
- Notifies you of changes that you must make after you migrate,including the following changes:
    - Authentication aliases that are not migrated because
you added them in the source environment
    - Data sources that are not migrated because you added
them in the source environment
- Notifies you of the key changes that occur during migration, includingthe following changes:

- Security changes
- Changes to XML configuration properties files. Some
XML security configuration properties are moved to the WebSphere® Application
Server configuration
files automatically. These properties are exported to the properties
file and will be moved to the WebSphere Application
Server configuration
files when you run the command. See the table in WebSphere Lombardi
Edition XML configuration properties that are migrated to WebSphere
Application Server configuration files for a list of the properties
that have been moved.
- Notifies you of current configuration that you might need tofix after migration, including the following configuration:

- XML configuration properties files
- Lightweight Third-Party Authentication (LTPA) key file
- Topology information
- Database validation:

- Notifies you if the volume of data will increase the
downtime required for migration
- Checks for customized indexes
- Analyzes the tables for migration impact and, if required,
recommends actions that you can take before migration
- Checks that the log file size is sufficient and,
if not, provides the command that you should run to update it
- Checks that the records in the Business Space tables
are valid.
- Reminds you to check the oobLoadedStatus.properties
file.

```
Generating the report for migration prevalidation...
Migration prevalidation was completed. You can review the report in: /BPM\_precheck\_report
```

4. If the report does not open automatically,
go to the report directory that you specified and open the index.html file
in a browser to view the report. 
View
each of the areas in the report. Wherever you see an error or warning,
you can click it for more information.
5. Investigate the warnings and fix the problems.
Run the BPMMigrationPreValidation command again
and make sure that all problems are fixed before you proceed with
the migration.

## Related information

- Working with failed events in IBM Business Automation Workflow
- BPMMigrationPreValidation command-line utility
- Sample migration.properties files