# Selecting the EPV data to use in snapshot deployment or instance
migration

## About this task

The interim fix JR47706 modified the EPV behavior
by adding the default EPV data for the target snapshot to the EPV
table with an Effective On date that reflects the date that the snapshot
was deployed. If instances of earlier snapshots are later migrated
to this snapshot, the EPV Effective On values in them will be earlier
than that of the default EPV data for the target snapshot, which will
result in the default EPV data becoming the effective snapshot. The
later interim fix JR52960 restores the behavior
where the latest modified EPV data is used rather than the default
EPV data.

The epv-deploy-default setting
specifies whether to use the latest modified EPV data or the default
EPV data from the snapshot for deployment of the snapshot or instance
migration. If false is specified (which is
the default), the latest modified EPV data from the snapshot is used.
If true is specified, the default EPV data
from the snapshot is used.

```
<server>
   <instance-migration merge="mergeChildren">
      <epv-deploy-default merge="replace">false
      </epv-deploy-default>
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
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/instance-migration/epv-deploy-default', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminConfig.save() Replace the true\_or\_false variable
with either true or false.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.