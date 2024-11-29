<!-- image -->

# Suspend transaction qualifier

The suspend transaction qualifier applies when the implementation
is running in a global transaction and makes a synchronous invocation.
It determines if that global transaction is to be propagated to the
target component. A transaction cannot propagate to the target if
the implementation is running in a local transaction or if the invocation
is done asynchronously. Under those conditions, this qualifier is
ignored.

If the implementation is running in a global transaction,
that transaction is propagated on all synchronous invocations to the
target components by default. If
those target components can join the global transaction and you do
not want this to happen, add this qualifier and set its value to "true".

Location: The
suspend transaction qualifier is set on a reference.

- False (default) - Synchronous invocations
run completely within any client global transaction.
- True - Synchronous invocations occur outside
any client global transaction. The target service's transactional
environment is not affected by this qualifier.

Application: When suspend transaction is set to
"true", the target component's effective transaction environment
is either a new global transaction or a local transaction. The suspend
transaction reference qualifier is ignored for asynchronous interactions.