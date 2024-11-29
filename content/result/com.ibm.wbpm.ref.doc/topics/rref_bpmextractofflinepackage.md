# BPMExtractOfflinePackage command

If you want to install a snapshot on an offline Workflow Server, use
the BPMExtractOfflinePackage command in connected
mode from a Workflow Center server
to extract the installation package to a file. The extracted file
can then be installed on the offline Workflow Server.

The BPMExtractOfflinePackage command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must
run this command on the node containing the application cluster member
that handles Workflow Server applications.
Do not run this command from the deployment manager profile.
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
BPMExtractOfflinePackage 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-serverName server\_name
-outputFile output\_file\_path
```

## Parameters

If you are not working with a snapshot, use Tip as
the value for this parameter.

## Example

The following example illustrates
how to extract an installation package for the snapshot of the BillingDispute
process application. The package was created by using the BPMCreateOfflinePackage command
or Workflow Center.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMExtractOfflinePackage('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -serverName processServer315 -outputFile C:/myProcessApps/BILLDISP201.zip]')
```