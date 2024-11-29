# SMO context

SMO context objects are either user-defined or system-defined.
You define the structure of user-defined context objects, and WebSphere® Integration Designer defines
the structure of system-defined context objects.

## System-defined context objects

- failInfo. The failInfo context object is used to hold exception
information.
- primitiveContext. The primitiveContext object contains information
used by specific mediation primitives.
- dynamicProperty. The dynamicProperty object contains mediation
policy information that is used to override promoted properties.

## User-defined context objects

Generally,
you define the structure of a user-defined context object in a business
object. Then you use the business object in the input node of the
request flow. User-defined context objects can be used to store properties
that mediation primitives use later in the flow.

The userContext
is slightly different to other user-defined context objects. It is
used to pass data that is not part of the message payload, between
multiple SCA components in the same module.

- correlation
- transient
- shared
- userContext

## Accessing user-defined context data

- Set a property value using a Database Lookup mediation primitive.
- Map between a context object and the message body, using a Mapping
mediation primitive.
- Create a Custom Mediation primitive to get or set a property value.

```
/context/transient/oldAddress
```

## Correlation context

The correlation context
is used when mediation primitives want to pass values from the request
flow to the response flow. You can use the correlation context to
link a specific request message with its response.

## Transient context

The transient context
is used for passing values between mediation primitives in the current
flow: either the request flow or the response flow. The transient
context cannot link requests and responses.

For example, a
Mapping mediation primitive might save an input message to the transient
context, and create an input message for a Service Invoke mediation
primitive. After the Service Invoke call, the next Mapping mediation
primitive could create another message by combining the Service Invoke
response, and the original message stored in the transient context.

## Shared context

The shared context is a storage
area you can use if you want to aggregate data: there is only one
shared context per thread, per flow. Generally, there is one thread
for the request flow and one thread for the response flow. Therefore,
the request flow has one shared context and the response flow has
another shared context. Theoretically, if you had a Service Invoke
mediation primitive between a Fan Out and a Fan In, the Service Invoke
could make an asynchronous call with callback. An asynchronous call
with callback creates a thread and a request (or response) flow. However,
the runtime environment does not allow this and forces Service Invoke
calls, inside a Fan Out and Fan In, to be asynchronous with response.
Therefore, there is no contention for the use of the shared context.

If
you use a Service Invoke mediation primitive outside of a Fan Out
and Fan In aggregation sequence, and you use an invocation style of
asynchronous with callback, then the shared context is empty after
the service invocation.

After you have defined the shared context,
you can use it to store data during aggregation operations. You need
to design the shared context business object carefully, to make sure
that  it is suitable for all aggregation scenarios within a specific
flow. The content of the shared context business object does not persist
across a request and response flow through callout invocation: the
shared context content is only available within the scope of a single
request or response flow.

- The shared context is a thread-based storage area. Generally,
one request flow has one thread, even if the path splits. Therefore,
generally, one request flow shares the same shared context.
- The content of the shared context business object does not persist
across a request and response flow, through callout invocation. Whatever
data is in the shared context of the request flow cannot be reused
during the response flow.
- The shared context can be used to aggregate data when using the
Fan Out and Fan In mediation primitives: it is not intended for general
data storage during a flow. The correlation context and transient
context are available for general data storage.
- After a Service Invoke call, the shared context is empty underthe following conditions:
    - The Service Invoke mediation primitive is configured for an asynchronous
call with callback.
    - The Service Invoke mediation primitive is used outside of a Fan
Out and Fan In aggregation sequence.

## userContext

Generally, you might use a userContext
object if you had a module that contained different types of SCA components,
and you wanted to pass data between the components.

For example,
you could populate a userContext from a Java™ component,
using the context service API. You could then access the userContext
data from a mediation flow component, using the SMO.

You can
control whether a userContext object is created by using a qualifier
on the export.

## Using user-defined contexts

There can be
multiple copies of an SMO within one mediation flow. Each instance
of an SMO has its own correlation context and transient context. Therefore,
if there are multiple copies of an SMO within one flow, there are
multiple versions of the correlation context and transient context.

However,
there is only one shared context per thread, per flow. Therefore,
you can have multiple instances of an SMO, but they can all use the
same shared context. For example, a request flow path might split
and rejoin, but the different paths would all have access to the same
shared context.

Figure 1. Mediation
flow path split

<!-- image -->

1. The FanOut1 mediation primitive splits the path. The Fan Out mediation
primitive is defined with the default mode, but the out terminal
is wired to two Mapping mediation primitives.
2. The first branch of the path goes through XSLT1 and has access
to the original SMO (SMO1) and its correlation context and transient
context. The first branch has access to the shared context. This branch
continues until the FanIn1 mediation primitive. Then the second branch
begins.
3. The second branch of the path goes through XSLT2 and has access
to a copy of the SMO (SMO2) and new correlation context and transient
context. The second branch has access to the shared context.
4. The FanIn1 mediation primitive brings the paths together. The
message it outputs is the last message received on the input terminal
(SMO2). The correlation context and transient context are associated
with the last message received: in this example, the correlation context
and transient context belonging to SMO2. The shared context is the
same as has been used throughout both branches of the path.