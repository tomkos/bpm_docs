# Setting the save mode in IBM® Process
Designer
(deprecated)

## About this task

## Procedure

To add and enable the collaboration-mode configuration setting in the
100Custom.xml file, complete the following steps:

1. Stop the server for Workflow Center.
2. Open each 100Custom.xml file. For information about the individual
100Custom.xml files that need to be updated and their locations, see the topic
Location of 100Custom configuration files.
3. In each 100Custom.xml file, add the
collaboration-mode setting and associated elements under the
<properties> element, as shown in the following example:
<web-pd>        
<collaboration-mode merge="replace">HYBRID</collaboration-mode>
</web-pd>(If
you want to switch modes, change the value to TP.)
4. In each 100Custom.xml file, save your changes.
5. In a browser, open each 100Custom.xml file to ensure that it contains no
special characters.
6 Complete one of the following steps:
    - In a clustered environment, ensure that the changes are propagated to the nodes by forcing a
synchronization and restarting the deployment environment.
    - In a stand-alone server environment, restart the server.