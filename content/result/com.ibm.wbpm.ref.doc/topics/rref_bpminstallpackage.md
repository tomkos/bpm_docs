# BPMInstallPackage command

Use the BPMInstallPackage command in connected mode from a workflow server to
install a snapshot installation package on the workflow server.

The BPMInstallPackage command
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
containing the application cluster member that handles workflow server applications. Do not run this
command from the deployment manager profile.
- You must have write access to the temporary directory where the installation package is
stored.
- The installation package must already be created and extracted on the server. After this command
is complete, the installed snapshot is active.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMInstallPackage
-inputFile input\_file\_path
-showSnapshotInfo true or false
-inactive true or false
-caseDosName input\_dos\_name
-caseProjectArea input\_project\_area
-caseOverwrite true or false
```

## Parameters

## Example

The following example illustrates
how to install a snapshot of the BillingDispute process application.

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMInstallPackage('[-inputFile C:/myProcessApps/BillingDispute.zip -showSnapshotInfo true]')
```

```
wsadmin>AdminTask.BPMInstallPackage('[-inputFile C:/myProcessApps/BillingDispute.zip -inactive true]')
```