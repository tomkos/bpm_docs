<!-- image -->

# Example: executing a long running process using the Business
Process Choreographer JMS API (deprecated)

## About this task

## Procedure

1. Set up the JMS environment, as described in Deprecated: Accessing the Business Process Choreographer JMS API.
2 Obtain a list of installed process definitions.
    - Send queryProcessTemplates.
    - This returns a list of ProcessTemplate objects.
3 Obtain a list of start activities (receive or pick with createInstance="yes" ).

- Send getStartActivities.
- This returns a list of InboundOperationTemplate objects.
4. Create an input message. This is environment-specific,
and might require the use of predeployed, process-specific artifacts.
5 Create a process instance. With the JMS API, you can also use the call operationfor interacting with long-running, request-response operations providedby a BPEL process. This operation returns the operation result orfault to the specified reply-to destination, even after a long periodof time. Therefore, if you use the call operation,you do not need to use the query and getOutputMessage operationsto obtain the process' output or fault message.

- Issue a  sendMessage.

With the JMS API, you can also use the call operation
for interacting with long-running, request-response operations provided
by a BPEL process. This operation returns the operation result or
fault to the specified reply-to destination, even after a long period
of time. Therefore, if you use the call operation,
you do not need to use the query and getOutputMessage operations
to obtain the process' output or fault message.

6 Optional: Obtain output messages from the processinstances by repeating the following steps:

1. Issue query to obtain the finished
state of the process instance.
2. Issue getOutputMessage .
7 Optional: Work with additional operations exposedby the process:

1. Issue getWaitingActivities or getActiveEventHandlers to
obtain a list of InboundOperationTemplate objects.
2. Create input messages.
3. Send messages with sendMessage.
8. Optional: Get and set custom properties that
are defined on the process or contained activities with getCustomProperties and setCustomProperties.
9 Finish working with a process instance:

1. Send delete and terminate to
finish working with the long-running process.