# Instance Activities List

The view uses CometD web messaging to automatically refresh
the contents of the view. For more information, see Configuring notification and refresh behavior.

## Restrictions and limitations

- This view supports only the Required, Hidden,
and None visibility properties.
- To enable navigation actions for the view in a custom
dashboard, also add the Navigation Controller control to the custom
dashboard. For more information, see Navigation Controller control.
- In some situations, the system administrator
might disable cometD web messaging. If you use this view in a custom
dashboard, ensure that the dashboard contains an alternative refresh
mechanism, such as Refresh Controller or Refresh Button. For more
information, see Refresh Controller control and Refresh Button control.

## Configuration properties

| Configuration property          | Property variable                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Height                          | height (Integer)                                     | The height of the view in pixels. If the list exceeds the specified height, a scroll bar is shown. To show the complete list without a scroll bar, enter 0. Default: When no value is specified, the height of the control is 600 pixels.                                                                                                                                                                                                                                                                                                              |
| Instance ID                     | instanceId (String)                                  | The instance ID filters the list of activities. This property is required.Default: None                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Selected category               | selectedCategory (String)                            | Displays activities in the selected category. You can bind this property to a selection control, for example, the Category Selection control. Alternatively, you can set it to a static value so that the control always shows the same subset of activities, for example, all activities.Default: The first entry in the list of categories that are defined for the Define selectable categories configuration property. If no selectable categories are defined, ready activities are displayed.                                                    |
| Define selectable categories    | categories (List of String)                          | Defines the set of selection categories and the order in which they appear in a user interface. A category represents a subset of activities, for example, ready activities, and its sort criteria. The categories can be a combination of predefined and user-defined categories.  Default: Ready, InProgress, Completed, All                                                                                                                                                                                                                         |
| User-defined categories         | userDefinedCategories (List of ActivityListCategory) | A list of user-defined categories. The names of these categories must be unique and not one of the predefined category names: Ready, InProgress, Completed, or All.Default: None                                                                                                                                                                                                                                                                                                                                                                       |
| Generated selection categories  | categoriesSelectionList (List of NameValuePair)      | The subset of the selectable categories that you want to include in the user interface.The list is generated from the value of the Define selectable categories configuration property. It consists of name-value pair objects; the name property is the display name of the category, and the value property is the category value. You can bind this configuration property to a selection view, for example, the Category Selection view to provide tabbed selection categories at the top of the list.  Default: Ready, InProgress, Completed, All |
| Text filter                     | textFilter (String)                                  | Filters the activity list by activity name based on the text that is entered by the user. Default: None                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Refresh trigger                 | refreshTrigger (Boolean)                             | Enables the contents of the view to be refreshed. Bind this property to the private variable that is used by Refresh Controller, Refresh Button, or both.When the value of the bound variable changes to true, the view is refreshed. After the view is refreshed, the value of the variable returns to false. Default: false (no refresh pending)                                                                                                                                                                                                     |
| Retrieve activities             | retrieveActivityListService                          | The service that retrieves the list of activities. Default: Default Instance Activities List Service                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Activities                      | activities (List of ActivityListItem)                | The list of activities that are displayed. This configuration property is read-only.Default: None                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Retrieve details of an activity | retrieveActivityDetailsService                       | The service that retrieves the details of an activity. Default: Default Activity Details Service                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Execute action on activity      | activityActionService                                | The service that executes an action on an activity. Default: Default Activity Action Service                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Localization Service            | localizationService                                  | The service that is used to retrieve the globalized strings for use with this viewDashboards Localized Messages Loader                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Predefined categories

The following table
shows how the predefined categories map to activity states.

| Category    | Description                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------|
| Ready       | Shows the activities that can be started. These activities are in either the READY state or the WAITING state.    |
| In Progress | Shows the activities that are in progress. These activities are in either the WORKING state or the WAITING state. |
| Completed   | Shows the activities that are in any of the following end states: COMPLETED, FAILED, or SKIPPED.                  |
| All         | Shows the activities in any of the following states: READY, WAITING, WORKING, COMPLETED, FAILED, or SKIPPED       |

