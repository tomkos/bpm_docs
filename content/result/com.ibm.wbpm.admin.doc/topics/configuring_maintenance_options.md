# Configuring notifications and actions for system maintenance

## Before you begin

Before you customize the notifications, especially before you change the warning and critical
thresholds, make sure that your system is sized and tuned to perform as expected with the increased
number of artifacts. It is recommended to perform load tests in your pre-production environment to
verify that the current sizing and tuning can cope with the increased number of artifacts, or to
define needed tuning actions. For information about tuning multiple areas of your system, see Tuning and Tuning IBM Business Automation Workflow.

- JVM tuning, see Tuning the IBM virtual machine for Java and Java virtual machine settings.
- Cache tuning, see Using process instrumentation data for cache tuning and Cache and cache-related settings
- Enabling the saved search acceleration tools, see Saved search acceleration tools

After you have made sure your system can cope with a higher number of artifacts, you can override
the default values for the notification and action settings. For that, you can use the
updateBPMConfig command to add or modify the settings in the
100Custom.xml file.

## About this task

You can use the following settings to control the artifact types that you want to monitor, when
to log messages, and the actions to take when the amount of data exceeds the thresholds. The
settings are enabled by default. To disable them, set enabled to
false.

- type: The artifact type that you want to monitor
- servertype (optional): For named and unnamed snapshots, specify the server
location where you want to monitor the artifact type. For a workflow server, set the value to
PS. For a workflow center, set the value to PC. To specify both
locations, ensure that the value is set to ALL, which is the default value.

- NAMED\_SNAPSHOTS on a workflow server: 128
- NAMED\_SNAPSHOTS on a workflow center: 500
- UNNAMED\_SNAPSHOTS: 10000
- PROCESS\_INSTANCES: 600000
- TASK\_INSTANCES: 2400000
- DURABLE\_MESSAGES: 8000000

- NAMED\_SNAPSHOTS on a workflow server: 100
- NAMED\_SNAPSHOTS on a workflow center: 400
- UNNAMED\_SNAPSHOTS: 5000
- PROCESS\_INSTANCES: 400000
- TASK\_INSTANCES: 1600000
- DURABLE\_MESSAGES: 5000000

On a workflow server, specifying the INSTALL
value disables snapshot installation. INSTALL is the default value for the
NAMED\_SNAPSHOTS monitor. To enable installation, replace the monitor
element in the 100Custom.xml file, and omit this setting.

```
<server>
   <system-maintenance-monitor merge="replace" enabled="true">
     <log-on-server-start merge="replace">true</log-on-server-start> 
     <log-interval merge="replace">1400</log-interval>

     <monitor type="NAMED\_SNAPSHOTS" merge="replace" enabled="true" servertype="PS">
          <critical-threshold>128</critical-threshold>
          <warning-threshold>100</warning-threshold>
          <prevent-lifecycle-action>INSTALL</prevent-lifecycle-action>
     </monitor>

     <monitor type="NAMED\_SNAPSHOTS" merge="replace" enabled="true" servertype="PC">
          <critical-threshold>500</critical-threshold>
          <warning-threshold>400</warning-threshold>
          <prevent-lifecycle-action>INSTALL</prevent-lifecycle-action>
     </monitor>     

     <monitor type="UNNAMED\_SNAPSHOTS" merge="replace" enabled="true" servertype="PC">
          <critical-threshold>10000</critical-threshold>
          <warning-threshold>5000</warning-threshold>
         <show-message-on-lifecycle-action>INSTALL</show-message-on-lifecycle-action>
     </monitor>

     <monitor type="PROCESS\_INSTANCES" merge="replace" enabled="true">
          <critical-threshold>600000</critical-threshold>
          <warning-threshold>400000</warning-threshold>
          <show-message-on-lifecycle-action>INSTALL</show-message-on-lifecycle-action>     
     </monitor>

     <monitor type="TASK\_INSTANCES" merge="replace" enabled="true">
          <critical-threshold>2400000</critical-threshold>
          <warning-threshold>1600000</warning-threshold>
           <show-message-on-lifecycle-action>INSTALL</show-message-on-lifecycle-action>
     </monitor>

      <monitor type="DURABLE\_MESSAGES" merge="replace" enabled="true">
          <critical-threshold>8000000</critical-threshold>
          <warning-threshold>5000000</warning-threshold>
          <show-message-on-lifecycle-action>INSTALL</show-message-on-lifecycle-action>
      </monitor>
   </system-maintenance-monitor>
</server>
```

If thresholds aren't defined, no action will occur because it uses the thresholds to initiate its
action. <critical-threshold>, <warning-threshold>, or
both settings must be defined for the corresponding action to work.

For information about changing the 100Custom.xml files, see The 100Custom.xml file and configuration. For information about the individual
100Custom.xml files that must be updated and their locations, see Location of 100Custom configuration files.

However, to consistently and reliably change the value of the two settings in all of the
100Custom.xml files in your Business Automation Workflow deployment environment,
it is recommended that you use the updateBPMConfig command as described in the
following procedure:

## Procedure

1. Stop the servers for Workflow Server and Workflow Center.
2. Start the scripting client in disconnected mode as described in the topic updateBPMConfig command.
3. For each property, run the following commands to simultaneously update all affected
servers:

wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/@merge', '-xNodeValue', 'replace' ] )  
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/@enabled', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/log-on-server-start', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/log-interval', '-xNodeValue', 'interval\_value' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/@merge', '-xNodeValue', 'replace' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/@type', '-xNodeValue', 'artifact\_type' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/@enabled', '-xNodeValue', 'true\_or\_false' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/@servertype', '-xNodeValue', 'server\_type' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/critical-threshold', '-xNodeValue', 'critical\_threshold\_value' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/warning-threshold', '-xNodeValue', 'warning\_threshold\_value' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/prevent-lifecycle-action', '-xNodeValue', 'application\_action' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/system-maintenance-monitor/monitor/show-message-on-lifecycle-action', '-xNodeValue', 'application\_action' ] )
wsadmin> AdminConfig.save()
Replace the true\_or\_false variable with either
true or false and other variables such as
interval\_value,
artifact\_type, server\_type,
critical\_threshold\_value,
warning\_threshold\_value, and
application\_action with their respective values. Note: The
previous commands assume the properties are not defined in the 100Custom.xml
file yet. If they are available already, choose option -update instead of
-create for these updateBPMConfig commands.
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.