# Enabling browser caching to improve web Process Designer performance

## About this task

The following settings control whether browser caching
is enabled for resources in toolkits:

Specifies whether the browser cache is enabled for the snapshots
of system toolkits. The default value is false.
If the enable-browser-cache-for-snapshot setting
is set to true, caching of snapshots of system
toolkits is also enabled and changing the enable-browser-cache-for-system setting
to false has no effect.

```
<web-pd>
   <enable-browser-cache-for-snapshot merge="replace">false</enable-browser-cache-for-snapshot>    
   <enable-browser-cache-for-system merge="replace">true</enable-browser-cache-for-system>
</web-pd>
```

For information about the individual 100Custom.xml files
that need to be updated and their locations, see the topic Location of 100Custom configuration files.

However, to
consistently and reliably change the value of the two settings in
all of the 100Custom.xml files in your Business Automation Workflow deployment
environment, it is recommended that you use the updateBPMConfig command
as described in the following procedure:

## Procedure

1. Stop the servers for Workflow Server and Workflow Center.
2. Start the scripting client in disconnected mode as described
in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all
affected servers:  wsadmin> AdminTask.updateBPMConfig( [ '-create', '/web-pd' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/web-pd/enable-browser-cache-for-snapshot', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/web-pd/enable-browser-cache-for-system', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminConfig.save() Replace the true\_or\_false variable
with either true or false.
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files
is by running the updateBPMConfig command. However,
if the updates are unsuccessful, you can manually update the files
by following the steps in the topic Creating a 100Custom.xml configuration file.