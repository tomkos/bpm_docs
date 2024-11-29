# Starting the target environment

Disable
the automatic starting of all applications and schedulers in the target
environment, start the deployment manager, start the managed node
or nodes, and then start the servers.

Figure 1. Sample environment after the target is
started. The source environment is not running. The target can read
from the databases.

<!-- image -->

<!-- image -->

## Procedure

1 Disable the automatic starting of allapplications and schedulers in the target environment by running thefollowing command: install\_root \bin\BPMManageApplications.bat -autoStart false -target -propertiesFile target\_migration\_properties\_file where: This command ensures that no newevents or processes are entering the system. You can followthe progress of the command by reading the output, which includesthe following actions: After the command has completed successfully, you seea message similar to the following message:CWMCO4021I: Auto-start properties were set for all applications and the scheduler daemon.

```
install\_root\bin\BPMManageApplications.bat -autoStart false -target -propertiesFile target\_migration\_properties\_file
```

    - target\_migration\_properties\_file is the full path to themigration properties file in which you specified the configuration information for the targetenvironment. Make sure that the following updates have been made:
        - The admin.username, admin.password,
bpm.home, and profile.name properties have been changed to
the target environment.
        - The value of the target.config.property.file property is set to the full
path of the configuration properties file that you used to create your target environment.
        - The value of profile.name is set to the name of the target deployment
manager profile.
        - The values of source.*.cluster.name are still set to the source
environment.
- -target specifies that the command will disable
the target environment.

This command ensures that no new
events or processes are entering the system.

- Changing the auto start setting for each individual application
- Setting the auto start for each scheduler
- Synchronizing all custom nodes with the cell repository

```
CWMCO4021I: Auto-start properties were set for all applications and the scheduler daemon.
```

2. Start the deployment manager in the
target environment.
3. Start the nodes and make sure that they
are synchronized with the deployment manager. Important: If you have an environment with the Business Space
component (for Heritage Process Portal) installed
on multiple managed nodes in a cell, start only one node first and
start the other nodes only after the first node has already started.
4. Start the clusters.
5. Check to make sure that all clusters,
servers, and messaging engines have started.

## Related reference

- Error message when server first starts

## Related information

- BPMManageApplications command-line utility
- Sample migration.properties files
- Starting and stopping your environment