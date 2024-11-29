# Exporting SIB messages and applications from the source environment

Take a snapshot of your source
environment to export the service integration bus (SIB) messages and
advanced Business Automation Workflow applications.
You will import the messages and applications to the target environment
in a later step. You need one snapshot for each deployment environment
in your source cell. You do not need a separate snapshot for each
profile in your source cell.

Figure 1. Sample environment after the source is
shut down for migration. The source environment can still read from
the databases but can no longer write to them. The target is not running
but contains a deployment environment.

<!-- image -->

<!-- image -->

## Before you begin

If the source environment is a network deployment
environment, ensure that the deployment manager, node agent, and clusters
have been started. If the source environment is a stand-alone environment,
ensure that the stand-alone server has been started.

## About this task

## Procedure

For each deployment environment in your
source environment, complete the following steps:

1 Take a snapshot of the source environmentto export the SIB messages and advanced applications. where: For example:BPMExtractSourceInformation -backupFolder /tmp/snapshot -propertiesFile /opt/BPM/util/migration/resources/source\_migration.properties You can follow the progress of the commandby reading the output, which includes the following actions: After the command has completed successfully, you see a messagesimilar to the following message:CWMCO1002I: All steps of the snapshot completed successfully. Thelog location is listed in the output. If there are any errors or exceptions,they appear in the log. If you have errors and need to rerun thisstep, you must remove all contents from the directory you identifiedwith the -backupFolder parameter in the command.
    - If you installed the new version of the product on the same computer
as the source environment, run the following command in the target
environment:install\_root\_24.0.0.0/bin/BPMExtractSourceInformation.sh -backupFolder snapshot\_folder -propertiesFile source\_migration\_properties\_file
    - If you installed the new version of the product on a different
computer and copied the migration files to the source environment,
run the following command on the source computer:remote\_migration\_utility/bin/BPMExtractSourceInformation.sh -backupFolder snapshot\_folder -propertiesFile source\_migration\_properties\_file
    - snapshot\_folder is the directory where the
exported information is stored.
    - source\_migration\_properties\_file is the full
path to the migration properties file in which you specified the configuration
information for the source environment. Make sure that the values
for admin.username, admin.password,
bpm.home, profile.name and
source.*.cluster.name are from your source environment.

```
BPMExtractSourceInformation -backupFolder /tmp/snapshot -propertiesFile /opt/BPM/util/migration/resources/source\_migration.properties
```

    - Taking a snapshot of the SIB messages
    - Taking a snapshot of the applications
    - Exporting business level applications (BLAs)
    - Querying the deployment configuration for the adapters

```
CWMCO1002I: All steps of the snapshot completed successfully.
```

The
log location is listed in the output. If there are any errors or exceptions,
they appear in the log. If you have errors and need to rerun this
step, you must remove all contents from the directory you identified
with the -backupFolder parameter in the command.

2 Shut down the source environment beforeyou proceed with the migration. If you have a network deployment environment:

1. Stop the clusters.
2. Stop the nodes.
3. Stop the deployment manager.

## Results

| Folder                    | Contents                                                                                          |
|---------------------------|---------------------------------------------------------------------------------------------------|
| Adapters                  | Adapter configurations at the application level                                                   |
| Applications              | WebSphere® Application Server applications and HTM\_PredefinedTask system applications             |
| BLAs and CompositionUnits | Assets used by business-level applications                                                        |
| Messages                  | Service integration bus (SIB) messages that have not yet been processed in the source environment |

## Related information

- Starting and stopping your environment
- BPMExtractSourceInformation command-line utility