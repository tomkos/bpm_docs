# BPMInstall command

Use the BPMInstall command in connected mode from a Workflow Center server to install a
process application snapshot on an online workflow server.

The BPMInstall command is run using the AdminTask object of the wsadmin
scripting client.

When this command is called, unless the -skipGovernance parameter is set to
true, the governance process that is defined for the process application runs
asynchronously. Therefore, the command might successfully return before the governance process
finishes. Also, if the process application contains advanced content, advanced deployment might
complete after the command has successfully returned. Check the state of the snapshot to verify
whether it has been deployed and check the server logs for errors if the state does not change to
active.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must run this command on the node
containing the application cluster member that handles Workflow Server applications. Do not
run this command from the deployment manager profile.
- Note: If you are using a SOAP connection, the command can take longer to complete than the specified
SOAP timeout value. Although the command continues to run until it is finished, you might see the
exception java.net.SocketTimeoutException: Read timed out. To prevent this
exception, set a higher value for the com.ibm.SOAP.requestTimeout property in the
profile\_root/properties/soap.client.props file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMInstall 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-serverName server\_name
-skipGovernance true|false
-caseProjectArea input\_project\_area
```

## Parameters

## Example

The following example illustrates how to install a snapshot of the BillingDispute process
application on the online Workflow Server ProcessServer01. In
the example, the user establishes a SOAP connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMInstall('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -serverName ProcessServer01 -skipGovernance false]')
```