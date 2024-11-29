# Team Summary

- TeamTaskSummary[] tw.system.retrieveTeamSummaries (searchFilter,
checkAuthorization)
- TeamTaskSummary Team.dashboard.retrieveTeamSummary (searchFilter,
checkAuthorization)

| Binding                           | Description                            |
|-----------------------------------|----------------------------------------|
| teamSummaryData (TeamTaskSummary) | Returns task information for a team ID |

| Instance configuration label   | Description                                                                                                         | Definition configuration option                      | Default value                        |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|--------------------------------------|
| Localization Service           | The service that is used to retrieve the localized strings that are used with this Coach View                       | localizationService (dashboards Localized  Messages) | Dashboards Localized Messages Loader |
| Lock Control In Expanded Mode  | Whether the control should be initialized and locked in the Expanded setting (true) with descriptions fully visible | lockExpanded (Boolean)                               | False (not selected)                 |
| Custom Theme                   | A custom theme to use instead of the default Business Automation Workflow theme                                     | customTheme (String)                                 | False (not selected)                 |

This view does not use the visibility property.

To enable navigation actions for the view in a custom
dashboard, also add the Navigation Controller control to the custom
dashboard. For more information, see Navigation Controller control.