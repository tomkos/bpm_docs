# BPMSetSAPServerProperties command

The BPMSetSAPServerProperties command
is run using the AdminTask object of the wsadmin scripting client.
The variables that are updated by this command must already exist.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, an application cluster member
runs the Workflow Server and Workflow Center applications.
Therefore, you must run this command on the node that contains that
application cluster member. Do not run the command from the deployment
manager profile.

## Location

Start the wsadmin scripting client from the install\_root/bin directory.

## Syntax

```
BPMSetSAPServerProperties
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
-serverName server\_name
[-systemName systemname]
[-location location]
[-client client]
[-httpPort httpport\_number]
[-httpsPort httpsport\_number]
```

## Parameters

## Example

The following examples first show
how to set the SAP server connection variables on the SAP\_SYSTEM server.
These variables are in a snapshot of the FrenchFinance process application.
In the next example, the location is updated to paris.com.
When a property value is set to null, the command does not update
the property value. The next example shows a short form of the same
example. The last example removes the location value. To remove a
value, use "" or do not pass a value to the property.

In the
example, the user establishes a SOAP connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSetSAPServerProperties('[-containerAcronym FRENCHFINANCE -containerSnapshotAcronym V001 -systemName SAP\_SYSTEM 
-location mycorp.com -client 500 -httpPort 8010 -httpsPort 8020]')

wsadmin>AdminTask.BPMSetSAPServerProperties('[-containerAcronym FRENCHFINANCE -containerSnapshotAcronym V001 -serverName SAP\_SYSTEM 
-location paris.com -client null -httpPort null -httpsPort null]')

wsadmin>AdminTask.BPMSetSAPServerProperties('[-containerAcronym FRENCHFINANCE -containerSnapshotAcronym V001 -serverName SAP\_SYSTEM 
-location paris.com]')

wsadmin>AdminTask.BPMSetSAPServerProperties('[-containerAcronym FRENCHFINANCE -containerSnapshotAcronym V001 -serverName SAP\_SYSTEM 
-location ""]')
```