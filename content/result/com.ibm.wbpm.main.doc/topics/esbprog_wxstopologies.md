<!-- image -->

# WebSphere eXtreme
Scale topologies

This section describes different topologies that can be used when configuring the WebSphere eXtreme
Scale ObjectGrid with IBM® Business Automation Workflow.

The ObjectGrid is hosted by container servers that might be part of a IBM Business Automation Workflow process or as a standalone process. Each of
the WebSphere eXtreme
Scale topologies in this section
assumes a IBM Business Automation Workflow
golden topology is available. A golden topology is a topology that has a deployment
manager, application cluster, messaging cluster and an optional support cluster. The more container
servers your topology contains, the more scalable and reliable the ObjectGrid becomes. However, to
prevent impact on performance, consider the physical resources available to each container
server.

This section does not describe the different configurations available to the individual container
servers. These configurations are discussed in depth in the WebSphere eXtreme
Scale documentation. eXtreme Scale Catalog servers are responsible for managing the
data grid and directing clients to the data they require. Considerations for the catalog server are
discussed later on in this section.

## Embedded eXtreme Scale cluster

Figure 1. Embedded cluster topology

<!-- image -->

- Simplifies administration because there are fewer processes to manage
- The container servers can be managed by the deployment manager
- Supports partitioning and high availability
- Reduces the number of processes required
- Access the grid locally

- Increases the memory footprint of the eXtreme Scale client
process because data is colocated with IBM Business Automation Workflow applications.
- Increases CPU utilization for servicing client requests.
- More difficult to handle application upgrades using this topology, because eXtreme Scale clients are using the same application Java archive
files as the eXtreme Scale container servers.
- Scaling of clients and grid servers cannot increase at the same rate. When servers are
externally defined, you can have more flexibility in managing the number of processes.
- Starting and stopping application processes in response to load or service activities will force
eXtreme Scale data to be transferred between container
servers.

## Distributed eXtreme Scale cluster

This topology adds a new eXtreme Scale cluster to the
golden topology that contains servers that are used exclusively by eXtreme Scale. eXtreme Scale clients can optionally have a local, in-line cache
when eXtreme Scale is used in this topology. This
optional cache is called a near cache: an independent ObjectGrid on each client, serving as a cache
for the remote server-side cache. The near cache is enabled by default when locking is configured as
optimistic or none and cannot be used when configured
as pessimistic.

Figure 2. Distributed cluster topology

<!-- image -->

An alternative to this topology is to augment the servers in the support cluster. This is
suitable when the support cluster usage is light or the cluster is not used.

Figure 3. Distributed cluster - alternative topology

<!-- image -->

- Offers a faster response time when data is retrieved from the near cache.
- The container server can be managed using the Integrated Solutions Console.
- Container server processes are isolated from application processes. This reduces impact on
application resources, and the container servers can be started and stopped independently of the
application servers.

- Increase the likelihood of stale data because the near cache at each tier might not be
synchronized with the current data in the data grid
- Relies on additional configuration to invalidate data to help avoid running out of memory
- Increased number of processes to administer

## External eXtreme Scale cluster

Figure 4. External eXtreme Scale cluster topology

<!-- image -->

- More data can be put in the grid because the processes are separated, therefore no resource is
consumed by the application server
- Can result in reduced maintenance of container servers
- Startup time for the container servers can be faster than if you use an augmented application
server

- Not as easy to manage as a server in a network deployment environment
- Starting and stopping the servers must be performed using scripting
- No graphical user interface for administrating the container servers

## Catalog Server considerations

Hosting a catalog server in the same process as a container server will impact maintainability
and reliability. For high availability of the ObjectGrid, configure a catalog service domain. A
catalog service domain consists of multiple processes, including a master process and backup
processes.

A catalog server will not start successfully until at least one other catalog server is found. To
avoid a single point of failure for your catalog service domain start a minimum of three catalog
servers on three separate nodes. If you are using only two nodes, configure two catalog servers on
each of the nodes for a total of four catalog server processes. Using this configuration ensures
that when only one of the nodes is started, two catalog servers are running. All catalog servers
defined in a catalog service domain start automatically in a WebSphere Application
Server environment.