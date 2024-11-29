<!-- image -->

# Interfaces

An interface provides the input and output of a component.
It is created independent of the internal implementation of the component.
All components have WSDL type interfaces, but Java components can
have Java interfaces as well as WSDL interfaces.

To users of a service component, all that matters is its interface,
which dictates how to use it. The interface specifies
the operations that can be called and the data that is passed, such
as input arguments, returned values, and exceptions. An operation is
a function or query that is provided by a service component. An import
and export also have interfaces so that the published service can
be invoked.

An operation can contain inputs, outputs, and faults. Input might
be a string representing a person's name. Output might be a credit
rating associated with that string. The interface can optionally specify
any faults that the operation might throw because of an error condition
during the service call. An operation might have no inputs, outputs,
or faults if it is only being used to trigger an action.

It usually makes sense to store interfaces in a library so that
they can be shared by more than one module.

In the assembly editor, the component's interfaces are represented
by a single icon, , on the left side of the component. The following
image shows the CustomerQuery component which has one or more interfaces
defined:

When you drag an implementation onto the assembly editor's canvas
to create a new component, the interface of the implementation is
automatically added to the component. If you are doing top-down development,
you can create the component first and then add the interface to it.
See "Creating and wiring components" for instructions on how to add
interfaces to a node.

All components have WSDL type interfaces. Only Java™ components
support Java type interfaces in addition
to WSDL type interfaces. If a component, import, or export has more
than one interface, all the interfaces must be the same type. See
the related topics for links to more information about working with
Java components.

A component can be called synchronously or asynchronously (this
call is independent of whether the implementation is synchronous or
asynchronous). The interfaces on the component are defined in the
synchronous form and asynchronous support is also generated for them.
For an interface, you can specify a preferred interaction style
as synchronous or asynchronous. The asynchronous type advertises to
users of the interface that it contains at least one operation which
may take a significant time to complete. As a consequence, the calling
service should avoid keeping a transaction open while waiting for
the operation to complete and send its response. The interaction style
applies to all the operations in the interface.

Interfaces link the components in a module. The inputs and outputs
of each component, specified by the interface, determine which data
can be passed from one component to another. An interface is created
independent of the implementation of the component. An interface may
also be created for a component that has no implementation; that is,
the implementation will be done later.

Although most components would have interfaces, you can create
components that do not have any interface. For example, you can create
a component providing a timer service which starts when the system
is brought up so that nothing explicitly makes a call to it as a component.
In this case, the component only has partner references to invoke
other components but it has no interfaces.

To share the interfaces between modules, put the interfaces into
a library. Then, for both modules, add a dependency on the library
to use its resources. See related tasks for more information on dependencies.

You can apply a role-based permission qualifier on an interface
so that only authorized applications can invoke the service using
that interface. If the operations require different levels of permission
for their use, you will need to define separate interfaces to control
their access. See the related links for more details on qualifiers.