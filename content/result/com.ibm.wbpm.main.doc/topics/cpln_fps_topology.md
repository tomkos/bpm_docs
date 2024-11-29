# Planning the topology of your federated environment

## Terminology

The terms federated system or federated instance can refer to either an
IBM® Business Process Manager
 or a
Business Automation Workflow server that is
part of the federated environment.

## Federated environment components

Federated environments consist of the following components:

Process Federation Server
provides API access to lists of resources that are federated from Business Automation Workflow or IBM Business Process Manager
 environments, such as
the task list and launch list. The federated data repository service provides fast access to
federated resources, and relieves federated systems from expensive queries.

Workplace is
available in both traditional and container Business Automation Workflow environments, which makes
it the common work portal for different platforms. You can host Workplace on a dedicated Business Automation Workflow server, or on one of the
federated Business Automation Workflow
V23.0.1 or higher. Workplace offers a consolidated
user experience to orchestrate, prioritize, track, and complete different types of work in one
place. Unlike Process Portal, where you can work with processes only, Workplace enables you to work
with both processes and cases. You can work on tasks and participate in workflows and cases that
have a consistent look and feel to complete work. Therefore, you may want to consider stepping up
and improving the way you do your work by choosing to use Workplace instead of Process Portal. For more information
about Workplace, see
Managing work in Workplace.

In
federated systems, Process Portal provides business
users a single view of process resources across the federated environment to work on tasks and start
business processes. When users log into Process Portal on the host Business Automation Workflow system, the user profile information is saved in
the database on this system.

## Topologies for federated environments

<!-- image -->

<!-- image -->

## Characteristics of a production topology

Your production topology for Process Federation Server uses a remote
Elasticsearch or OpenSearch cluster to implement the Federated Data Respository.

- The number of cluster nodes to use depends on the number of shards and replicas that you want to
use for your federated system indexes. The general recommendation is to start with a cluster of 3
cluster nodes and to build from there.
- To support high availability, use at least two Process Federation Server nodes. However,
as the indexing of federated systems can be distributed between Process Federation Server nodes, you can
add nodes if you need more indexing power. Similarly, to dispatch saved search requests between
Process Federation Server nodes
for supporting your target number of simultaneous Process Federation Server REST API
clients, you can add nodes to have more search client processors.