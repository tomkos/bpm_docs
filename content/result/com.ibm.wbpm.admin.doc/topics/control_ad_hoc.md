# Monitoring and repairing user and group memberships for ad hoc groups

Generally, you should never change the user and group membership of an ad hoc group.
Regardless, in previous releases there were several ways to change the membership and inadvertently
render the ad hoc group incorrect. Since all ad hoc groups are shared, any change in the membership
means that all subsequently created tasks (which are assigned to the same list of users and groups)
are associated with the incorrect ad hoc group and its membership. However, you can monitor ad hoc
groups and repair incorrect user and group memberships by adding the
enable-ad-hoc-group-monitoring configuration setting to the
100Custom.xml files.

For
more information about ad hoc groups, see the topic IBM Business Automation Workflow default group types.

## About this task

## Procedure

- Traditional: To add and enable the enable-ad-hoc-group-monitoring configuration settingin the 100Custom.xml file, complete the following steps:
    1. Stop the servers for Workflow Server or Workflow Center.
    2. Open each 100Custom.xml file. For information about the individual
100Custom.xml files that need to be updated and their locations, see the topic
Location of 100Custom configuration files.
    3. In each 100Custom.xml file, add the
enable-ad-hoc-group-monitoring setting and associated elements under the
<properties> element, as shown in the following
example:<server>
   <portal>
      <enable-ad-hoc-group-monitoring merge="replace">true</enable-ad-hoc-group-monitoring>
   </portal>
</server>(If for some reason you want to later disable the monitoring of ad hoc
groups, change the value to false.)
    4. In each 100Custom.xml file, save your changes.
    5. In a browser, open each 100Custom.xml file to ensure that it contains no
special characters.
    6 Complete one of the following steps:
        - In a clustered environment, ensure that the changes are propagated to the nodes by forcing a
synchronization and restarting the deployment environment.
        - In a stand-alone server environment, restart the server.