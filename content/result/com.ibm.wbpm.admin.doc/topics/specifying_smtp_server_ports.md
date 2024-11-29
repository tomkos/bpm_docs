# Specifying a port number for an SMTP server

## About this task

In the past, a default port number of 25 was used for the SMTP server in
all scenarios. However, using the new mail-smtp-port setting, you can now
specify any port number for an SMTP server.

```
<server>
   <email merge="mergeChildren">
      <mail-smtp-port merge="replace">465</mail-smtp-port>
   </email>
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
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/email' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/email/mail-smtp-port', '-xNodeValue', setting\_value ] )
wsadmin> AdminConfig.save()
Replace the setting\_value variable with a port number.
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.