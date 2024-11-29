<!-- image -->

# WebSphere
Business Integration Adapter application use within
clusters

A WebSphere Business Integration Adapter module application
configured
solely for EIS imports (outbound traffic only) can be used within
a cluster.

Although an application that has inbound or bidirectional
(which
includes EIS exports) WebSphere Business Integration Adapter traffic
cannot be used within a cluster, it can still be made available in
a network deployment by use of single remote messaging engine for
all cluster members. This allows for a single point of input entry
for the adapter, yet still allows the applications to accept the input
and run in parallel.

Note, however, that creating a single remote
messaging engine also
creates a single point of failure for incoming adapter input. This
can be counteracted by protecting the messaging engine using an external
Operating System High Availability (HA) management software package,
such as HACMP, Veritas or Microsoft Cluster
Server.