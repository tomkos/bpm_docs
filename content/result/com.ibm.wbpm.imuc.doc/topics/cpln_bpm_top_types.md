# Overview: Deployment environment topologies and patterns

## What is a topology?

A topology is the physical layout of the deployment environment required to meet
your business needs for capacity, availability, and scalability.

You can set up topologies for both the Workflow Center and Workflow Server components of IBM Business Automation Workflow.

Many factors affect how you design and implement your topology. For example, you must consider
business and application requirements, resource requirements and constraints, the intended purpose
of the environment, and the operating system.

- Single Cluster (the only option for a IBM Business Automation Workflow
Express environment)
- Application, Remote Messaging, and Remote Support

Each topology pattern has certain design characteristics that address a particular business need.
For example, on distributed systems, the Single Cluster topology pattern is typically used for a
testing or proof of concept scenario.

The design characteristics of each topology have been captured as topology patterns
that are supplied as configuration templates with the product.

## The purpose of deployment environment patterns

A deployment environment topology pattern specifies the constraints and requirements of the
components and resources involved in a deployment environment. There are IBM-supplied topology
pattern for each topology layout. These topology patterns provide rules and guidelines for component
interaction that are characteristic of the most commonly used Business Automation Workflow topology patterns. The IBM-supplied topology
patterns are based on well-known and tested configuration scenarios. They contain a repeatable and
automated method of creating a deployment environment. Each topology pattern is designed to meet the
configuration requirements and business needs of the associated topology. Using topology patterns
helps you create a deployment environment in the most straightforward way.

Because the deployment environment topology patterns represent recommended topologies with
component configurations that work together, you can be sure that you are building a fully
functional deployment environment. You can use the configuration rules of a deployment environment
topology pattern to generate a fast path configuration. This action is possible because many design
decisions are implemented in the topology pattern; for example, which components to configure, and
which default parameters and resources are needed.

- Understand the requirements of the business solution that you are creating.
- Review and understand the capabilities and characteristics of the IBM-supplied topology
patterns.
- Decide which topology pattern to use.

## Databases and deployment environments

- The Common database (CMNDB)
- The Process database (BPMDB)
- The Performance Data Warehouse database (PDWDB)
- The content database (CPEDB)

You or your database administrator might need to create and configure databases outside the
installer.

For more information, see Planning your database configuration.

## Functions of IBM-supplied deployment environment topology patterns

Any IBM Business Automation Workflow deployment contains a basic
set of functions that together form a complete production environment.

To design a robust deployment environment, you must understand the functionality that each
cluster can provide in an IBM-supplied topology pattern. You can allocate a specific type of
function (for example, the support infrastructure function) to a particular cluster. Understanding
the functions can help you choose the deployment environment topology pattern that best meets your
needs.

For network deployment, clusters can collaborate to provide specific functionality to the
environment. Depending on your requirements, you assign specific functions to each cluster within
the deployment environment, to provide performance, failover, and capacity.

The clusters configured in a deployment environment provide the following functions.

- If the applications contain human task or business process artifacts, install an Advanced
Workflow Server or Advanced Workflow Center, and then create an Advanced Workflow Server, Advanced Workflow Center, or AdvancedOnly Workflow Server deployment environment.

In a Single Cluster topology pattern, the application deployment target provides the entire
functionality of the deployment environment.

- Business rules
- Selectors
- Human tasks
- Business processes

The business rules are not tied to the supporting infrastructure
cluster. In fact, business rules can exist and work everywhere in the cell. The business rules
administrative function (performed from the Business Rules Manager) can be deployed on the
supporting infrastructure cluster (in a three cluster configuration). The same principle applies to
the human tasks and business processes. The human tasks and business processes run on the
application deployment target cluster, because that is where the human task and business process
containers are configured. However, you administer processes and tasks from the Business Process
Choreographer Explorer, which can reside on the supporting infrastructure cluster (in a three
cluster configuration).

For topologies in all environments, the fundamental pieces of IBM Business Automation Workflow is always similar. In all IBM Business Automation Workflow cells, the deployment manager is the central
point of administration for the cell.

## Related information

- Topologies of a network deployment environment