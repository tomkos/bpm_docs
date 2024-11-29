# Traditional: Exporting and importing a process application that uses customized governance
(deprecated)

## About this task

## Procedure

1. Export a
snapshot of the process application that is under governance
as a .twx file.  The governance process
selection is also exported in the .twx file.
2. Optional: If you want to use the current governance
process on the new server, export a snapshot of the governance process
as well. Import a snapshot of the governance process. Mark it as Released.  If you import a snapshot of the governance
process first, the dependency is restored when the process application
is imported. If a released snapshot of the governance process that
is identified in the process application dependency is not present
in the target Process Center, the
governance selection changes to the default governance process.
3. Import the
snapshot of the process application to the new server.
4. Optional: If you are applying a new governance
process instead of using one that was previously imported, associate
a snapshot of the new governance process with the process application.
 The snapshots of the governance process and the process application
must be in the same Process Center.

## Results

- If the process application in the target Process Center has
a dependency on a governance process that is not the default process,
the new snapshot uses that dependency. The imported dependency is
ignored.
- If the process application in the target Process Center has
a dependency on a default governance process, the new snapshot adopts
an imported dependency if a released snapshot of the governance process
identified in the .twx file is available in the Process Center.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)