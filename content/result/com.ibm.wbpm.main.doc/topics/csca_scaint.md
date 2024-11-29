<!-- image -->

# SCA interactions

The diagram summarizes the different interface types, the supported
invocation methods and models, and how data is passed between client
and service.

For synchronous invocation, data is passed by reference within
the same SCA module, while for asynchronous calls the data is passed
by value. The table also summarizes when it is possible to use either
type safe or dynamic invocation based upon the interface type. The
dynamic invocation methods are always available for either WSDL port
type or Java interfaces. However, in order to have type safe invocation
methods available to the client a Java interface type must be used
for the interface definition on the appropriate client reference.

Figure 1. Summary of invocation models along
with supported methods for passing data

<!-- image -->

## Dynamic client invocation

There are a number
of key methods and interfaces needed to support both synchronous and
asynchronous interaction when using dynamic client invocation.

| Interface       | Methods                                          | Description                                                                                                                 |
|-----------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Service         | Object invoke(Service String, Object)            | Used to invoke synchronous service requests                                                                                 |
| Service         | Ticket invokeAsync(String, Object)               | Used to invoke one-way or deferred response asynchronous service requests                                                   |
| Service         | Ticket invokeAsyncWithCallback(String, Object)   | Used to invoke request with callback asynchronous service requests. The client must implement the ServiceCallback interface |
| Service         | Object invokeResponse(Ticket, long)              | Used to get response in the case of deferred response invocation                                                            |
| ServiceCallback | void onInvokeResponse(Ticket, Object, Exception) | Callback interface must be implemented by the client using a request with callback asynchronous service invocation          |