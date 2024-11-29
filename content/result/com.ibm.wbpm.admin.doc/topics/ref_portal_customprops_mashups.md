# Configuring mashup custom properties

In environments that use a database earlier than PostgreSQL (for example DB2, Oracle) or in
Liberty or Cloud environments, you can configure the following mashup properties. You can add the
custom properties either to the administrative console or to 100Custom.xml
(Liberty and Cloud environments).

1. In the administrative console, go to Resources >  Resource Environment > Resource Environment Providers > Mashups\_ConfigService > Custom properties.
2. Add the appropriate custom property.
3. For your changes to property values to take effect, update the
Mashups\_ConfigService provider, synchronize the nodes, and then restart the
nodes.  For more information, see Administering deployment environments.

See also Creating localization resources and Setting the Process Portal default locale.

```
com.ibm.bpm.portal.autoRefreshDelay={millisecond refresh period}
```

- Work
- Processes
- Process Performance
- Team Performance

For more information about setting the dashboards order in the Process Admin
Console, see Setting the Process Portal tab order for a user group.

```
/tasks/queries?query=query\_name
```

```
/tasks/queries?query=My%20Saved%20Search%201
```

```
/dashboards?dashboard=human\_service\_name
```

```
/dashboards?dashboard=https%3A%2F%2Fmycompany.com%3A9443%2Fteamworks%2FexecuteServiceByName
%3FprocessApp%3DTWP%26serviceName%3DTeam%2BPerformance%26snapshot%3Dtest1
```

```
/rest/bpm/wle/v1/exposed?avoidBasicAuthChallenge=true&includeServiceSubtypes=startable\_service,dashboard,scoreboard
```

```
https://<hostname>:<port\_number>/teamworks/executecf?modelID=1.fd478df8-2585-4b9a-a015-d4c3e59a53e8%26branchID%3D2063.98c45224-263e-4978-8fc0-5343b30f0fb6%26zResumable=true
```

```
/dashboards?dashboard=https//<hostname>:<port\_number>/teamworks/executecf?modelID=1.fd478df8-2585-4b9a-a015-d4c3e59a53e8%26branchID%3D2063.98c45224-263e-4978-8fc0-5343b30f0fb6%26zResumable=true
```

- com.ibm.bpm.portal.restrictModifyTask
- com.ibm.bpm.portal.restrictModifyTask.reassign
- com.ibm.bpm.portal.restrictModifyTask.due
- com.ibm.bpm.portal.restrictModifyTask.priority
- com.ibm.bpm.portal.hideWorkDashboard

- If the user sets a value that is not strictly positive (such as characters or a negative value),
the count value defaults to 25.
- If the user sets a positive value from 0 to 9, the count value defaults to
10.

- The strategy property defines a lazy loading policy: savedsearches other than the favorite ones are not displayed immediately but only when the user clicksShow More . This property can take the following values:
    - incremental is the default value: each click on Show
More displays the additional number of saved searches that is defined by the value of
the count parameter. If the list contains more elements than the
count value, the user must click Show More again to
display the next ones.
    - The full value loads the complete list of elements to display when the user
clicks Show More.
    - The preload value loads the complete list of elements for immediate display,
without waiting for the user to click Show More. This value reflects the
previous default behavior and is not recommended because it reduces display performance.

- If a task has a custom web-based user interface that is based on an external implementation, it
always opens in a new browser window regardless of the value of this custom property.
- When the disableOpenInNewWindows property is set to true, it
overrides the openTaskInNewWindow property.

- If the property is set to all, the logout behavior applies to all users.
- If the property is set to a comma-separated list of user groups, the logout behavior applies to
all the users who belong to that group.

- If the showNextTaskDashboard property is set to all, the
Next Task dashboard is shown to all users.
- To allow only some users to display the dashboard, set the property to a comma-separated list of
user groups.

1. Click New and add the
com.ibm.bpm.social.enableDeferNewWindowOpen property.
2. Set the property to true.
3. Keep the default java.lang.String type.
4. Click OK, and then click Save.
5. Stop and restart the entire environment, including cluster members, node agents, and the
deployment manager for a network deployment environment.

For more information about designing resumable services, see Enabling resumable services.

For mashup properties that are specific to Heritage Process Portal, which is deprecated,
see the Heritage Process Portal
custom properties section in the Process Portal mashup custom
properties topic.