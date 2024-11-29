<!-- image -->

# Service invocation styles

- Synchronous
- Asynchronous with deferred response
- Asynchronous with callback
- Asynchronous one way

The synchronous invocation style is often the fastest. Using the synchronous invocation style, a
mediation flow can share a global transaction with a service. The mediation flow processing
continues when the service returns a response.

The asynchronous styles provide a separation between the processing carried out by the mediation
flow, and the service. This is necessary if an operation takes a significant amount of time for the
service to complete, or where it is required that the service invocation is not carried out, until
all mediation flow processing is complete.

- Synchronous invocation

When a service component is called synchronously, or performs a synchronous invocation, both the service requester and the service provider run in the same thread of execution (a thread of execution is defined as the smallest unit that can be scheduled in an operating system). The calling component within IBM Workflow Server is blocked until a response is received from the provider.
- Asynchronous invocation

When a service component is called asynchronously, the service requester and the service provider run in different threads of execution. For an asynchronous invocation, the calling component within IBM Workflow Server is not blocked while the request is processed by the provider. The SCA runtime returns control to the requester immediately, allowing it to continue processing.
- Invocation Style property for request-response operations

The Invocation Style property of the Service Invoke mediation primitive or the Callout node determines the invocation style that is used to invoke a service.
- Invocation Style property for one way operations

The Invocation Style property of the Service Invoke mediation primitive or the Callout node determines the invocation style that is used to invoke a service
- Invocation style compatibility with prior releases

In version 8.0 of IBM Business Automation Workflow, additional invocation style options are available to control the invocation style that is used by the mediation flow component when it invokes a service. The Async (Compatibility) and Default (Compatibility) invocation style options are for compatability with earlier versions. It is recommended that you use the non-compatibility invocation style options.