The predefined categories are implemented with
the getPredefinedCategories JavaScript method.
To view the implementation, in Process Designer, on
the Behavior tab for the view, select Inline
JavaScript.

## Customizing the Instance Activities List
coach view

- Customize the categories that are used for filtering activities
by changing the values of the corresponding configuration properties.
For more information, see Customizing categories.
- Overwrite the default services that are provided by the control.
    - Instance Activities List Service: modify the query properties,
for example, sortCriteria, filters, includeHidden properties,
or modify the query result, for example, to remove available actions
    - Activity Details Service: for example, to modify the narrative
    - Activity Action Service: for example, to trigger other actions,
such as notifications or updating data
- Modify resource strings in the Localization Service resource file,
for example, to change the labels of the selection categories
- Modify the style settings in the .css file

## Customizing categories

```
// Define categories to be available
tw.local.categories = new tw.object.listOf.String();
tw.local.categories[0] = "Ready";
tw.local.categories[1] = "Completed";
tw.local.categories[2] = "All";
```

```
tw.local.userDefinedCategories = new tw.object.listOf.ActivityListCategory();

// define a user-defined category to replace the predefined ready category, no waiting activies
tw.local.userDefinedCategories[0] = new tw.object.ActivityListCategory();
tw.local.userDefinedCategories[0].name = "ReadyOnly"; 
tw.local.userDefinedCategories[0].label = tw.resource.MyResource.category.ready;
tw.local.userDefinedCategories[0].sortCriteria = new tw.object.listOf.String();
tw.local.userDefinedCategories[0].sortCriteria[0] = "NAME\_ASC";
tw.local.userDefinedCategories[0].filters = new tw.object.listOf.ActivityListFilter();
tw.local.userDefinedCategories[0].filters[0] = new tw.object.ActivityListFilter();
tw.local.userDefinedCategories[0].filters[0].executionStateFilter = new tw.object.listOf.String();
tw.local.userDefinedCategories[0].filters[0].executionStateFilter[0] = "READY";
tw.local.userDefinedCategories[0].filters[0].activityTypeFilter = new tw.object.listOf.String();
tw.local.userDefinedCategories[0].filters[0].executionTypeFilter = new tw.object.listOf.String();
tw.local.userDefinedCategories[0].filters[0].executionTypeFilter[0] = "MANUAL";
tw.local.userDefinedCategories[0].filters[0].optionTypeFilter = new tw.object.listOf.String();

// define a new user-defined category for waiting activities
tw.local.userDefinedCategories[1] = new tw.object.ActivityListCategory();
tw.local.userDefinedCategories[1].name = "Waiting";
tw.local.userDefinedCategories[1].label = tw.resource.MyResource.category.waiting;
tw.local.userDefinedCategories[1].sortCriteria = new tw.object.listOf.String();
tw.local.userDefinedCategories[1].sortCriteria[0] = "NAME\_ASC";
tw.local.userDefinedCategories[1].filters = new tw.object.listOf.ActivityListFilter();
tw.local.userDefinedCategories[1].filters[0] = new tw.object.ActivityListFilter();
tw.local.userDefinedCategories[1].filters[0].executionStateFilter = new tw.object.listOf.String();
tw.local.userDefinedCategories[1].filters[0].executionStateFilter[0] = "WAITING";
tw.local.userDefinedCategories[1].filters[0].activityTypeFilter = new tw.object.listOf.String();
tw.local.userDefinedCategories[1].filters[0].executionTypeFilter = new tw.object.listOf.String();
tw.local.userDefinedCategories[1].filters[0].executionTypeFilter[0] = "MANUAL";
tw.local.userDefinedCategories[1].filters[0].optionTypeFilter = new tw.object.listOf.String();

// Define categories to be available
tw.local.categories = new tw.object.listOf.String();
tw.local.categories[0] = "ReadyOnly"; // user-defined
tw.local.categories[1] = "Waiting"; // user-defined
tw.local.categories[2] = "All"; // predefined

// Define initially selected category
tw.local.selectedCategory = "All";
```