# BPMListProcessApplications command

Use the BPMListProcessApplications command
in connected mode from either Workflow Center server
or Workflow Server to
return a list of all process applications and toolkits on that server.
The output from this command is useful when scripting with other process
application wsadmin commands.

The BPMListProcessApplications command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must
run this command on the node containing the application cluster member
that handles Workflow Server or Workflow Center applications.
Do not run this command from the deployment manager profile.
- The installation package must already be created and extracted
on the server. After this command is complete, the installed snapshot
is active.
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
BPMListProcessApplications
```

## Parameters

The command has no parameters.

## Example

The following example illustrates
how to list all process applications and toolkits on a server. In
the example, the user establishes a SOAP connection to the Workflow Center server.

```
wsadmin -conntype SOAP -port 8880 -host ProcessCenterServer01.mycompany.com -user admin -password admin -lang jython

wsadmin>print AdminTask.BPMListProcessApplications()
```

```
Containers:
Name:SampleProcessApp
Acronym:PA1
Description:My sample application
Toolkit:false

Name:SampleToolkit
Acronym:TKDEMO
Description:My sample toolkit
Toolkit:true
```