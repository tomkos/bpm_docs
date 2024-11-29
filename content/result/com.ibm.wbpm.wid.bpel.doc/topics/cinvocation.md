<!-- image -->

# Invocation scenarios for BPEL processes

- Wires for connecting an SCA client (reference) and the interface
of a component that represents a business process
- SCA qualifier settings for component references and interfaces
that determine aspects, such as interaction style, transaction behavior,
and interaction reliability

- Factors affecting BPEL process interactions

A number of factors affect the behavior of BPEL processes in the various invocation scenarios. These include the interaction style, the type of BPEL process, the operation type, and the service endpoint resolution.
- Dynamic binding between BPEL processes and services

This scenario assumes that a business process is used as a client, and the process model allows BPEL partner links to be assigned when the process runs. Dynamic service bindings allow business processes to invoke services, the addresses of which are determined at run time. This is especially useful if the service endpoint is unknown at when the process is modeled.
- Data exchange between BPEL processes and services

A Business Process Execution Language (BPEL) process can consume service component architecture (SCA) services, or it can be consumed by other SCA services. The way in which data is exchanged between the SCA service and the process depends on how the process was modeled.