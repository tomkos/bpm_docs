# Error when sending event (ServiceUnavailableException)

## Cause

- The event server is not running.
- The event source application is not configured to use the correct
JNDI provider URL.

## Remedy

1. To check the status of the event server, go to the profile\_root/bin directory
and run the serverStatus command:serverStatus servername
2. If the event server is not running, use the startServer command
to start it:startServer servername
3. Check the host name and Remote Method Invocation (RMI) port for
the server containing the application that cannot connect to the event
server. Confirm that the same values are specified in the JNDI URL
configured for the event source application. If the CEI server is
located on another server, then the JNDI needs to be resolved with
that remote deployment target.