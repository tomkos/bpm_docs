# BPMSyncTeamBindings command

The BPMSyncTeamBindings command is
run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, an application cluster member
runs the Workflow Server and Workflow Center applications.
Therefore, you must run this command on the node that contains that
application cluster member. Do not run the command from the deployment
manager profile.

1. In the tree view of the WebSphere administrative console, select Servers
> All servers.
2. In the Middleware Servers pane, click the link on the name of
the middleware server. For example, SingleClusterMember1.
3. Expand Container services and click the Transaction
service link.
4. In the Total transaction lifetime timeout field,
specify a larger value.
5. Click Apply and then click the Save link
to save the changes to the master configuration.

## Location

Start the wsadmin scripting client
from the install\_root/profiles/node\_profile/bin directory.

## Syntax

```
BPMSyncTeamBindings 
-containerAcronym process\_application\_acronym
-sourceContainerSnapshotAcronym snapshot\_acronym
-targetContainerSnapshotAcronym snapshot\_acronym
```

## Parameters

## Example

The following example illustrates
how to establish a SOAP connection to the Workflow Center server
and then copy teams from one snapshot to another.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMSyncTeamBindings(’[-containerAcronym HSS -sourceContainerSnapshotAcronym "V1" -targetContainerSnapshotAcronym "V2"]’)
```