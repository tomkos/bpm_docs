# Configuring transaction timeouts

## About this task

The default-transaction-timeout and
default-long-transaction-timeout configuration settings are commonly used in
Business Automation Workflow to specify transaction timeouts. These
settings are described in the following list:

These two settings are not used for SCA transactions or BPEL transactions.

Although you should be aware of these two Business Automation Workflow settings, their default values are generally
sufficient and you rarely (if ever) need to modify their values. However, you need to ensure that
the values of the corresponding WebSphere® Application
Server settings
are appropriate given the values of the two Business Automation Workflow settings. The corresponding WebSphere Application
Server settings are described in the following list:

Generally, the default values are sufficient for these WebSphere Application
Server settings and you should not modify their values.
Detailed information about these settings is found in the WebSphere Application
Server topic Configuring transaction properties for an application
server.

```
<server merge="mergeChildren">
  <default-transaction-timeout merge="replace">480</default-transaction-timeout>
  <default-long-transaction-timeout merge="replace">14400</default-long-transaction-timeout>
</server>
```

For information about the individual 100Custom.xml files that need to be
updated and their locations, see the topic Location of 100Custom configuration files.

However, to consistently and reliably change the value of the settings in all of the
100Custom.xml files in your Business Automation Workflow deployment environment, it is recommended that
you use the updateBPMConfig command as described in the following procedure:

## Procedure

1. Stop the servers for Workflow Server and
Workflow Center.
2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all affected servers (but first modify the
default values as needed):

wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/default-transaction-timeout', '-xNodeValue', '480' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/default-long-transaction-timeout', '-xNodeValue', '14400' ] )
wsadmin> AdminConfig.save()
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.