# Enabling logging of client IP address for login events in IBM Business Automation
Workflow applications

## Procedure

To consistently enable the log-client-ip-at-logon setting for all of
the 100Custom.xml files in your IBM Business Automation
Workflow
deployment environment, perform the following actions:

1. Stop the server for Workflow Server or Workflow Center.
2. Start the scripting client in disconnected mode, as described in updateBPMConfig command.
3. To simultaneously update the setting on all affected servers, run the following commands:

wsadmin -connType none -lang jython
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security' ] )
wsadmin> AdminTask.updateBPMConfig( [ '-create', '/common/security/log-client-ip-at-logon', '-xNodeValue', 'true' ] )
wsadmin> AdminConfig.save()
4. Restart the servers.
5 If the updates are unsuccessful, you can update the individual100Custom.xml files manually:
    1. Identify the locations of the 100Custom.xml files that need to be updated.
See  Location of 100Custom configuration files.
    2. If a necessary 100Custom.xml file does not exist perform the steps in
Creating a 100Custom.xml configuration file.
    3. Add the following to each file:

<common merge="mergeChildren">
  <security>
    <log-client-ip-at-logon>true</log-client-ip-at-logon>
  </security>
</common>
    4. Save the changes in the 100Custom.xml files.
    5. Optional: 
Open the 100Custom.xml files in a browser to make sure that they contain
no special characters.
    6. In a clustered environment, make sure that the changes are carried to the nodes by doing a
force synchronize and restarting the deployment environment.
    7. In a stand-alone server environment, restart the server.