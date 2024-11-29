# Preventing tasks from completing in suspended BPD instances

## About this task

If the prevent-complete-task-in-suspended-instance setting is not set or is
set to the default value of false, tasks are permitted to complete in
suspended BPD instances. However, if you change the setting value to true,
tasks cannot complete in suspended BPD instances.

```
<server>
   <bpd-engine>
      <prevent-complete-task-in-suspended-instance merge="replace">true</prevent-complete-task-in-suspended-instance>
   </bpd-engine>
</server>
```

For information about the individual 100Custom.xml files that need to be
updated and their locations, see the topic Location of 100Custom configuration files.

However, to consistently and reliably change the value of the setting in all of the
100Custom.xml files in your Business Automation Workflow deployment environment, it is recommended that
you use the updateBPMConfig command as described in the following procedure:

## Procedure

1. Stop the servers for Workflow Server and
Workflow Center.
2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
3. Run the following commands to simultaneously update all affected servers:

wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/bpd-engine' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/bpd-engine/prevent-complete-task-in-suspended-instance', '-xNodeValue', setting\_value ] )
wsadmin> AdminConfig.save()
Replace the setting\_value variable with either
true or false.
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.