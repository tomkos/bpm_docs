<!-- image -->

# Creating a dynamic endpoint selection pattern

## About this task

## Procedure

1. Start the IBM Integration Designer.
2. In Integration Designer, click the Patterns Explorer tab.
A list of patterns to select from is displayed on the
left panel.
3. Select Dynamic Endpoint selection. On
the main page you can view information about the selected pattern
category.

## Example

<!-- image -->

- Configuring Dynamic Endpoint Patterns using Patterns Explorer

IBM Integration Designer provides patterns to select from while creating an  integration pattern for dynamic service routing using business rules. These business rules help determine the appropriate endpoint selection and routing. Each pattern includes a wizard that generates a rules-based endpoint selection pattern instance based on the parameters that you provide.
- Creating a rules-based dynamic endpoint selection pattern

Rules Based Endpoint Selection is an integration pattern for dynamic service routing which uses business rules to determine the appropriate endpoint selection and routing. The implementation can be done by using either WebSphere® Process Server rules or IBM® ODM rules. Rules Based Endpoint Selection routes the service requester to an appropriate service endpoint based on an in-bound message without modifying the message or the core business logic.
- Rules-based dynamic endpoint selection artifacts

This topic lists the artifacts that are created by Rules Based Dynamic Endpoint Selection in IBM Integration Designer.
- Approaches to rules-based endpoint selection

You can employ two different approaches to use business rules to perform simple endpoint selection using decision services. The decision services expose the business rules created using decision tables. Decision tables are very powerful tools to express complex rules using a set of conditions and actions and have proven to be an effective mechanism for authoring endpoint selection rules.
- Example Scenario

Intelligent Business Services pave the way for advanced integration solutions that can dynamically select and run endpoints. Dynamic endpoint selection and execution can be achieved by using the combination of a type of business rule called policy and message payload. This selection pattern solves the problem of integrating diverse back-end services, third-party systems, and older applications. The complexity of applications commonly used by the Telecom and Healthcare industry domains are good examples to illustrate this problem. This scenario demonstrates how you can solve this problem by customizing and employing the built-in dynamic endpoint selection pattern provided by IBM Integration Designer and IBM BPM Telecom Pack assets to create rules-based routing implementations.