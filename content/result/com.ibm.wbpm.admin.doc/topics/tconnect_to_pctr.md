# Using wsadmin commands to customize the Workflow Server settings
used to connect to Workflow Center

## About this task

Workflow Server initially
connects to Workflow Center
by using a connection defined in processCenterUrl. Workflow Center then tells Workflow Server which URL to connect
with depending on the endpoint resolution for the INTERNAL\_CLIENT and WS\_TO\_WC endpoint scenarios.
So you don't have multiple URLs used during each connection, set up the settings to generate the
same URLs. For more information about this connection, see Connections from IBM Process Server to Workflow Center.

Typically, each workflow server in a runtime environment is connected to a workflow center; a
single workflow center can be connected to multiple servers. You can install process application
snapshots from the workflow center to one or more of these connected workflow servers. Using wsadmin
commands, you can customize many Workflow Server
settings that are used to connect to Workflow Center, such as the following settings:

- Update the host and port name of the workflow center connection details.
- Change a workflow server from an offline server to a workflow center connected server (online
server), and vice-versa.
- Change the Workflow Center connection
URL.

## Procedure

To customize the settings that are used by a workflow server to connect to a workflow
center, complete the following steps.Note: For network deployment Workflow Server environments, complete the following steps on
the deployment manager node, synchronize the nodes, and restart the application cluster
member.

1. Stop the Workflow Server environment.
In a network deployment environment, stop the deployment manager and
the nodes.
2 Complete the following steps to update the server settingswith the WebSphere command-line administration tool (wsadmin) AdminConfigcommands.
    1. Start the wsadmin scripting tool.
To start wsadmin using the Jython language, run
the following command from the bin directory
of the Business Automation Workflow installation:
wsadmin -conntype NONE -lang jython -profileName profileName
where profileName is the name of the deployment manager profile. For IBM Business Automation Workflow
Express, profileName is the name of
the stand-alone profile (and may be omitted if this is the only profile).
    2 Get the workflow server configuration of the application cluster.
        - For a clustered environment, specify the following command
syntax:wsadmin> ps = AdminConfig.getid("/Cell:/ServerCluster:application\_cluster\_name/BPMClusterConfigExtension:/BPMProcessServer:/")
        - For a stand-alone environment, specify the following command
syntax:wsadmin> ps = AdminConfig.getid("/Cell:/Node:node\_name/Server:server\_name/BPMServerConfigExtension:/BPMProcessServer:/")
3. Update the processCenterUrl variable.
This setting specifies the URL that the workflow server uses to connect to a pre-V8.5.0.1
process center. It uses Form-based Authentication. To ensure that the workflow server can connect to
a workflow center from any release of Business Automation Workflow, this setting should
always be
specified.wsadmin> AdminConfig.modify(ps, [['processCenterUrl', 'https://new\_server\_name/ProcessCenter']])
4. To change the state of an offline workflow server to online, update the
heartBeatInterval value to a number that is greater than 0 (zero). The heartbeat
interval is the polling interval, in seconds, that is used by the workflow server to communicate its
location and characteristics to the workflow center. For example, to set the value to
60 seconds, enter the following command:

wsadmin> AdminConfig.modify(ps, [['heartBeatInterval', '60']])
To bring the server offline, disable polling by setting the heartBeatInterval
value to a number that is less than or equal to 0 (zero). For
example:wsadmin> AdminConfig.modify(ps, [['heartBeatInterval', '-1']])
5. Verify your updates. wsadmin> print AdminConfig.show(ps)The
output looks something like the following example:...
[heartBeatInterval 60]
...
[processCenterUrl https://hostname:9082/ProcessCenter]
6. Save the changes and exit.  wsadmin> AdminConfig.save()
wsadmin> exit
3. Review the Business Automation Workflow security
roles by navigating in the WebSphere Application Server administrative
console to Servers > Deployment
Environments > Deployment Environment Name > Related Items > Authentication Aliases. See Business Automation Workflow security roles.
4. Note the authentication alias for the ProcessCenterUser
and BPMAuthor roles.
5. If it does not exist, create the ProcessCenterUserAlias,
which is the default authentication alias that is used to connect
from Workflow Server to Workflow Center. It
includes a user name and password that can be used to log into Workflow Center. See Modifying authentication aliases. For ProcessCenterUserAlias,
use a valid user name and password from the Workflow Center environment.
The user will be used during the heartbeat to log into Workflow Center and
it does not need any special authorization in Workflow Center.
6. Optional: 
If you plan to use a user other than DeAdmin (the default) to deploy snapshots from Workflow Center to the runtime workflow server, create a new
BPMAuthorAlias (which is the default authentication alias that is used to connect from Workflow Center to Workflow Server). The BPMAuthorAlias receives a user name and
password from Workflow Server that is used to log
into Workflow Server.
For BPMAuthorAlias, use a valid user name and password from the Workflow Server environment that has the authority to access
and deploy snapshots to the runtime workflow server.
7. In the security roles screen, map the ProcessCenterUser
role to ProcessCenterUserAlias and the appropriate alias to the BPMAuthor
role.
8. Because Workflow Center connects to Workflow Server by HTTPS by default,
you must verify that the Workflow Server root signer SSL
certificate is imported into Workflow Center. If you configure the
processCenterUrl variable to use HTTPS, then you also must verify that the Workflow Center root signer
certificated is imported into Workflow Server. 
Follow the steps in Configuring Secure Sockets Layer (SSL) communication in a network deployment environment.Tip: If you want to connect
Workflow Center to Workflow Server by HTTP, see Re-enabling HTTP access in Business Automation Workflow temporarily .
9. Restart the deployment manager after you have completed
your updates.
10. Restart the workflow server cluster or server. For network
deployment Workflow Server environments,
synchronize the nodes and restart the application cluster member.

## Results