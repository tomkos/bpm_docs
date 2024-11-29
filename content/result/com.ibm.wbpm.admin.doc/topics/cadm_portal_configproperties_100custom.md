# Changing configuration properties for Process Portal in
the 100Custom.xml file

- Configuring a custom Default Instance Details UI service

After you upgrade to IBM® Business Automation Workflow 19.0.0.2 or 19.0.0.3, the customized Default Instance Details service from a Heritage Process Portal process app is no longer automatically used as the Default Instance Details UI service. However, you can manually customize your own Default Instance Details UI service and then use the default-instance-details-ui setting in the 100Custom.xml files to configure the service on Workflow Server and Workflow Center.
- Configuring Process Portal notification and refresh behavior

In nonfederated environments, Process Portal uses CometD web messaging to push notifications and data refreshes to users when relevant events happen in the system. You can configure notification and refresh behavior by updating settings in the 100Custom.xml configuration file.
- Tuning authorization performance for Process Portal

Authorization for many actions in REST API-based clients, such as Process Portal, is determined by the security groups and teams that a user belongs to. If users belong to many (thousands of) security groups and teams, they might experience performance issues because of frequent authorization lookups. You can improve the performance in such situations by restricting authorization lookups to the groups and teams that are relevant in a specific context.
- Configuring the default duration for projected path discovery in Process Portal

There are several routes, or paths, that can be followed to complete a process instance. If projected path management is enabled for a BPD, the Gantt chart in Process Portal can display the projected path for an instance if distinct paths from the start to end nodes are found. You can configure the default time that Process Portal can take to discover the projected path.
- Disabling the display of time tracking information in Process Portal

By default, time tracking information is displayed for individuals listed on the Experts tab on the task details page in Process Portal.
- Opening services in Heritage Process Portal in a new browser window (deprecated)

By default, services, such as tasks and startable services, are opened in the Heritage Process Portal browser window. You can change the browser behavior by setting the launch-in-new-window-enabled property in the 100custom.xml configuration file.
- Setting the default locale

The locale that your work portal, Workplace or Process Portal, applies when the user has set no preference is the locale of the Java virtual machine (JVM). By changing the JVM locale, you change the default locale.