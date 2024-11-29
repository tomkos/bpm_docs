# Starting and stopping node agents

## Before you begin

Before you can start and stop a node agent, you must federate
the node into a cell.

If you used the BPMConfig command
to create your profiles and deployment environment, and you did not
specify the -federateLater option, the node has been
federated automatically.

If you used the BPMConfig command
to create your profiles and deployment environment, and you specified
the -federateLater option, you need to first run
the WebSphere addNode command before you can start
and stop any node agents.

Before you can stop a node agent,
you must stop all the servers managed by that node agent.

## About this task

Use the following steps to start, stop, or restart a node
agent.

| Action               | Perform these steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start a node agent   | From the administrative console of the deployment manager, verify that the node agent is not currently running. (Click System administration > Node agents to see its status.) Use the startNode command to start the node agent. Note: You must start the node agent from the command line of the host on which the node is configured, in the install\_root/bin directory (where install\_root is the installation location of IBM® Business Automation Workflow).  Verify that the server started successfully by checking the profile\_root/logs/server\_name/startServer.log log file for the message Server nodeagent open for e-business; process id is nnnn. |
| Stop a node agent    | From the administrative console of the deployment manager, click System administration > Node agents. Select the node agent that you want to stop, and then click Stop.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Restart a node agent | From the administrative console of the deployment manager, click System administration > Node agents. Select the node agent that you want to restart, and then click Restart. The node agent is stopped and then restarted.                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Example

- To start the node agent in the default profile, type startNode
- To list the options, type startNode -help
- To start the node agent in the Custom03 profile, type startNode
-profileName Custom03
- To start the node agent in the Custom03 profile and write trace
information to the log file called install\_root/profiles/Custom03/logs/startServer.log,
type startNode -logfile -profileName Custom03