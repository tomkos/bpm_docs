# BPMImport command

Use the BPMImport command in connected mode from Workflow Center server to import a workflow project that was exported from a different Workflow Center server.

The BPMImport command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- In a network deployment environment, you must run this command
on the node containing the application cluster member that handles Workflow Center applications.
Do not run this command from the deployment manager profile. The 
input file is read from the machine on which the connected server
is running. If you want to access the file from another machine, establish
a remote wsadmin session from the current machine to the server on
the machine where the file is stored.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
BPMImport 
-inputFile input\_file\_path
```

## Parameters

## Example

The following example illustrates
how to import the BILLDISP.twx file into the Workflow Center server.
In the example, the user establishes a SOAP connection to the Workflow Center server.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>AdminTask.BPMImport('[-inputFile C:\processApps\BILLDISP.twx]')
```