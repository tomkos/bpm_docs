<!-- image -->

# A long-running BPEL process appears to have stopped

## Reason

1. A navigation message has been retried too many times and has been
moved to the retention or hold queue.
2. A reply message from the Service Component Architecture (SCA)
infrastructure failed repeatedly.
3. The process is waiting for an event, timeout, or for a long-running
invocation or task to return.
4. An activity in the process is in the stopped state.
5. An activity in the process is looping. Check for a CWWBE0201W message in the
system log file.

## Resolution

1. Use the failed event manager console to display details about
a failed message and to replay it.
2 Check if there are any failed message in the failed event managementview of the administrative console.
    - If there are any failed events from Service Component Architecture
(SCA) reply messages, reactivate the messages.
    - Otherwise, either force complete or force retry the long-running
activity.
3. Check if there are activities in the stopped state or looping, and repair these activities. If
your system log contains a CWWBE0057I message you might also need to correct your model as described
in An activity has stopped because of an unhandled fault (Message: CWWBE0057I).