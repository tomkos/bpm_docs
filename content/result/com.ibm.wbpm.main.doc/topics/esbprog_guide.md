<!-- image -->

# Enterprise Service Bus programming

- Introduction

This development guide is for enterprise architects, integration architects and developers who are responsible for implementing integration and connectivity solutions. It begins with the high-level concepts and abilities that will help you to understand the capabilities and usage patterns of an Enterprise Service Bus (ESB). The development guide then describes how to implement the capabilities and patterns.
- Common Usage Patterns

There are seven common usage patterns that help to speed up the process of implementing connectivity and integration solutions. The patterns summarize some of the more common solutions in the connectivity space. These patterns are common usage scenarios that all Enterprise Service Bus (ESB) technologies should support.
- Service Component Architecture

Service Component Architecture (SCA) is a model to define and implement SOA based solutions. This section details the IBM implementation of SOA within an Advanced deployment environment, and its associated tooling, Integration Designer.
- Imports and exports

The components used for Service Component Architecture (SCA) module to module and SCA module to external service invocation are called imports and exports. Imports and exports are represented from the point of view of the module.
- JMS binding

A Java Message Service (JMS) provider, enables messaging based on the Java Messaging Service API and programming model. Use protocol-specific bindings with imports and exports to specify the means of transporting the data into or out of the module. Use the JMS import and export bindings to allow a Service Component Architecture (SCA) module to make calls to, and receive messages from external JMS systems.
- WebSphere MQ binding

The WebSphere MQ import binding allows components within your SCA module to communicate with services provided by external WebSphere MQ-based applications.
- Web service binding

A web service import binding allows you to call an external web service from your Service Component Architecture (SCA) component. A web service export binding allows you to expose your SCA component to clients, as web services.
- Mediation Flow Component

Mediation flows operate on messages that are in-flight between the service requester and service provider. Mediation primitives are the building blocks of mediation flows. You create mediation flows in mediation flow components. Mediation flow components can exist in either modules or mediation modules.
- Routing Messages Within a Mediation Flow

There are several mediation primitives that can be used for routing messages in a mediation flow.
- Data Transformation

Within a mediation module, the message is received from a service requester before it is sent to a service provider. The structure of the message from a service requester is not always the same as that of a service provider. One of the common uses of a mediation is to transform data from one format to another.
- Invocation of Services

Services can be invoked with IBM Workflow Server, so that you can create solutions that interact with other services. You can use the Callout node or the Service Invoke mediation primitive to call a service. Service invocations can be made by both request and response flows, using synchronous and asynchronous programming styles. This sections details the different ways that services invocations can be made.
- Service gateway

A service gateway is a single access point and acts as a proxy for multiple services. A service gateway enables transformations, routing, and common processing across all the services.
- Aggregation

Aggregation is a powerful and important enterprise service bus (ESB) pattern. An inbound request might map into several individual outbound requests. The responses from these requests can be used to enrich a final request to a service or can be aggregated into a single response for the original request.
- Error handling in the mediation flow component

This topic provides information on the various ways to deal with errors in the mediation flow, including ways to use the Stop and Fail mediation primitives, where to look for fail information in the message, and how to handle modelled and unmodeled faults.
- Testing and Debugging

This topic provides information on tools in Integration Designer. The tools can be used to test modules and components, and to debug problems.
- WebSphere eXtreme Scale

Use WebSphere® eXtreme Scale (eXtreme Scale) with IBM Business Automation Workflow to improve service response times and reliability and to provide additional integration functionality.
- Mediation flow with mediation policy

It is more cost-effective if system changes, associated with a change in the use of services by a business, can be done without changing the code or the need to redeploy the service. You can use a carefully designed mediation flow that uses mediation policy to make these changes.