# BPMSetEnvironmentVariable command

Traditional: 
Use the BPMSetEnvironmentVariable command to set the value of an
environment variable for a process app or toolkit.

The BPMSetEnvironmentVariable command
is run using the AdminTask object of the wsadmin scripting client.

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
BPMSetEnvironmentVariable
-containerAcronym process\_application\_acronym
-containerSnapshotAcronym process\_application\_snapshot\_acronym
[-containerTrackAcronym track\_acronym]
-environmentVariableName Name
-environmentVariableValue Value
```

## Parameters

- You can't use the BPMSetEnvironmentVariable wsadmin command to update
environment variable of a toolkit if the environment variable name is not unique in a process app
and its dependent toolkits. Instead, use update the runtime environment variable value of a toolkit
in the Process Admin Console.
- Ensure the environment variable name is a valid JavaScript identifier; it must begin with a
letter or the \_ character and can contain only letters, digits, or the \_ character.
The following examples are all valid names: ecmsystem\_port,
ecmSystem\_port, and ecm\_system\_port.

## Example

The following example illustrates
how to set the mediationServiceURL environment
variable to a snapshot of the BillingDispute process application.
The snapshot is part of the Main track. In the example, the user establishes
a SOAP connection to the Workflow Center server.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMSetEnvironmentVariable('[-containerAcronym BILLDISP -containerSnapshotAcronym SS2.0.1 -containerTrackAcronym Main 
-environmentVariableName mediationServiceURL -environmentVariableValue https://mycompany/prodServices/mediation]')
```