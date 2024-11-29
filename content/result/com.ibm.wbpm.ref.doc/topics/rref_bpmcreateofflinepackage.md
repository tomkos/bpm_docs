# BPMCreateOfflinePackage command

The BPMCreateOfflinePackage command
is run using the AdminTask object of the wsadmin scripting client.

When
this command is called, unless the -skipGovernance parameter
is set to true, the governance process that is defined
for the process application runs asynchronously. Therefore, the command
might successfully return before the governance process finishes.

## Prerequisites

- To run this command successfully, you must have Business Automation Workflow administrative
privileges. Make sure that you are a member of the default tw\_admins
group, or the group defined by the bpmAdminGroup properties if the
default group has been modified.
- If you want to install a snapshot on an offline Workflow Server, use
the BPMCreateOfflinePackage command in connected
mode from a Workflow Center server
to create an installation package of a snapshot. This package is stored
in the database. You can extract the package to a zip file with the
BPMExtractOfflinePackage command, and then install the zip file on
the offline Workflow Server with
the BPMInstallOfflinePackage command.
- In a network deployment environment, you must
run this command on the node containing the application cluster member
on the Workflow Center server.
Do not run this command from the deployment manager profile.
- Note: If you are using a SOAP connection, the command can take
longer to complete than the specified SOAP timeout value. Although
the command continues to run until it is finished, you might see the
exception java.net.SocketTimeoutException: Read timed out.
To prevent this exception, set a higher value for the com.ibm.SOAP.requestTimeout
property in the profile\_root/properties/soap.client.props
file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMCreateOfflinePackage 
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-serverName offline\_process\_server
-skipGovernance true|false
```

## Parameters

For detailed
information about the process applications in Workflow Center, use the
BPMListProcessApplications command. Use the
BPMShowProcessApplication command to know about the process application
snapshots, including acronyms.

## Example

The following example illustrates
how to establish a SOAP connection to the Workflow Center server,
and then create an installation package for the snapshot of the BillingDispute
process application.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMCreateOfflinePackage('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -serverName processServer315 -skipGovernance false]')
```