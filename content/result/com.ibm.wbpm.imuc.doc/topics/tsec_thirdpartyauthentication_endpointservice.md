# Configuring Business Automation Workflow endpoints
to match your topology

## Before you begin

- The commands must be run on the deployment manager node.
- If the deployment manager is stopped, use the wsadmin
-conntype none option to run the commands in disconnected
mode.
- If the deployment manager is running, you must connect with a
user ID that has WebSphere Application Server configurator privileges.
Do not use the wsadmin -conntype none option.

Start the wsadmin scripting client from the deployment\_manager\_profile/bin directory.
The setBPMVirtualHost, setBPMDefaultVirtualHost,
 and setBPMEndpoint commands do not write to a
log file, but the wsadmin scripting client always writes a profile\_root/logs/wsadmin.traceout log
file where you will find exception stack traces and other information.

## About this task

It is important to identify the different entry points
in your network, such as load balancers and web servers, for external and internal clients. For
example, generally, the protocol, host name, and port number of the entry point server must be used
in any generated links that are served to clients. Sometimes the endpoints can be defined as a
static URL, but in more complex topologies it might be necessary to use a dynamic strategy, such as
extracting the information from the header of the request.

In simple
topologies, the defaults should work without any changes. Generally, a production environment
requires some changes to the defaults. For example, if you have a web server for
external clients, see Customizing IBM BPM to work with a
web server.

More complex topologies and ones that include multiple deployment
environments require more targeted configuration of specific objects.

For each scenario, if
the url attribute is specified, that URL is returned before any of the
strategies are attempted.

For each scenario, the strategies are attempted in the order that
they are listed until one returns the required information. Each strategy uses a different approach
to determine the transport protocol, host, and port that are used to generate URLs, for example, by
extracting them from a particular header in the request.

- The optional scenario is checked.
- The default scenario is checked.
- The default virtual host for the deployment environment is checked.
- The CurrentJVMDefaultTransportStrategy is used.

## Procedure

To configure the endpoints, complete the following actions:

1. Identify the components and structure of your topology.
 Components to consider include such things as load balancers, external
web servers, reverse proxies, firewalls, internal web servers, process
servers, and process centers.
2. Identify which default scenarios you must modify, and decide
whether to use a virtual host object, a URL, or a list of dynamic
strategies to determine the correct endpoint. See Default IBM BPM endpoint
scenario keys and Strategies for identifying
endpoint information.
3. Connect to the wsadmin client by entering the following
command: wsadmin.bat -conntype NONE -lang jythonwsadmin.sh -conntype NONE -lang jython
4. Change the default scenarios as required for each deployment
environment. See Changing
default scenarios.
5. If you have a complex topology, you might need to configure
optional scenarios for specific types of generated URLs. See Setting up optional scenarios
for complex topologies.
6. Activate the new settings by performing a ripple start
of your clusters.
7. Optional: Verify that the endpoints that you
configured are working as expected. Workflow Center environments
provide a servlet to verify the configuration of the endpoint service.
It can be accessed at the following URL: /ProcessCenterInternal/endpointUrl?specificScenario=EXPOSED\_ITEMS&defaultScenario=EXTERNAL\_CLIENT&webAppName=teamworks.war Depending
on which endpoints you configured, check that the clients that are
affected by the endpoint changes are working correctly. For example,
any changes to a scenario with a key that starts with the string PROCESS\_PORTAL can
be tested by using Process Portal from
a browser. If there are any problems, check and correct the endpoint
settings for URLs that are not working.
8. If you are using Business Space and the federated REST API, you need to ensure that you
update the URLs in the REST Services Gateway as in earlier versions of the product.

## Results

- Default Business Automation Workflow endpoint scenario keys

Configuration of endpoints for your topology might require changes to the default settings in Business Automation Workflow. For each deployment environment, use the following table to identify which of the default scenarios you must change, and whether to use a static virtual host definition, a static URL, or a list of dynamic strategies to get the host information for generated URLs.
- Strategies for identifying endpoint information

For each endpoint configuration scenario, an Business Automation Workflow endpoint defines a list of strategies. The following table describes all strategies that are available.
- Changing default scenarios

You can change the default Business Automation Workflow scenarios to configure the endpoints for your topology.
- Setting up optional scenarios for endpoint configuration for complex topologies

If you have a complex topology, you might need to configure optional scenarios for specific types of generated URLs.

## Related information

- setBPMVirtualHost command
- setBPMDefaultVirtualHost command
- setBPMEndpoint command
- getBPMEndpoint command