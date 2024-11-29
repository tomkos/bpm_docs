# Tasks Due

The view uses CometD web messaging to automatically refresh
the contents of the view. For more information, see Configuring notification and refresh behavior.

## Restrictions and limitations

- This view does not use the visibility property.
- In some situations, the system administrator
might disable cometD web messaging. If you use this view in a custom
dashboard, ensure that the dashboard contains an alternative refresh
mechanism, such as Refresh Controller or Refresh Button. For more
information, see Refresh Controller control and Refresh Button control.

## Configuration properties

Set or modify view configuration
in the Configuration properties tab.

| Configuration property   | Property variable             | Description                                                                                                                                                                                                             |
|--------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Team ID                  | teamId                        | Filters the tasks due data that is retrieved from the back end based on the team ID. When no value is specified, data is retrieved for all teams that are associated with the current user.Default: None                |
| User ID                  | userId                        | Filters the tasks due data that is retrieved from the back end based on the user ID. When no value is specified and no Team ID is specified, data is retrieved for all tasks assigned to the current user.Default: None |
| List scope               | listScope                     | Filters the scope of tasks due data that is retrieved from the back end based on whether a task is open, completed, that are assigned, or unassigned.Default: Open Tasks                                                |
| Search filter            | searchFilter                  | Filters the tasks due data that is retrieved from the back end based on the search string that is specified.Default: None                                                                                               |
| Selected range           | selectedRange                 | Shows only the tasks that are due between the specified start date and end date. This option is overwritten at run time by the selection that the user makes.                                                           |
| Fire event on selection  | fireEventOnSelection          | Generates a boundary event during run time when the user makes a selectionDefault: False (not selected)                                                                                                                 |
| Retrieve task due data   | retrieveTaskDueSummaryService | The service that is used to retrieve data from the back end for the tasks due histogramDefault: Default Tasks Due Service                                                                                               |
| Localization Service     | localizationService           | The service that is used to retrieve the localized strings for use with this coach view.Default: Dashboards Localized Messages Loader                                                                                   |

## Configuring the Tasks Due control

You can
use the Team ID,  User ID,
and List scope configuration options together
in various combinations to filter the tasks due data.