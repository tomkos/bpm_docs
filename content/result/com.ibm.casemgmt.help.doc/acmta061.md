# Case management configuration fails because the case management add-ons cannot be
installed

## Symptoms

```
Finished running Configure the Case Management Object Stores
An error occurred while running Configure the Case Management Object Stores
The task failed because of the following error: The case management add-ons cannot be 
installed in Content Engine. The indicated resource was not found. All prerequisites for 
add-on "5.3.2 Case Manager History and Analytics Extensions" have not been installed into 
the object store.
```

## Causes

## Resolving the problem

- Shut down all but one node and then run the Configure the Case Management Object Stores task.
After all of the case configuration tasks complete, start up the other nodes.
- Before you run the Configure the Case Management Object Stores task, change the IBM® HTTP Server (IHS) to redirect all traffic to one node instead of
evenly distributing work to all nodes. After all of the case configuration tasks complete, change
the IHS to evenly redistribute work to all nodes.

Alternatively, you can specify the Content Platform Engine
Web Services (WSI) transport URL for one node instead of the load balancer URL. However, this method
is not preferred.