<!-- image -->

# Transferring BPEL process work items if you are the administrator
of the process

## Before you begin

- You must be a process administrator or system administrator. However,
if Business Flow Manager is using the alternative process administration
mode that restricts process administration to system administrators,
then only users in the BPESystemAdministrator role can perform this
action.
- The process instance must be in the running, failing, or terminating
execution state.
- When work items with the assignment reasons administrator or reader are
transferred, the transfer is automatically propagated to all enclosed
activity instances.

## About this task

In Business Process Choreographer Explorer, complete the
following steps to transfer a process work item.

## Procedure

1. Display the process instances that you can administer.
Click Administered By Me under Process
Instances in the Views tab navigation
pane.
2. Display the work items for a process instance. In
the Process Instances Administered By Me page, select the check box
next to one or more process instances, and click Work Items.
3 Transfer the work item.
    1. In the New Owner / Group Name field,
enter either the user ID or the name of the group to which the work
item will be transferred. Work items that are assigned to a user can
only be transferred to another user, and work items that are assigned
to a group can only be transferred to another group.
    2. Select one or more work items and click Transfer.

## Results

<!-- image -->