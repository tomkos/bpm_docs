# BPMUpdateDependency command

Use the BPMUpdateDependency command
in connected mode from Workflow Center to
update a process application or toolkit dependency on a toolkit. You
can run this command only on Workflow Center.

The BPMUpdateDependency command is
run using the AdminTask object of the wsadmin scripting
client.

## Prerequisites

- In a network deployment environment,
an application cluster member runs the  Workflow Center applications.
Therefore, you must run this command on the node that contains that
application cluster member. Do not run the command from the deployment
manager profile.
- You can run the command for only one process application or toolkit at a time.

- In
an environment with multiple security domains configured, use the
PALService MBean instead of this wsadmin command. See The Process Application LifeCycle (PAL) MBean.
- If
you are using a SOAP connection, the command can take longer to complete
than the specified SOAP timeout value. Although the command continues
to run until it is finished, you might see the exception java.net.SocketTimeoutException:
Read timed out. To prevent this exception, set a higher
value for the com.ibm.SOAP.requestTimeout property in the profile\_root/properties/soap.client.props file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMUpdateDependency
-containerAcronym process\_application\_or\_toolkit\_acronym
-containerTrackAcronym process\_application\_or\_toolkit\_track\_acronym
-toolkitAcronym toolkit\_acronym
[-toolkitTrackAcronym toolkit\_track\_acronym]
-toolkitSnapshotAcronym toolkit\_snapshot\_acronym
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMUpdateDependency("[-containerAcronym TPA -containerTrackAcronym Main -toolkitAcronym TK1 -toolkitTrackAcroynm Main -toolkitSnapshotAcronym SS1]")
```

<!-- image -->