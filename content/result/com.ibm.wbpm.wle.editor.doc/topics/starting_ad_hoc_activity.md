# Example: Starting an unstructured (ad hoc) activity (JavaScript
API)

## Before you begin

- BPM admin
- Process/case admin
- Process/case instance owner
- Default lane team of the corresponding lane

## Procedure

To start an unstructured (ad hoc) activity, complete
the following steps.

1 Retrieve a list of matching unstructured activities andtheir IDs on a TWProcessInstance object. On the ActivityListItem object there is a list of available actions for thecurrent user (the user that executed the retrieveActivityList() call), as well asthe ID of the activity. Refer to the description of the TWProcessInstance object inJavaScript API in processes and service flows . log.info("querying for piid: " + tw.local.piid);var pi = tw.system.findProcessInstanceByID(tw.local.piid);log.info("found process instance: " + pi);var activitiyListProperties = new tw.object.ActivityListProperties();var activityListFilter = new tw.object.ActivityListFilter();activityListFilter.executionStateFilter = ["READY"];activitiyListProperties.filters = newtw.object.listOf.ActivityListFilter();activitiyListProperties.filters.insertIntoList(0, activityListFilter);log.info("querying for activity list ...");tw.local.activities = pi.retrieveActivityList(activitiyListProperties)log.info("activities found: " + tw.local.activities);tw.local.aiid = // get the id of the activity you want to start (and'actions' contains 'ACTION\_START\_ACTIVITY')
    - Set the hiddenFilter parameter to retrieve hidden activities.
    - Set the checkAuthorization parameter to true to receive only
those results that the current user is authorized to view for the process or case instance.

```
log.info("querying for piid: " + tw.local.piid);
var pi = tw.system.findProcessInstanceByID(tw.local.piid);
log.info("found process instance: " + pi);

var activitiyListProperties = new tw.object.ActivityListProperties();

var activityListFilter = new tw.object.ActivityListFilter();
activityListFilter.executionStateFilter = ["READY"];

activitiyListProperties.filters = new
tw.object.listOf.ActivityListFilter();
activitiyListProperties.filters.insertIntoList(0, activityListFilter);

log.info("querying for activity list ...");
tw.local.activities = pi.retrieveActivityList(activitiyListProperties)
log.info("activities found: " + tw.local.activities);

tw.local.aiid = // get the id of the activity you want to start (and
'actions' contains 'ACTION\_START\_ACTIVITY')
```

2. When you have the ID of the unstructured activity, use
the findActivityInstanceByID() call to retrieve the
instance of the activity. Then call start(...) to
start the instance.   Refer to the description of the TWBPDSystemNamespace object in JavaScript API in processes and service flows. The optional parameter
taskOwnerUserId reassigns the task to the specified user id. This feature works
only for unstructured activities with a user task implementation. Refer to the description of the
ActivityInstance object in JavaScript API in processes and service flows.
log.info("querying for aiid: " + tw.local.aiid);
var ai = tw.system.findActivityInstanceByID(tw.local.aiid);
log.info("starting activity with id: " + tw.local.aiid);
ai.start();