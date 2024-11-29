<!-- image -->

# Service components

A component consists of an implementation and one or more interfaces,
which defines its inputs, outputs, and faults, and also its references,
if applicable. A reference identifies the interface of another service
or component that this component requires or consumes. An interface
can be defined in a WSDL port type language or in Java™. An interface supports synchronous and
asynchronous interaction styles. A component's implementation can
be in various languages.

The recommended interface type is WSDL, which is the language used
by the provided tutorials and samples. A Java interface, however, is supported and used mostly in the
case when a stateless session EJB is imported (discussed later in Imports and exports). If you define a component and add the Java implementation later, you should
still use a WSDL interface. You cannot mix WSDL-interface-based components
with Java interface-based components.

<!-- image -->

<!-- image -->

When you are working with a component, as shown in the following
diagram, you see only the component itself. A reference to this component
from another component appears as a line to its interface. A reference
from this component would be revealed by a line from its reference
point to the interface of other component. A reference represents
a service that this component consumes. When you name a reference
and specify its interface only, you allow the component implementation
author to defer binding that reference to an actual service until
later. The ability to defer binding and reuse implementations is one
of the key reasons for using IBM® Integration
Designer's Service Component Architecture.

A component might also have properties and qualifiers. A qualifier
is a quality of service (QoS) directive on interfaces and references
for the runtime environment.

<!-- image -->

## Related concepts

- Service data objects
- Service qualifiers
- Modules
- Imports and exports
- Service implementation types