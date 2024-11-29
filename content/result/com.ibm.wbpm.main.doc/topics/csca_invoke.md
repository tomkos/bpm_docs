<!-- image -->

# Invocation styles

A component exposes business-level interfaces to its application business logic so that the
service can be used or invoked. The interface of a component defines the operations that can be
called and the data that is passed, such as input arguments, returned values, and exceptions. An
import and export also has interfaces so that the published service can be invoked.

All components have interfaces of the WSDL type. Only Java™
components support Java-type interfaces. If a component, import or export, has more than one
interface, all interfaces must be the same type.

A component can be called synchronously or asynchronously; independent of whether the
implementation is synchronous or asynchronous. The component interfaces are defined in the
synchronous form and asynchronous support is also generated for them. You can specify a preferred
interaction style as synchronous or asynchronous. The asynchronous type advertises to users of the
interface that it contains at least one operation that can take a significant amount of time to
complete. As a consequence, the calling service must avoid keeping a transaction open while waiting
for the operation to complete and send its response. The interaction style applies to all the
operations in the interface.

When authoring applications in IBM Integration Designer, it is a best to explicitly set the
invocation style that each of your components use to call each other. At a minimum, you want to know
what invocation styles are used throughout your application while you do performance analysis or
develop your error handling strategy. You certainly need to understand the interactions in your
application when you consider/set your transaction boundaries. Users are often surprised to find
that setting or determining invocation styles between components is not as easy a task as it seems.
This section explains how to set or determine which invocation style is used at run time, based on
specific characteristics of your application.

- Synchronous
- Asynchronous using one-way operation
- Asynchronous with callback
- Asynchronous with deferred response

- invoke(): Synchronous
- invokeAsync(): Asynchronous
- invokeAsyncWithCallback(): Asynchronous

In general, when considering an interaction from one component (source or client) to another
(target), the service client determines what type of invocation is used. For example, if your source
component is a Java component, the invocation style from source to target is determined by the
particular SCA invocation API you use in the implementation, such as invoke(), invokeAsync(), or
invokeAsyncWithCallback(). Each of the other components provided in Integration Designer has a set
of rules that it uses to determine whether an invocation is synchronous or asynchronous.

- Long running BPEL
- Human tasks
- MQ/MQ imports
- JMS/Generic imports
- JMS/JMS imports

- Synchronous invocation

Service component interfaces (SCA) are always defined in the synchronous form. For each synchronous interface, one or more asynchronous interfaces can be generated.
- Asynchronous invocation

IBM® Business Automation Workflow delivers a powerful programming model for developing asynchronous applications. With asynchronous invocation in SCA, there are three types of asynchronous interaction styles available: one way, deferred response, and request with callback. With all three types of asynchronous invocation, the client receives control back immediately from the SCA runtime upon an invokeAsync() call.
- Synchronous-over-asynchronous invocation

Avoid using synchronous-over-asynchronous invocation, which occurs when a component synchronously calls another component that has an asynchronous implementation.
- SCA interactions

SCA supports synchronous and asynchronous invocation of modules. Developers have the option of selecting the appropriate interfaces and invocation methods for their SCA interactions.
- Exception handling for synchronous invocation

When a service component is invoked synchronously, both the client and the service provider run in the same thread. The target can return a response message, an exception, or nothing (in a one-way operation) to the client. If the result is an exception, it can be either a business exception or a system exception. The client in this case can be either application code or some form of system code.
- Exception handling for asynchronous invocation

When a service component is invoked asynchronously, the client and service provider are run in different threads, and error conditions can occur in either thread. The client may experience a system exception during the invocation, or the service provider may experience a business or system exception while servicing the request.
- SCA data object containment and wrapper usages

The SCA execution environment requires that invocation parameters be contained within a business object wrapper as determined by the operation and the interface.
- Considerations when invoking services on different servers

One of the benefits of service-oriented architecture is the ability for consumers to use services that exist in other service modules. To balance the workload equitably, you should install applications on different servers in a cell and those applications should reside on different physical servers.