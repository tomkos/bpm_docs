# Connections from Workflow Server to Workflow Center

- Behavior
- Settings
- Other sources of information

## Behavior

When Workflow Server
connects to Workflow Center,
authentication is required. The user ID and password that are used for authentication are the same
as specified for the authentication alias, this is mapped to the Business Automation Workflow Security role
ProcessCenterUser.

When Workflow Server
successfully establishes a connection to Workflow Center, it sends Workflow Center the following
information (which Workflow Center stores in the
LSW\_Server table):

- Deployed snapshots and running instances
- The user ID and password that are used for Workflow Center to establish a return
connection to Workflow Server. The user ID and password that are sent to Workflow Center are retrieved from the
authentication alias that is mapped to the Business Automation Workflow Security role
BPMAuthor.
- Host and port information, which are used when Workflow Center needs to connect for
online deployment or to display a link to the Process Admin console for the Workflow Server.

The host and port information are retrieved from the Business Automation Workflow endpoint configuration by
evaluating the following scenarios in sequence:

- HEARTBEAT\_DESIGNATED\_DEPLOYMENT\_ENDPOINT
- INTERNAL\_CLIENT

By default, there is no configuration for the HEARTBEAT\_DESIGNATED\_DEPLOYMENT\_ENDPOINT
scenario. As a result, the default settings from the INTERNAL\_CLIENT
scenario are applied. The default behavior for the INTERNAL\_CLIENT
scenario is to evaluate the following functions:

- The default virtual host (defaultVH attribute)
for the deployment environment (if configured).
- The secure web container transport of the current application
server.

In a clustered environment, the use of a web
server is recommended. For additional information, see the topic Customizing Business Automation Workflow to work with a web server.

In case your Workflow Center environment cannot connect to the web server of Workflow Server, do not set the web
server as the defaultVH attribute. Instead, only add it to the EXTERNAL\_CLIENT
scenario. Specify a virtualHost or url attribute for the
INTERNAL\_CLIENT scenario that can be contacted by clients running in the data center, such as your
Workflow Center environment.
If online deployment requires a dedicated URL that is different from what all of the other
INTERNAL\_CLIENT scenarios use, create a HEARTBEAT\_DESIGNATED\_DEPLOYMENT\_ENDPOINT scenario. For
example,

```
AdminTask.setBPMEndpoint( [ '-scenario', 'HEARTBEAT\_DESIGNATED\_DEPLOYMENT\_ENDPOINT', '-url', 'https://myHost:9443' ] )
```

For
additional information and instructions, see the topic Configuring endpoints to match your topology.

## Settings

The following table lists settings that are used in connections between Workflow Server and Workflow Center:

| Variable             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| processCenterUrl     | Workflow Server connects to a Workflow Center with this URL. This setting should always be specified.                                                                                                                                                                                                                                                                                                                                                                                      |
| interval             | Time in seconds of the health check or heartbeat that is sent fromWorkflow Server to Workflow Center. Set to 0 (zero) or -1 when offline.                                                                                                                                                                                                                                                                                                                                                  |
| ProcessCenterUser    | The authentication alias containing a user and password that are capable of being used to log in to the Workflow Center from Workflow Server. The default alias is ProcessCenterUserAlias and can be set by using wsadmin commands or the administrative console.The specified user does not need to be valid in Workflow Server but must be valid in Workflow Center. The user is valid in both Workflow Server and Workflow Center when they share the same user registry, such as LDAP. |
| ProcessCenterInstall | A group authorized to perform installations on Workflow Server. Workflow Center checks to ensure that the user is a member when attempting to install. The group should exist in the user registry. An internal group is not be specified because users can add members to internal groups. See the topic Restricting installation access to runtime servers.                                                                                                                              |

Information about security configuration properties and
roles is found in the following topics:

- Security configuration properties
- Configuration properties for the BPMConfig command
- Business Automation Workflow security roles
- Restricting installation access to runtime servers

IBM Business Automation
Workflow uses an
authentication alias that is mapped to the ProcessCenterUser role to connect
Workflow Center to Workflow Server. By default, the
authentication alias is defaulted to the DeAdmin authentication alias. To
change the authentication alias for the Workflow Center role by using the
administrative console, see Modifying authentication aliases. To change the authentication
alias for the Workflow Center
role by using the command line, see Customizing the Workflow Server settings used to connect to Workflow Center.

Typically, each Workflow Server in a runtime environment is connected to a Workflow Center; a single Workflow Center can be connected to
multiple servers. You can install process application snapshots from the Workflow Center to one or more of
these connected servers.

For additional information on modifying settings and properties for connections between Workflow Server and Workflow Center, see the following
topics:

- Customizing the Workflow Server settings used to connect to Workflow Center
- Using the administrative console to customize the Workflow Server settings used to connect to Workflow Center

## Other sources of information

Other relevant
information is found in the following topics:

- Configuring Secure Sockets Layer (SSL) communication in a network deployment environment
- Configuring endpoints to match your topology

## Related tasks

- Configuring authentication to deploy to a production environment