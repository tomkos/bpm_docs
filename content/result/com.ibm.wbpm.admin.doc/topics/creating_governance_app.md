# Traditional: Creating a governance process for installing a process application
(deprecated)

## About this task

Business Automation Workflow includes
the System Governance toolkit, which supplies the process templates,
service flows, and business objects that you need to create a governance
process. This topic describes creating a process relating to the installation
of a process application snapshot. You can also create a governance
process relating to changing the status of a snapshot for a process
application or a toolkit.

By default, when anyone tries to install a snapshot of a process application, an instance of the
Default Installation Requested governance process from the System Governance toolkit is started.
That default governance process just allows the installation to proceed. If you want to apply
governance to that process application, you need to replace that default governance process with one
that is customized to your requirements. You can use the governance process to notify people of the
installation or you can set approvals in place so that no one can install it from Process Center on a workflow server until those approvals
have been completed. Governance can provide a way to ensure that proper testing is done and
approvals are secured before a snapshot of a process application is installed.

A governance process created in IBM Business Process Manager V8.0.0 cannot be used in this
version. You must use a governance process from V8.0.1 or later. You must use the process described
here to create a governance process. You must build your governance process using a template from
the System Governance toolkit.

## Procedure

1. In Process Center, create
a process application to use for governance. This process
application will contain your installation governance process. (You
cannot create a governance process in a toolkit. Only process applications
can be used to create governance processes.)
2. In Process Designer, add a dependency on the System Governance
toolkit to your process application. The process application
must have a direct dependency on the System Governance toolkit snapshot
to be able to create governance processes. Indirect dependencies are
not supported.
3. Create a process for use as a governance process. In the
New Process window, give the governance process a name that will be
meaningful to potential users, and click the Select button
to open a window where you can choose which governance template you
want to use. For this governance process, choose the Installation
Requested template. Click Finish.   The
governance templates are only available for use with a process application
when a dependency on the System Governance toolkit has been established.
Once you save the governance process after making the governance template
selection, the input variable, ProcessAppInstallationRequest, that
has been set by the template cannot be changed.
4 Using the governance process template as a base, developa governance process to meet your organization's requirements. You can build upon the governance process using the governanceservice flows; see the related link. For more information, see Configuring email for task notification assignments .
    1. Add an activity that calls the Install Snapshot service
flow, which is located in the System Governance toolkit, similar to
what is done in the Default Installation Requested governance process
(the product default).  The installation will be considered
finished once the Install Snapshot service flow or the Cancel Snapshot
Installation service flow has run.
    2. Add activities and email to customize the governance
process to fit your governance requirements.

## What to do next

When the governance process is complete, take a snapshot
of the process application, label it, and set the status of the snapshot
to "Released." Only a released snapshot can be applied to a process
application by an administrator.

Apply the new governance process
as the governance for process applications. See the related link to
instructions for that task.

- An administrator changes the association to the default governance
process from System Governance toolkit.
- An administrator changes the association to a different released
snapshot of the same governance process.
- An administrator changes the association to a released snapshot
of a different governance process application.

## Related tasks

- Traditional: Applying a governance process to a process application or snapshot (deprecated)
- Traditional: Migrating a governance process from IBM Business Process Manager V8.0.0 (deprecated)
- Traditional: Creating a governance process for the status of a snapshot (deprecated)
- Traditional: Creating a governance process that installs a snapshot when the status changes (deprecated)
- Traditional: Changing a governance application (deprecated)
- Traditional: Testing a governance process (deprecated)
- Traditional: Exporting and importing a process application that uses customized governance (deprecated)
- Traditional: Recovering if a process application under governance fails to install (deprecated)
- Traditional: Removing governance to install a snapshot on Workflow Server (deprecated)

## Related reference

- Traditional: Governance service flows (deprecated)