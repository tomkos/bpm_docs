# Deleting process instance tokens when a referenced task does
not exist

## About this task

In the past, you could not delete process instance tokens
if an associated task ID could not be found. A missing task ID can
be caused by process instances that contain active tokens that are
set on an event but the associated task no longer exists. In this
situation, the tokens could not be deleted and a Task
ID not found error occurred. Another situation that
can occur is when a token is set on a flow line and an attempt is
made to move or delete the token using the REST API. In this situation,
a 200 success code is returned but the
token is not actually removed.

However, you can now use the force-token-action setting
to specify whether orphaned process instance tokens can be deleted
when they do not have tasks. If true is specified
(which is the default), you can delete process instance tokens that
have no tasks. If false is specified, you cannot
delete process instance tokens that have no tasks.

```
<server>
   <instance-migration merge="mergeChildren">
      <force-token-action merge="replace">true
      </force-token-action>
   </instance-migration>
</server>
```

For information about the individual 100Custom.xml files
that need to be updated and their locations, see the topic Location of 100Custom configuration files.

However, to
consistently and reliably change the value of the setting in all of
the 100Custom.xml files in your Business Automation Workflow deployment
environment, it is recommended that you use the updateBPMConfig command
as described in the following procedure:

## Procedure

1. Stop the servers for Workflow Server and Workflow Center.
2. Start the scripting client in disconnected mode as described
in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all
affected servers:  wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/instance-migration' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/instance-migration/force-token-action', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminConfig.save() Replace the true\_or\_false variable
with either true or false.
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files
is by running the updateBPMConfig command. However,
if the updates are unsuccessful, you can manually update the files
by following the steps in the topic Creating a 100Custom.xml configuration file.