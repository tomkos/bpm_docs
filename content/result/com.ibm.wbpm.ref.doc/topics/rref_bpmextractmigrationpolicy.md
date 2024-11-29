# BPMExtractMigrationPolicy command

When you are installing a snapshot on an offline Process
Server, use the BPMExtractMigrationPolicy command
in connected mode from a Workflow Center server
to extract the information used to migrate instances from other snapshots
to the newly installed snapshot.

The BPMExtractMigrationPolicy command
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
To prevent this exception, set a higher value for the com.ibm.SOAP.requestTimeout property
in the profile\_root/properties/soap.client.props file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMExtractMigrationPolicy 
-containerAcronym process\_application\_acronym
-containerSourceSnapshotAcronym snapshot\_acronym
-containerTargetSnapshotAcronym snapthot\_acronym
-outputFile output\_file\_path
```

## Parameters

## Example

The following example illustrates
how to extract the migration policy information for the BillingDispute
process application.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMExtractMigrationPolicy('[-containerAcronym BILLDISP -containerSourceSnapshotAcronym SS2.0.1 -containerTargetSnapshotAcronym SS2.0.2 -outputFile C:\myProcessApps\SS2.0.1\_to\_SS2.0.2.xml]')
```