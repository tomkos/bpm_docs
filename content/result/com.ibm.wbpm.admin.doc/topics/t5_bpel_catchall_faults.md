<!-- image -->

# BPEL catch-all fault handlers don't catch all runtime faults

## Reason

If a BPEL invoke activity synchronously called a one-way service (Interface is one-way, and
Preferred interaction style is synchronous), which throws an exception, the BPEL process handles
this exception. However, if the transaction boundary is immediately before the Invoke activity, the
BPEL catch-all fault handlers don't catch the runtime faults.

## Resolution

1. Log in to the WebSphere administrative console as cell administrator.
2. Go to Servers > Clusters > WebSphere application server clusters and click the cluster name of the application target cluster.
3. On the Configuration tab, in the Business Automation Workflow section, select Business Process Choreographer > Business Flow Manager.
4 Return to the Configuration tab and, in the Additional Propertiessection, select Custom properties , click New , andenter the following information:
    - Name: Engine.alwaysUseFaulthandlersOnSyncInvokes
    - Value: true
5. Press Apply and click Save.
6. Synchronize the change to all nodes.
7. Restart the application target cluster.