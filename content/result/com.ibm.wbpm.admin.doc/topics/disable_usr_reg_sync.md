# Disabling user registry group synchronization during server startup

## About this task

```
<common>
  <security>
    <synchronize-user-registry-groups-on-start-up merge="replace">false</synchronize-user-registry-groups-on-start-up>
  </security>
</common>
```

## Procedure

- Traditional: To consistently and reliably change the value of the setting in all of the 100Custom.xml files inyour Business Automation Workflow deploymentenvironment, it is recommended to use the updateBPMConfig command as described inthe following procedure:
    1. Stop the servers for Workflow Server and Workflow Center.
    2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
    3. Run the following commands to simultaneously update all affected
servers:wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security/synchronize-user-registry-groups-on-start-up', '-xNodeValue', true\_or\_false ] )
wsadmin> AdminConfig.save()
    4. Replace the true\_or\_false variable with either
true or false.
    5. Restart the servers.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Customizing Business Automation Workflow properties.