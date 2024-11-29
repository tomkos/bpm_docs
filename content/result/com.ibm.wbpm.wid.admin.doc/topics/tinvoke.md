<!-- image -->

# Invoking operations

## Before you begin

To invoke an operation:

## Procedure

1. If the Events page is not already open, click the Events tab
to open it.
2. Click the Continue icon  to invoke your operation. (If
an exception is received that states that the server must be running
in development mode, you can enable development mode for the server
by following the instructions in the topic Enabling development mode for stand-alone test environment servers.)

## What to do next

Depending on the deployment state of the module, the Deployment
Location wizard may open to prompt you to select a deployment location
for the module. If the Deployment Location wizard opens, follow the
instructions described in the topic "Deploying modules from the integration
test client." If the deployment wizard does not open and the test
pauses at a manual Emulate event, specify some output parameter values
or select an exception to throw as described in the topic "Specifying
emulation values."

If the test does not pause at a manual Emulate
event, it will most likely run to completion and you will probably
want to reinvoke the operation or generate an Invoke event to invoke
and test a different operation. These tasks are described in the topics
"Reinvoking operations" and "Generating Invoke events."

If you
encounter a ServiceRuntimeException when running a test that involves
asynchronous invocations from a mediation flow, the exception is expected
and can be ignored. It is thrown when the mediation flow polls for
results but the invocation response is not yet available.

If
you want to test an application on a remote machine and you are experiencing
communication problems with the remote server, such as problems in
publishing to the remote server or obtaining the status of the server,
see the topic Resolving communication problems with remote servers.