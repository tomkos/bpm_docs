<!-- image -->

# Verifying that Business Process Choreographer works

## Procedure

1. Using either the administrative console or the wsadmin command,
deploy the application in install\_root/installableApps/bpcivt.ear.
Restriction: In a network deployment environment, you
can only deploy one instance of the Business Process Choreographer
installation verification application. For example, if you have two
Business Process Choreographer clusters in the same network deployment
cell, you can deploy the bpcivt.ear application only
on one of the clusters. Later, if you want to deploy it on the second
cluster, you must first undeploy it from the first cluster.

After the enterprise application is deployed, it is in
the state stopped, and any process and task templates
that it contains are in the state started. No process
or task instances can be created until the application is started.
2. Make sure that at least one member of the cluster is running.
3. Make sure that the database system, and messaging service
are running.
4. Select the application BPCIVTApp and click Start to
start the application.
5. Verify that the application works. Using a web
browser, open the following page:http://app\_server\_host:port\_no/bpcivt
Where app\_server\_host is
the network name for the host of the application server and port\_no is
the port number used by the virtual host to which you mapped the IVT
web module when installing the file bpcivt.ear.
The port number depends on your system configuration.You
should see a message indicating success.
6. Optional: Stop and remove the bpcivt application.
For more information about undeploying
BPEL process and human task applications, see Undeploying BPEL process and human task applications, using the administrative console.
7 If an error occurs, it can be caused by any of the followingsituations:
    - If Business Process Choreographer cannot access the database,
check that the database system is running, that all database clients
are correctly configured, and that the data source is defined correctly.
Make sure that the user ID and password for the data source are valid.
    - If Business Process Choreographer cannot read the input queues,
check that the messaging service is running, and make sure that the
JMS provider and JMS resources are defined correctly.
    - For further help, see Troubleshooting the Business Process Choreographer configuration.

## Results

## What to do next

- Understanding the startup behavior of Business Process Choreographer

This topic explains why Business Process Choreographer is unavailable until all enterprise applications are started.

<!-- image -->