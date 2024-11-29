# Team Roster

The coach view uses CometD web messaging to
refresh the online availability of team members. Task counts are refreshed
indirectly through CometD notifications in the Task List control.
For more information, see tadm\_portal\_config\_notifications.

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

## Data binding

| Description     | Data type                      |
|-----------------|--------------------------------|
| A list of users | users (TeamRosterEntry) (List) |

## Configuration properties

Set or modify view configuration
in the Configuration properties tab.

| Configuration property   | Property variable                                   | Description                                                                                                                                                                                                         |
|--------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title                    | title (String)                                      | The title that is displayed for the coach view.Default: If no value is specified, the default title is Roster.                                                                                                      |
| Priority team members    | filteredMembers (UserInfo) (List)                   | The team members that are displayed at the top of the roster.Default: None                                                                                                                                          |
| Team ID                  | teamId (String)                                     | The ID of the team that facilitates dashboard page navigation so that the user can view or return to the page of the specified team.Default: None                                                                   |
| Height                   | height (Integer)                                    | The height of the list in pixels.Default: When no value is specified, the default height is 600 pixels.                                                                                                             |
| Localization Service     | localizationService (dashboards Localized Messages) | The service that is used to retrieve the localized strings for use with this coach view.Default: Dashboards Localized Messages Loader                                                                               |
| Retrieve team data       | retrieveTeamMember                                  | The service that refreshes task data for members of the specified team ID. If no value is specified for Team ID, task data refreshes only when the page is refreshed.Default: Default Team Member Retrieval Service |