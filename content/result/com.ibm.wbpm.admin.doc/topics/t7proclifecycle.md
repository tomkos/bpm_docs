<!-- image -->

# Managing the lifecycle of BPEL processes using Business Process
Choreographer Explorer

- State transition diagrams for BPEL process instances

Processes change state whenever something of significance happens during the lifecycle of the process instance. For example, an API request causes a process in the running state to be put into the suspended state. State transition diagrams show the state transitions that can occur during the process lifecycle. Microflows and long-running processes have different state transition diagrams.
- State transition diagrams for activities in BPEL processes

The state of an activity instance changes when a significant step in the execution of the activity instance occurs. The states and the state transitions depend on the type of activity.
- Lifecycle management of BPEL subprocesses

A process that is created and started by another process is known as a subprocess. The way in which the lifecycle of subprocesses can be managed depends on how these processes are modeled.
- Lifecycle of stand-alone human tasks that are invoked by a BPEL process

The lifecycle of an inline task is always managed by its associated BPEL process. The lifecycle of a stand-alone to-do task can be managed by the calling BPEL process depending on the definition of the task.
- Starting a new process instance

You can start a new BPEL process instance from any of the BPEL process templates that you are authorized to use.
- Monitoring the progress of a BPEL process instance

You can monitor the progress of a process instance to determine whether you need to take action so that the process can run to completion.
- Dynamic modification of BPEL process instances

Typically, a BPEL process is navigated as defined in the process model. However, sometimes you might need to override the navigation of a process instance at run time, for example, so that you can repair a process instance, or perform only those activities that are appropriate for the current context.
- Viewing and modifying the variables of an activity

View and modify the activity variables of a process instance using Business Process Choreographer Explorer.
- Suspending and resuming BPEL process instances

You can suspend a long-running, parent process instance. You might want to do this, for example, so that you can configure access to a back-end system that is used later in the process, or to fix a problem that is causing the process instance to fail. When the prerequisites for the process are met, you can resume the process instance.
- Terminating BPEL process instances

You might want to terminate a process instance, for example, if the work or documents it represents are no longer needed, if no one is available to complete the process instance, if you have encountered problems with the process template and it needs to be redesigned, and so on.
- Deleting BPEL process instances using Business Process Choreographer Explorer

Process templates can be modeled so that process instances are not automatically deleted when they complete. You can explicitly delete these process instances after they complete.

<!-- image -->