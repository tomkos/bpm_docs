<!-- image -->

# Store-and-forward in a clustered environment

A service control point is the place in your scenario where the store-and-forward qualifier is
specified. This is the point in your scenario where storage is enabled. Each service control point
has a unique name which is specified by the user.

When the store-and-forward feature is enabled in a clustered environment, things that would
normally cause one service control point to start or stop causes all the service control points in
the cluster to start or stop. This includes both service runtime exceptions and the manual starting
and stopping of the store-and-forward feature by a user in business space.

The number of listeners configured in a business space influences how many failed events might
appear in the failed event manager before storing begins. This is because it takes time for the
store to activate. If multiple events fail before storing is triggered, these appear in the failed
event manager. All events received after the store is triggered are stored until the Store and
Forward widget state is changed to Forward in the business space.

The following sections describe the behavior of the store-and-forward feature in a clustered
environment under various circumstances.

## Store-and-forward feature triggered by an exception, activated for all servers in a cluster

When a service runtime exception is generated, the store-and-forward service checks the
configured policy to determine whether this exception means that the service is down. If it is
determined that the service is down, the store is started on all servers in the cluster and all new
asynchronous requests are stored before they can reach their associated imports.

Figure 1. Behavior of the servers in a cluster when the store-and-forward feature is activated

<!-- image -->

## Store-and-forward feature started in business space, activated for all servers in a cluster

When the store is started in business space for one server in a cluster, storing is activated for
all the servers in the cluster.

Figure 2. Behavior of the servers in a cluster when the store-and-forward feature is started for one
server in a business space

<!-- image -->

## Store-and-forward feature stopped in business space, stopped for all servers in a cluster

When the status is changed from store to forward in a business space for one server in a cluster,
storing is stopped for all the servers in the cluster.

Figure 3. Behavior of the servers in a cluster when the store is stopped in one server in a business
space

<!-- image -->