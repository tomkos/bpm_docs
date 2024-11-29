# Managing installed snapshots

## About this task

When you click the Installed Apps option in the Process Admin Console,
you  see the list of snapshots of process applications installed on the current workflow server.
Within each process application snapshot, only exposed processes are shown. For each process, you
can see the number of instances currently running.

- Sort and filter the list of snapshots on the server.Click the All,
Active, or Default option to filter the list of
snapshots shown.Tip: If you are using the Process Admin Console to monitor
and configure the Workflow Center server, the list of
snapshots are those of the process applications created on the current server. When you create a
snapshot and save it in the Workflow Center repository, it is
displayed as an inactive snapshot. (Click the All option to see all
snapshots, including inactive ones.) If you activate a particular snapshot using Workflow Center, the snapshot
is shown as active in this list.
- Configure runtime settings for a snapshot.Click a snapshot,
and then use the Exposing, Team
Bindings, or Environment Vars options
complete the configuration.
- Administer a snapshot.Click a snapshot, and then select one of the options from the Process
Admin Console. The available actions vary depending on the content and current state of the
installed snapshot, and include the following options. 

Option
Description

Activate Application
Activates the snapshot, which includes starting the
associated business level application (BLA).Activates the snapshot.

Deactivate Application
Deactivates the snapshot, allowing all currently running instances to
complete. Deactivated snapshots remain installed, but you cannot start a new instance of the exposed
processes or services. Tip: If you use the Process Admin Console to deactivate a
snapshot, active process instances in it remain active. This means that they
remain visible in Process Portal for example. If you
want the process instances to immediately suspend, you must instead use the
BPMDeactivate command with suspendAllBPDInstances set to
true. Snapshots that you run this command on with the parameter have an Inactive with
suspended instances state in the Process Admin Console.
Tip: You can delete an inactive process application snapshot on any test or production
workflow server using the wsadmin commands. See Deleting snapshots on workflow servers.

 Traditional: 
Stop Application
Stops the snapshot and its BLA. This option is available only for deactivated
snapshots that contain Advanced Integration Services.

Migrate In-flight Data
Migrates currently running instances to the version of the selected snapshot.

Sync Settings
Copies specified settings from the current snapshot to another snapshot.

Make Default Version
Makes the selected snapshot the default version on the current server. This
option is available only when you have more than one snapshot on the server.

 Traditional: 
Update Tracking
Definitions
If a problem occurs during snapshot installation and tracking definitions are
not sent to the Performance Data Warehouse, you can use this option to send the definitions for the
selected snapshot. Because tracking definitions are automatically sent to the Performance Data
Warehouse during snapshot installation, you should use this option only when a problem occurs.

 Traditional: 
Undeploy Application
Removes the snapshot's corresponding BLA and any Advanced Integration Service
artifacts from the workflow server, although the snapshot remains in the repository. This option is
available only for stopped snapshots that contain Advanced Integration Services.

If you want to administer a snapshot that contains advanced content, such
as a BPEL process, the user or group to which you belong must be assigned to the Configurator,
Operator and Deployer administrative security role. If you are not currently assigned to all
of these roles, click Users and Groups in the WebSphere administrative
console to modify the user or group roles. See Administrative security roles.

- Activating installed process applications

Use the Process Admin Console to activate snapshots installed on a workflow server.
- Deactivating and stopping installed process applications

Use the Process Admin Console to deactivate snapshots. All installed snapshots, except the default version, can be deactivated. If a snapshot contains advanced content generated in IBM® Integration Designer (such as SCA modules or BPEL processes), you can also stop the snapshot that is installed on a workflow server.
- Designating default snapshots

On a workflow server, the first snapshot you install is considered the default version. This means that the items within it run when an event or other trigger that applies to more than one version of a process or service is received. When you install subsequent snapshots, you can use the Make Default Version option in Process Admin Console to ensure the snapshot you want to run is the default.
- Synchronizing snapshots

Use the Process Admin Console to copy settings from one snapshot to another. You can copy the settings for environment variables, team bindings, and exposed process values. When environment variables are synchronized, the servers' information can be synchronized because the servers are implemented as environment variables.
- Configuring runtime settings for installed snapshots

You can use Process Admin Console to configure runtime settings for each process application snapshot that is installed on a workflow server. Runtime configuration settings include team bindings, exposed process and services, and environment variables.
- Scripting tools for managing process applications

 Traditional: 
Manage process applications with the WebSphere administrative (wsadmin) scripting program by using administrative commands (AdminTasks) or the Process Application Lifecycle (PAL) MBean.
- Deleting snapshots on workflow servers

 Traditional: 
Run the BPMDeleteSnapshot command to delete the process application snapshot from the server. If you are deleting the default snapshot, you must use the -force parameter.