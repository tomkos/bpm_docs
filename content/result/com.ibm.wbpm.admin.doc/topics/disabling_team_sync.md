# Disabling team synchronization
during process instance migration

## About this task

The disable-team-sync setting disables
team synchronization during process instance migration. If false is
specified (which is the default), team synchronization is not disabled
during process instance migration and deleted groups and members will
be automatically added back to teams. If true is
specified, team synchronization is disabled during process instance
migration and deleted groups and members will not be added back to
teams.

```
<server>
   <instance-migration merge="mergeChildren">
      <disable-team-sync merge="replace">false
      </disable-team-sync>
   </instance-migration>
</server>
```

For information about the individual 100Custom.xml files
that need to be updated and their locations, see the topic Location of 100Custom configuration files.

To consistently
and reliably change the value of the setting in all of the 100Custom.xml files
in your Business Automation Workflow deployment
environment, it is recommended that you use the updateBPMConfig command
as described in the following procedure:

## Procedure

1. Stop the servers for Workflow Server and Workflow Center.
2. Start the scripting client in disconnected mode as described
in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all
affected servers:  wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/instance-migration' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/instance-migration/disable-team-sync', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminConfig.save() Replace the true\_or\_false variable
with either true or false.
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files
is by running the updateBPMConfig command. However,
if the updates are unsuccessful, you can manually update the files
by following the steps in the topic Creating a 100Custom.xml configuration file.