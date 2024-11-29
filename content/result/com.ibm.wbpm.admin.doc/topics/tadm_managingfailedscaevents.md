<!-- image -->

# Managing failed SCA events

## About this task

A Service Component Architecture (SCA) event is a request or response that is received by a
service application. It might come from an external source, such as an inbound application adapter,
or an external invocation to a web service. The event consists of a reference to the business logic
that it wants to operate and its data, which is stored in a Service Data Object. When an event is
received, it is processed by the appropriate application business logic.

- Event failures that occur during an asynchronous invocation of an SCA operation
- Event failures that are caused by a runtime exception, for example, any exception that is not
declared in the methods used by the business logic

The Recovery service sends failed SCA asynchronous interactions to failed event destinations that
have been created on the deployment environment bus. The data for failed events is stored in the
failed event database (by default, WPCRSDB). You can find the data in the failed event manager.

- If the exception occurs during the initial request, Component A is the source and Component B is
the destination for the failed event manager.
- If the exception occurs during the response, Component B is the source and Component A is the
destination for the failed event manager.

Because runtime exceptions are not declared as part of the interface, component developers should
attempt to resolve the exception and thus prevent a runtime exception from inadvertently being
propagated to the client if the client is a user interface.

To manage a failed SCA event, perform the following steps.

## Procedure

1. Use the failed event manager to locate information about the failed SCA event, taking note of
the exception type.
2. Locate the exception type in Table 1 to
determine the location and possible causes of the error, as well as suggested actions for managing
the failed event.

Table 1. Failed SCA events

Exception type
Possible cause of error
Suggested action

ServiceBusinessException
A business exception occurred during the execution of a business
operation.
Look at the exception text to determine the exact cause, and then take
appropriate action.

ServiceExpirationRuntimeException
A SCA asynchronous message has expired.
Set the expiration time using the RequestExpiration qualifier on the service
reference.Investigate why the service is not responding fast enough.

ServiceRuntimeException
A runtime exception occurred during the invocation or execution of a
service.
Look at the exception text to determine the exact cause, and then take
appropriate action.

ServiceTimeoutRuntimeException
Response to an asynchronous request was not received within the configured
period of time.
Set the expiration time using the RequestExpiration qualifier on the service
reference.Investigate why the service is not responding fast enough.

ServiceUnavailableException
This exception is used to indicate that there was an exception thrown while
invoking an external service via an import.
Look at the exception text to determine the exact cause, and then take
appropriate action.

ServiceUnwiredReferenceRuntimeException
A SCA reference used to invoke a service is not wired correctly.
Look at the exception text to determine the exact cause, and then take
appropriate action to correctly wire the SCA reference.