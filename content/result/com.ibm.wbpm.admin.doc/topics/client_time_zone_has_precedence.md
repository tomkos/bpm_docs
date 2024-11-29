# Configuring time zone precedence

## About this task

If the client-time-zone-has-precedence setting is not specified in the
100Custom.xml files, or it is specified and set to the default value of
false, the time zone setting in the user preferences does not take precedence
over the server-side time zone setting. However, if the
client-time-zone-has-precedence setting is set to true,
the system attempts to obtain the time zone setting from the user preferences. If the system cannot
retrieve the time zone setting from the user preferences, the server-side time zone setting is
used.

```
<server>
   <client-time-zone-has-precedence merge="replace">true</client-time-zone-has-precedence>
</server>
```

For information about the individual 100Custom.xml files that need to be
updated and their locations, see the topic Location of 100Custom configuration files.

However, to consistently and reliably change the value of the setting in all of the
100Custom.xml files in your Business Automation Workflow deployment environment, it is recommended that
you use the updateBPMConfig command as described in the following procedure:

## Procedure

1. Stop the servers for Workflow Server and
Workflow Center.
2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all affected servers:

wsadmin -connType none -lang jython
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/client-time-zone-has-precedence', '-xNodeValue', 'true' ] )
wsadmin> AdminConfig.save()
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.