<!-- image -->

# Overview of developing modules

Developing modules involves ensuring that the components, staging modules, and libraries
(collections of artifacts referenced by the module) required by the application are available on the
production server.

Integration Designer is the main tool for developing
modules for deployment to IBM Business Automation Workflow. Although
you can develop modules in other environments, it is best to use Integration Designer.

IBM Business Automation Workflow supports modules for business services and mediation modules.
Both modules and mediation modules
are types of Service Component Architecture (SCA) module. A mediation module allows communication
between applications by transforming the service invocation to a format understood by the target,
passing the request to the target and returning the result to the originator. A
module for a business service implements the logic of a business process. However, a module can also
include the same mediation logic that can be packaged in a mediation module.

The following sections address how to implement and update modules for IBM Business Automation Workflow.

## Components

SCA modules contain components, which are the basic building blocks to encapsulate reusable
business logic. Components provide and consume services and are associated with interfaces,
references, and implementations. The interface defines a contract between a service component and a
calling component.

With IBM Business Automation Workflow, a module can either export
a service component for use by other modules or import a service component for use. To invoke a
service component, a calling module references the interface to the service component. The
references to the interfaces are resolved by configuring each reference from the calling module to
its interface.

1. Define or identify interfaces for the components in the module.
2. Define or manipulate business objects used by components.
3. Define or modify components through their interfaces. Note: A component is defined through its
interface.
4. Export or import service components.
5. Create an enterprise archive (EAR) file to deploy to the run time. You create the file using
either the export EAR feature in Integration Designer or the
serviceDeploy command.

## Development types

IBM Business Automation Workflow provides a component programming
model to facilitate a service-oriented programming paradigm. To use this model, a provider exports
interfaces of a service component so that a consumer can import those interfaces and use the service
component as if it were local. A developer uses either strongly-typed interfaces or
dynamically-typed interfaces to implement or invoke the service component. The interfaces and their
methods are described in the References section within this documentation.

After installing service modules to your servers, you can use the administrative console to
change the target component for a reference from an application. The new target must accept the same
business object type and perform the same operation that the reference from the application is
requesting.

## Service component development considerations

- Will this service component be exported and used by another module?If so, make sure the
interface you define for the component can be used by another module.
- Will the service component take a relatively long time to run?If so, consider implementing an
asynchronous interface to the service component.
- Is it beneficial to decentralize the service component?If so, consider having a copy of the
service component in a service module that is deployed on a cluster of servers to benefit from
parallel processing.
- Does your application require a mixture of 1-phase and 2-phase commit resources?If so, make
sure you enable last participant support for the application.
Note: If you create your
application using Integration Designer or create the
installable EAR file using the serviceDeploy command, these tools automatically
enable the support for the application. See the topic, Using one-phase and two-phase commit
resources in the same transaction in the WebSphere® Application
Server Network Deployment documentation.