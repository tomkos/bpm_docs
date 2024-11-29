# BPMShowProcessApplication command

Use the BPMShowProcessApplication command
in connected mode from either a Workflow Center server
or Workflow Server to
return detailed information about a process application, including
a list of all its snapshots.

The BPMShowProcessApplication command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment,
you must run this command on the node containing the application cluster
member that handles Workflow Server or Workflow Center applications.
Do not run this command from the deployment manager profile.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command, the ID being used
must have a WebSphere® Application
Server role
with more privileges than the monitor role. See Administrative roles for information about
roles.
- To run this command, you must have one of these permissions: read or administrative access to
the process application or toolkit, or administrative access to the Workflow Center repository.

## Location

Start the wsadmin scripting
client from the deployment\_manager\_profile/bin directory.

## Syntax

```
BPMShowProcessApplication 
-containerAcronym process\_application\_acronym
```

## Parameters

## Example

The following example illustrates
how establish a SOAP connection to the Workflow Center server
and then show the details of the BillingDispute process application.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMShowProcessApplication('[-containerAcronym BILLDISP]')
```

```
Name: Credit Card Dispute Management
Acronym: CCDMDIP
Description: Main Process Application of the Credit Card Dispute Management Application.

Contains:

- the Manage Dispute Case type
- the related Launch UI
- related Activities
Toolkit: false
Tracks:

Track Name: Main
Track Acronym: Main
Default: true

Tip:
Created On: 2014-05-13 11:21:30.289
Created By: User.1
State: State[Inactive]
Capability: Capability[Standard]
No of running instances: 0

List of Snapshots:
Name: sn\_for\_Hursley
Acronym: SFH
Created On: 2014-05-12 14:05:08.563
Created By: User.9
Is Default: false
State: State[Inactive]
Capability: Capability[Standard]
No of running instances: 0

Name: ws\_changed\_smtpServer2
Acronym: WCSS2
Created On: 2014-05-13 11:21:30.289
Created By: User.1
Is Default: false
State: State[Inactive]
Capability: Capability[Standard]
No of running instances: 0
```