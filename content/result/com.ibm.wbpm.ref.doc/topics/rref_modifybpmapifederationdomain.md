# modifyBPMApiFederationDomain command

This command adds or removes
targets from a federation domain. The Federation API is automatically
configured with your product as part of the REST Services Gateway
application. If you want to change that configuration for your environment
with multiple deployment targets, use wsadmin commands to create and
manage federation domains. Use the addTarget step
to add one or more deployment targets to a federation domain. Use
the deleteTarget step to delete one or more deployment
targets from a federation domain. The Federation API federates over
all systems on the added deployment targets.

- For Jython:AdminConfig.save()
- For Jacl:$AdminConfig save

If the
application server is not running, supply the -conntype
NONE option when running this command.

## Target object

Scope at which the federation
domain is to be administered. The target object can be used instead
of the nodeName, serverName and clusterName parameters.

## Required parameters

## Required parameters for the addTarget and deleteTarget
steps

## Examples

The following example uses the modifyBPMApiFederationDomain command
to delete the deployment target myNode, myServer and
add a new deployment target myNewNode, myNewServer.

- Jython example:AdminTask.modifyBPMApiFederationDomain('[-nodeName node\_name
-serverName server\_name -name myCustomFederationDomain
-deleteTarget [["" myNode myServer ""]]')
-addTarget [["" myNewNode myNewServer ""]]]')
- Jacl example:$AdminTask modifyBPMApiFederationDomain {-nodeName node\_name
 -serverName server\_name -name myCustomFederationDomain
 -deleteTarget {{"" myNode myServer ""}}
 -addTarget {{"" myNewNode myNewServer ""}}}