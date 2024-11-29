# Data

## Restrictions and limitations

- This view supports only the Required, Hidden,
and None visibility properties.
- If you use this view in a custom dashboard, you
also need to add the Refresh Controller view to the custom dashboard
to enable the contents of the view to be refreshed. To enable users
to also manually refresh the contents of the view, add Refresh Button
to the dashboard, too. For more information, see Refresh Controller control and Refresh Button control.

## Configuration properties

| Configuration property   | Property variable                                   | Description                                                                                                                                                                                                                                                                                                                                        |
|--------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Height                   | height (Integer)                                    | The height of the control in pixels. When no value is specified, the height of the control is 100 pixels by default.                                                                                                                                                                                                                               |
| Instance ID              | instanceId (String)                                 | The instance to which the data belongs.Default: None                                                                                                                                                                                                                                                                                               |
| Retrieve data            | retrieveDataService (Default Retrieve Data Service) | The service that retrieves the data.Default: Default Retrieve Data Service                                                                                                                                                                                                                                                                         |
| Refresh trigger          | refreshTrigger (Boolean)                            | Enables the contents of the view to be refreshed. Bind this property to the private variable that is used by Refresh Controller, Refresh Button, or both.When the value of the bound variable changes to true, the view is refreshed. After the view is refreshed, the value of the variable returns to false. Default: false (no refresh pending) |
| Localization Service     | localizationService                                 | The service that is used to retrieve the globalized strings for use with this viewDefault: Dashboards Localized Messages Loader                                                                                                                                                                                                                    |