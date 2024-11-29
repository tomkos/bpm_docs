# Instance Summary Section

- Timeline control. A graphical view of the general progress of
the instance
- Stream indicator control. A graphical representation of the comments
and documents that are posted for the instance
- Status control. Shows the current status of the instance.

The coach view uses CometD web messaging to refresh the
online availability of team members that are shown in this section.
 For more information, see tadm\_portal\_config\_notifications.

## Restrictions and limitations

- This view supports only the Required, Hidden,
and None visibility properties.
- In some situations, the system administrator
might disable cometD web messaging. If you use this view in a custom
dashboard, ensure that the dashboard contains an alternative refresh
mechanism, such as Refresh Controller or Refresh Button. For more
information, see Refresh Controller control and Refresh Button control. Also add
a Service Controller control to handle boundary events.

- Document attachments can be posted only for process instances.

## Data binding

| Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Data type       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Contains the objects that represent the data that is shown in the instance summary, for example, the due date and the status of the instance. You can bind the control to the Instance Summary business object. You can use the Default Instance Details Initialization Service in the Dashboards toolkit as an example of how to retrieve and refresh the Instance Summary business object If you add this control to a coach view that contains the Refresh Controller control, the Refresh Button control, or both also add the Service Controller control to trigger the boundary events to call the Ajax service to refresh the data. | instanceSummary |

## Configuration properties

| Configuration property   | Property variable   | Description                                                                                                                     |
|--------------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Localization Service     | localizationService | The service that is used to retrieve the globalized strings for use with this viewDefault: Dashboards Localized Messages Loader |
| Current Date             | currentDate (Date)  | This property is used to determine the current position on the timelineDefault: None                                            |