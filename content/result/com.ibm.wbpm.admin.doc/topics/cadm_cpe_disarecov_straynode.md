# Stray nodes

When you implement disaster-recovery strategy, IBM Business Automation
Workflow cluster members are distributed across the primary
data center and the secondary data center, but only the cluster members in the primary data center
are active. The cluster members in the secondary data center are activated when a disaster occurs,
and the primary data center becomes invalid. The data in the database is replicated from the primary
data center to the secondary data center by using database technology (for example, Db2 HADR) or SAN
replication.

IBM Business Automation
Workflow integrates case capabilities into
products. If an external Content Platform Engine is designed to store document and related objects
to use the flexibility of a stray nodes disaster-recovery approach, one sample topology can use
multiple Content Platform Engine clusters that are configured with advanced storage
area.

In such a set-up (see Figure 2), IBM Business Automation
Workflow
cluster members are distributed across the primary data center and the secondary data center. The
configuration changes in the IBM Business Automation
Workflow clusters are
replicated to the secondary data center automatically through the node agent. The data changes in
the database are replicated to secondary data center by using database replication technology.

Each data center configures a Content Platform Engine cluster. The advanced storage
area is configured across the Content Platform Engine clusters in different data
centers, automatically assure the content that is replicated between the data centers. While
IBM Business Automation
Workflow persists documents to an external Content
Platform Engine, document objects are persisted into a replica of the advanced storage
area in the primary data center. The advanced storage area
automatically replicates these documents to peer replicas.

To enable Content Platform Engine clusters to service, data requests in the primary data center,
request forwarding is configured. IBM Business Automation
Workflow cluster members are located in primary data center
to communicate with the Content Platform Engine cluster in same primary data center. IBM Business Automation
Workflow cluster members that are located in secondary data
center communicate with the Content Platform Engine cluster in same secondary data center.

To access the external Content Platform Engine, map one virtual hostname to a different Content
Platform Engine node in different data centers. The virtual hostname is used during configuration
with IBM Business Automation
Workflow to access the external Content
Platform Engine.

During Content Platform Engine configuration, the servers in the Content Platform Engine clusters
are organized into different Content Platform Engine sites and the object stores are associated to
the site located in primary data center. When activating the secondary data center, the related
components must be associated to the site located in the secondary data center.

To move the related components from the Content Platform Engine site located in the primary data
center to another Content Platform Engine site located in the secondary data center, use the IBM
Administration Console for Content Platform Engine. At the same time, remove the request
forwarding configuration from the Content Platform Engine configuration, restart the
Content Platform Engine clusters that are located in secondary data center, and then start the
IBM Business Automation
Workflow cluster members that are located in the
secondary data center.

Figure 2. Stray Nodes disaster recovery

- Installation and configuration requirements for the sample topology

Consider the requirements to install and configure the sample topology.
- Failover to secondary data center

In case of a failover, you need to start the secondary data center.
- Fallback to primary data center

In case of a fallback, you need to bring back up the data center.