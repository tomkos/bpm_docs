<!-- image -->

# Asynchronous invocation

In addition to its published APIs and tools to develop asynchronous programs using Java™, IBM Business Automation Workflow also comes with a number of built-in
asynchronous messaging bindings and built-in asynchronous components.

Asynchronous invocation is said to be one way if the client does not want to capture a
response at all. This can only be selected on a one way operation.

There are two different ways that the client can capture the response at a later time. One is for
the client to call invokeAsync() and then continue processing until some later time
when the client makes a request to capture the response. This scenario is termed deferred
response, and it can only be selected on a request-response operation. Alternatively the client
also has the option of doing an asynchronous request with callback. To do this, the client
must first implement the ServiceCallback interface. Then, after calling
invokeAsyncWithCallback(), the SCA runtime provides a callback to the
ServiceCallback handler to provide the response to the client. Asynchronous with callback can only
be used on a request-response operation, and should only be used if the mediation flow component is
invoked as asynchronous with callback.

Figure 1. Asynchronous invocation models

<!-- image -->

SCA interfaces are always defined in the synchronous form. For each synchronous interface, one or
more asynchronous interfaces can be generated. When a callback mechanism is chosen by the client,
the client component needs to implement a class: <interface
name>.Callback.java. The interface of this class is derived from the interface of the
actual component that the client wants to use.