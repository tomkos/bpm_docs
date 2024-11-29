# Managing online and offline workflow servers

As a non-admin user, you can see the list of servers, their type and status, and process application
 details if you have access to that application.
However, you can't perform the actions that an admin user can perform.

An online workflow server is actively connected to Workflow Center.
If a workflow server is set up to be online, it will connect when it starts and send notifications
of its settings and updates with data about the installed snapshots.

An offline server is configured to work with runtime workflow servers that are not connected to
Business Automation Workflow so
that you can manage offline snapshot deployment packages for a particular environment. The method
for deploying process application snapshots to an offline workflow server differs from the method
for deploying process application snapshots to an online workflow server.

On the Servers page, the Connection status column
indicates whether each server is online or offline.

Ensure you have repository administrator access to perform the following tasks.

- Monitoring installed snapshots on each workflow server from Workflow Center

You can monitor snapshots installed on workflow servers from Workflow Center. For the list of servers, each server also shows its environment type and status.
- Accessing IBM Workflow Servers from Workflow Center

You can access the Process Admin Console for workflow servers from Workflow Center. For example, you can manage caches or perform task cleanup for the workflow servers.
- Adding offline servers to Workflow Center

You can create deployment packages of a process applications snapshot to install it to workflow servers that are not connected to the Workflow Center server, but to use custom deployment packages instead of generic ones you must first add an offline server to Workflow Center.
- Removing offline servers from Workflow Center

If an offline server has been removed from your IBM® Business Automation Workflow configuration, you can remove it from Workflow Center.
- Taking workflow servers offline

If a runtime workflow server is connected to IBM Workflow Center and is currently online, you can take the server offline.
- Bringing workflow servers back online

To bring a server back online, remove the offline server from IBM Workflow Center and edit the configuration files for the workflow server.
- Server capability

The capability of the playback server and any associated workflow (production) servers must match, both for server registration purposes and for process application snapshot testing and deployment purposes.