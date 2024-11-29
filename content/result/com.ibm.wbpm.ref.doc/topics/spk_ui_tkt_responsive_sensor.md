# Responsive sensor

## Data binding

Set or modify the data binding for the Responsive sensor view in the General
properties.

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

| Configuration property   | Description                                                                            | Data type   |
|--------------------------|----------------------------------------------------------------------------------------|-------------|
| name                     | The name of the box factor, which responsive horizontal and vertical layouts refer to. | String      |
| withUpTo                 | The maximum width this box factor applies to.                                          | Integer     |

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

- On load: Activated when the view loads, for example
me.refreshLayout()
- On selected: Activated when the view hits a Box Factor boundary, for
example console.log(event.boxFactor)

## Methods

For detailed information about the available methods for Responsive sensor, see the Responsive sensor JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.