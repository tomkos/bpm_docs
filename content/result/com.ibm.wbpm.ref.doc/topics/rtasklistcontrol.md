# Task List

The view uses CometD web messaging to automatically refresh
the contents of the view. For more information, see Configuring notification and refresh behavior.

## Restrictions and limitations

- This view does not use the visibility property.
- To enable navigation actions for the view in a custom
dashboard, also add the Navigation Controller control to the custom
dashboard. For more information, see Navigation Controller control.
- In some situations, the system administrator
might disable cometD web messaging. If you use this view in a custom
dashboard, ensure that the dashboard contains an alternative refresh
mechanism, such as Refresh Controller or Refresh Button. For more
information, see Refresh Controller control and Refresh Button control.

## Configuration properties

Set or modify view configuration
in the Configuration properties tab.

| Configuration property   | Property variable                                   | Description                                                                                                                                                                                                                                                                                                                   |
|--------------------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Height                   | height (Integer)                                    | The height of the control in pixels. If the task list exceeds the specified height, a scroll bar is shown. To show the complete task list without a scroll bar, enter 0. Default: When no value is specified, the control height is 600 pixels.                                                                               |
| Initial list size        | initialMaxRows (Integer)                            | The initial number of tasks that are displayed in the list.Default: When no value is specified, 25 tasks are displayed.                                                                                                                                                                                                       |
| Team ID                  | teamId (String)                                     | Filters the task list based on the team ID. When no value is specified, the tasks for all teams are displayed.Default: None                                                                                                                                                                                                   |
| User ID                  | userId (String)                                     | Filters the task list based on the user ID. When no value is specified and no Team ID is specified, all the tasks for the current user are displayed.Default: None                                                                                                                                                            |
| List scope               | listScope (TaskListScope)                           | The scope of the tasks that are displayed to be open, completed, assigned, or unassigned. This option works with the Team ID and User ID options. For examples of how the options can work together to produce different combinations of scoped views, see the Configuring the Task List control section. Default: Open Tasks |
| Include assigned users   | includeAssignedUsers (Boolean)                      | Enables the data binding to contain a list of users that have tasks assigned in the task list resultsDefault: None                                                                                                                                                                                                            |
| Filter by due range      | dueSlice (DateRange)                                | Shows only the tasks that are due between the specified start date and end date. To show all tasks that are due up to or after a specified date, leave the start date or end date blank.Default: None                                                                                                                         |
| Search filter            | searchFilter (String)                               | Shows only the tasks that match the specified search criteria.Default: None                                                                                                                                                                                                                                                   |
| Retrieve task list       | retrieveTaskListService (Default Task List Service) | The service that retrieves the task list.Default: Default Task List Service                                                                                                                                                                                                                                                   |
| Expand all rows          | expandAllRows (Boolean)                             | Provides a toggle option for the user to display or hide task details in all rows.Default: False (not selected)                                                                                                                                                                                                               |
| Assigned users           | assignedUsers (UserInfo) (List)                     | The list of users that have assigned tasks in the task list. This is a read-only option.Default: None                                                                                                                                                                                                                         |
| Tasks                    | tasks (TaskListItem) (List)                         | The list of tasks currently that are displayed. This is a read-only option.Default: None                                                                                                                                                                                                                                      |

## Configuring the Task List control

- Current user view (default) - When both Team ID and  User
ID options are blank, the list shows unassigned
tasks for all teams of the current user and all tasks that are assigned
to the current user.
- Team view - When a value for Team ID is specified and User
ID is blank, the list shows unassigned tasks for the specified team and
tasks that are assigned to all users of the team.Note: You must be a team manager to see the tasks
that are assigned to all users of the team.
- Team member view - When values are specified for both Team
ID and  User ID, the list shows
all unassigned tasks for the specified team and the associated team
tasks that are assigned to the specified user.
- Individual user view - When Team ID is
blank and a  User ID is specified, the list
shows unassigned tasks for the associated teams of the specified user
and tasks that are assigned to the specified user. Only tasks from
teams that the current user manages are shown.