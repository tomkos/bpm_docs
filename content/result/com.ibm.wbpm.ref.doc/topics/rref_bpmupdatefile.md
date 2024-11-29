# BPMUpdateFile command

You use the AdminTask object of the wsadmin scripting client to run the
BPMUpdateFile command.

## Prerequisites

- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- In a network deployment environment, you must run this command on the node
that contains the application cluster member that handles IBM® Workflow
Server applications. Do not run this command
from the deployment manager profile.
- Note: If you use a SOAP connection, the command can take longer to complete than the specified SOAP
timeout value. Although the command runs until it is finished, you might see the exception
java.net.SocketTimeoutException: Read timed out. To prevent this exception,
set a higher value for the com.ibm.SOAP.requestTimeout property in the
profile\_root/properties/soap.client.props file.

## Location

Start the wsadmin scripting client from the
profile\_root/bin directory. The
BPMUpdateFile command does not write to a log file, but the wsadmin scripting
client always writes a profile\_root/logs/wsadmin.traceout
log file where you will find exception stack traces and other information.

## Syntax

```
BPMUpdateFile
-containerAcronym process\_application\_acronym
[-containerTrackAcronym track\_acronym]
-fileType file\_type
-fileName file\_name
-inputFile input\_file\_path
[-fileDescription file\_description]
```

## Parameters

## Example

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer.mycompany.com -user admin -password admin
AdminTask.BPMUpdateFile( [ '-containerAcronym', 'HSB', '-containerTrackAcronym', 'Main',
'-fileType', 'Server', '-fileName', 'monitor.jar', '-inputFile', 'C:\misc\monitor\_v3.jar',
'-fileDescription', 'External implementation of the Monitor component' ] )
```