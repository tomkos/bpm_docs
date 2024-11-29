<!-- image -->

# Cannot find nor create a process instance (Message: CWWBA0140E)

## Reason

A common reason for this error is
that a message is sent to a receive or pick activity that cannot instantiate
a new process instance because its createInstance attribute
is set to no and the values that are
passed with the message for the correlation set which is used by this
activity do not match any existing process instances.

## Resolution

To correct this problem you must
pass a correlation set value that matches an existing process instance.

For
more information about using correlation sets in BPEL processes, see   Correlation sets in BPEL processes.