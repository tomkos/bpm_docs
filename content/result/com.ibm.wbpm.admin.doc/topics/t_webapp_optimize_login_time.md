# Optimizing the login time for web applications

## About this task

When a user logs in to IBM® Business Automation Workflow web applications such
as the Process Portal, group
membership is recalculated and can be cached for that user on the database. This process might
significantly affect performance because it can take up to several seconds, depending on how many
user groups are registered to the system. Moreover, any interaction from the user is blocked while
the group memberships are calculated. See also, Specifying that members of a group member cache are retrieved from the database.

When a user logs in and out several times within a period, or logs in to different applications,
the group memberships are refreshed each time. To help improve performance, you can use the
user-group-membership-sync-cache-expiration configuration property to specify
the amount of time, in minutes, after which the calculation of user group membership is repeated.
For example, if the user logs in and out and in again to Process Portal, and if the time that elapsed since the first
login is shorter than the specified number of minutes, the group memberships are not recalculated on
the second login.

The default
value is 1 minute. If you set this property to -1, user group
memberships are never refreshed upon login. Specify this value only when specific administration
procedures regularly refresh group memberships. For more information about
group membership synchronization, see Synchronizing group membership by users.

For more information about customizing configuration properties, see The 100Custom.xml file and configuration.

## Procedure

- Traditional: To set this property to false in the 100Custom.xml files, complete the following steps:
    1. Stop the servers for Workflow Server and Workflow Center.
    2. Open the 100Custom.xml file and overwrite the value for the
user-group-membership-sync-cache-expiration property.The following XML
example specifies an expiration time of 2 hours:<common>
   ...
      <security
         <user-group-membership-sync-cache-expiration merge="replace">120</user-group-membership-sync-cache-expiration>
      </security>
   </common>
    3. Save your changes to each 100Custom.xml file.
    4. Retart the servers for Workflow Server and Workflow Center.
- Containers: 
 If
you use containers, make changes to the 100Custom.xml file by following the
procedure described at Customizing Business Automation Workflow properties.