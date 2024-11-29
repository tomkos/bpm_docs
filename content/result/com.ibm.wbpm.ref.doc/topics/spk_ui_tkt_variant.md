# Variant

## Configuration properties

Under
Configuration, set or modify the behavior properties for the view.

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                           | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Auto select control               | The control used is automatically selected, based on the data binding type. Use Auto select only when the Initial control index is not provided. If there is a value specified for the Initial control index, auto select is ignored, even if it is enabled.                          | Boolean     |
| Initial control index             | Determines the initial control to display. This expression returns a 0-based index that corresponds to the control that is shown by default. For example, if the control index is 0, the control in the first tab is shown . If the control index is 1, then the second tab is shown. | String      |

## Events

- On load: Activated when the Variant control is loaded, for
exampleme.reset()
- On change: Activated when a change is detected., for
exampleconsole.log(me.getValue())

## Methods

For detailed information about the available methods for Variant, see the Variant JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.