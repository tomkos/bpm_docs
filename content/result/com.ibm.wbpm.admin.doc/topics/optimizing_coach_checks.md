# Optimizing performance for collaboration operations

## About this task

Although you can use both coaches and heritage coaches as a user interface for human services,
heritage coaches do not support the collaboration features. Depending on the complexity of your
process design, authorization checks that include heritage coaches can be time-consuming. However,
you can use the allow-collaboration setting to include or exclude heritage
coaches in the authorization checks.

The allow-collaboration setting accepts one of the following three
values:

```
<server merge="mergeChildren">
   <allow-collaboration merge="replace">checkForCoaches</allow-collaboration>
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
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/allow-collaboration', '-xNodeValue', setting\_value ] )
wsadmin> AdminConfig.save()
Replace the setting\_value variable with one of the three
available values.
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.