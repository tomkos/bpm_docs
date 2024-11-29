# Topology patterns and supported product features

- The operating system on which you have installed IBM® Business Automation Workflow
- The primary deployment environment feature and the complimentary feature

| Topology pattern                                  |   Number of clusters | Description                                                                                                                                                                                                                                                                                                                                                                                             | Supported products and features                                                                                           |
|---------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Single Cluster                                    |                    1 | Messaging, application deployment target, and application support functions are contained in a single cluster. This topology pattern is useful for synchronous messaging, proof of concept, or application testing environments.A Single Cluster topology pattern is ideal for limited hardware. Because all of the components are installed in the same cluster, fewer physical machines are required. | Supported by the following products: IBM Business Automation Workflow Enterprise IBM Business Automation Workflow Express |
| Application, Remote Messaging, and Remote Support |                    3 | This topology pattern defines one cluster for application deployment, one remote cluster for the messaging infrastructure, and one remote cluster for supporting applications.                                                                                                                                                                                                                          | Supported by the following products: IBM Business Automation Workflow Enterprise IBM Business Automation Workflow Express |

## Configurable components
for each configuration

When you install the various configurations
of IBM Business Automation
Workflow,
certain components are visible to you during the installation and
configuration process. For network deployment, these components can
be in one cluster or in multiple clusters.

| Component                                                               | Enterprise   | Express   |
|-------------------------------------------------------------------------|--------------|-----------|
| Workflow Server                                                         | X            | X         |
| Performance Data Warehouse                                              | X            | X         |
| Common database                                                         | X            | X         |
| Service Component Architecture (SCA)                                    | X            | X         |
| Business Space                                                          | X            | X         |
| Process Portal                                                          | X            | X         |
| Business Process Choreographer                                          | X            | X         |
| Business Process Choreographer Explorer                                 | X            | X         |
| Business Automation Workflow messaging engine (service integration bus) | X            | X         |
| Case Management (additional license, optional installation)             | X            | X         |