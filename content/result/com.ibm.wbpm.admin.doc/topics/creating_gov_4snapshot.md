# Traditional: Creating a governance process for the status of a snapshot (deprecated)

## About this task

The System Governance toolkit (TWSYSG) contains the machinery
required to build a governance process. The toolkit has service flows
for installation and snapshot status, templates for governance processes,
and governance business objects.

When you create a snapshot
or change status, an instance of the Default Snapshot Status Change
governance process from the System Governance toolkit is started.
When a new snapshot of a process application or toolkit is created
or when the status of a snapshot changes, a message event is triggered.
If you have created a governance process and bound to the snapshot
event for the process application, you can use the governance process
to track status changes and issue notifications.

## Procedure

1. Create a new process application. This process
application will contain your snapshot governance process. (You cannot
create a governance process in a toolkit. Only process applications
can be used to create governance processes.)
2. In Process Designer, add
a dependency to the System Governance toolkit. You can
see the System Governance toolkit in your list of available toolkits
when you click the plus sign to add a dependency.
3. Create a process for use as a governance process. In the
New Process window, give the governance process a name that will be
meaningful to potential users, and click the Select button
to open a window where you can choose which governance template you
want to use. For this governance process, choose the Snapshot Status
Change template. Click Finish.   The
governance templates are only available for use with a process application
when a dependency on the System Governance toolkit has been established.
Once you save the governance process after making the governance template
selection, the input variable, SnapshotStatusRequest, that has been
set by the template cannot be changed.
4. Using the template as a base, develop a governance process
to meet your organization's requirements. Add activities and email
to customize the governance process to fit your governance requirements.
For information about email, see Configuring email for task notification assignments.

## Results

When the governance process is complete, take a snapshot
of the process application, label it, and set the status of the snapshot
to "Released." Only a released snapshot of the governance process
can be applied to a process application by an administrator.

Apply
the new governance process as the governance for process applications.
See the related link to instructions for that task. A new process
instance of your governance process starts whenever a new snapshot
is created or the status of the snapshot is changed.

- An administrator changes the association to the default governance
process from System Governance toolkit.
- An administrator changes the association to a different released
snapshot of the same governance process.
- An administrator changes the association to a released snapshot
of a different governance process application.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)