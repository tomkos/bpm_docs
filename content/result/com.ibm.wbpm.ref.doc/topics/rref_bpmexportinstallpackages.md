# BPMExportInstallPackage command

Use the BPMExportInstallPackage command to install a process application or
case solution on any workflow server.

The BPMExportInstallPackage command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must
run this command on the node containing the application cluster member
that handles Workflow Center applications.
Do not run this command from the deployment manager profile. The generated
file is saved on the machine where the connected server is running.
In order to save the generated file on another machine, establish
a remote wsadmin session from the current machine to the server on
the machine where you want to save the file.
- Note: If you are using a SOAP connection, the command can take
longer to complete than the specified SOAP timeout value. Although
the command continues to run until it is finished, you might see the
exception java.net.SocketTimeoutException: Read timed out.
To prevent this exception, set a higher value for the com.ibm.SOAP.requestTimeout
property in the profile\_root/properties/soap.client.props file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMExportInstallPackage 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-outputFile file\_path
```

## Parameters

If you are not working with a snapshot, use Tip as
the value for this parameter.

## Example

The following example illustrates
how to export a snapshot of the BillingDispute process application.
In the example, the user establishes a SOAP connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMExportInstallPackage('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -outputFile C:\processApps\BILLDISP201.zip]')
```