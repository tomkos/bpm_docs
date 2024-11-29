<!-- image -->

# Concepts

IBM® Integration
Designer is
a business integration product that enables you to create integration
logic for invoking and exposing services, and to create business processes
that integrate applications and data.

A mediation flow intercepts and modifies messages that are passed between existing services
(providers) and clients (requesters) that want to use those services. Mediation flows can be
implemented in modules or mediation modules. Mediation modules can be deployed to IBM Workflow
Server. In this sample, you
use a mediation module.

A business process is a defined set of business activities that represent the steps required to
achieve a business objective. Business processes can only be implemented in standard business
integration modules and they cannot be implemented in mediation modules. For this reason, business
processes and the modules that contain them can only be deployed and run on IBM Workflow
Server. (The Hello World
Part 2 sample introduces business processes.)

Modules and mediation modules in IBM Integration
Designer are composed of
components that call each other in a loosely coupled way. This loose coupling is achieved by each
component declaring not only the interfaces by which it can be invoked, but also the interfaces of
the components it wants to call or reference. By only defining the interfaces of these required
components and not the actual components, it enables you to easily change the component used to
satisfy those references.

These components are implemented in a number of supported ways, such as with a mediation flow,
or with a business process, or with Java. Each kind of implementation has its own editor, and in
this sample you will be introduced to the mediation flow editor.

These components are defined and wired together within a module using the assembly editor.
Defining a component means supplying it with a name, and identifying its interfaces and references,
as well as its implementation type, and opening it in the appropriate editor to define its
implementation. Wiring components means connecting one component's references with other components
to satisfy its requirements.

To group together components for deployment to a particular server, you use a module. For a
client application or another module to invoke a deployed module, you use other kinds of assembly
diagram nodes called exports to export one of the components in the module so that it can be
invoked remotely. There are a number of options you can use to expose a component beyond its module
boundary. You could expose a component as a web service or by using a queuing technology such as
Java Message Service. These options are called bindings. For module-to-module communication, there
is an optimized option called an SCA binding. SCA (Service Component Architecture) is the standard
upon which this loose-coupling capability is built. You will use an SCA binding in this sample, so
that the module in the Hello World Part 2 sample can invoke the module created here in the Hello
World Part 1 sample.

Sometimes components within modules also need to invoke existing services that are external to
the module, and this is done through another kind of assembly diagram node known as an
import. An import is used to represent external services in the module so that they can
be used to satisfy component references, just like any local component. The following figure shows a
component MyService1 in the middle that has two references: one satisfied by an import of an
external service, and the other satisfied by another local component. The MyService1 component is
also exported so that other services that are external to the module can invoke the MyService1
component remotely, as shown in the following figure:

<!-- image -->

In this sample, you will use an import with a web service binding to enable the mediation flow
component to invoke an existing but external web service that is supplied for you.

All components in IBM Integration
Designer, including imports
and exports, declare interfaces so other components or clients know how to invoke them. Usually
these interfaces are defined with the Web Services Description Language (WSDL), although Java
components can also use Java interfaces. You use the interface editor to declare WSDL interfaces in
IBM Integration
Designer, and you can
also import existing WSDL files into your library and module projects. In this sample, you will
create a new interface and bring in an existing interface.

Interfaces contain one or more operations, each of which contains one or more input and output
parameters, which use standard built-in data types or user-defined data types known as business
objects. You will create a business object in this sample.