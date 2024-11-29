# Disabling server-side JavaScript syntax validation

## About this task

- In Workflow Center, under
the current version of an application and each named snapshot.
- In the Process Designer
footer, click Validation errors and warnings
. You can choose to view the
errors in the current artifact or project.

Because validation occurs
on the workflow server, it can slow down performance for the user. For this reason, you might choose
to enable it only when you want to import and test a process application for errors before you
deploy the application on a production system. Alternatively, if your environment requires only
client-side validation, you might prefer not to enable JavaScript syntax validation.

Use the
javascript-serverside-validation-enabled setting to control whether server-side
JavaScript syntax validation is enabled in Process Designer. The default value is
true.

```
<server>
   <javascript-serverside-validation-enabled merge="replace">false</javascript-serverside-validation-enabled>
</server>
```

## Procedure

To consistently and reliably change the value of these settings in all the
100Custom.xml files in your Business Automation Workflow deployment environment, use the
updateBPMConfig command:

1. Stop the servers for Workflow Server and
Workflow Center.
2. Start the scripting client in disconnected mode as described in updateBPMConfig command.
3. Run the following commands to simultaneously update all affected servers:

wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/javascript-serverside-validation-enabled', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminConfig.save()
Replace the true\_or\_false variable with either
true or false.
4. Restart the servers.

## Results