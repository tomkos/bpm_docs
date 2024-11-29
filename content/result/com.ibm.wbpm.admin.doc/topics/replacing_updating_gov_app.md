# Traditional: Changing a governance application (deprecated)

## About this task

In IBM® Business Automation
Workflow,
governance is always enabled, but the default implementations impose
no constraints on installation or status change. You can provide a
governance process to require notifications or approvals when a snapshot
is installed on a server or when a snapshot changes status. To put
this new process into use, replace the existing governance process
with your new one. For information about how to create governance
processes, see the related links.

- An administrator changes the association to the default governance process from System
Governance toolkit.
- An administrator changes the association to a different released snapshot of the same governance
process.
- An administrator changes the association to a released snapshot of a different governance
process application.

## Procedure

1. Terminate or complete the running instances of the snapshot
that is under governance by the process that you are going to change.
2. Log in to Process Center using
an ID that has administrative authority for the process application
for which you want to provide governance.
3. Open the process application for which you want to apply
governance. If you are applying governance for status changes to a
snapshot, you can open a process application or a toolkit.
4. Choose the governance process that you want to replace and click
Change.
A window opens where you can choose the governance process that you want to use as a
replacement. You can see a list of governance processes available for use. The list includes only
released processes with a dependency on the System Governance toolkit for the current version. You
can sort the list of governance processes by name or creation date.
5. Choose the governance process that you want to use and
click OK.

## Results

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)