<!-- image -->

# Service Runtime Exception handling

Service Runtime Exceptions are used to signal an unexpected condition
in the runtime.

Component developers can handle Service Runtime Exceptions in the
following ways:

1. Catch them and perform some alternative logic. For example,
if one partner is not able to service a request perhaps another one
might.
2. Catch the exception and "re-throw" it to your client.
3. Remap the exception to a business exception. For example, a
timeout for a partner may result in a business exception that indicates
most of the request was processed but there was one piece of the request
that was not completed and should be retried later or tried with different
parameters.

If an exception is not caught, the exception is passed on to the
component that called the current component.  This call chain continues
back to the original caller in the chain. For example, Module
A calls Module B and Module B calls Module
C and then Module C throws an exception, Module
B might or might not catch the exception. If Module
B does not catch the exception, then the exception travels
back to Module A.

When a ServiceRuntimeException is
thrown from a component, the current transaction will be rolled back.
This type of exception processing is repeated for all components
in the chain. For example, if a ServiceRuntimeException is
thrown from Module C, that transaction will be marked
for rollback. Then the exception is thrown to Module B,
where if it is not caught and another transaction is present, that
transaction also will be rolled back. Component developers can use
quality of service (QoS) qualifiers to control whether invocations
occur in the current transaction or a new transaction. So, if Module
A calls Module B and Module B is
part of a new transaction, then Module A can "catch"
a ServiceRuntimeException from Module B and continue
processing, without Module A's transaction rolling
back.

You should be aware that the contents of the
rolled back transaction can vary, depending on the nature of the transaction.
For example, long-running BPEL processes can be segmented into many
smaller transactions. Asynchronous request and response calls are
broken out of a transaction automatically (otherwise the calling application
might have to wait a long time for the response).

In instances where a transaction is broken into
multiple asynchronous calls (as opposed to one large transaction),
the initial work for the transaction would rollback at the occurrence
of a ServiceRuntimeException. However, the response from the asynchronous
call is sent from a different  transaction, and because the response
from the asynchronous call would have no place to go, an event is
created in the Failed Event Manager  (FEM).

The following list is of 4 current subclasses of ServiceRuntimeException:

1. ServiceExpirationRuntimeExceptionThis exception
is used to indicate that an asynchronous SCA message has expired.
Expiration times can be set using the RequestExpiration qualifier
on a service reference.
2. ServiceTimeoutRuntimeException This exception
is used to indicate that the response to an asynchronous request was
not received within the configured period of time. Expiration times
can be set using the ResponseExpiration qualifier on a service reference.
3. ServiceUnavailableExceptionThis exception
is used to indicate that there was an exception thrown
while invoking an external service via an import.
4. ServiceUnwiredReferenceRuntimeExceptionThis
exception is used to indicate that the service reference on the component
is not wired correctly.