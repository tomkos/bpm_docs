<!-- image -->

# BPEL process administration-frequently asked questions

- How is administering enterprise applications that contain BPEL processes different when they are part of a process application, which is deployed using Workflow Center?
- How is administering enterprise applications that contain BPEL processes different when development mode is enabled, or when the application is running on a Workflow Center server?
- What happens if a process template is in the started state, but the application it belongs to is in the stopped state?
- How do I stop new process instances being created?
- What happens to running instances when a newer process template becomes valid?
- What happens to a running instance if the template it was created from is stopped?
- How can I tell if any process instances are still running?
- Why can't I stop an enterprise application if it has BPEL process instances?

## How is administering enterprise applications
that contain BPEL processes different when they are part of a process
application, which is deployed using Workflow Center?

Applications that contain BPEL processes as part of a process
application should be started, stopped, deployed, and undeployed using Workflow Center. Certain
lifecycle operations, such as starting and stopping templates are
not available in Workflow Center. You
must perform these operations using either the administrative console
or the administrative scripts.

Applications that contain BPEL
processes cannot be stopped or undeployed if instances of BPEL process
or human task templates in any state are present. This restriction
does not apply if the process server is running in development mode
or the process application is running on a Workflow Center server.

## How is administering enterprise
applications that contain BPEL processes different when development
mode is enabled, or when the application is running on a Workflow Center server?

When development mode is enabled
on a stand-alone process server, you can stop and uninstall business
process applications even when the application contains running instances
of BPEL processes or human tasks. In a production system, making sure
that development mode is not enabled can protect your long-running
instances from being accidentally stopped or uninstalled.

## What happens if a process template is in
the started state, but the application it belongs to is in the stopped
state?

If a currently valid process template is in the started
state, but the application is in the stopped state, no new process
instances are created from the template. Existing process instances
cannot be navigated while the application is in the stopped state.

## How do I stop new process instances being
created?

Using the administrative console, select a process
template, and click Stop. This action puts
the process template into the stopped state, and no more instances
are created from the template. After the template stops, any attempts
to create a process instance from the template result in an EngineProcessModelStoppedException error.

## What happens to running instances when a
newer process template becomes valid?

If a process template
is no longer valid, this fact has no effect on running instances that
were instantiated from the template. Existing process instances continue
to run to completion. Old and new instances run in parallel until
all of the old instances have finished, or until they have been terminated.

## What happens to a running instance if the
template it was created from is stopped?

Changing the state
of a process template to 'stopped' only stops new instances being
created. Existing process instances continue running until completion
in an orderly way.

## How can I tell if any process instances
are still running?

Log in to the Business Process Choreographer
Explorer as a process administrator, and go to the Process Instances
Administered By Me page. This page displays any running process instances.
If necessary, you can terminate and delete these process instances.

## Why can't I stop an enterprise application
if it has BPEL process instances?

For a process instance
to run, its corresponding application must also be running. If the
application is stopped, the navigation of the process instance cannot
continue. For this reason, you can only stop an enterprise application
if it has no BPEL process instances.

<!-- image -->