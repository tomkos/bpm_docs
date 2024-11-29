# Controlling warning limits for variable sizes of process and service flows

## Before you begin

For detailed information about resolving different kinds of memory issues for servers, see the
topic Troubleshooting JVM issues.

## About this task

In addition to warning messages, the following data is also logged to the
SystemOut.log file for the variables of process and service flows:

- For process flows:
    - The specified warning limit
    - The actual variable size
    - The process activity
    - The process instance
- For service flows:

- The specified warning limit
- The actual variable size
- The step name
- The service name

- twobject-array-length-warning-limitSpecifies a warning limit for an array of variables or an
array of properties in a complex BO. The warning limit check is performed whenever a new element is
added to an array. The default warning limit is 10000. To ignore any
specified limit wherever it is found, you can specify -1.
- saved-symbol-table-sizeSpecifies a warning limit for the execution context, which includesthe variable table. The warning limit check is performed whenever an activity is completed orprocess (or a step is completed in a service flow). However, a warning limit check is only performedafter the execution context is saved. The setting accepts the following child element:
    - softSpecifies the warning limit that causes a warning message to be issued. The default value
is -1, which causes any specified limit to be ignored wherever it is
found.

```
<server>
   <twobject-array-length-warning-limit merge="replace">10000</twobject-array-length-warning-limit>
   <limits>
      <saved-symbol-table-size><soft merge="replace">-1</soft></saved-symbol-table-size>
   </limits>
</server>
```

For information about the individual
100Custom.xml files that need to be updated and their locations, see Location of 100Custom configuration files.

However, to consistently and
reliably change a warning limit in all of the 100Custom.xml files in your
deployment environment, it is recommended that you use the updateBPMConfig
command as described in the following procedure:

## Procedure

1. Stop the servers for Workflow Server and Workflow Center.
2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all affected servers: 
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/twobject-array-length-warning-limit', '-xNodeValue', warning\_limit ] )

wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/limits' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/limits/saved-symbol-table-size' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/limits/saved-symbol-table-size/soft', '-xNodeValue', warning\_limit ] )
wsadmin> AdminConfig.save()
Replace the warning\_limit variable with a new value for the
warning limit.
4. Restart the servers.

## Results

Traditional:  The
recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.