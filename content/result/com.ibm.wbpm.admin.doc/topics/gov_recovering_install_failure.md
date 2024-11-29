# Traditional: Recovering if a process application under governance fails to install
(deprecated)

## About this task

## Procedure

- If a customized governance process is faulty, change to
the default governance process, fix your customized governance process,
and then change back to your process from the default process.
- If the server stopped, the server administrator must fix
the problem.
- If the connection to the server fails during installation
of a snapshot, bring the server back online and reinstall the snapshot.
- If the installation failed because the process application
snapshot is invalid, it can never be installed. Create a new snapshot.
- If the administrator can determine the cause of the failure,
the administrator should fix the problem and then try again to install
the process application.
- If a governance process is used to install a snapshot,
process the InstallResponse returned by the Install Snapshot service
flow to make sure installation is successful. If the installation
is not successful, use the Cancel Snapshot Installation service flow
to cancel the previous installation request. This method
of cancellation is required if the installation is triggered through
a governance process which is associated with Snapshot Status Change
event. Changing the Snapshot Status Change governance assignment to
the default does not reset the status of failed installations.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)