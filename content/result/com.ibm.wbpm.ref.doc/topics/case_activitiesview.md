# Case Activities

When the Case Activities view is used in the context of the process user task page, the view
configures itself based on the parent case, without specifying the case identifier and  target
object store name in the view’s configuration. You can add new discretionary activities for workflow
process activities. For process activities, you can view the instance by using the view process
action.

Each Case Activity can be expanded to list out the configured system information and business
information (maximum 20 data). You can see View Process for process
activities.

## Configuration properties

| Property                    | Description                                                                                                          | Data type   |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------|-------------|
| Case Identifier             | The Case Identifier of the case instance as required by the view.                                                    | String      |
| Target Object Store Name    | The repository name that the view needs to connect.                                                                  | String      |
| Edit title                  | To edit the title of this view.                                                                                      | Any         |
| Hide title                  | To hide the title as an option.                                                                                      | Any         |
| Get Repository Name Service | Service to retrieve the repository name that is associated with the case activity.                                   | String      |
| Initial Size                | Initial number of table rows to display.                                                                             | Integer     |
| Show Footer                 | Show or hide the footer. The footer is also displayed if any of the footer views are enabled, for example, Show Add. | Boolean     |
| Hide Add Activity Button    | To hide the default Add Activity button from the Case Details page.                                                  | Boolean     |

## Events

You can assign the following types of event handlers to events:

Filter Add activities: Apply custom filtering to discretionary activities.

addActivitiesList is an array of objects of all discretionary activities for
current case, which can be customized. Each activity array is an object of:
activityID (ID of the activity), activityDisplayName (default
display name of the activity), and state (state of the activity).

- YES - Include in the add activity list. This is the default state.
- NO - Do not include in the add activity list.
- LOCK - Include in the add activity list, but the activity display name is not customizable.

```
var customizedAddActivityList=addActivitiesList;
customizedAddActivityList.forEach(function(discretionaryActivity){
        if (discretionaryActivity.activityID =="SolnID\_Activity1"){
                discretionaryActivity.state= "NO"; 
        }
        else if (discretionaryActivity.activityID =="SolnID\_Activity2"){
                 discretionaryActivity.state= "LOCK";
                 discretionaryActivity.activityDisplayName= "New Activity Name";
        }
});
return customizedAddActivityList;
```

Filter Activities List: Apply custom filtering to the activities.

activitiesList is an array of objects of all activities for current case, which
can be customized. Each activity array is an object of: activityID (ID of the
activity), and state (state of the activity).

- YES - Include in the activity list. This is the default state.
- NO - Do not include in the activity list.

This is triggered when applying custom filtering to the activities. This event itself is the
handler for custom filtering. There are no other custom filtering options.

```
var customizedActivityList=activitiesList;
customizedActivityList.forEach(function(activity){ 
       if (activity.activityID =="SolnID\_Activity1"){
             activity.state= "NO";
       }
       else if (activity.activityID =="SolnID\_Activity2"){
             activity.state= "NO";
       }
}); 
return customizedActivityList;
```