<!-- image -->

# Cleanup procedures for Business Process Choreographer

## Types of tools available for deleting objects

- The cleanup service.
- The cleanup daemon for deleting shared work items and unused cached
people query results.
- The administrative console.
- Administrative scripts to delete objects.
- The modeling tool.
- Failed Event Manager.
- Business Process Choreographer Explorer.
- Business Process Choreographer APIs.

## Objects that can be deleted and tools to use

The
following Business Process Choreographer database objects can be deleted
when they are no longer needed.

- Run a script to delete templates:
    - Deleting process templates that are no longer valid.
    - Deleting human task templates that are no longer valid.

- Using the Process Admin Console or
REST API calls, as described in Monitoring and maintaining system data.
- Using the administrative console to configure the cleanup service
to schedule jobs that periodically delete eligible instances, which
is described in Configuring the cleanup service and cleanup jobs.
- Run a script to delete completed instances:
    - Deleting BPEL process instances using an administrative script.
    - Deleting completed task instances using an administrative script.
- Set the appropriate properties in the business model, using Integration Designer:
For business processes:
The property Automatically delete the BPEL process after
completion can have the value Yes, No,
or On successful completion. If this property has
the value No or On successful completion,
it makes sense to configure a cleanup job to delete the process instances.
For human tasks:
The property Auto deletion mode can have the
value On completion, or On successful completion (which
is the default). Deletion will only take place, and you can only change
the value for Auto deletion mode, if the property Duration
until task is deleted either has the value Immediate or
a defined interval. If the property Duration until task is
deleted has the value Never, automatic
deletion is disabled, the Auto deletion mode property
cannot be changed, and it makes sense to configure a cleanup job to
delete the human tasks. Otherwise, if Duration until task
is deleted does not have the value Never,
and Auto deletion mode has the value On
successful completion, then it makes sense to define a cleanup
job to delete the human tasks that do not complete successfully.
- To delete a few instances, it can be convenient to use the Business
Process Choreographer Explorer, which you can use to check details
about the instances before you delete them.

- Querying and replaying failed messages, using the administrative console describes how to replay messages
using the Business Process Choreographer pages, and using the failed
event manager page.
- Querying and replaying failed messages, using administrative scripts

You can delete unused shared work items by running the cleanupUnusedStaffQueryInstances.py
script with the -cleanupSharedWorkItems option,
which is described in Removing unused people query results, using administrative scripts.

| Human Task Manager custom property   | Description                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SharedWorkItemCleanup.Interval       | This property uses the WebSphere crontab format to control the schedule. The default value of 0 0 3 * * ? causes the daemon to run every night at three o'clock. To disable the daemon, set the value to the value DURATION\_INFINITE. This schedule applies to both the cleanup of shared work items and the cleanup of unused cached people query results. |
| SharedWorkItemCleanup.Timeout        | Specifies the maximum number of seconds that the shared work item cleanup can take. If this custom property is not set, the default that is used is 3600 seconds (one hour).                                                                                                                                                                                |

| Human Task Manager custom property   | Description                                                                                                                                                      |
|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UnusedStaffCleanup.Timeout           | Specifies the maximum number of seconds that the people query cleanup can take. If this custom property is not set, the default used is 3600 seconds (one hour). |
| UnusedStaffCleanup.SliceSize         | The number of unused people query results that are deleted in each transaction. If this custom property is not set, the default value of 500 is used.            |

<!-- image -->