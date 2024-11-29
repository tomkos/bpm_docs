# Controlling administrator access to task instance data

## About this task

## Procedure

- Traditional: To add the configuration setting to the 100Custom.xml file, complete thefollowing steps:
    1. Stop the servers for Workflow Server or Workflow Center.
    2. Open each 100Custom.xml file. For information about the individual
100Custom.xml files that need to be updated and their locations, see the topic
Location of 100Custom configuration files.
    3. In each 100Custom.xml file, add the
authorization-enabled-for-admins-to-get-set-task-data setting. For example, to
prevent administrators from accessing task instance data, add the following elements under the
<properties> element:<server>
   <portal>
      <authorization-enabled-for-admins-to-get-set-task-data merge="replace">noadmins
      </authorization-enabled-for-admins-to-get-set-task-data>
   </portal>
</server>
    4. In each 100Custom.xml file, save your changes.
    5. In a browser, open each 100Custom.xml file to ensure that it contains no
special characters.
    6 Complete one of the following steps:
        - In a clustered environment, ensure that the changes are propagated to the nodes by forcing a
synchronization and restarting the deployment environment.
        - In a stand-alone server environment, restart the server.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Customizing Business Automation Workflow properties.