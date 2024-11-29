<!-- image -->

# Deleting work items for BPEL process using Business Process
Choreographer Explorer

## Before you begin

- You must be a process administrator or system administrator. However,
if Business Flow Manager is using the alternative process administration
mode that restricts process administration to system administrators,
then only users in the BPESystemAdministrator role can perform this
action.
- The process instance must be in the running, failing, or terminating
execution state.
- A work item with an assignment reason administrator can
only be deleted when it is not the last work item with this assignment
reason for the process instance.
- A work item for a specific user cannot be deleted when the work
item is assigned to everybody.
- The deletion of a process reader or administrator work item is
automatically propagated to all enclosed activities.

## About this task

In Business Process Choreographer Explorer, complete the
following steps to delete a process work item.

## Procedure

1. Display the process instances that you administer.
Click Administered By Me under Process
Instances in the Views tab navigation
pane.
2. Display the work items for a process instance. In
the Process Instances Administered By Me page,
select one or more process instances, and click Work Items.
3. Delete the work items. Select one or more
work items and click Delete.

## Results

<!-- image -->