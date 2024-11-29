# How to process mediations in parallel

## Introduction

- Asynchronous with callback, where the response is handled on a
separate thread
- Asynchronous with deferred response, where the response is handled
on the same thread as the request

If the service call is asynchronous with callback, the
initial thread does not wait and can do other mediation work. This
invocation style is not supported in an aggregation block (an aggregation
block is a group of mediation primitives that occur between a Fan
Out mediation primitive and a Fan In mediation primitive). Asynchronous
with callback can only be selected on a request-response operation.
If the service call is asynchronous with deferred response, and the
Service Invoke mediation primitive is in an aggregation block, the
initial thread can also do other mediation work. Asynchronous with
deferred response can only be selected on a request-response operation.

Whether
a service call is asynchronous with callback, or not, is determined
by a number of factors. One key factor is how the mediation flow component,
containing the Service Invoke mediation primitive, is called. Generally,
the export binding determines the way the mediation flow component
is called. A service call using asynchronous with callback is only
possible if the mediation component itself is also called using asynchronous
with callback.

Whether a service call is asynchronous with deferred
response, or not, is determined by the properties of the Service Invoke
mediation primitive. It must be a request-response operation. If the invocation
style property is async, and the require
mediation flow to wait for service response when the flow component
is invoked asynchronously with callback property is true,
then the service call for a request-response operation is asynchronous
with deferred response. If the invocation style property
is default, then other factors, listed in the
details section, determine whether the service call is synchronous,
asynchronous with deferred response, or asynchronous with callback.
If it is a one way operation, the invocation style is asynchronous
one way. For more information about the invocation model see: Service Invoke mediation primitive

If the invocation
style property of the Service Invoke mediation primitive
is default, the preferred interaction style
is specified on the target service. You can specify a preferred interaction
style on the interface. You can specify synchronous or asynchronous.
The default is ANY, which means you do not
specify a preference.

## Details

| Invocation style                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Synchronous                         | The thread blocks and waits for the response. The response returns on the same thread. The invoke style of Service Component Architecture (SCA) invocation is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Asynchronous with deferred response | The thread waits for the response. If the Service Invoke mediation primitive is not in an aggregation block, the thread waits after each service request, until a response is received. If the Service Invoke mediation primitive is in an aggregation block, further processing of the aggregation can be performed before the thread waits for responses to all outstanding service requests. In both cases, the invokeAsync style of SCA invocation is used. For a request-response operation, invokeResponse is used to retrieve the response from the service. The async timeout property can be used to specify the maximum time to wait for the response. This can only be selected on a request-response operation.Note: If there is an existing transaction, the wait occurs inside the existing transaction; therefore, the wait is also bound by the global transaction timeout. |
| Asynchronous with callback          | The original thread does not wait for a response or callback. The original thread continues and any further mediation primitives wired on the input side of the Service Invoke mediation primitive are called. The Service Invoke response is received on a new thread, and the new thread continues the mediation flow from the Service Invoke mediation primitive. This can only be selected on a request-response operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

- The invocation style used to call the mediationflow component, which can be one of the following:
    - Synchronous (invoke).
    - Asynchronous with deferred response (invokeAsync ).
    - Asynchronous with callback (invokeAsyncWithCallback).
- The invocation style property of the Service
Invoke mediation primitive.
- If the invocation style property of the Service
Invoke mediation primitive is default, the
preferred interaction style is specified on the target service. You
can specify a preferred interaction style on the interface. You can
specify synchronous or asynchronous. The default is ANY,
which means you do not specify a preference.
- Whether the operation is one-way or request-response.
- The require mediation flow to wait for service response
when the flow component is invoked asynchronously with callback property
of the Service Invoke mediation primitive. This property defaults
to false, which means that you do not force
a service call to act in a synchronous manner.

## Calling the mediation flow component

- An export with a web services binding invokes a mediation flow
component using invoke.
- For a one-way operation, an export with a JMS or MQ binding invokes
a mediation flow component using invokeAsync .
- For a request-response operation, an export with a JMS or MQ binding
invokes a mediation flow component using invokeAsyncWithCallback .
- An export with an SCA binding can invoke a mediation flow component
using invoke or invokeAsync or invokeAsyncWithCallback.

## Calling the service

The invocation
style that is used to call the service is determined by
the properties of the Service Invoke mediation primitive. For more
information on invocation style options, see: Service Invoke mediation primitive

## Parallel threads example

The following figure
shows a Message Filter mediation primitive with two output terminals
that are wired to other mediation primitives. Assume that these terminals
have associated filter patterns and that the Distribution
mode property is set to All. Therefore,
if both patterns match, both output terminals are fired. The first
terminal to match is fired first, followed by the second terminal
to match and so on.

For the purposes of this example, assume
that the mediation flow component is called using invokeAsyncWithCallback,
and that the preferred interaction style of the references associated
with the two callout nodes is asynchronous.

Figure 1. Using
the Service Invoke mediation primitive for parallel processing

<!-- image -->

1. The first matching output terminal of MessageFilter1 is fired.
2. The input terminal of ServiceInvoke1 receives the input message,
and ServiceInvoke1 performs an asyncWithCallback invocation.
The call does not wait for a response and returns immediately.
3. The thread traces back up the wiring path to the MessageFilter1
mediation primitive.
4. The second matching output terminal of MessageFilter1 is fired.
5. The input terminal of XSLT2 is reached, and the transformation
occurs.
6. The response to the invocation made by ServiceInvocation1 is received.
The flow engine handles this and resumes the processing in ServiceInvoke1
on a new thread.

From now on, the threads can process in parallel.

1. The output terminal of XSLT2 is fired.
2. The Partner2 callout is invoked. This results in the invocation
of the reference, and whatever the reference is wired to. For example,
the sending of a SOAP message from a web services import.
3. Because this is the end of the wiring path, the thread tracks
back up the wire to the MessageFilter1 primitive.
4. There are no more output terminals to fire. Therefore, MessageFilter1
has completed and the thread tracks the wire back out of the input
terminal to the previous mediation primitive, which in this case is
the Input node.
5. At this point, thread one has completed.

1. The input terminal of XSLT1 is reached, and the transformation
occurs.
2. The output terminal of XSLT1 is fired.
3. The Partner callout is invoked. This results in the invocation
of the reference, and whatever the reference is wired to. For example,
the sending of a SOAP message from a web services import.
4. Because this is the end of the wiring path, the thread tracks
back up the wire to the ServiceInvoke1 primitive.
5. At this point, thread two has completed.