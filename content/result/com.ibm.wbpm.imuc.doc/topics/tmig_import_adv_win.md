<!-- image -->

# Importing SIB messages and applications to the target environment

Import the snapshot from the source environment
into the target environment. The snapshot includes service integration
bus (SIB) messages and advanced IBM BPM Advanced applications.

Figure 1. Sample environment after the target is
started. The source environment is not running. The target can read
from the databases.

<!-- image -->

<!-- image -->

## Before you begin

Make sure that the messaging engines
in the target environment are started successfully before you run
the BPMMigrate utility, or the command will fail
with the exception: Cannot find message engine.

## About this task

Run the BPMMigrate utility
to migrate the snapshot from your previous version to your new version.

- Installs your applications in the target environment.
- Syncs the managed nodes.
- Runs the command to move the SIB messages from the source environment
to the target environment.
- Runs the command to re-create the scheduler tasks.
- Updates the WebSphere Adapters.

## Procedure

For each deployment environment that
you are migrating, complete the following steps:

1 Optional: If your applicationsuse WebSphere Adapters and you are migrating to a different computer,you must edit the XML file that contains the application deploymentconfiguration. You extracted the application deploymentconfiguration when you copied the migration utilities to the sourcecomputer. Now, edit the ApplicationMigrationInformation.xml fileto mark the WebSphere adapter instances that are to be updated tothe new version during migration.
    1. Locate the ApplicationMigrationInformation.xml file
in the following directory:snapshot directory\Adapters
    2. Edit the ApplicationMigrationInformation.xml file.Change
the value in <update> from false to true to
update a specific WebSphere adapter instance to the new version. Additionally,
copy the new version RAR file of the WebSphere adapter being marked
for update into the following directory: target\_install\_root\installableApps. Note:  Set
the <update> value to true for
any application that embeds WebSphere Adapter for SAP or WebSphere
Adapter for SAP instances that are configured at node or cluster scope.
Attention:  If the WebSphere adapter deployed
at node level is used to configure the WebSphere adapter at cluster
scope, the update of the WebSphere adapter must be applied in a consistent
manner. If the WebSphere adapter at cluster scope must be updated
to the new version, the corresponding instance of WebSphere adapter
that is defined at each individual node scope for nodes that are participating
in the cluster must be updated as well. Failure to perform the WebSphere
adapter update in a consistent manner for participating nodes and
cluster level can lead to failures of applications using a WebSphere
adapter instance. See Configuring Resource Adapters in the WebSphere
Application Server documentation.
2. Optional: 
If your source environment has business process applications that rely on shared libraries
under the install\_root\lib\ext directory, you must copy
those libraries to install\_root\_24.0.0.0\lib\ext in
the target environment before you migrate the snapshot. If the target environment is on more than
one computer, copy the libraries to the target environment on each computer.
3. Check that the target\_migration.properties file contains the configuration
information for the target environment.
When you migrate advanced applications to the target environment, the
use.default.virtual.host property gives you a choice as to whether the default
value default\_host is used. If you want to keep the original virtual host value,
which was configured in the source environment, you do not need to modify this property. Otherwise,
set the value to true, which means that all web applications in the target
environment will use the default virtual host value default\_host.
4 Migrate the snapshot from the source environment. Tips: Run the BPMMigrate command:install\_root \bin\BPMMigrate.bat -backupFolder snapshot\_folder -propertiesFile target\_migration\_properties\_file where: You can follow the progress of the command by reading theoutput, which includes the following actions: After the command has completed successfully, you seea message similar to the following message:CWMCO1004I: All steps of the migration completed successfully. Notes:

- Check the number of scheduler tasks in your source environment,
by looking at the number of BPEScheduler tasks in the migration  prevalidation
report under Database > Data
Volume. If you are warned that you have
a large number of scheduler tasks, increase the default timeout value
(180 seconds) by modifying the com.ibm.SOAP.requestTimeout property
in the install\_root\profiles\deployment\_manager\_profile\properties\soap.client.props file.
- If there are a large number of SIB messages in your source environment,
increase the default timeout value (180 seconds) by modifying the com.ibm.SOAP.requestTimeout property
in the install\_root\util\migration\resources\soap.client.props file.

```
install\_root\bin\BPMMigrate.bat -backupFolder snapshot\_folder -propertiesFile target\_migration\_properties\_file
```

- snapshot\_folder is the directory where the source information that was
extracted by the BPMExtractSourceInformation command is stored.
- target\_migration\_properties\_file is the full path to the migration propertiesfile in which you specified the configuration information for the target environment. Make sure thatthe following updates have been made:
    - The admin.username, admin.password,
bpm.home,  profile.name, and
target.config.property.file properties are all using the target environment
values.
    - The values of source.*.cluster.name are still set to the source environment
cluster members and not the target environment cluster members. If the cluster names are different
between the source and the target, these values are used to map the applications between the source
and target environments.

- Migrating each application
- Synchronizing the custom nodes
- Migrating the adapters
- Migrating each of the SIB messages
- Re-creating each of the schedulers

```
CWMCO1004I: All steps of the migration completed successfully.
```

- If you receive a connection timeout when
re-creating schedulers, the problem is caused by the call from the
wsadmin environment to the deployment manager. Increase the default
timeout value (180 seconds) by modifying the com.ibm.SOAP.requestTimeout property
in the install\_root\profiles\deployment\_manager\_profile\properties\soap.client.props file.
- If you receive a connection timeout when
importing SIB messages, increase the default timeout value (180 seconds)
by modifying the com.ibm.SOAP.requestTimeout property
in the install\_root\util\migration\resources\soap.client.props file.
- If a large number of scheduler tasks will expire
during your migration window, you might see a destination
not available exception during server startup because the
threshold for the number of messages for this destination has already
been reached. If so, modify the message threshold before you start
the target environment and verify migration. The message threshold
number should be larger than number of scheduler tasks that will expire.
To update the message threshold in the administrative console, follow
this example: Modify Buses > BPM.WPSDE.Bus > Destinations > BPEIntQueue\_AppCluster > Queue points > BPEIntQueue\_AppCluster@MECluster.000-BPM.WPSDE.Bus- > High message threshold.

## Related information

- BPMMigrate command-line utility
- Sample migration.properties files