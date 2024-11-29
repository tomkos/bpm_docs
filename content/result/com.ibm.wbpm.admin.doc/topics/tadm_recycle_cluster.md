# Stopping and restarting a cluster member

## Before you begin

1 Prevent new work from entering the cluster member:
    - If you are using the IBM® HTTP
Server, change the plugin\_cfg.xml file to remove
the cluster member for HTTP traffic. If you are using another HTTP
server, follow the directions for your HTTP server to remove the cluster
member.
    - For IIOP traffic, set the runtime weight to zero for the cluster
member.
2. Verify that work that is destined for the cluster member is complete.
Either wait a period of time or use Performance Monitoring Infrastructure
counters to determine when the cluster completes all of the queued
work.

## About this task

To stop and restart a server by using
the administrative console, complete the following steps:

## Procedure

1. In the
administrative console, navigate to Servers > Server Types > WebSphere application
servers.
2. Select the servers or cluster members to
be stopped and click Stop.
3. Wait for the servers or cluster members
to stop.
4. Select the servers or cluster members to
be restarted and click Start.
5. Wait for the servers or cluster members
to start. Note: Alternatively, you can
stop and restart cluster members from the command line using the stopServer  and startServer commands
for your operating system or from the administrative console
cluster panel by selecting Servers >  Clusters > WebSphere application server
clusters > cluster\_name.