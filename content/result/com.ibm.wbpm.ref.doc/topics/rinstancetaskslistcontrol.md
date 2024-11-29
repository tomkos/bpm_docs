# Instance Tasks List

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

## Configuration
properties

| Configuration property         | Property variable                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Height                         | height (Integer)                                | The height of the view in pixels. If the list exceeds the specified height, a scroll bar is shown. To show the complete list without a scroll bar, enter 0.  When no value is specified, the control height is based on the style attributes of the control.Default: If the control is not positioned absolutely or has no height or max-height style settings, the height is 600 pixels.                                                                                                                                            |
| Initial list size              | initialMaxRows (Integer)                        | The initial number of tasks that are displayed in the list. When no value is specified, all the tasks are displayed.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Instance ID                    | instanceId (String)                             | The instance ID filters the list of tasks. This property is required.Default: None                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Selected category              | selectedCategory (String)                       | Displays tasks in the selected category. You can bind this property to a selection control, for example, the Category Selection control. Alternatively, you can set it to a static value so that the control always shows the same subset of tasks, for example open tasks.Default: The first entry in the list of categories that are defined for the Define selectable categories configuration property. If no selectable categories are defined, open tasks are displayed.                                                       |
| Define selectable categories   | categories (List of String)                     | Defines the set of selection categories and the order in which they appear in a user interface. A category represents a subset of tasks, for example, open tasks, and its sort criteria. Open, Completed                                                                                                                                                                                                                                                                                                                             |
| Generated selection categories | categoriesSelectionList (List of NameValuePair) | The subset of the selectable categories that you want to include in the user interface.The list is generated from the value of the Define selectable categories configuration property. It consists of name-value pair objects; the name property is the display name of the category, and the value property is the category value. You can bind this configuration property to a selection view, for example, the Category Selection view to provide tabbed selection categories at the top of the list.  Default: Open, Completed |
| Refresh trigger                | refreshTrigger (Boolean)                        | Enables the contents of the view to be refreshed. Bind this property to the private variable that is used by Refresh Controller, Refresh Button, or both.When the value of the bound variable changes to true, the view is refreshed. After the view is refreshed, the value of the variable returns to false. Default: false (no refresh pending)                                                                                                                                                                                   |
| Retrieve task list             | retrieveTaskListService                         | The service that retrieves the task list. Default Instance Tasks List Service                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Tasks                          | tasks (TaskListItem) (List)                     | The list of tasks that are displayed. This property is read-only.Default: An empty list                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Localization Service           | localizationService                             | The service that is used to retrieve the globalized strings for use with this viewDefault: Dashboards Localized Messages Loader                                                                                                                                                                                                                                                                                                                                                                                                      |

## Predefined categories

The following table
shows how the predefined categories map to task states.

| Category   | Description                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------|
| Open       | Shows the tasks that can be worked on. These tasks are in either the NEW state or the RECEIVED state. |
| Completed  | Shows the completed tasks. These tasks are in the CLOSED state.                                       |

The predefined categories are implemented with
the getPredefinedCategories JavaScript method.
To view the implementation, in Process Designer, on
the Behavior tab for the view, select Inline
JavaScript.

## Customizing the Instance Tasks List coach view

- Extend the Instance Task List coach view to include selection
categories for filtering the tasks that are shown in the view, for
example, to show open tasks. The selectedCategory and categorySelectionList properties
can be bound to a selection control, for example, the Category Selection
control.
- Overwrite the default Instance Tasks List Service, for example,
to modify the query result
- Modify resource strings in the Localization Service resource file,
for example, to change the labels of the selection categories
- Modify the style settings in the .css file
-