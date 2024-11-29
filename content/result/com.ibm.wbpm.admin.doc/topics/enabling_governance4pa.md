# Traditional: Applying a governance process to a process application or snapshot
(deprecated)

## Before you begin

Read Applying governance to a process application to understand
the overall context for this task.

You need administrative
authority for a process application before you can apply governance
to it.

## About this task

Version 8.0.1 provides new function in the System Governance
toolkit (TWSYSG), which contains the machinery required to build a
governance process. Governance processes designed for Version 8.0.0
will not run in later versions.

By default, when anyone tries
to install a snapshot of a process application, an instance of the
Default Installation Requested governance process from the System
Governance toolkit is started. That default governance process just
allows the installation to proceed. If you want to apply governance
to that process application, you need to replace that default governance
process with one that is customized to your requirements.

Also
by default, when a snapshot changes status, an instance of the Default
Snapshot Status Change governance process from the System Governance
toolkit is started. If you want to apply governance to the process
application, you need to replace that default governance process with
one that places notifications or controls around status changes.

You
can restore the system default governance process at any time or change
the governance process to a new version or a different process.

Follow
these steps to apply governance to a process application:

## Procedure

1. Before you apply governance to a process application, you
need to have a governance process in place on the Process Center server.
The governance process must have a snapshot in released status.
See the related links for instructions about how to create a new governance
process for installing process application snapshots.
2. On the Governance page for the process application, click the Change
link next to the current governance process and select another governance process to replace
it.
 Unless you already have another governance process in place, you are replacing the system
Default Installation Requested governance process or the system Default Snapshot Status Change
governance process. When your new installation governance process has been selected, any attempt to
install a snapshot of that process application to a server will start the governance process. If
your new governance process deals with changes to snapshot status, every new snapshot or status
change in a snapshot will trigger the governance event to provide notifications that the change has
happened.

## Results

## Related tasks

- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)