# Traditional: Creating a governance process that installs a snapshot when the status changes
(deprecated)

## About this task

The System Governance toolkit (TWSYSG) contains the resources that you need to build a governance
process. The toolkit has service flows for installation and snapshot status changes, templates that
provide governance processes for installation and snapshot status changes, and governance business
objects.

When you create a snapshot or change its status, an instance of the Default Snapshot Status
Change governance process from the System Governance toolkit is started. You can create a custom
governance process to replace the default process. Bind the custom process to the snapshot event for
the process application and add a call to the Install Snapshot service flow. You can then use the
governance process to install a snapshot on a server whenever someone changes the status. For
example, you can set up a governance process that installs snapshots to a test server as soon as the
status is changed to Test. This implementation contributes to continuous integration.

In its simplest form, this custom governance process has a start event, an end event, and three
activities. The first activity provides a list of available servers for the process application that
is under this governance. The second activity initializes the required data in the
ProcessAppInstallation object since the Install Snapshot service flow expects this object. The third
activity starts the installation request. However, this is a governance process, so make sure the
governance goals are met. If your process installs a snapshot on a production server, you probably
want an approval process as part of this snapshot governance process, so that it goes through proper
review and approval before it is automatically installed.

## Procedure

1. In IBM® Process
Center,
create a process application to use for governance. This
process application contains your installation governance process.Note: You
cannot create a governance process in a toolkit. Use process applications
to create governance processes.
2. In IBM Process
Designer,
add a dependency on the System Governance toolkit to your process
application. The process application must have a direct
dependency on the System Governance toolkit snapshot to function as
a governance process. Indirect dependencies are not supported.
3. Create a process that you can use for governance in the New Process window
using the Snapshot Status Change template. Click Finish. 

The governance templates are available only when a dependency exists on the System Governance
toolkit. After you save the governance process, the input variable,
SnapshotStatusRequest, that was set by the template cannot be changed.Note: The
governance process must be created using the governance template. You cannot manually create a
variable of type SnapshotStatus and have your governance process work correctly.
4 Using the template as a base, develop the governance process to meet your organization'srequirements. The following steps provide some suggestions.
    1. Create an activity that calls the Get All Process Servers service flow from the System
Governance toolkit.
This service flow provides a list of the servers that can be used to install a snapshot of
that process application.
    2. Create an activity that calls the Install Snapshot service flow from the System Governance
toolkit. This service flow takes a ProcessAppInstallation object for input.
    3. Provide process application and snapshot parameters from the
SnapshotStatusRequest process input object. For the server parameter, use a
server object that is in the list of servers from the Get All Process Servers call.
5. When the governance process is complete, take a snapshot
of the process application, label it, and set the status of the snapshot
to Released.  Only a released snapshot of the governance
process can be applied to a process application.
6. Apply the new governance process as the Snapshot Status Change governance process for process
applications that you want to govern. See the related link to instructions for that task.

## Results

A new process instance of your governance process now starts whenever a new snapshot is created
or the status of the snapshot is changed.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for installing a process application (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)