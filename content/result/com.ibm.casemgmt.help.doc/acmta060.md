# Case configuration tool does not
create the baw and bawadmin desktops

## Symptoms

## Causes

## Resolving the problem

- Shut down all but one node and then run the Register Project Area or Register Target Environment
task. After all of the case configuration tasks complete, start up the other nodes.
- Before you run the Configure the Register Project Area or Register Target Environment task,
change the IBM® HTTP Server (IHS) to redirect all traffic to
one node instead of evenly distributing work to all nodes. After all of the case configuration tasks
complete, change the IHS to evenly redistribute work to all nodes.

Alternatively, you can specify the Content Platform Engine
Web Services (WSI) transport URL for one node instead of the load balancer URL. However, this method
is not preferred.