# BPMMigrateInstances command

- SystemOut.log and other server log files.
- If the process application is exposed to the Process Admin Console, check the
Installed Apps page in the Process Application Console.

The BPMMigrateInstances command is
run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, an application cluster member runs the Workflow Server and IBM® Workflow
Center applications. Therefore, you must run
this command on the node that contains that application cluster member. Do not run the command from
the deployment manager profile.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- To access the wsadmin command, the ID being
used must have the WebSphere® Application
Server administrator
role. See Administrative roles for information about
roles.

## Location

Start the wsadmin scripting client from the install\_root/bin directory.

## Syntax

```
BPMMigrateInstances 
-containerAcronym process\_application\_acronym
-sourceContainerSnapshotName snapshot\_name | -sourceContainerSnapshotAcronym snapshot\_acronym
-targetContainerSnapshotName snapshot\_name | -targetContainerSnapshotAcronym snapshot\_acronym
[-orphanTokenPolicyFile file\_path]
[-useNetworkAvailablePolicyFile true | false]
```

## Parameters

## Example

The following example illustrates
how to establish a SOAP connection to the Workflow Center server
and then migrate process instances.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotName "V1" -targetContainerSnapshotName "V2"]’)
```

The
following example uses  -sourceContainerSnapshotAcronym and -targetContainerSnapshotAcronym.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotAcronym "V1" -targetContainerSnapshotAcronym "V2"]’)
```

The
following example uses  -sourceContainerSnapshotName and -targetContainerSnapshotAcronym.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotName "V1" -targetContainerSnapshotAcronym "V2"]’)
```

The
following example uses the orphanTokenPolicyFile parameter.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotAcronym "V1" -targetContainerSnapshotAcronym "V2" -orphanTokenPolicyFile C:\\policyFiles\optFile.xml]’)</p>)
```

The
following example uses the orphanTokenPolicyFile and -useNetworkAvailablePolicyFile parameters.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com 
-user admin ID -password administrator password -lang jython

wsadmin>AdminTask.BPMMigrateInstances(’[-containerAcronym HSS -sourceContainerSnapshotAcronym "V1" -targetContainerSnapshotAcronym "V2" -orphanTokenPolicyFile C:\\policyFiles\optFile.xml -useNetworkAvailablePolicyFile true]’)
```