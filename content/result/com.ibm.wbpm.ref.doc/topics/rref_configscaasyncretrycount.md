# configSCAAsyncRetryCount command

The configSCAAsyncRetryCount command
sets asynchronous retry counts for all service integration bus destinations
that are created. The command targets all SCA modules in a server
and overrides all retry settings that were created during the design
phase.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
configSCAAsyncRetryCount
-serverName server\_name
-nodeName node\_name
-clusterName cluster\_name
-retryCount value
[-applicationName name\_of\_application]
```

## Required parameters

## Optional parameters

## Examples

```
AdminTask.configSCAAsyncRetryCount('[-serverName My\_Server
 -nodeName myNode -retryCount 3]')
```