# Enabling non-admin users to run REST APIs in Workflow Server

## Before you begin

Non-admin users need read permissions on all process apps in the Workflow Server environment.

## About this task

The default value of the enforce\_authorization\_check\_for\_ps\_model\_data
setting is true. If the value is set to false, the
enforce\_authorization\_check\_for\_ps\_model\_data setting enables non-admin users
to run the following REST APIs in Workflow Server:

- Assets
- AssetsCompare
- BusinessObject
- BusinessProcessModel
- CoachFlowWorklight
- EPV
- ExternalActivityModel
- ParticipantGroup
- ProcessAppSettings
- SLA
- Snapshot
- Snapshots
- TimingInterval
- TrackingGroup
- UCA
- WebService

```
<server>
   <enforce-authorization-check-for-ps-model-data merge="replace">false</enforce-authorization-check-for-ps-model-data>
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

wsadmin -connType none -lang jython
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/enforce-authorization-check-for-ps-model-data', '-xNodeValue', 'false' ] )
wsadmin> AdminConfig.save()
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.