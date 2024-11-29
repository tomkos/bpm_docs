# Application, Messaging, and Support topology pattern

The Application, Messaging, and Support topology pattern is the preferred topology for IBM® Business Process
Manager Server.

- IBM Content
Navigator
- Business Process Choreographer
(BPC) container
- Workflow Server
- Business Rules manager
- Business Space
- Process Portal
- REST API Services

The messaging infrastructure cluster hosts a single
service integration bus and single messaging engine that use the same
database schema as the product database by default. Each deployment
environment has its own bus. The single bus is called BPM.deployment\_environment\_name.Bus.

- Performance Data Warehouse
- Business Process Choreographer Explorer
- The BPMEventEmitter application for IBM Business Automation
Insights

In a Application, Messaging, and Support topology pattern, the deployment environment functions
are divided among three separate clusters. One cluster is used for applications, one cluster is used
for messaging functionality, and one cluster for support functionality.

Figure 1. Application, Messaging, and Support pattern

<!-- image -->

## Related information

- Managing Business Performance Data Warehouses
- Business Process Choreographer Explorer overview