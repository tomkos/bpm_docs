# Setting up optional scenarios for endpoint configuration for
complex topologies

## Procedure

To configure optional scenarios, complete the following
actions:

1. Optional: Test Business Automation Workflow clients,
generated links, and functionality that you suspect might not work
correctly with the default scenario settings in your topology.
2. For each deployment environment, use Optional scenario keys to identify
any scenarios for types of generated URLs that cannot be handled correctly
by the default scenarios. Focus on any clients or types of links that
do not work correctly. For each scenario key, decide whether
the scenario will use a fixed URL, a fixed virtual host object, or
a list of dynamic strategies to resolve the endpoint information.
3 For each optional scenario in Optional scenario keys that must beconfigured, perform the following actions (where SCENARIO\_KEY isthe Business Automation Workflow endpointscenario key):
    1. Identify the scenario by entering the following command:scenario='SCENARIO\_KEY'Remember: Replace SCENARIO\_KEY with the appropriate
scenario key value from Optional scenario keys.
    2 Create a new endpoint or modify an existing endpoint by completingone of the following actions:
        - If you decided to use a virtual host object, modify the Business Automation Workflow endpoint
for the scenario, scenario, to set the virtualHost pointer
to the new Business Automation Workflow virtual
host, default\_vh.AdminTask.setBPMEndpoint( [ '-de', deployment\_env\_name, '-scenario', scenario, '-virtualHost', 'default\_vh' ] )If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.Important: If
it is not appropriate to use the default virtual host information,
create a new one, and set the pointer to that one. For example:AdminTask.setBPMVirtualHost( ['-de', deployment\_env\_name, '-name', 'scenario\_vh', '-transportProtocol', 'https', '-hostname', 'internal.example.com', '-port', '9443' ] )
AdminTask.setBPMEndpoint( [ '-de', deployment\_env\_name, '-scenario', scenario, '-virtualHost', 'scenario\_vh' ] )If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.
        - If you decided to use a fixed URL, set the url attribute
on the Business Automation Workflow endpoint
for the scenario, scenario. For example, to set the
URL https://webserver.example.com:443, enter the
following command:AdminTask.setBPMEndpoint( [ '-de', deployment\_env\_name, '-scenario', scenario, '-url', 'https://webserver.example.com:443' ] )If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.
        - If you decided to use dynamic predefined strategies
to extract the host information, modify the Business Automation Workflow endpoint
for the scenario, scenario to set the strategies property.
For example, to set the Business Automation Workflow endpoint
to use the WebsphereProxyHeaderStrategy, XForwardedHeaderStrategy,
and HttpProtocolHostStrategy' strategies, enter the
following command:AdminTask.setBPMEndpoint( [ '-de', deployment\_env\_name, '-scenario', scenario, '-strategies', 'WebsphereProxyHeaderStrategy, XForwardedHeaderStrategy, HttpProtocolHostStrategy' ] )If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.
3. Save any changes.AdminConfig.save()

- Optional scenario keys

You can use the optional Business Automation Workflow endpoint scenario keys to configure endpoints for complex topologies.