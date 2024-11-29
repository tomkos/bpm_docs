<!-- image -->

# Developing service modules

## Before you begin

## About this task

After analyzing your requirements, you might decide that providing and using service components
is an efficient way to process information. If you determine that reusable service components would
benefit your environment, create a service module to contain the service components.

## Procedure

1. Identify service components other modules can use.

After you have identified the service components, continue with Developing service
components.
2. Identify service components in an application that could use service components in other
service modules.

After you have identified the service components and their target components, continue with 
Invoking components or Dynamically invoking components.
3. Connect the client components with the target components through wires.

- Overview of developing modules

A module is a basic deployment unit for IBM® Business Automation Workflow applications. A module can contain components, libraries, and staging modules used by the application.
- Developing service components

Develop service components to provide reusable logic to multiple applications within your server.
- Invoking components

Components with modules can use components on any node of cluster on IBM Business Automation Workflow.
- Dynamically invoking a component

When an module invokes a component that has a Web Service Descriptor Language (WSDL) port type interface, the module must invoke the component dynamically using the invoke() method.