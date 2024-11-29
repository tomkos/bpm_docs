<!-- image -->

# Undeploying BPEL process and human task applications, using
the administrative console

## Before you begin

- If the application is deployed on a stand-alone server,
the server must be running and have access to the Business Process
Choreographer database.
- If the application is deployed on a cluster, the deployment
manager and at least one cluster member must be running. The cluster
member must have access to the Business Process Choreographer database.
- If the application is deployed on a managed server, the
deployment manager and the managed server must be running. The server
must have access to the Business Process Choreographer database.
- Either there are no instances of BPEL
process or human task templates present in any state, or you have
a stand-alone server that is running in development mode.
- If a process instance was migrated to a newer version of
the process but it is waiting for a service invocation to reply, the
application that contains the previous version cannot be undeployed
until the reply is received. In all other cases, instances that have
been migrated are considered to be instances of the new version, and
the application that contains the older version of the process can
be undeployed.
- Make sure that no other modules depend on
the services exported by the application that you want to undeploy.

## About this task

## Procedure

1. In the administrative console, click Applications > Application Types > WebSphere enterprise
applications.
2. Select the application that you want to undeploy and click Stop.
This step fails if any process instances or task instances
still exist in the application. You can either use the Business Process
Choreographer Explorer to delete the instances, or the -force option
of the manageTemplates.py administrative
script to stop and delete these instances before the application is
undeployed.
3. Select the application that you want to undeploy, and click Undeploy.
4. Click Save to save your changes.

## Results

The application is undeployed.