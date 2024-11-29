# Planning your network deployment environment

## Before you begin

- Choose a database type
- Identify available resources
- Identify necessary security authorizations

## About this task

## Procedure

1 Identify the functional requirements of the deploymentenvironment.
    1. Identify the features or runtime capabilities of your
deployment environment. Consider
the components that the deployment environment will support, such
as the various process applications, toolkits, processes, or modules.
    2. Identify the component types that you will deploy.
Consider the component types and the interactions between
components as part of the requirements.
    3. Identify the import and export implementation types
and transports. Consider the resources needed for the
databases or Java™ Message Service
(JMS) resources and the need for business events and their transmission
mechanism.
    4. Identify any functional requirements that are not related
to applications. Consider security servers, routers,
and any other hardware or software requirements to handle business
events.
2. Identify the capacity and performance requirements for
your environment.
3. Decide on the number of physical servers
that you need for each function.
4 Identify the redundancy requirements for your environment.

1. Identify the number of servers that you need for failover.
2. Identify the number of routers that
you need. Your choice of router is influenced
by exports of deployed modules, the types of queues you define on
the service integration bus, Service Component Architecture (SCA)
exports, and the type of load balancing that you want among your clusters. IBM® provides an embedded router
used for web services exports with Service Object Access Protocol
(SOAP)/JMS transports, or JMS exports. However, if you choose not
to use this embedded router provided by IBM,
you will need to determine how to balance the load among your clusters,
based on the technology that you are using.
5 Design your deployment environment. Decide on the pattern. For IBM Business Automation Workflow , youcan select one of two established topology patterns: For more information about the patterns and the differences between them, see Topologies of a network deployment environment .

- Single Cluster
- Application, Remote Messaging, and Remote Support
6. Understand the methods available to you for configuring
your deployment environment. You can configure a standardized
network deployment environment based on a topology pattern template
included with the software, and you can implement it using the BPMConfig command
or the Deployment Environment wizard. 
You can use the Deployment Environment wizard to create
clusters with the Single Cluster and (if applicable) Application,
Remote Messaging, and Remote Support topology patterns.

- Overview: Deployment environment topologies and patterns

A network deployment environment can have many topologies, and can be created from several standard topology patterns.
- Topologies of a network deployment environment

A topology is the physical layout of the deployment environment. You can create the topology that best addresses your business needs by choosing one of the patterns provided by IBM.
- Considerations for selecting a topology

Selecting an appropriate topology for your deployment environment depends upon several factors.
- Topology patterns and supported product features

A topology is the physical layout of the deployment environment. The product features and default usage depends on your choice of topology pattern.
- Load balancing and failover with IBM HTTP Server

In a network deployment environment, you can configure a routing server, such as IBM HTTP Server, WebSphere Application Server proxy server, or others, as a proxy server for workload balancing and failover purposes. Instead of incoming HTTP requests going directly to an application server, they go to the proxy server, which then distributes the requests across multiple application servers that perform the work.
- Expanding your topology

There are three ways to expand your topology: adding members to a cluster, adding cells, or adding deployment environments.
- On-demand routing and dynamic cluster support

WebSphere Application Server Network Deployment provides extended application infrastructure virtualization capabilities that include intelligent load balancing and clustering techniques. It introduces the concepts of on-demand routing and dynamic clustering, which provide an on-demand flexible infrastructure for enterprise-scalable applications.