<!-- image -->

# Service implementation types

The standard implementations of the services are described in this
section. These implementations will appear in services in the assembly
editor and or within BPEL processes.

- Java objects

An implementation of a component in Java™ is referred to as a Java object. One common implementation is a component that is written in Java. This implementation is sometimes nicknamed a plain old Java object or POJO.
- BPEL process

The Business Process Execution Language (BPEL) is a standard industry language. A BPEL process component implements a business process.
- State machines

A state machine is an alternative way of creating a business process. A state machine is suited for processes related to changing states rather than a flow of control. A state defines what an artifact can do at a point in time.
- Business rules

Business rules complement business processes and state machines. If there is condition with a variable, for example, you can use a business rule to change the value in that variable at run time.
- Selectors

Integrated applications contain many ways to interact. A selector is used to route an operation from a client application to one of several possible components for implementation.
- Human tasks

A human task component implements a task done by a person. It represents the involvement of a person in a business process.
- Mediation flows

Mediation is a way of mediating or intervening dynamically between services. A mediation flow implements a mediation.
- Stand-alone references

Stand-alone references are references to applications that are not defined as Service Component Architecture (SCA) components (for example, JavaServer Pages or servlets). Stand-alone references permit these applications to interact with Service Component Architecture components.

## Related concepts

- Service components
- Service data objects
- Service qualifiers
- Modules
- Imports and exports