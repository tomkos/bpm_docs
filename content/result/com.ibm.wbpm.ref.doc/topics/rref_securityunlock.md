# BPMSecurityUnlock command

The BPMSecurityUnlock command is run
using the AdminTask object of the wsadmin scripting client.

Because
group replication occurs at the application-cluster level and application
clusters contain multiple servers, group replication starts simultaneously
on multiple servers when you start a cluster or group. IBM® Business Automation
Workflow designates
a server to synchronize the external security group using a lock mechanism.
Therefore, the cluster member that acquired the lock synchronizes
an external Lightweight Directory Access Protocol (LDAP) security
provider and an internal database. The other cluster members wait
for the lock to be released and then read the information from the
database.

If the cluster member that controls the lock stops,
leaving the lock set in the database, the other cluster members can
go into an interminable loop. If a failure is detected, unlock the
application cluster member that acquired the lock by running the BPMSecurityUnlock command.

To
ensure that you do not interrupt normal processing, you must allow
enough time for your normal server start up time. For example, if
normal server start up time is 20 minutes, wait 20 minutes before
executing the command.

## Prerequisites

## Error logs

```
CWLND0004W - The system has been waiting for the group replication lock to be released for the last 20 minutes.
Explanation: For more information, see the BPMSecurityUnlock command topic in the Information Center.
User action: To ensure that you do not interrupt normal processing, allow enough time for your server to start up normally before you unlock the application cluster member that acquired the lock by running the BPMSecurityUnlock command.
```

```
CWLND0005I - The group replication process has started.
Explanation: This message is for informational purposes only.
User action: No action is required.
```

```
CWLND0006I - The group replication process has competed.
Explanation: This message is for informational purposes only.
User action: No action is required.
```

## Parameters

None.

## Example

The following example illustrates
how to run the BPMSecurityUnlock command. In the
example, the user establishes a SOAP connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython
AdminTask.BPMSecurityUnlock()
```