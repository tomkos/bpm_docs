# Changing default scenarios

## Procedure

For each deployment environment that requires changes
to the default scenarios, complete the following actions:Remember: Because the default scenario objects always exist
in each deployment environment configuration, you never need to create
them.

1. Create an Business Automation Workflow virtual
host for the deployment environment deployment\_env\_name.
AdminTask.setBPMVirtualHost(['-de', deployment\_env\_name, '-name', 'default\_vh', '-hostname', 'example.com', '-port', '9443'])If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter. Also, if you are
using the default port value for the protocol (443 for
HTTPS or 80 for HTTP), you can omit the -port parameter.
2. You can set the default virtual host for the deployment environment
to point to the new Business Automation Workflow virtual
host. This will ensure that all scenarios that use strategies to read
virtual host information, such as the strategy WCCMConfigStrategy,
will read configuration data from this object when the virtualHost attribute
for the scenario is not explicitly set. By default, the INTERNAL\_CLIENT scenario
does not have any strategies configured by default. The configuration
will default to the current HTTPS port of the application server.
Setting a default virtual host for the deployment environment overrides
this behavior and will cause INTERNAL\_CLIENT scenarios
to use URLs that point to the default virtual host of the deployment
environment. If you want to configure a default virtual host for a
deployment environment to reuse the same information in many scenarios,
and you want to continue to default to the current HTTPS port of the
application server for the INTERNAL\_CLIENT scenario,
you can add an appropriate strategy to the INTERNAL\_CLIENT scenario.
For example, the strategy CurrentJVMSecureStrategy.
AdminTask.setBPMDefaultVirtualHost( [ '-de', deployment\_env\_name, '-name', 'default\_vh' ] )If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.
3 For each default scenario that you want to modify for thedeployment environment deployment\_env\_name :
    1 Identify the scenario to modify by entering one of the followingcommands: Remember: Because the default scenarios that arelisted in Default Business Automation Workflow endpoint scenario keys are always defined, you do not needto create them.
        - scenario='EXTERNAL\_CLIENT'
        - scenario='INTERNAL\_CLIENT'
        - scenario='RELATIVE'
2 Set the scenario by performing one of the following actions:
    - If you decided to use a virtual host object, modify the Business Automation Workflow endpoint
for the scenario, scenario, to set the virtualHost pointer
to the new Business Automation Workflow virtual
host, default\_vh.AdminTask.setBPMEndpoint( [ '-de', deployment\_env\_name, '-scenario', scenario, '-virtualHost', 'default\_vh' ] )If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.Important: If
it is not appropriate to use the default virtual host information,
create a new one, and set the pointer to that one. For example:AdminTask.setBPMVirtualHost( ['-de', deployment\_env\_name, '-name', 'internal\_vh', '-transportProtocol', 'https', '-hostname', 'internal.example.com', '-port', '9443' ] )
AdminTask.setBPMEndpoint( [ '-de', deployment\_env\_name, '-scenario', scenario, '-virtualHost', 'internal\_vh' ] )If
there is only one deployment environment in the WebSphere cell, you
can omit the -de parameter.
Important: If you set values for virtualHost and url,
the url setting is used and the virtualHost setting
is ignored.
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
4. Save your changes.  AdminConfig.save()