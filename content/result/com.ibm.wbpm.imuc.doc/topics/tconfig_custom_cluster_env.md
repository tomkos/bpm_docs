# Customizing Business Automation Workflow to work
with a web server

## Before you begin

- Unusual or unexpected User is not authenticated messages.
- A node goes offline and the portal becomes unavailable while other
nodes are still running.
- Inconsistent data is returned when you are using the common URL
set up by the load balancer. However, you see correct data if you
do the tasks directly on a node.
- Between tasks, users are asked to log in again before the session
times out.

- The commands must be run on the deployment manager node.
- If the deployment manager is stopped, use the wsadmin
-conntype none option to run the commands in disconnected
mode.
- If the deployment manager is running, you must connect with a
user ID that has WebSphere Application Server configurator privileges.
Do not use the wsadmin -conntype none option.

Start the wsadmin scripting client from the deployment\_manager\_profile/bin directory.
The setBPMVirtualHost and setBPMDefaultVirtualHost commands
do not write to a log file, but the wsadmin scripting client always
writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

Make
sure that the Workflow Server or Workflow Center has
been installed and configured, and that you have configured the deployment
environment. You cannot start the cluster until you have completed
the procedures in this topic.

## About this task

If you use a web server as an entry point into your network,
you must configure virtual host information about the web server so
that Business Automation Workflow generates
URLs that are based on the host name of the web server.

## Procedure

The following procedure describes the steps to follow
for a simple configuration. For an advanced configuration, refer to
the topic "Configuring Business Automation Workflow endpoints
to match your topology."

1. Stop the deployment manager.
2. Start the wsadmin scripting client from the deployment
manager profile /bin directory: wsadmin -conntype none -lang jython
3. Create the virtual host object for your web server: 
webserver\_vh = AdminTask.setBPMVirtualHost( [ '-de', 'De1', '-name', 'webserver\_vh', '-transportProtocol', 'https', '-hostname', 'webserver.example.com' ] )Note: If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.
4. Point to the newly created Business Automation Workflow virtual
host from the EXTERNAL\_CLIENT endpoint scenario: AdminTask.setBPMEndpoint( [ '-de', 'De1', '-scenario', 'EXTERNAL\_CLIENT', '-virtualHost', 'webserver\_vh' ] )Note: If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.
5. Save your changes: AdminConfig.save()
6. Restart the deployment manager.
7 Map each application's web modules to your web server. This is in addition to the cluster mapping that is done whenthe deployment environment is created. For more details, see Mapping modules to servers . Note:
    - Existing applications are mapped to the web server by default
when it is created if Application mapping to the web server is
set to ALL. If the default cluster mappings
are removed, the application does not function properly.
    - The ICMBPMServices application is not mapped to the web server
by default, you must map this application to the web server manually.
For more information, see Mapping modules to servers.
    - When web module mappings are changed, you must regenerate the web server plug-in and propagate
it to the web server. For more information, see Plug-ins configuration.

## Related information

- WebSphere Application Server syncNode command
- Stopping and restarting a cluster member
- Changing IBM Business Automation Workflow passwords
- Configuring the web server plug-in for Secure Sockets Layer
- Securing communications
- Selecting a web server topology diagram and roadmap
- Setting up a remote web server
- setBPMVirtualHost command
- setBPMDefaultVirtualHost command
- setBPMEndpoint command