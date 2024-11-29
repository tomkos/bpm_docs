# BPMSetILOGRulesServerProperties command

The BPMSetILOGRulesServerProperties command
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
BPMSetILOGRulesServerProperties
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
-serverName server\_name
[-hostname hostname]
[-port port\_number]
```

## Parameters

## Example

The following examples first show
how to set the ILOG Rules server connection variables on the ILOGRULES\_SERVER server.
These variables are in a snapshot of the CanadianFinance process application.
In the next example, the hostname is updated to toronto.
When a property value is set to null, the command does not update
the property value. The next example shows the short form of the same
example. The last example removes the hostname value. To remove a
value, use "" or do not pass a value to the property.

In the
example, the user establishes a SOAP connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSetILOGRulesServerProperties('[-containerAcronym CANADIANFINANCE -containerSnapshotAcronym V001 -serverName ILOGRULES\_SERVER 
-hostname hostname -port 1234]')

wsadmin>AdminTask.BPMSetILOGRulesServerProperties('[-containerAcronym CANADIANFINANCE -containerSnapshotAcronym V001 -serverName ILOGRULES\_SERVER 
-hostname toronto -port null]')

wsadmin>AdminTask.BPMSetILOGRulesServerProperties('[-containerAcronym CANADIANFINANCE -containerSnapshotAcronym V001 -serverName ILOGRULES\_SERVER 
-hostname toronto]')

wsadmin>AdminTask.BPMSetILOGRulesServerProperties('[-containerAcronym CANADIANFINANCE -containerSnapshotAcronym V001 -serverName ILOGRULES\_SERVER 
-hostname ""]')
```