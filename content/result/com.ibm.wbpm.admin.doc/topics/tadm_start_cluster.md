# Starting and stopping a cluster

## Before you begin

- Prerequisites for starting a cluster
    - Ensure that the node agents are running.
    - Verify that all resources required by applications deployed to
the cluster are available.
    - Start all prerequisite subsystems.
- Prerequisites for stopping a cluster

- Make sure there is no work in progress; performance monitoring
infrastructure counters can indicate whether all queued work is complete.
- Prevent new work from starting by disabling HTTP and IIOP traffic
on the cluster members and quiescing the service integration buses.

## About this task

1 Infrastructure startup sequence:
    1. Database, Lightweight Directory Access Protocol (LDAP), and web
servers
    2. Deployment manager (if needed)
    3. Node agents
2 Cluster startup sequence:

1. Messaging infrastructure cluster
2. Application deployment cluster
3. Support cluster
3 Cluster shutdown sequence:

1. Support cluster
2. Application deployment cluster
3. Messaging infrastructure cluster

To
start or stop a cluster, perform the following steps.

## Procedure

1. From the administrative console of the deployment manager,
click Servers > Clusters > WebSphere application server clusters.
2 Select the cluster you want to start or stop, and thentake the following action. Option Description Start a cluster Click Start or Ripplestart tostart the cluster. When you request that all members of a cluster start, thecluster state changes to partially started and eachserver that is a member of that cluster launches, if it is not alreadyrunning. After all members of the cluster are running, the clusterstates changes to running . Stop a cluster Click Stop or ImmediateStop to stop the cluster.

| Option          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start a cluster | Click Start or Ripplestart to start the cluster.  If your servers are stopped, select the Start option. Start launches the server process of each member of the cluster by calling the node agent for each server to start the servers. If a call to a node agent for a server fails, the server does not start. If your servers are running, select the Ripplestart option. Ripplestart combines stopping and starting operations. It first stops and then restarts each member of the cluster in sequence, and ensures that at least one server in the cluster is online to handle requests. For example, imagine that your cluster contains three cluster members: server\_1, server\_2, and server\_3. When you click Ripplestart, server\_1 stops and restarts, then server\_2 stops and restarts, and finally server\_3 stops and restarts.Attention: Do not perform a ripplestart on multiple clusters simultaneously. If you plan on using Ripplestart to start clusters, do so on one cluster at a time.   When you request that all members of a cluster start, the cluster state changes to partially started and each server that is a member of that cluster launches, if it is not already running. After all members of the cluster are running, the cluster states changes to running. |
| Stop a cluster  | Click Stop or Immediate Stop to stop the cluster. Stop halts each server in such a way that the server can finish work in progress. This option allows failover to another cluster member.  Immediate Stop halts each server quickly, ignoring any current or waiting tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |