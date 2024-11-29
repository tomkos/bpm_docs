# Configuring mail for WebSphere Application
Server mail
sessions

## Before you begin

If you have an existing Java integration implementation that uses the older WebSphere Javamail
library, the implementation may throw exceptions. For troubleshooting information, see the topic
Existing Java integration implementations may throw exceptions when using the WebSphere Javamail library.

## About this task

```
<server>
   <email>
      <extension-by-jndi-name merge="replace">JNDI\_session\_name</extension-by-jndi-name>
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

wsadmin -connType none -lang jython
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/email' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/server/email/extension-by-jndi-name', '-xNodeValue', 'JNDI\_session\_name' ] )
wsadmin> AdminConfig.save()
4. Restart the servers.

## Results

The recommended way of updating the 100Custom.xml files is by running the
updateBPMConfig command. However, if the updates are unsuccessful, you can
manually update the files by following the steps in the topic Creating a 100Custom.xml configuration file.