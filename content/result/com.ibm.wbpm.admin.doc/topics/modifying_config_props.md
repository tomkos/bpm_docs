# Modifying individual configuration properties

- Configuring notifications and actions for system maintenance

 Traditional: 
 IBM® Business Automation Workflow systems can get overloaded if you don't tune your system and perform regular maintenance on artifact types that accumulate over time, such as process instances, named snapshots, unnamed snapshots, task instances, and durable messages. Without tuning or regular maintenance, systems eventually experience slowdowns and in extreme cases outages.
- Configuring transaction timeouts

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can add or modify configuration settings that are used to specify transaction timeouts.
- Setting default time zones for ECM servers

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can add or modify the ecm-server-default-timezone configuration setting that is used to set default time zones for ECM servers.
- Enabling logging of client IP address for login events in IBM Business Automation Workflow applications

 Traditional: 
 By default, IBM Business Automation Workflow apps do not log the client IP address for login events because that information is regarded as sensitive information. To enable the logging of this information, you must change the log-client-ip-at-logon configuration property in the appropriate 100Custom.xml files. This update is best made using the updateBPMConfig command.
- Specifying a port number for an SMTP server

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can set a configuration setting to specify a port number for a Simple Mail Transfer Protocol (SMTP) server.
- Setting the save mode in IBM Process Designer (deprecated)

 Traditional: 
 You can set the option that determines how changes in the editor are saved in the Process Designer by adding the collaboration-mode configuration setting to the 100Custom.xml files.
- Enabling browser caching to improve web Process Designer performance

 Traditional: 
 In Business Automation Workflow, there are two settings that control whether browser caching is enabled for resources in the snapshots of toolkits. When browser caching is enabled, it reduces the number of network calls for resources that are needed by editors. This improves the scalability of the editor and enhances performance. To override the default value for these settings, you can use the updateBPMConfig command to add or modify the settings in the 100Custom.xml file.
- Increasing the maximum number of cached objects during refactoring

Your attempt to copy or clone a large project might fail with an error.
- Disabling server-side JavaScript syntax validation

 Traditional: 
 JavaScript syntax validation helps ensure that the code snippets in process applications and toolkits are correctly structured and free of syntax errors. IBM Business Automation Workflow supports server-side JavaScript validation in script activities and variable initialization in service flows and processes by default. To turn it off, you must add the setting to the 100Custom.xml file.
- Selecting the EPV data to use in snapshot deployment or instance migration

 Traditional: 
 In earlier releases of Business Automation Workflow, the latest modified EPV data was used in snapshot deployment or instance migration. Interim fix JR47706 introduced a new behavior where the default EPV data for a target snapshot version overwrites the EPV data set in the older snapshot release. However, the later interim fix JR52960 restores the behavior where the latest modified EPV data is used rather than the default EPV data. A configurable property epv-deploy-default has been introduced to let you toggle between these two behaviors.
- Optimizing performance for collaboration operations

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can set a configuration setting to control authorization checks for task actions in coaches, heritage coaches, or both. This can help you optimize performance for collaboration operations.
- Deleting process instance tokens when a referenced task does not exist

 Traditional: 
 In earlier releases of Business Automation Workflow, you could not delete process instance tokens if the task that the process refers to did not exist or the process did not contain tasks. However, a configurable property force-token-action has been introduced to let you delete these orphaned process instance tokens that have no associated tasks.
- Disabling team synchronization during process instance migration

 Traditional: 
 When you migrate process instances into a new IBM Business Automation Workflow snapshot on an Workflow Server environment, groups and members are automatically reinstated that were intentionally deleted from teams to prevent them from being able to launch a business process definition (BPD). However, you can use the configurable property disable-team-sync to disable team synchronization during process instance migration and prevent deleted groups and members from being automatically added back to teams.
- Disabling user registry group synchronization during server startup

