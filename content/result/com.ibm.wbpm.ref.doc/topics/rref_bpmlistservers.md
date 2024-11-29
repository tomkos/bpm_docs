# BPMListServers command

Use the BPMListServers command in
connected mode from the Workflow Center server.
It has no parameters, and returns a list of Workflow Server instances.

The BPMListServers command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must run
this command on the node containing the application cluster member
that handles Workflow Server or Workflow Center applications.
Do not run this command from the deployment manager profile.
- Note: If you are using a SOAP connection, the command can take
longer to complete than the specified SOAP timeout value. Although
the command continues to run until it is finished, you might see the
exception java.net.SocketTimeoutException: Read timed out.
To prevent this exception, set a higher value for the com.ibm.SOAP.requestTimeout
property in the profile\_root/properties/soap.client.props file.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMListServers
```

## Parameters

The command has no parameters.

## Example

The following example illustrates
how to list all federated Workflow Server instances
for a workflow center. In the example, the user establishes a SOAP
connection to the Workflow Center server.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

AdminTask.BPMListServers()
```

```
Name:serverName
URL:URL
```

```
Name:TEST\_SERVER\_1
URL:corbaname:iiop:server1.mycompany.com:2816

Name:TEST\_SERVER\_2
URL:corbaname:iiop:server2.mycompany.com:2816
```