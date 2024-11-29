# Monitoring and maintaining system data

## Monitoring system data

To view the status, log in to the Process
Admin Console, and click the System Maintenance Status tab.

To access the
dashboard, log in to the Process Admin Console. In the Server Admin area of the console, click
Performance > Performance Dashboard.

## Maintaining system data

The following table enumerates the Process Admin Console functions, REST API,
and wsadmin commands to maintain the key artifacts. For additional guidance on maintaining the
system, see Managing persisted data.

| Artifact type       | Process Admin Console                                                                      | REST API                                                | wsadmin commands                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process instances   | Workflow Admin > Health ManagementSee Deleting process instances                           | See Deleting process instances                          | IBM® Workflow Server BPMProcessInstancesPurge commandBPMDeleteSnapshot command also purges related process data.    IBM Workflow Center  The following wsadmin commands purge related process data. BPMRemoveProcessApplication command BPMRemoveToolkit command BPMSnapshotCleanup wsadmin command                                                                                   |
| Tasks               | Workflow Admin > Task Cleanup                                                              | Not available                                           | Workflow Server BPMTasksCleanup wsadmin commandThe following wsadmin commands also purge related task data. BPMDeleteSnapshot command BPMProcessInstancesPurge command    Workflow Center BPMTasksCleanup wsadmin commandThe following wsadmin commands also purge related task data. BPMRemoveProcessApplication command BPMRemoveToolkit command BPMSnapshotCleanup wsadmin command |
| Event Manager Tasks | Workflow Admin > Health Management                                                         | See Listing on-hold Event Manager tasks.                | See BPMListOnHoldEMTasks command.                                                                                                                                                                                                                                                                                                                                                     |
| Named snapshots     | Workflow Admin > Health ManagementSee Deleting snapshots                                   | See Deleting snapshots                                  | Workflow Server BPMDeleteSnapshot command Workflow Center BPMSnapshotCleanup wsadmin commandThe following wsadmin commands also purge related snapshot data. BPMRemoveProcessApplication command BPMRemoveToolkit command     See also BPMShowOrphanedToolkits wsadmin command                                                                                                        |
| Unnamed snapshots   | Workflow Admin > Health ManagementSee Deleting snapshots Not applicable to Workflow Server | See Deleting snapshotsNot applicable to Workflow Server | Workflow Server Not applicable Workflow Center BPMSnapshotCleanup wsadmin commandSee also Deleting unnamed snapshots from a Workflow Center server, automated method Deleting unnamed and archived snapshots, manual                                                                                                                                                                  |
| Durable messages    | Not available                                                                              | Not available                                           | Workflow Server BPMDeleteDurableMessages command Workflow Center BPMDeleteDurableMessages command                                                                                                                                                                                                                                                                                     |

- Deleting process instances

You can use the Process Admin Console, a REST API call, or a wsadmin command to delete process instances that match specified criteria.
- Deleting BPEL process instances

You can use the Process Admin Console, a REST API call, or a wsadmin command to delete BPEL process instances that match specified criteria.
- Deleting tasks

You can use the Process Admin Console or wsadmin commands to delete tasks and associated data and attachments from the Process database.
- Deleting snapshots

You can use the Process Admin Console or a REST API call to delete snapshots of process applications or toolkits from Workflow Server or Workflow Center.
- Deleting old data from the Performance Data Warehouse database

You can use the Process Admin Console or a REST API call to delete old data from the Performance Data Warehouse database.

## Related information

- Cleanup procedures for Business Process Choreographer