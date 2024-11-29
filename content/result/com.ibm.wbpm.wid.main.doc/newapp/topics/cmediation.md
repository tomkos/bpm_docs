<!-- image -->

# Mediation modules

A mediation module is a WebSphere® Business
Integration project that is used for development, version management,
organizing resources, and deployment of mediation flows to the IBM® Workflow
Server.

- Transforming a message from one format to another so that the
receiving service can accept the message
- Conditionally routing a message to one or more target services
based on the contents of the message
- Augmenting a message by adding data from a data source

A mediation module provides a mediation service, which is modeled
as Service Components Architecture (SCA) components wired together
in its module assembly. This module can contain all the resources
that are used in the service, but these resources are private and
can only be used within the module. To reuse the logic in a module
from other modules, you can export the component's interfaces. For
details on components, see the related concepts listed at the end
of this topic.

- Mediation flow
- Java™

The mediation module assembly contains a diagram (referred to as
the assembly diagram) consisting of components and the wires
that connect them. You use the assembly editor to visually compose
the integrated application by using elements that you drag from the
palette or from the tree in the Business Integration view.

The implementations of components that are used in a module's assembly
reside within the module. Components belonging to other modules can
be used through imports. Components in different modules can be wired
together by publishing the services as exports that have their interfaces,
and then dragging the exports into the required assembly diagram to
create imports.

Modules can export interfaces, but they cannot share resources.
Resources that are to be shared must be stored in a library.
You can add dependent libraries, Java projects,
and Java 2 Platform Enterprise Edition projects to a module and choose
to deploy them with the module.