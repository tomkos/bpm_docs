<!-- image -->

# Mediation flows

Mediation has several useful functions. For example, you can use
mediation when you need to transform data from one service into an
acceptable format for a subsequent service. You can use logging to
log messages from a service before they are sent to the next service.
You can use routing to route data from one service into an appropriate
service determined by the mediation flow.

A mediation can also be used to map interfaces. For example, two
components can have methods that perform basically the same action
but have different names such as getCredit and getCreditRating. They can
also have different operation names and the operations can have different
parameter types. An interface map maps the operations and parameters
of these methods so that the differences are resolved and the two
components may interact. An interface map is like a bridge between
the interfaces of two components allowing them to be wired together
despite differences.

A mediation operates independently of the services that it connects.
A mediation in the assembly editor appears as a mediation flow component
between exports and imports.

In the following diagram, three service requesters or exports send
their output data to the interface of the mediation flow component.
The mediation flow component then routes the appropriate data to two
service providers or imports.

<!-- image -->

A mediation flow is a flow-like construct created with the mediation
flow editor. When you select a mediation flow component in the assembly
editor, you automatically open the mediation flow editor. In the mediation
flow editor, an operation from one service, the service requester
or export, is mapped to the operation of another service, the service
provider or import, along with functions provided by the mediation
flow editor. These functions are called mediation primitives and are wired in a mediation flow as shown in the following diagram.
You can use mediation primitives supplied by IBM, or you can create
your own custom primitives. Mediation primitives can act on both message
content and message context, where context is binding-specific information
such as Simple Object Access Protocol (SOAP) or Java Message Service
(JMS) headers, or user-defined properties.

In the diagram that follows an operation, applyforLoan, sends a
message first to a logging primitive, Log, that records the message.
Log sends the message to the Filter primitive, which, depending on
the message, routes the message to either a processBusinessLoan operation
or a processPersonalLoan operation.

<!-- image -->

Both types of modules can contain mediation flow components and
Java components that augment the mediation flow component. For more
information, see the Modules section.

## Related concepts

- Java objects
- BPEL process
- State machines
- Business rules
- Selectors
- Human tasks
- Stand-alone references