Group names from the configured user registry are replicated into the product database when the server starts. If the user registry contains many groups, the server startup can take longer than expected. However, you can use the configurable property synchronize-user-registry-groups-on-start-up to disable the user registry group synchronization during server startup. In this case, it is recommended to call the group synchronization REST API or the syncGroupMembershipForGroups tool at a convenient time to perform the group synchronization manually (see Synchronizing group membership by groups).
- Retrieving all user registry groups during server startup

Logging into the server can take longer than expected or even fail when some of the user registry groups cannot be retrieved during server startup. This problem can occur when some groups are marked as inactive during server startup and are not retrieved along with the other groups. However, you can use the configurable property mark-group-inactive-as-needed-in-start-up to prevent groups from being marked inactive.
- Monitoring and repairing user and group memberships for ad hoc groups

Generally, you should never change the user and group membership of an ad hoc group. Regardless, in previous releases there were several ways to change the membership and inadvertently render the ad hoc group incorrect. Since all ad hoc groups are shared, any change in the membership means that all subsequently created tasks (which are assigned to the same list of users and groups) are associated with the incorrect ad hoc group and its membership. However, you can monitor ad hoc groups and repair incorrect user and group memberships by adding the enable-ad-hoc-group-monitoring configuration setting to the 100Custom.xml files.
- Controlling authenticated user access to internal service types

 Traditional: 
 In earlier releases of Business Automation Workflow, you could invoke a service by using the executeServiceByName URL and there was no access restriction based on the service type. Instead, services that were only meant for internal use were available to all authenticated users. Although this release of Business Automation Workflow includes behavior that now validates the service type for invocations that are performed using the executeServiceByName URL, an enforce-correct-service-type-for-execute-service-by-name configuration setting has been introduced for backwards compatibility. You can add the setting to the 100Custom.xml files and use it to intentionally permit authenticated users to invoke internal service types.
- Resolving user mismatch between the user information cache and the database

When the user is mismatched between the user information cache and the database, the user information cache holds references to users that are not in the database. If the user information in the cache is used for further database operations, a database transaction that follows the mismatch might fail with a constraint violation exception. To prevent this mismatch, you can add the user-info-cache-block-period configuration setting to the 100Custom.xml files. Using this setting, you can specify a period of time during which the cache entry is considered invalid and is not used (if it has not been confirmed by at least one successful read from the database).
- Controlling administrator access to task instance data

By default, administrators are permitted to obtain and view task instance data regardless of whether they own the associated tasks. However, you can control administrator access to task instance data by adding the authorization-enabled-for-admins-to-get-set-task-data configuration setting to the 100Custom.xml files.
- Disabling access to process instance variables in REST APIs

Configure authorization-for-process-data-access to disable the access to process instance variables in REST APIs.
- Preventing tasks from completing in suspended BPD instances

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can use the prevent-complete-task-in-suspended-instance setting to prevents tasks from completing in suspended BPD instances.
- Restricting Inspector actions for online workflow servers

You can limit Inspector actions for specific workflow servers or environment types.
- Specifying an absolute URL for the TWManagedFile JavaScript API

By default, a relative URL is used for the .url property of the TWManagedFile JavaScript API. However, if necessary, you can use an absolute URL instead by adding a configuration setting in the 100Custom.xml file.
- Web services

Some behaviors of web services can be modified by setting configuration properties.
- Controlling warning limits for variable sizes of process and service flows

There are some settings in configuration files that define warning limits for the variable sizes of process and service flows. If a warning limit is reached or exceeded for any of the settings, a warning message is logged in the SystemOut.log file. You can, however, override the default warning limits for the settings by adding the settings to the 100Custom.xml file.
- Detecting infinite loops in services and process instances

There are two loop detection properties that you can use to detect and handle infinite loops in services and process instances.
- Modifying the stateful session bean cache

 Traditional: 
 To modify the default cache timeout, edit the session-bean-cache-expiry-timeout value in the appropriate 100Custom.xml file to your topology.
