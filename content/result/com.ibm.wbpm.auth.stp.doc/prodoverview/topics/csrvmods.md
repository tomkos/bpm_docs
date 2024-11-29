<!-- image -->

# Modules

A module is a composite of service components, imports, and exports.
The service components, imports, and exports are stored in the same
project and root folder, which also contain the wiring that links
the components and the bindings needed for the imports, and exports.
A module can also contain the implementations and interfaces referenced
by its components, imports and exports, or these may be placed in
other projects, such as a library project.

There are two types of modules. A module called module (sometimes
referred to as a business integration module) contains a choice of
many component types, often used to support a business process. A
module called mediation module, contains one or more mediation flow
components. It can also contain a component, and one or more Java
components that augment the mediation flow component

A module may contain one or more mediation flow components.

The first type of module is primarily designed for business processes.
A mediation module is like a gateway to existing external services,
which is common in enterprise service bus architectures. These external
services or exports are accessed in a mediation module by imports
or service providers. By decoupling client service requesters from
service providers by a mediation flow, your applications gain flexibility
and resilience, a goal of service-oriented architecture. For example,
your mediation flow can log incoming messages, route messages to a
specific service determined at run time or transform data to make
it suitable to pass to another service. These functions can be added
and changed over time without modifying the requester or provider
services.

Modules and mediation modules result in a service applications
that can be tested and deployed to the IBM® Workflow
Server.
Both types of modules support imports and exports.

Implementations, interfaces, business objects, business object
maps, roles, relationships and other artifacts often need to be shared
among modules. A library is a project used to store these shared
resources.

<!-- image -->

In the following diagram, the module contains an export, two imports
and a service component that uses them. Wiring is shown linking the
interfaces and references.

<!-- image -->

## Related concepts

- Service components
- Service data objects
- Service qualifiers
- Imports and exports
- Service implementation types