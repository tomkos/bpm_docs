# Retrieving all user registry groups during server startup

## About this task

Business Automation Workflow replicates
group names from the configured user registry into the product database when the server starts. For
this purpose, a wildcard query is used to retrieve all groups during server startup. Some user
registries do not return all groups (or any groups) in response to this query; for example, some
groups may not be returned if the threshold is exceeded for a configured maximum result size.

Groups that have been replicated into the Business Automation Workflow database – but are not
returned as part of the wildcard query when the server starts – are marked deleted in the Business Automation Workflow database and are not
added to the in-memory group cache. If these groups exist, this marked as
deleted indicator in the database is incorrect. Moreover, if the groups are used for
task assignment or they are observed as groups of a user when that user tries to log in,
performance-intensive database queries occur that can lead to poor login performance or even lock
congestion.

The mark-group-inactive-as-needed-in-start-up setting is used to disable or
enable the mechanism for marking user registry groups as inactive. If false
is specified, no user registry groups are marked as inactive during server startup. If
true is specified (which is the default), user registry groups are marked as
inactive as needed during server startup.

```
<common>
   <security>
      <mark-group-inactive-as-needed-in-start-up merge="replace">false</mark-group-inactive-as-needed-in-start-up>
   </security>
</common>
```

For more information about the individual 100Custom.xml files that need to
be updated and their locations, see Location of 100Custom configuration files.

## Procedure

- Traditional: To consistently and reliably change the value of the setting in all of the 100Custom.xml files inyour Business Automation Workflow deploymentenvironment, it is recommended to use the updateBPMConfig command as described inthe following procedure:
    1. Stop the servers for Workflow Server and Workflow Center.
    2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
    3. Run the following commands to simultaneously update all affected
servers:wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security/mark-group-inactive-as-needed-in-start-up', '-xNodeValue', true\_or\_false ] )
wsadmin> AdminConfig.save()
    4. Replace the true\_or\_false variable with either
true or false.
    5. Restart the servers.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Customizing Business Automation Workflow properties.