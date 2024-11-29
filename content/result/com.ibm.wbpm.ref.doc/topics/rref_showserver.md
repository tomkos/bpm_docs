# BPMShowServer command

Use the BPMShowServer command in connected
mode from either a Workflow Center server
or Workflow Server to
return detailed information about a server instance.

The BPMShowServer command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you
must run this command from either a Workflow Center server
or Workflow Server to
return detailed information about a server instance.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMShowServer 
-serverName server\_instance\_name
```

## Parameters

## Example

The following example illustrates
how establish a SOAP connection to the Workflow Center server
and then return detailed information about Server01.

<!-- image -->

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMShowServer('[-serverName Server01]')
```

The
output is similar to the following example.

```
Name:Server01
URL:corbaname:iiop:server1.mycompany.com:2816
Address: server1.mycompany.com
Port: 9085
Availability: true
Username: User1
```