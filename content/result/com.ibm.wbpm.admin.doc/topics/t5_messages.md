<!-- image -->

# Troubleshooting the execution of BPEL processes

## About this task

## Procedure

1. On the error page, click the Search for more
information link. This starts a search for the error code
on the IBM technical support site. This site only provides
information in English.
2. Copy the error message code that is shown on the error
page to the clipboard. The error code has the format CWWBcnnnnc,
where each c is a character and nnnn is
a 4-digit number. Go to the technical support
page.
3. Paste the error code into the Additional search
terms field and click Go.

## What to do next

- BPEL catch-all fault handlers don't catch all runtime faults

In some cases, BPEL catch-all fault handlers on synchronous one-way operations don't catch runtime faults.
- ClassCastException when stopping an application containing a microflow

The SystemOut.log file contains ClassCastException exceptions around the time when an application containing a microflow had been stopped.
- XPath query returns an unexpected value from an array

Using an XPath query to access a member in an array returns an unexpected value.
- An activity has stopped because of an unhandled fault (Message: CWWBE0057I)

The system log contains a CWWBE0057I message, the process is in the state "running", but it does not proceed its navigation on the current path.
- A microflow is not compensated

A microflow has called a service, and the process fails, but the undo service is not called.
- A long-running BPEL process appears to have stopped

A long-running process is in the state running, but it appears that it is doing nothing.
- Invoking a synchronous subprocess in another EAR file fails

When a long-running process calls another process synchronously, and the subprocess is located in another enterprise archive (EAR) file, the subprocess invocation fails.
- Hung threads when a long-running process is invoked synchronously (Message: WSVR0605W)

A long-running process invokes another long-running process synchronously. Under heavy workload conditions, the thread monitor reports hung threads in the SystemOut.log file (message WSVR0605W).
- Late binding calls the wrong version of a subprocess

A parent process invokes a subprocess using late binding. Both processes are in the same module. A new version of the subprocess is created by copying the module and changing the valid-from timestamp. After the module is deployed, the running instances of the parent process continue to invoke the old version of the subprocess instead of the new version.
- Versioned parent process calls a subprocess with the wrong parent process version

A versioned parent process invokes a subprocess by sending a request message and expects to receive a response message. If a new version of the parent process was deployed and the BPEL process that uses the invoke activity is a different version, you might receive an information message and the process might fail at a subsequent invoke activity.
- Unexpected exception during execution (Message: CWWBA0010E)

Either the queue manager is not running or the Business Process Choreographer configuration contains the wrong database password.
- Event unknown (Message: CWWBE0037E)

An attempt to send an event to a process instance or to start a new process instance results in a CWWBE0037E: Event unknown. exception.
- Cannot find nor create a process instance (Message: CWWBA0140E)

An attempt to send an event to a process instance results in a 'CreateRejectedException' message.
- The failed state of the process instance does not allow the requested sendMessage action to be performed (Message: CWWBE0126E)

An attempt to send an event to a process instance results in an 'EngineProcessWrongStateException' message.
- Uninitialized variable or NullPointerException in a Java snippet

Using an uninitialized variable in a BPEL process can result in diverse exceptions.
- Standard fault exception "missingReply" (message: CWWBE0071E)

The execution of a microflow or long-running process results in a BPEL standard fault "missingReply" (message: CWWBE0071E), or this error is found in the system log or SystemOut.log file.
- A fault is not caught by the fault handler

A fault handler is attached to an invoke activity to catch specific faults that are thrown by the invoked service. However, even if the invoked service returns the expected fault, the fault handler is not run.
- Parallel paths are sequentialized

There are two or more parallel invoke activities inside a flow activity, but the invoke activities are run sequentially.
- Copying a nested data object to another data object destroys the reference on the source object

A data object, Father, contains another data object, Child. Inside a Java snippet or client application, the object containing Child is fetched and set on a substructure of data object, Mother. The reference to Child in data object Father disappears.
- CScope is not available

Starting a microflow or running a navigation step in a long-running process fails with the following assertion: 'postcondition violation !(cscope != null) '.