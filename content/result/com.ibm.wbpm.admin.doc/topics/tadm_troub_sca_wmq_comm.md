<!-- image -->

# Troubleshooting Service Component Architecture and WebSphere
MQ communications

## Before you begin

## About this task

## Procedure

1. Display the SCA module communicating with WebSphere MQ
to make sure it is still processing. Navigate to this page
using Applications > SCA Modules.
2. Display the queue manager to make sure it is still operational.
Use WebSphere MQ administrative tools to perform this task.
3. Display the bindings between the SCA module and the queue
manager to make sure the binding is correct. If the binding is incorrect,
change the binding. Navigate to this page using Applications > SCA modules >moduleName > Imports|Exports > importName|exportName > Bindings > bindingName [type].
4 Locate any messages that may indicate failed transactions. You will have to investigate system, SCA-specific message areas,WebSphere MQ-specific message areas, the failed event queue and otherlocations to determine what has failed.
    1. Examine SystemOut.log for any messages
that would indicate processing failures. If there is
a WebSphere MQ error, there will be an MQException linked somewhere
in the stack trace with a WebSphere MQ reason code (for example, 2059
is queue manager unavailable).
    2. Check AMQERRxx.LOG and
the WebSphere MQ FFDC files to determine the cause of a WebSphere MQ
error.
    3. Examine the application queues to determine if there
are any unprocessed messages. Make sure you examine both
WebSphere MQ and Service Integration Bus (SIB) queues.
    4. Examine the WebSphere MQ dead letter queue and the SIB
exception destination.
    5. Examine the failed event queue to determine if there
are any messages related to the applications of interest.