- Optimizing group membership retrieval during user login

 Traditional: 
 Use WebSphere native configuration to optimize group retrieval for users and their group memberships between Lightweight Directory Access Protocol (LDAP) and the Business Automation Workflow database.
- Disabling updates for user names with trailing blanks

IBM Business Automation Workflow considers user names that contain trailing blanks and their corresponding entries without the trailing blanks in the Lightweight Directory Access Protocol (LDAP) registry identical. By default Business Automation Workflow updates the information for user names with trailing blanks in its database with their LDAP counterparts during synchronization. This is also the recommended behavior. However, for compatibility reasons you can disable updates for user names with trailing blanks.
- Configuring the file size of uploaded content management documents

 Traditional: 
 To avoid resource depletion (such as disk space and network throughput) by uploading very large files or files that are not required for the defined use cases, the system administrator can restrict the file size of the uploaded content management documents for the document list coach view.
- Restrictions on large file uploads and SVG browser display for ECM and BPM documents

To prevent any potential security issues, additional restrictions on large file uploads and SVG browser display apply to ECM and BPM documents.
- Hiding frequent logging of error messages

 Traditional: 
 The log-tracked-loudly configuration property in the appropriate 100Custom.xml files to your topology enables or disables logging of frequent error messages.
- Hiding warnings about missing groups

 Traditional: 
 The warn-of-membership-referring-to-missing-group configuration property in the appropriate 100Custom.xml files in your topology enables or disables the logging of warnings about missing groups.
- Disabling group membership update at login time for web applications

When a user logs in to Business Automation Workflow web applications such as Process Portal, group membership is recalculated and can be cached for that user on the database, in order to keep accurate permission checks based on group memberships. This process might significantly affect performance because it can take up to several seconds, depending on how many user groups are registered in the system. You can use the synchronize-user-registry-groups-on-login configuration property to disable this mechanism. In this case, it is recommended to call the group synchronization REST API or the syncGroupMembershipForGroups tool at a convenient time to perform the group synchronization manually (see Synchronizing group membership by groups).
- Enabling adding user registry groups of a user at login time for web applications

When a user logs in to Business Automation Workflow web applications such as Process Portal, group membership is recalculated and can be cached for that user on the database, in order to keep accurate permission checks based on group memberships.
- Optimizing the login time for web applications

To help improve performance, you can reduce the time that a user spends logging in to web applications, including Process Portal. For this purpose, you set the user-group-membership-sync-cache-expiration configuration property to a number of minutes under which that user's membership to user groups is not recalculated.
- Specifying that members of a group member cache are retrieved from the database

Use the group-member-cache-source setting in the appropriate 100Custom.xml file in your topology to specify that members of a group are retrieved from the IBM Business Automation Workflow database only, and not from a user registry, for example LDAP. This setting significantly increases the speed at which group members are loaded into the cache and reduces the number of cache reloads.
- Optimizing the group member cache heap size

To tune the group member caching, use the group-member-cache-memory-optimized and group-member-cache-max-size settings in the appropriate 100Custom.xml file.
- Configuring additional system lane users

 Traditional: 
 You can update your configuration settings to add, replace, or remove additional system lane users in the IBM Business Automation Workflow environment.
- Changing the block size allocation for primary keys

 Traditional: 
 When instances, tasks and other objects are created in Business Automation Workflow, a primary key is generated. Primary keys are internal to Business Automation Workflow and they are created as needed. The default block size allocation for a primary key is 50 and this value should not need to be changed in most environments. However, in high-volume environments, you might need to increase the block size allocation for a primary key. This is accomplished by specifying the <pri-key-block-size> configuration setting in the appropriate 100Custom.xml file to your topology.
- Enforcing the scope of private variables when using the executeServiceByName JavaScript API

 Traditional: 
 When you use the executeServiceByName JavaScript API, you can provide a map with input variables. If an input variable name is identical to the name of a private variable of the called service, the API overwrites the value of the private variable. To preserve the application data of the called service, you can enforce the scope of the private variables by configuring a property in the appropriate 100Custom.xml file in your topology.
