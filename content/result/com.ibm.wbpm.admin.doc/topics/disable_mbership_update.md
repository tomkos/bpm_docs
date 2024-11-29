# Disabling group membership update at login time for web applications

When a user logs in to Business Automation Workflow web applications such as
Process Portal, group
membership is recalculated and can be cached for that user on the database, in order to keep
accurate permission checks based on group memberships. This process might significantly affect
performance because it can take up to several seconds, depending on how many user groups are
registered in the system. You can use the
synchronize-user-registry-groups-on-login configuration property to disable
this mechanism. In this case, it is recommended to call the group synchronization REST API or the syncGroupMembershipForGroups tool at a
convenient time to perform the group synchronization manually (see Synchronizing group membership by groups).

If you do not want to disable the group membership update at login time entirely, you can fine
tune its performance by using additional properties described in Optimizing the login time for web applications.

## About this task

```
<common>
  <security>
    <synchronize-user-registry-groups-on-login merge="replace">false</synchronize-user-registry-groups-on-login>
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
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security/synchronize-user-registry-groups-on-login', '-xNodeValue', true\_or\_false ] )
wsadmin> AdminConfig.save()
    4. Replace the true\_or\_false variable with either
true or false.
    5. Restart the servers.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Customizing Business Automation Workflow properties.