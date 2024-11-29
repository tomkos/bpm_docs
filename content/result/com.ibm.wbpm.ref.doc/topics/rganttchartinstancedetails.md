# Gantt Chart Instance Details

| Binding                                     | Description                                                                           |
|---------------------------------------------|---------------------------------------------------------------------------------------|
| ProcessData (GanttChartInstanceDetailsData) | Contains process instance data, such as the process name and ID, start date, due date |

| Instance configuration label   | Description                                                                                                                                                                                      | Definition configuration option                     | Default value                        |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------|
| Show task details              | This option is used internally.                                                                                                                                                                  | showDialog (Boolean)                                | False (not selected)                 |
| Update service                 | The service that saves data input and persists changes to the back end                                                                                                                           | saveService                                         | Default Instance Gantt Save Service  |
| Unsaved Changes                | Detects when the chart contains changes that have not been saved. When creating a Coach View, this option must be enabled if not bound to a private variable in the containing service.          | hasPendingChanges (Boolean)                         | False (not selected)                 |
| Save changes                   | Persists changes made to the chart. When creating a Coach View, this option must be enabled if not bound to a private variable in the containing service.                                        | triggerSaveCall (Boolean)                           | False (not selected)                 |
| Chart reset                    | Resets changes made to the chart by reloading information from the server. When creating a Coach View, this option must be enabled if not bound to a private variable in the containing service. | triggerChartReset (Boolean)                         | False (not selected)                 |
| Localization Service           | The service used to retrieve the localized strings for use with this Coach View                                                                                                                  | localizationService (dashboards Localized Messages) | Dashboards Localized Messages Loader |
| Preview service                | The service that manages server inquiries                                                                                                                                                        | WhatIfService                                       | Default Instance Gantt Data Service  |
| Calendar type                  | The date format to be to be Gregorian, Hebrew, or Islamic                                                                                                                                        | calendarType (CalendarType)                         | Gregorian                            |
| Available actions              | The list of available actions the user is authorized to perform                                                                                                                                  | availableActions (String) (List)                    | (empty list)                         |

This view does not use the visibility property.

To enable navigation actions for the view in a custom
dashboard, also add the Navigation Controller control to the custom
dashboard. For more information, see Navigation Controller control.