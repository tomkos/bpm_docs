<!-- image -->

# Service Component Architecture

1. Service assembly, which details the service definitions and relationships
of the export, import, components and interfaces
2. Service implementation, which details the construction of the
service definition and the transport of information through defined
protocols (web services, JMS, MQ, adapters).

- Module

A module is a unit of deployment, where services are packaged together. Components within a module are assembled for performance, and can pass their data by reference. A module can be seen as a scoping mechanism; it sets an organizational boundary for services.
- SCA implementation in Integration Designer

You can build SCA modules within Integration Designer. Modules contain all the artifacts required to create a complete SCA application and they can be organized into projects. Additionally SCA libraries can be created in Integration Designer. You can build libraries to store artifacts, and you can share them between multiple SCA modules. Libraries are detailed later on in the chapter.
- Library

A library is a project that is used to store resources and artifacts, so that the resources or artifacts can be shared by multiple modules defined in the library. The usage of libraries is good practice where interfaces are shared across multiple mediation modules.

<!-- image -->