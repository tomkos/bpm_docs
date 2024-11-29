<!-- image -->

# Deleting BPEL process instances using Business Process Choreographer
Explorer

## Before you begin

The
process instance must be in the finished, failed, terminated, or compensated
state.

## About this task

You might
want to keep process instances in your database, for example, to query
data from process instances that are not written to the audit log,
or if you want to defer the deletion of processes to off-peak times.
However, old process instance data that is no longer needed can impact
disk space and performance. Therefore, you should regularly delete
or archive process instance data that you no longer need or want to
maintain. Make sure that you run this maintenance task at off-peak
times.

You can delete completed process instances using either
Business Process Choreographer Explorer, for example, to delete individual
process instances, or the deleteCompletedProcessInstances administrative
script to delete several process instances at once. Alternatively,
you can archive completed process instances in the Business Process
Archive database.

In Business Process Choreographer Explorer,
complete the following steps to delete a process instance.

## Procedure

1. Display the process instances that you administer.
Click Administered By Me under Process
Instances in the Views tab navigation
pane.
2. Select the process instance that you want to delete and
click Delete.

## Results

<!-- image -->