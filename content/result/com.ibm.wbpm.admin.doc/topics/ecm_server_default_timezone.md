# Setting default time zones for ECM servers

## About this task

When you work with ECM documents on an IBM® Business Automation
Workflow server that is connected to an ECM server, and that ECM server does not provide time zone
information in date/time properties, you may notice that the values for these fields are incorrect
in regards to the time zone. This issue occurs when time zone information is not provided by the ECM
server, which causes the IBM Business Automation
Workflow server to
assign its own time zone to the date/time values. If the ECM server and IBM Business Automation
Workflow server are in different time zones, the wrong
date/time values will be displayed.

Using the ecm-server-default-timezone configuration setting, you can
explicitly provide a time zone offset for date/time property values arriving from the ECM server
(which does not provide an explicit time zone). You can set this configuration option with the
expected time zone returned by the ECM server. The server configuration field value must be
formatted to be compatible with the values accepted by the
java.util.TimeZone.getTimeZone(String ID) method, such as
America/Chicago or Europe/Berlin (as described in the
topic Class TimeZone).

```
<server merge="mergeChildren">
   <ecm-server-default-timezone>America/Chicago</ecm-server-default-timezone>
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
value as needed):

wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/ecm-server-default-timezone', '-xNodeValue', 'America/Chicago' ] )
wsadmin> AdminConfig.save()
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.