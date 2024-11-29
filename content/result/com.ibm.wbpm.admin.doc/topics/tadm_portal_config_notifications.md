# Configuring Process Portal notification and
refresh behavior

## About this task

| Type                             | Behavior when enabled="true"                                                                                                               |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| NOTIFY\_TASK\_RESOURCE\_ASSIGNED    | Notifications are sent to users when tasks are assigned to them as individuals or when tasks are assigned to the team that they belong to. |
| NOTIFY\_TASK\_COLLABORATION\_INVITE | Heritage Process Portal only. Users receive notifications when they are invited to attend a collaboration session.                         |
| NOTIFY\_PROCESS\_COMMENT\_TAGGED    | Notifications are sent to users who are mentioned in comments that are posted to process instances.                                        |

| Type                            | Behavior when enabled="true"                                                                                                                               |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TASKLIST\_TASK\_RESOURCE\_ASSIGNED | Task data in the Work dashboard, Team Performance dashboard, and the instance details UI is refreshed when a task is assigned to an individual or a group. |
| TASKLIST\_TASK\_FIELD\_CHANGED     | Task data in the Work dashboard, Team Performance dashboard, and the instance details UI is refreshed when a task is changed.                              |

- No task data refreshes that are controlled by task list subscriptions occur, for example, the
Work dashboard does not refresh.
- No task assignment  or post notifications are sent.
- The user profile does not contain any notifications settings.

```
<server>
   <web-messaging-push merge="replace" match="elementName" enabled="true">
      <web-messaging type="NOTIFY\_TASK\_RESOURCE\_ASSIGNED" enabled="true"/>
      <web-messaging type="NOTIFY\_TASK\_COLLABORATION\_INVITE" enabled="true"/>
      <web-messaging type="NOTIFY\_PROCESS\_COMMENT\_TAGGED" enabled="true"/>
      <web-messaging type="TASKLIST\_TASK\_RESOURCE\_ASSIGNED" enabled="true"/>
      <web-messaging type="TASKLIST\_TASK\_FIELD\_CHANGED" enabled="true"/>
   </web-messaging-push>
</server>
```

For information about making and deploying 100Custom.xml configuration
changes, see Creating a 100Custom.xml configuration file.