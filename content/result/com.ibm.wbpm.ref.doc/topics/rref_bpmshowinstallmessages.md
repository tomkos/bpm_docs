# BPMShowInstallMessages command

You can use the information returned by the BPMShowInstallMessages command
to troubleshoot a failed installation and also to determine the current
step in the snapshot installation process.

The BPMShowInstallMessages command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you
must run this                             command on the node containing
the application cluster member that                             handles Workflow Server or Workflow Center applications.
Do not run this                             command from the deployment
manager profile.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command, the ID being used
must have a WebSphere® Application
Server role
with more privileges than the monitor role. See Administrative roles for information about
roles.
- To access the Business Automation Workflow API used
by this command, the ID being used must belong to either the bpmAdminGroup
or bpmAuthorGroup. The default name for the bpmAdminGroup is tw\_admins
and the default name for the bpmAuthorGroup is tw\_authors. See IBM Business Automation Workflow default group types for information about groups.Tip: By default, only the DeAdmin user has both the WebSphere Application
Server administrator
role and membership in the bpmAdminGroup.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

<!-- image -->

## Syntax

```
BPMShowInstallMessages 
-containerAcronym process\_application
-containerSnapshotAcronym snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-serverName  process\_server\_instance\_name
[-verbose true|false]
```

## Parameters

## Example

The following example illustrates
how to establish a SOAP connection to the Workflow Center server
and then show messages from the installation of the BillingDispute
process application. The snapshot is part of the Main track.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython
```

```
AdminTask.BPMShowInstallMessages('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -serverName dev]')
```

```
[x] Initiate install of snapshot SS1 to server dev as tw\_admin
    [i] Process Application uses govenance process DEFAULT
[x] Start governance process DEFAULT
[x] Assemble artifacts and send to server dev1
    [i] Use address http://localhost:9080/teamworks
[x] Workflow server dev received artifacts from Workflow Center
[x] Initiate install of snapshot SS1 as tw\_author
[*] Install the necessary library items and assets for the process application and referenced toolkits
    [*] Install Toolkit TK1, snapshot SS1

Legend: (x = Complete, * = Running, f = Failed, e = Error, w = Warning, i = Informational, r = Recovery )
```

```
wsadmin>AdminTask.BPMShowInstallMessages('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main -serverName dev -verbose true]')
```

```
[x] [1123a,server1,05/23/2014 12:24:30.112 PM EST,05/23/2014 12:24:30.390 PM EST] Initiate install of snapshot SS1 to server dev as tw\_admin
    [i] [1123a,server1,05/23/2014 12:24:30.112 PM EST] Process Application uses govenance process DEFAULT
[x] [1123a,server1,05/23/2014 12:24:30.112 PM EST,05/23/2014 12:24:30.390 PM EST] Start governance process DEFAULT
[x] [1123a,server1,05/23/2014 12:24:30.112 PM EST,05/23/2014 12:24:30.390 PM EST] Assemble artifacts and send to server dev1
    [i] [1123a,server1,05/23/2014 12:24:30.112 PM EST] Use address http://localhost:9080/teamworks
[x] [1123a,server1,05/23/2014 12:24:30.112 PM EST,05/23/2014 12:24:30.390 PM EST] Workflow server dev received artifacts from Workflow Center
[x] [1123a,server1,05/23/2014 12:24:30.112 PM EST,05/23/2014 12:24:30.390 PM EST] Initiate install of snapshot SS1 as tw\_author
[*] [1123a,server1,05/23/2014 12:24:30.112 PM EST,05/23/2014 12:24:30.390 PM EST] Install the necessary library items and assets for the process application and referenced toolkits
    [*] [1123a,server1,05/23/2014 12:24:30.112 PM EST,05/23/2014 12:24:30.390 PM EST] Install Toolkit TK1, snapshot SS1

Legend: (x = Complete, * = Running, f = Failed, e = Error, w = Warning, i = Informational, r = Recovery )
```