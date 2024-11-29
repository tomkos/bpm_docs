# Single Cluster topology pattern

A Single Cluster topology pattern is ideal for limited hardware.
Because all the components are installed in the same cluster, fewer
physical machines are required. However, because each server instance
must run the supporting applications and your integration applications,
you need more memory for the individual Java Virtual Machines (JVMs).
In addition, one or more members of the cluster must also run the
messaging engines required for asynchronous interactions. Thus, the
Single Cluster topology pattern is typically used for proof of concept,
development, and testing environments.

- Because asynchronous interactions (involving
JMS and MQ/JMS bindings), human tasks, state machines, and long-running
business processes can make extensive use of the messaging infrastructure,
a single cluster environment is not ideal for applications with these
components.
- Any messaging requirements must be kept to a minimum with this topology pattern.
- Service Component Architecture (SCA) internal asynchronous invocations,
the Java™ Message Service (JMS),
and MQ messaging bindings do not support multiple messaging engines
in the same cluster.

The Single Cluster topology pattern is suitable for scenarios that
are focused on running applications and on synchronous invocations.

From an administrative and scalability perspective, the Single
Cluster topology pattern has advantages. A single cluster where each
member runs all the IBM Business Automation Workflow components
are simpler to administer. Instead of several server instances in
multiple clusters, you have a single cluster with fewer members. If
the needs of your environment grow, scaling the infrastructure is
a simple matter of adding additional nodes and cluster members. Thus,
the process of adding capability is simple, but all components are
scaled at the same rate. For example, if the messaging engines spread
across server members use policies, there could be some additional
administrative effort in creating and maintaining the policies.

In a Single Cluster topology pattern, all deployment environment
functions and functional groups of components run on a single cluster:

- The components:
    - IBM Content
Navigator
    - Business Process Choreographer
(BPC) container
    - Workflow Server
    - Business Rules manager
    - Business Space
    - Process Portal
    - REST API Services
- The messaging infrastructure cluster hosts a single
service integration bus and single messaging engine that use the same
database schema as the product database by default. Each deployment
environment has its own bus. The single bus is called BPM.deployment\_environment\_name.Bus.
- The support infrastructure components:

- Performance Data Warehouse
- Business Process Choreographer Explorer
- The BPMEventEmitter application for IBM Business Automation
Insights

Figure 1. Single cluster topology pattern

<!-- image -->