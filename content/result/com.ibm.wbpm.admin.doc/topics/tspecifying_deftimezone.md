# Specifying a default time zone for work schedules

## About this task

```
<server>
   <default-work-schedule>         
        <time-zone merge="replace">time\_zone\_identifier</time-zone>     
   </default-work-schedule>
</server>
```

## Procedure

To consistently and reliably update the time zone setting for work schedules in all the
100Custom.xml files in your Business Automation Workflow deployment environment, complete the following
steps:

1. Stop the servers for Workflow Server and
Workflow Center.
2. Start the scripting client in disconnected mode as described in the updateBPMConfig command topic.
3. Run the following commands to simultaneously update all affected servers:

wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/default-work-schedule' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/default-work-schedule/time-zone', '-xNodeValue', time\_zone\_identifier ] )
wsadmin> AdminConfig.save()
Replace time\_zone\_identifier with the time zone that you want. For example,
to set the default time zone for work schedules to Chinese Standard Time use
Asia/Shanghai for the time zone identifier.Note: If you use the default time
zone and it differs from your system time zone, you might get unexpected results when due dates are
calculated or when you use the JavaScript tw.system.calculateBusinessDate() method to calculate
business dates.
4. Restart the servers.

## Results

The preferred way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in Creating a 100Custom.xml configuration file.