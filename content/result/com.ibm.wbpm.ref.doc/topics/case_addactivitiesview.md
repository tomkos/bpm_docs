# Add Activities

1. Click Add Activity.
2. Select the type of discretionary activity that you want to add.
3. Specify a name for this activity that you and others who must work on this activity can
understand.
4. Click OK.

## Configuration properties

| Property                    | Description                                                                                                    | Data type   |
|-----------------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| Target Object Store Name    | The repository name that the view needs to connect.                                                            | String      |
| Case Identifier             | The Case Identifier of the case instance required by the view.                                                 | String      |
| Get Repository Name Service | Service to retrieve the repository name that is associated with the case activity.                             | String      |
| Appearance                  | Appearance                                                                                                     | Appearance  |
| Hide Add Activity Button    | Allows to hide the default Add Activity button from the Case Details page.                                     | Boolean     |
| Color style                 | To change the button color style.                                                                              |             |
| Shape style                 | To change the button shape style.                                                                              |             |
| Size                        | To change the button size style.                                                                               |             |
| Outline only                | To use an outline only appearance for the button.                                                              | Boolean     |
| Icon                        | To change the button appearance to an icon.                                                                    | String      |
| Width                       | To change the width of the button.                                                                             | String      |
| Icon location               | The location of the inout icon.                                                                                |             |
| Ghost style                 | To change the button appearance with no solid fill (the body of the button adopts the look of the background). | Boolean     |

## Events

You can assign the following types of event handlers to events:

Filter Add activities: Apply custom filters to discretionary
activities.

addActivitiesList is an array of objects of all discretionary activities for
current case which can be customized. Each activity array is an object of:
activityID (ID of the activity), activityDisplayName (default
display name of the activity) and state ( state of the activity).

It returns the addActivitiesList with customizable objects for discretionary
activities, each defined by activityID,

activityDisplayName (default display name of the activity) and
state (YES, NO, LOCK)

- YES - Include in the add activity list. This is the default state.
- NO - Do not include in the add activity list.
- LOCK - Include in the add activity list, but activity display name is not customizable.

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