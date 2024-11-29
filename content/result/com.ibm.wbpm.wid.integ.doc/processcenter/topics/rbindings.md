<!-- image -->

# Considerations when using bindings

- Bindings with process applications and toolkits overview
- Rules to calling process applications and toolkits with different bindings
- Versioning and bindings
- Resource creation by binding

## Bindings with process applications and
toolkits overview

The available bindings to use when invoking
services are:

- SCA
- Web Service
    - SOAP/HTTP 1.2 JAX-WS
    - SOAP/HTTP 1.1 JAX-WS
    - SOAP/HTTP 1.1 JAX-RPC
    - SOAP/JMS 1.1 JAX-RPC
- EIS (Java EE connector architecture)
- Messaging

- JMS
- Generic JMS
- MQ
- MQ JMS
- HTTP
- EJB

The simplest of these to use within Process Server, because
it is a version aware binding and manages its own resource, is the
SCA binding. For example, you do not need to be concerned about issues
that you will need to know for other bindings, such as using the correct
context root for a URI in a HTTP binding,  managing a destination
queue in a message binding, or setting up security for a web service
policy binding. It is recommended that you use the SCA binding as
your default binding of choice, except when you need to use one of
the other bindings.

Some examples of when you would use a non-SCA
binding are as follows:

- You want to call an existing service which is exposed using one
of these other bindings.  For example, you may want to invoke a SAP
BAPI, a web service, or a MQ service.
- You are exposing your service or process to external clients who
do not have access to the SCA binding.
- The service you are calling may take a long time, so you need
to use a queue.

## Rules to calling process applications
and toolkits with different bindings

The following diagram
shows examples of binding calls with process applications and toolkits.
 Any cross-module calls within a process application (PA1 - PA1, PA1
- TK1, or TK1 - TK1) should be done using the Service Component Architecture
(SCA) binding.

- Process applications: PA1, PA2
- Toolkits: TK1, TK2
- Modules: M1, M2, M3, M4, M5, M6
- Export: E (not enumerated)
- Import: I (not enumerated)

<!-- image -->

You should not make the following calls:

- From a toolkit to a service in its containing process application
(TK1 - PA1)
- From a process application to a service in a toolkit of another
process application (PA1 - TK2)
- From a toolkit in one process application to a service in a toolkit
of another process application (TK1 - TK2)
- From an external application to a service in a toolkit (EIS -
TK1).

When making cross-process application calls you can use
the SCA, Messaging, HTTP or web service bindings.

When calling
an external application or an external application is invoking your
service, any of the bindings may be used.

## Versioning and bindings

Your
process or service may be designed so that it requires that only one
instance of it is ever deployed, or that co-deployment of different
versions are deployed.  You will need to consider the lifecycle of
the process or service, such as maintenance (that is, fixes) and enhancements
to the process or service as you receive new business requirements.
 Enhancements may have non-breaking changes (such as adding a new
operation) or breaking changes (such as modifying a business object).
 Depending on your service agreements, you may need to support co-deployment.

Your
process or service is versioned when you use a process application
and Process Center.  This will affect the provider of a service, in
how the end points for processes and services are managed, and this
will impact clients of the end points.  For example, let's consider
a service which uses the HTTP binding and makes the cross process
application call (PA1 - PA2) as shown in Figure 1.   The URL for the
HTTP service is formed as follows:

```
[http host address][Context root][operation specific portion of context path]
[http://myhost:9080][/ProviderWeb/ChequingImplExport][/operation1]
```

If
we add a process application and version then we have a URL as follows:

```
[http://myhost:9080][/PA2-1.0.0-ProviderWeb/ChequingImplExport][/operation1]
```

When
the default naming convention is followed then the URL will be automatically
renamed on application installation.  This ensures that all SCA intra-process
application calls will work correctly.  For inter-process application
calls, the export binding will be updated on application install,
but not the client.  After deploying the process application, you
will need to update the client bindings using the administrative console.

If the default naming convention is not followed then the
URL must be updated manually.

| Binding type                                            | Endpoint administration                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCA                                                     | Intra-process application: none Inter-process application: Need to update the client specifying the version of the provider to target                                                                                                                                                                     |
| Inter-process application or external application calls | Inter-process application or external application calls                                                                                                                                                                                                                                                   |
| Web Service                                             | SOAP/HTTP endpoint must be renamed to be unique between versions of the process application. SOAP/JMS destination queue must be renamed to be unique between versions of the process application.  Renaming can occur in the authoring environment or post installation using the administrative console. |
| HTTP                                                    | Endpoint URL must be renamed to be unique between versions of the process application.  Renaming can occur in the authoring environment or post installation from the administrative console.                                                                                                             |
| JMS                                                     | Specified JNDI resources, or Resources created on application installation with version mangle names. Need to update the client (with the JNDI name of the request destination).                                                                                                                          |
| Generic JMS                                             | Specified JNDI resources in authoring environment, or Resources created on deployment with version mangle names. Update resources in authoring environment or post installation using the administrative console.                                                                                         |
| MQ                                                      | Specified JNDI resources in authoring environment, or Resources created on deployment with version mangle names. Update resources in authoring environment or post installation using the administrative console.                                                                                         |
| MQ JMS                                                  | Specified JNDI resources in authoring environment, or Resources created on deployment with version mangle names. Update resources in authoring environment or post installation using the administrative console.                                                                                         |
| EIS                                                     | Normal administration for an external application.  Can be specified at author time or administrative console.                                                                                                                                                                                            |
| EJB                                                     | Normal administration for an application.                                                                                                                                                                                                                                                                 |

## Resource creation by binding

The
messaging and EIS bindings support two methods of specifying an endpoint:

- You can define the properties in the binding and the resource
will be created on deployment.
- You can specify the JNDI name of the resource on the server.

This applies for resources like a ConnectionFactory, ActivationSpec,
and Destination.

Other resources, such as a Java Authentication
and Authorization Service (JAAS) resource or a data source, need to
be created in the administrative console.  The name of the resource
is then specified in the binding.

When you provide connectivity
to a service using the messaging bindings, you need to be careful.

1. To support multiple clients, the provider specifies the request
destination and the client specifies the response destination.
2. For co-deployment, unique destinations are required for request
and response.
3. For Generic JMS, MQ, and MQ JMS bindings, there is actually a
level of indirection. For example, the JNDI resource in the administrative
console refers to a Queue manager and Queue defined in WebSphere MQ.
 The Queue must be unique.

EIS bindings are used to access a service in an external
application or be notified of an event in an external application.
 They are not used for inter-process application or intra-process
application calls.