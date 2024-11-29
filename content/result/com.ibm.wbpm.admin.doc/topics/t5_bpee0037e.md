<!-- image -->

# Event unknown (Message: CWWBE0037E)

## Reason

A common reason for this error is
that a message is sent to a process but the receive or pick activity
has already been navigated, so the message cannot be consumed by this
process instance again.

## Resolution

- If the event is supposed to be consumed by an existing process
instance, you must pass correlation set values that match an existing
process instance which has not yet navigated the corresponding receive
or pick activity.
- If the event is supposed to start a new process instance, the
correlation set values must not match an existing process instance.

For more information about using correlation sets in
BPEL processes, see the   technote on correlation sets in BPEL processes.