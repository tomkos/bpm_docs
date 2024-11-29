# Timer

In an implementation where the timer has a boundary event attached to it and ends with a
stay-on-page event, the timer can also be activated upon reaching the stay-on-page event after the
boundary event is emitted.

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

| Configuration property   | Description                                                                                                                             | Data type   |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Timeout value (ms)       | Specifies the time interval (in milliseconds) before the timer is activated.                                                            | Integer     |
| Repeatable               | Specifies whether the timer is triggered repeatedly for the specified timeout interval.                                                 | Boolean     |
| Initially stopped        | When selected, this option specifies that the timer does not start running until you specifically start it by using the start() method. | Boolean     |

## Events

- On timeout: Activated at timeout. If set to
Repeatable, this event handler is triggered multiple times. For
example:${CounterDisplay}.setText(me.getTicks())
- On boundary event: Activated upon reaching a stay-on-page event after a
boundary event is emitted by the Timer view. For example:
alert("Stay on Page status '" + status + "'")For
more information, see the context.trigger() method in the The coach view context object topic.

## Methods

For detailed information on the available methods for Timer, see the Timer JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.