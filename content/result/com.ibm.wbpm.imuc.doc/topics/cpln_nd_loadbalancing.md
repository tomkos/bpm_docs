# Load balancing and failover with IBM HTTP Server

1. Install IBM HTTP Server.
2. Install and configure the appropriate web server plug-in.
3. Configure Secure Sockets Layer (SSL) between the deployment manager for WebSphere
Application Server and the IBM HTTP Server administration server.. You must configure the
Application Server to accept a self-signed certificate from IBM HTTP Server so that SSL connections
are accepted and transactions are completed.
4. Customize the Workflow Server or Workflow Center cluster so that
the configuration file points to the web server and communication
is enabled for HTTP over SSL or HTTP Secure (HTTPs). See Customizing Business Automation Workflow to work with a web server.

- Unusual or unexpected User is not authenticated messages.
- A node goes offline and the portal becomes unavailable while other nodes are still running.
- Inconsistent data is returned when you are using the common URL set up by the load balancer.
However, you see correct data if you do the tasks directly on a node.
- Between tasks, users are asked to log in again before the session times out.