# BPMUpdateInstallationInformation command

Use the BPMUpdateInstallationInformation command
with the BPMExportInstallPackage command and the BPMInstallPackage command
to create scripts that install a snapshot onto a server.

The BPMUpdateInstallationInformation command
is run by using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must
run this command on the node that contains the application cluster
member that handles Workflow Center applications.
Do not run this command from the deployment manager profile. The generated
file is saved on the machine where the connected server is running.
To save the generated file on another machine, establish a remote
wsadmin session from the current machine to the server on the machine
where you want to save the file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMUpdateInstallationInformation 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-serverName server\_name
```

## Parameters

If you are not working
with a snapshot, use Tip as the value for this
parameter.

## Example

The following example illustrates
how to associate the installation package of a snapshot of the BillingDispute process
application with the server1 server. In the example,
the user establishes a SOAP connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMUpdateInstallationInformation('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -serverName server1]')
```