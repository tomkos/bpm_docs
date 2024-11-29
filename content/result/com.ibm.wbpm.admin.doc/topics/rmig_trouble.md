# Troubleshooting migration

- A SOAP invocation timeout might have occurred
- Migration commands for the target environment might have failed
for other reasons. You can diagnose some failures by enabling tracing
for specific command-line utilities and rerunning those specific commands.

If you ran all the migration commands on the source environment
and created a snapshot before the migration failed, you do not need
to rerun all the migration commands again from the beginning. If the
migration failed on the target, for example at the database upgrade
step or when you ran the BPMMigrate command, you
can restore the database and rerun the commands on the target only.

## SOAP invocation timeout

If you are using
a SOAP connection, the migration command can take longer to complete
than the specified SOAP timeout value. You might see an exception
like java.net.SocketTimeoutException: Read timed out.

- If you installed the new version of the product on the same computer
as the source environment, the file is found in BPM\_home\_8.5/util/migration/resources/.
- If you installed the new version of the product on a different
computer and copied the migration files to the source environment,
the file is found in remote\_migration\_utility/util/migration/resources/.

## Enabling tracing

1 Locate the logging.properties file.Forthe DBUpgrade command-line utility, the file isin BPM\_home\_8.5 /util/dbUpgrade . For example: For the following command-line utilities: The file is in BPM\_home\_8.5 /util/migration/resources .For example:
    - /opt/ibm/WebSphere/AppServer/util/dbUpgrade/logging.properties
    - C:\bpm 85\util\dbUpgrade\logging.properties
    - BPMExtractSourceInformation
    - BPMManageApplications
    - BPMMigrate
    - /opt/ibm/WebSphere/AppServer/util/migration/resources/logging.properties
    - C:\bpm 85\util\migration\resources\logging.properties
2. Set the log level in the logging.properties file.
The default log level is FINE for both global logging
level and file output log level. Change both properties to FINEST
to capture more detail in the log. For example: # default global logging level. Logging level possible values: FINEST, FINER, FINE, INFO, WARNING, SEVERE.
.level = FINEST
# file output properties
com.ibm.bpm.migration.logging.NonBlockingFileHandler.level = FINEST

If you see exceptions for any of the following commands,
change the log level to FINEST, run the command again, and then check
the results, as described for each command.

- BPMConfig -migrate troubleshooting

The BPMConfig -migrate command works correctly if the deployment environment was created by the Deployment Environment wizard and the name of the deployment environment is shown in the administrative console under Servers > Deployment Environment.
- BPMExtractSourceInformation troubleshooting

This command takes a snapshot of the source environment. If you see an exception when you run this command, you can diagnose the problem by changing the log level to FINEST and running the command again.
- BPMGenerateUpgradeSchemaScripts troubleshooting

This command generates SQL scripts and upgradeSchema scripts. If you see an exception when you run this command, you can diagnose the problem by changing the log level to FINEST and running the command again.
- BPMManageApplications troubleshooting

This command disables or enables the automatic starting of applications and schedulers. If you see an exception when you run this command, you can diagnose the problem by changing the log level to FINEST and running the command again.
- BPMMigrate troubleshooting

This command imports the migration snapshot. If you see an exception when you run this command, it might be caused by running out of memory. Otherwise, you can diagnose the problem by changing the log level to FINEST and running the command again.
- BPMMigrationPreValidation troubleshooting

This command checks for migration readiness. After you run this command, you check the report for actions that you need to take before migration.
- DBUpgrade troubleshooting

This command upgrades the databases. If you see an exception when you run this command, you can diagnose the problem by changing the log level to FINEST and running the command again.
- Business Process Choreographer Archive database upgrade troubleshooting

If you are using DB2, when you run the upgradeSchemaAll\_de\_name command or run the SQL scripts to upgrade the databases manually, you might see an error when a new column is added to a Business Process Choreographer Archive database table.
- Errors when starting application cluster after migrating

After you have migrated and you start the application cluster, you might have non-Business Automation Workflow applications that do not start and you might see errors in the log. This problem is caused when the proxy or HTTP server configurations that were present in your source environment need to be applied to your target environment.
- OutOfMemoryErrors after migration

If you have Java API for XML Web Services (JAX-WS) applications, you might see java/lang/OutOfMemoryError errors after you migrate from a previous version of IBM Business Automation Workflow.
- Error message when server first starts

When the server first starts after you have migrated the databases, you might see a database communication error about too many results. This error can safely be ignored. However, if you are using a SQL Server database, and you see errors about invalid object names, you must turn off XACT\_ABORT.
- Error message when creating a second deployment environment

After you have migrated, when you create a second deployment environment, the logs might show some errors, as follows. These errors can be ignored.
- Errors in log when starting applications

When you run applications after migration, you might see errors in the SystemOut.log about ComponentMetaData. These errors can be ignored.
- Instance Details UI controls fail to render

If you created a process application in IBM Business Process Manager V8.5.6 that contains one or more custom Instance Details UI controls, these controls might not display after you migrate to 24.0.0.0.
- java.lang.ClassNotFoundException during or after migration

If custom application JAR files were added to the WebSphere® Application Server installation in the install\_root/lib/ext directory, there might be a conflict between the custom application classes and the IBM Business Automation Workflow classes.