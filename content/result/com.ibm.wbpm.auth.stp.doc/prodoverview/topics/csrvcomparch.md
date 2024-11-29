<!-- image -->

# Service Component Architecture (SCA)

In this section, we examine SCA services and service data objects.

- Service components

A service component configures a service implementation. A service component is presented in a standard block diagram.
- Service data objects

Service data objects complement Service Component Architecture. Service Component Architecture defines the services as components and the connectivity between them. Service data objects define the data flowing between components.
- Service qualifiers

An application communicates its quality of service (QoS) needs to the runtime environment by specifying service qualifiers. They govern the interaction between a service client and a target service.
- Modules

A module is a unit of deployment that determines which artifacts are packaged together in an Enterprise Archive (EAR) file. Components within a module are collocated for performance, and can pass their data by reference. A module can be seen as a scoping mechanism; that is, it sets an organizational boundary for artifacts.
- Imports and exports

Imports and exports define the external interfaces or access points of a module. You can use an import to identify services outside of a module, so that they can be called from within the module. You can use an export to allow components to provide their services to external clients.
- Service implementation types

Service implementation types are the implementations of the service components.

## Related concepts

- Service-oriented architecture
- Deployment options for IBM Integration Designer
- The runtime environments for IBM Integration Designer
- Task flows

## Related reference

- Keyboard shortcuts for the workbench, Java development tools, and the Debug perspective

## Related information

- Team development in Business Automation Workflow