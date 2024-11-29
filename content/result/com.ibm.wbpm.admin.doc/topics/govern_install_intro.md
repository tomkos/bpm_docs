# Traditional: Applying governance to a process application in the Process Center
(deprecated)

With governance applied to a process application, requests to install a snapshot of the process
application from Process Center are referred
to a governance process. You can use a governance process to install to a connected server or to
generate an installation package for an offline server. Beginning in Version 8.5.0, the governance
process is also started by the installation of snapshots using the BPMInstall
wsadmin command and the creation of offline packages using the
BPMCreateOfflinePackage wsadmin command.

An installation governance process is a process application in Process Center that is active and uses the Install
Snapshot service flow defined in the System Governance toolkit. The governance process application
is not installed on a workflow server. To install a process application snapshot
for a workflow server that depends on the governance toolkit, delete all application artifacts that
depend on anything from the governance toolkit.

The following steps explain how governance is applied to the installation
of a process application, referred to as MortgageApp in this explanation.

1. An administrator or developer creates a process application to
be used for governance and sets a dependency on the System Governance
toolkit.
2. A business analyst or developer creates a new process using the
Installation Requested template. The dialog for a new process contains
an option to use the Installation Requested template in the System
Governance toolkit to create an installation governance process. The
template ensures compatibility between the process and the specific
governance event.
3. When the governance process has been created, the developer can
use Process Designer to
add email notifications and other activities that customize the governance
process. The developer can then connect the activities, take a snapshot
of the process application, and set the status to "Released".
4. When the governance process is released, it is ready to be applied
to a process application. The developer tells an administrator the
name of the governance process or applies a governance tag to the
process so the administrator can easily find it.
5. Typically, the administrator would now remove the developer's
access to the governance process application so it is now only available
to administrators.
6. An administrator can now open the MortgageApp process application,
select the Governance tab, and change to the new governance process
that you created. (The governance option is exposed only to users
who have administrative authority for the process application.) Once
the new governance process has been selected, it is instantly active
on Process Center.
As long as this governance process is applied to the MortgageApp process
application, snapshots of MortgageApp cannot be installed on any process
server until the conditions set in the governance process have been
completed.
7. Subsequently, whenever a developer selects a target workflow server
and completes an installation request to install a snapshot of MortgageApp
on a server, the installation request starts the registered governance
process.
8. If status messages have been enabled, the status in Process Center changes
as the approval process progresses, using default states or status
messages customized and set in the governance process. The status
messages change when the installation service is called, but the Set
Installation Status service flow can still be used to
alter the value. Once installation is complete, the status looks just
the same as if governance was not used.

- An administrator changes the association to the default governance
process from System Governance toolkit.
- An administrator changes the association to a different released
snapshot of the same governance process.
- An administrator changes the association to a released snapshot
of a different governance process application.

The person who creates a process application has administrative
authority to change the governance process being used on that process
application. Take this authority into consideration when establishing
governance practices. In most cases, the prudent practice is to limit
the number of people who create process applications.

- Traditional: Applying a governance process to a process application or snapshot (deprecated)

 Traditional: 
If you have administrative authority for a process application, you can apply a governance process to it. Your governance process might notify selected people that a new snapshot is being installed or it might ensure that a new snapshot cannot be installed on a server until certain approvals have been secured or it might send out notifications of snapshot status changes.
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)

 Traditional: 
The governance process was redesigned for IBM Business Process Manager V8.0.1. As a result, governance processes that were developed in V8.0.0 cannot be reused; they must be revised to fit the V8.0.1 design.
- Traditional: Creating a governance process for installing a process application (deprecated)

 Traditional: 
Before governance can be applied to a process application, someone must design and create the governance process. The governance process defines the steps that are required before the process application snapshot can be installed on a workflow server.
- Traditional: Creating a governance process for the status of a snapshot (deprecated)

 Traditional: 
You can create a governance process that reacts to the status change of a snapshot.
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)

 Traditional: 
You can call the Install Snapshot service flow from a governance process based on the Snapshot Status Change template. You can make use of that ability to create a custom governance process that installs a snapshot on a server when someone changes the status of the snapshot or creates a snapshot.
- Traditional: Changing a governance application (deprecated)

 Traditional: 
You can create a governance process to replace the default governance for a snapshot.
- Traditional: Testing a governance process (deprecated)

 Traditional: 
Testing a governance process is similar to testing other process applications.
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)

 Traditional: 
If you export a snapshot of a process application that is under governance, the governance process is not included in the export package. The association to the governance process is exported with the process application, but the governance process itself is not exported. If you want to export the governance process as well, you need to do that action separately.
- Traditional: Recovering if a process application under governance fails to install (deprecated)

 Traditional: 
If the installation of a process application fails while under governance, a number of remedies are available for administrators.
- Traditional: Governance service flows (deprecated)

 Traditional: 
The System Governance toolkit provides templates and service flows that you can use in IBM® Process Designer to create or customize a governance process.
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

 Traditional: 
To install a process application snapshot for IBM Workflow Server that depends on the governance toolkit, delete all application artifacts that depend on anything from the governance toolkit.