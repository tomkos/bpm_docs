# Gantt Chart Process Overview

The instance completion and termination statistics used
to create the chart are generated by business process definitions
(BPDs).

| Binding                                     | Description                                                           |
|---------------------------------------------|-----------------------------------------------------------------------|
| ProcessData (GanttChartProcessOverviewData) | Contains the process name and ID, task data, and the average duration |

| Instance configuration label   | Description                                                                                                                                                                                           | Definition configuration option                     | Default value                        |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------|
| Localization Service           | The service that is used to retrieve the localized strings for use with this Coach View                                                                                                               | localizationService (dashboards Localized Messages) | Dashboards Localized Messages Loader |
| Chart refresh                  | Refreshes the chartTypically, you would update the variable that this chart is bound to before refreshing the chart to display the updated data. After the refresh, this option resets to deselected. | triggerChartReset (Boolean)                         | False (not selected)                 |