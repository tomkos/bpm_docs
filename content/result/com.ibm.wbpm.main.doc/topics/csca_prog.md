<!-- image -->

# SCA programming model fundamentals

In SCA, every component must expose at least one interface. The assembly diagram shown in Figure 1 has three components. Each component has an interface that
is represented by the letter I. A component can also refer to other components. References
are represented by the letter R. References and interfaces are then linked in an assembly
diagram. Essentially, the integration developer resolves the references by connecting them
with the interfaces of the components that implement the required logic.

Figure 1. Assembly diagram

<!-- image -->

## Invoking SCA Components

To provide access to the services to be invoked, the SCA programming model includes a
ServiceManager class, which enables developers to look up available services by name. Here is
a typical Java™ code fragment illustrating service lookup. The
ServiceManager is used to obtain a reference to the BOFactory service, which is a system-provided
service:

```
//Get service manager singleton
ServiceManager smgr = new ServiceManager();
//Access BOFactory service
BOFactory bof =(BOFactory)
        smgr.locateService("com/ibm/websphere/bo/BOFactory");
```

Developers can use a similar mechanism to obtain references to their own services by specifying
the name of the service referenced in the locateService method. After you have obtained a
reference to a service using the ServiceManager class, you can invoke any of the available
operations on that service in a way that is independent of the invocation protocol and the type of
implementation.

- Synchronous SCA invocation: When using this invocation style, the caller waits
synchronously for the response to be returned. This style is the classic invocation mechanism.
- Asynchronous SCA invocation : This mechanism allows the caller to invoke a service withoutwaiting for the response to be produced immediately. Instead of getting the response, the callergets a ticket . The exact use of this ticket depends on the specific asynchronous invocationstyle used.
    - Asynchronous with callback SCA invocation: This invocation style delegates the
responsibility of returning the response to the callee. The caller needs to expose a special
operation (the callback operation) that the callee can invoke when the response is ready.
    - Asynchronous with deferred response SCA invocation: In this invocation style, the client
invokes a service and then continues processing until some later time when the client makes a
request to capture the response.
    - Asynchronous using one-way invocation. This applies when the operation being invoked does
not provide a return value.

## Imports

Sometimes, business logic is provided by components or functions that are available on external
systems, such as older applications, or other external implementations. In those cases, the
integration developer cannot resolve the reference by connecting a reference to a component
containing the implementation he or she needs to connect the reference to a component that points
to the external implementation. Such a component is called an import. When you define an
import, you need to specify how the external service can be accessed in terms of location and the
invocation protocol.

## Exports

Similarly, if your component has to be accessed by external applications, which is often the
case, you must make it accessible. You make it accessible by using a special component that exposes
your logic to the "outside world." Such a component is called an export. Exports can also be
invoked synchronously or asynchronously.

## Stand-alone references

In IBM® Business Automation Workflow, an SCA service module is
packaged as a Java EE EAR file that contains several other Java EE submodules. Java EE elements,
such as a WAR file, can be packaged along with the SCA module. Non-SCA artifacts such as JSPs can
also be packaged together with an SCA service module. This packaging lets them invoke SCA services
through the SCA client programming model using a special type of component called a stand-alone
reference.

The SCA programming model is strongly declarative. Integration developers can configure aspects
such as transactional behavior of invocations, propagation of security credentials, whether an
invocation should be synchronous or asynchronous in a declarative way, directly in the assembly
diagram. The SCA runtime, not the developers, is responsible for taking care of implementing the
behavior specified in these modifiers. The declarative flexibility of SCA is one of the most
powerful features of this programming model. Developers can concentrate on implementing business
logic, rather than focusing on addressing technical aspects, such as being able to accommodate
asynchronous invocation mechanisms. All these aspects are automatically taken care of by the SCA
runtime.

## Qualifiers

The qualifiers govern the interaction between a service client and a target service. Qualifiers
can be specified on service component references, interfaces, and implementations and are typically
external to an implementation.

The different categories of qualifiers include the following:

- Transaction, which specifies the way transactional contexts are handled in an SCA
invocation
- Activity session, which specifies how Activity Session contexts are propagated
- Security, which specifies the permissions
- Asynchronous reliability provides rules for asynchronous message delivery

SCA allows these quality of service (QoS) qualifiers to be applied to components declaratively
(without requiring programming or a change to the services implementation code). You can add service
qualifiers using WebSphere® Integration Developer.
Typically, you apply QoS qualifiers when you are
ready to consider solution deployment.

- Client programming model

The SCA client programming model is designed to locate a service, to create data objects, to invoke a service, and to handle exceptions that are raised by the invoked component.
- Interfaces

A service component has one or more interfaces with which it is associated. The interfaces associated with a service component advertise the business operations associated with this service.
- Developing service modules

A service component must be contained in a service module. Developing service modules to contain service components is key to providing services to other modules.
- Invocation styles

With SCA, you can invoke service components using synchronous and asynchronous programming styles. You can assemble modules into overall solutions where asynchronous channels between service components and modules can increase the overall throughput and flexibility of the system.
- Qualifiers

Qualifiers are an important part of SCA because they allow developers to place quality of service requirements on the IBM Business Automation Workflow runtime.

<!-- image -->