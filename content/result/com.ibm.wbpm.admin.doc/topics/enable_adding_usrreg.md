# Enabling adding user registry groups of a user at login time for web applications

When a user logs in to Business Automation Workflow web applications such as
Process Portal, group
membership is recalculated and can be cached for that user on the database, in order to keep
accurate permission checks based on group memberships.

Before 23.0.1, this mechanism also added user registry groups to the database. This is now
disabled by default for performance reasons, since such groups cannot occur in permission checks
yet. You can use the add-user-registry-groups-to-db-on-login configuration
property to re-enable the legacy behavior.

## About this task

```
<common>
  <security>
    <add-user-registry-groups-to-db-on-login merge="replace">false</add-user-registry-groups-to-db-on-login>
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
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security/add-user-registry-groups-to-db-on-login', '-xNodeValue', true\_or\_false ] )
wsadmin> AdminConfig.save()
    4. Replace the true\_or\_false variable with either
true or false.
    5. Restart the servers.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Customizing Business Automation Workflow properties.