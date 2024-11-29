<!-- image -->

# Exception handling

- invocation style
- binding type
- transaction qualifiers of the SCA components
- failed event manager configuration
- retry counts

- Synchronous, a blocking request is made to the target, and the response is returned on same
thread.
- Asynchronous, a non-blocking request is made, and the response is provided in a separate
thread.

- The JMS and MQ bindings are always asynchronous
- The web service and HTTP are synchronous
- The SCA binding can be either

## Exception handling for synchronous invocation

When a service component is called synchronously, or performs a synchronous invocation, both the
service requester and the service provider run in the same thread of execution (a thread of
execution can be defined as the smallest unit of processing that can be scheduled by an operating
system). The calling component is blocked until a response is received from the provider. Once the
service provider has been called, all processing is suspended until the thread returns a response.
The target can return a response message, an exception, or nothing (in a one way operation) to the
client. If the result is an exception, it can be either a business exception or a system
exception.

## Exception handling for asynchronous invocation

When a service component is called asynchronously, the service requester and the service provider
run in different threads. For an asynchronous invocation, the calling component is not blocked while
the request is processed by the provider. The SCA system returns control to the requester
immediately, allowing it to continue processing. The service requester may receive a system
exception during the invocation, or the service provider may experience a business or system
exception while processing the request. The service requester does not receive system exceptions
that occur in the service provider thread. According to the SCA asynchronous programming model,
runtime exceptions that occur at the target component are not returned to the source component.