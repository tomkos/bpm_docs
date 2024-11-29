<!-- image -->

# Asynchronous invocation qualifier

A synchronous call ties up a thread until it is complete.
An asynchronous invocation causes a message to be added to a message
queue; then, the client proceeds with its own processing without waiting
for a reply to its message.

Location: Asynchronous invocation
is set on a reference.

- Commit - The message is only sent if the
transaction is committed. Asynchronous invocations using the reference
will be transacted as a part of any client global transaction or extended
local transaction (that is, where the transaction Value qualifier
for the client implementation is local).
- Call (default) - Asynchronous invocations
using the reference occur immediately. This is logically equivalent
to suspending the current transaction and then invoking the target
service.

## Programming notes

The system ignores the
join transaction setting when a service is invoked asynchronously.

If
you use this qualifier on the reference of a Java component and if
the Java implementation makes asynchronous calls with a deferred response,
this qualifier must have the value "call". If the value is set to
"commit", the Java implementation waits for a response to a message
that has not yet been sent.