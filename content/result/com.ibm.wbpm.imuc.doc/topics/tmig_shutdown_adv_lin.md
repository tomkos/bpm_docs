# Shutting down applications

## Procedure

1 Run the BPMManageApplications commandto disable the automatic starting of all your applications and schedulers: where: This command ensures that no newevents or processes are entering the system. You can followthe progress of the command by reading the output, which includesthe following actions: After the command has completed successfully, you seea message similar to the following message:CWMCO4021I: Auto-start properties were set for all applications and the scheduler daemon. Check the log files. If you see the exception Couldn't flush user prefs:java.util.prefs.BackingStoreException: Couldn't get file lock , see Starting WebSphere Application Server gives warning message - Could not lock User prefs .
    - If you installed the new version of the product on the same computer as the source environment,
run the following command in the target environment. The properties in the
source\_migration\_properties\_file must point to the source
environment.install\_root\_24.x/bin/BPMManageApplications.sh -autoStart false -source -propertiesFile source\_migration\_properties\_file
    - If you installed the new version of the product on a different
computer and copied the migration files to the source environment,
run the following command on the source computer. The properties in
the source\_migration\_properties\_file must point
to the source environment.remote\_migration\_utility/bin/BPMManageApplications.sh -autoStart false -source -propertiesFile source\_migration\_properties\_file
    - -source specifies that the command will disable the source environment.
    - source\_migration\_properties\_file is the migration properties
file in which you specified the configuration information for the source environment. Make sure that
the values for admin.username, admin.password,
bpm.home, profile.name and
source.*.cluster.name are from your source environment.

This command ensures that no new
events or processes are entering the system.

    - Changing the auto start setting for each individual application
    - Setting the auto start for each scheduler
    - Synchronizing all custom nodes with the cell repository

```
CWMCO4021I: Auto-start properties were set for all applications and the scheduler daemon.
```

    - If you installed the new version of the product on the same computer as the source environment,
the log files are install\_root\_24.x/logs/migration/BPMManageApplications\_***.log and
install\_root\_24.x/logs/migration/BPMManageApplications\_***.wsadmin.trace.
    - If you installed the new version of the product on a different computer and copied the migration
files to the source environment, the log files are
remote\_migration\_utility/logs/migration/BPMManageApplications\_***.log
and
remote\_migration\_utility/logs/migration/BPMManageApplications\_***.wsadmin.trace.

If you see the exception Couldn't flush user prefs:
java.util.prefs.BackingStoreException: Couldn't get file lock, see Starting WebSphere Application Server gives warning message - Could not lock User prefs.

2 Restartthe source environment:

- If the source environment is stand-alone:
    1. Stop the source environment.
    2. Start the source environment.
- If the source environment is network deployment:

1. Stop the deployment manager, nodes, and servers.
2. Start the deployment manager, nodes, and servers.

## Results

Because you disabled automatic starting, the
applications and schedulers do not start automatically.

## What to do next

If migration
succeeds, you can no longer use the source environment because the
new version is using the databases. However, if migration fails and
you want to use the source environment again, you must run the following
command before you start the source environment:

```
install\_root\_24.x/bin/BPMManageApplications.sh -autoStart true -source -propertiesFile source\_migration\_properties\_file
```

```
remote\_migration\_utility/bin/BPMManageApplications.sh -autoStart true -source -propertiesFile source\_migration\_properties\_file
```

## Related information

- BPMManageApplications command-line utility
- Sample migration.properties files
- Starting and stopping your environment