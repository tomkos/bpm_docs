# BPMInstallOfflinePackage command

Use the BPMInstallOfflinePackage command in connected mode from a workflow
server to install a snapshot from a custom installation package on the workflow server. Use the
BPMInstallPackage command to install a snapshot from a custom installation
package or a generic installation package. For information, see BPMInstallPackage command.

The BPMInstallOfflinePackage command
is run using the AdminTask object of the wsadmin scripting client.

If
the process application contains advanced content, advanced deployment
might complete after the command has successfully returned. Check
the state of the snapshot to verify whether it has been deployed and
check the server logs for errors if the state does not change to active.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must run this command on the node
containing the application cluster member that handles Workflow Server applications. Do not run this command from
the deployment manager profile.
- You must have write access to the temporary directory where the installation package is
stored.
- The installation package must already be created and extracted on the server. After this command
is complete, the installed snapshot is active.

If the process application contains advanced content,
advanced deployment may complete after the command has successfully
returned. The state of the snapshot should be checked to confirm it
has been deployed. The server logs should be checked for errors if
the state does not change to active.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMInstallOfflinePackage 
-inputFile input\_file\_path
-inactive true or false
```

## Parameters

## Example

The following example illustrates
how to install a snapshot of the BillingDispute process application.
The snapshot installation package (BillingDispute.zip) was created
and extracted on the Workflow Center server
and is being installed on the offline Workflow Server.

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMInstallOfflinePackage('[-inputFile C:/myProcessApps/BillingDispute.zip]')
```

```
wsadmin>AdminTask.BPMInstallOfflinePackage('[-inputFile C:/myProcessApps/BillingDispute.zip -inactive true]')
```