# Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## About this task

You cannot install a process application that contains a governance process on a workflow server.
Governance processes are supported in Process Center only. Therefore, when you create a snapshot of a process application that depends on the
governance toolkit, the entire process application cannot be installed on a workflow server.

Furthermore, you cannot update the process application so that it can be installed on a workflow
server. Removing the system governance toolkit dependency does not resolve this issue.

To resolve this issue, complete
the following steps:

## Procedure

1. Verify that processes in the process application do not
directly depend on the system governance toolkit. If there are dependencies,
delete all application artifacts that depend on anything from the
governance toolkit.
2. Set the IS\_GOVERNANCE flag to F in
the LSW\_PROJECT table in Process Center.
3. Attempt to reinstall the process application.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)