- Handling an IllegalDataException for invalid XML during serialization

 Traditional: 
 When you convert a string that contains ASCII control characters to XML, you receive an IllegalDataException during serialization. You can add a configurable property the appropriate 100Custom.xml file in your topology to automatically make strings XML-compliant.
- Extending the maximum number of characters in tracked performance data

 Traditional: 
 By default, the maximum number of characters that is allowed in performance data (variable fields that are tracked to the Performance Data Warehouse for reporting purposes) is 64. You can extend this limit by making the following changes to the property file for Performance Data Warehouse. The changes that you make to this property affect the column sizes in the tracking group tables.
- callService configuration for running different service types

 Traditional: 
 IBM Process Portal uses the callService servlet and the tw.coach.callService JavaScript API to invoke services. This servlet is configured to run Ajax services by default. If you have custom client applications that rely on callService to call service types other than Ajax services, add a configuration property to the 100Custom.xml file in IBM Workflow Center or IBM Workflow Server to specify the allowlist of callable services.
- Displaying detailed error messages generated by custom applications

 Traditional: 
 To display detailed error messages that are generated by custom application code instead of a generic error message, add the display-debug-error-messages configuration setting in the appropriate 100Custom.xml file in your topology.
- Controlling the number of items displayed in the Event Manager monitor

 Traditional: 
 You can control how many items are displayed in the Event Manager page of the Process Admin Console by configuring the event-job-threshold setting in the appropriate 100Custom.xml file in your topology.
- Defining validation behavior for business objects

 Traditional: 
 In IBM Process Designer, you can create business object types that define restrictions on the simple types. For example, for a business object type that has Decimal as the base type, you can specify the precision and scale settings. These settings are validated in heritage coaches and when you set a variable value in a process or service. Through various settings, you can customize the validation to behave like the totalDigits and fractionDigits constraining facets as defined by the XML Schema.
- Configuring proxy settings

 Traditional: 
 If you use a proxy server for internet connections, you can configure IBM Business Automation Workflow so that it uses the appropriate server and protocol for internet connections, such as when connecting to Blueworks Live.
- Retrieving a user's full name in an easier-to-read format

 Traditional: 
 When you use federated repositories, you can configure the user property in the 100Custom.xml to use the displayName attribute so that the output is easier to read.
- Specifying a default time zone for work schedules

 Traditional: 
 In IBM Process Portal, the time zone that you specify for work schedules for users or for when activities are due is used to calculate due dates for processes and activities. If you do not specify the time zone, Central Standard Time zone is used as the default. However, you can apply a custom default value in the 100Custom.xml files in IBM Workflow Server, Workflow Center, or both environments.
- Configuring time zone precedence

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can use the client-time-zone-has-precedence setting to specify whether the time zone setting in the user preferences has a precedence over the server-side time zone setting. Generally, the client time zone is the time zone that is used in the user preferences.
- Enabling non-admin users to run REST APIs in Workflow Server

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can use the enforce\_authorization\_check\_for\_ps\_model\_data setting to enable users to run REST APIs in Workflow Server when they are not members of the tw\_admins group.
- Configuring a key for credential encryption

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, you can use the cipher-pass-passphrase setting to configure a key for credential encryption and decryption.
- Configuring mail for WebSphere Application Server mail sessions

 Traditional: 
 In the 100Custom.xml files for Workflow Server and Workflow Center, the extension-by-jndi-name setting enables you to use the mail session configured in WebSphere® Application Server to extend the use of functions defined in the session.
- Limiting the number of REST calls to the server

In the 100Custom.xml files for the workflow server and Workflow Center, you can add or modify configuration settings that are used to limit the number of REST calls to the server within a time interval and prevent a denial of service attack.
- Optimizing Performance Data Warehouse

 Traditional: 
 Performance Data Warehouse is not designed to store a large amount of data. You can reduce the number of rows inserted in tables of Performance Data Warehouse by making changes to the property file for Performance Data Warehouse.