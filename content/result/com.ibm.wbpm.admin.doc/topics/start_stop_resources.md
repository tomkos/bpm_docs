# Starting and stopping your environment

Traditional: 
 Use commands or the
administrative console to stop and start your environment. You can also start or stop individual
resources in the runtime environment, including deployment managers, node agents, deployment
environments, and clusters.

- Start the deployment manager.
- Start the nodes.
- Start the deployment environment.

Reverse the order to stop the deployment
environment.

When you start your deployment environment, all
the clusters start automatically. Clusters that are not in a deployment
environment must be started manually. You can also start or stop individual
clusters if necessary.

- Starting and stopping deployment managers

 Traditional: 
 The deployment manager is a server process. You must start the deployment manager before you can use its administrative console to manage the cell. Stop the deployment manager server process when performing certain maintenance activities such as migrating to a new version of the product or uninstalling the product. You can stop the deployment manager at any time without affecting the operation of the servers in its domain.
- Starting and stopping node agents

 Traditional: 
 Node agents are administrative agents that represent a node to your system and manage the servers on that node. The node agent is a server process that must be started before you can communicate with the deployment manager or start servers on the node. If you need to stop or restart the node agent (for example, for system maintenance like changing the system clock), use the administrative console.
- Starting and stopping deployment environments

 Traditional: 
 You can start or stop deployment environments based on IBM-supplied patterns directly from the administrative console; this action stops and starts all clusters in the deployment environment.
- Starting and stopping a cluster

 Traditional: 
 You can start or stop all of the servers in a cluster (cluster members) in one action. When you start a cluster you automatically enable workload management.