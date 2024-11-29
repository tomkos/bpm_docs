# Deferred section

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

| Configuration property   | Description                                                                                                 | Data type   |
|--------------------------|-------------------------------------------------------------------------------------------------------------|-------------|
| Lazy-load automatically  | Specifies whether the section is automatically loaded lazily after the specified delay has passed.          | Boolean     |
| Delay for auto-loading   | Specifies the time interval (in milliseconds) during which the automatic loading of the section is delayed. | Integer     |

## Events

- OnLazyLoad: Activated when the lazy load is complete. For example:
alert("Lazy load complete")

Depending on the specific event, you can use JavaScript logic to modify the effects of
the view.

## Methods

For detailed information on the available methods for Deferred section, see the Deferred section JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.