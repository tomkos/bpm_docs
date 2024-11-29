# Navigation event

The Navigation event view cannot be used by itself. It must be used in combination with other
views.

## Configuration properties

Under
Configuration, set or modify the behavior properties for the view.

The behavior configuration properties for the Navigation event view are shown in the following
table:

| Behavior configuration property   | Description                             | Data type    |
|-----------------------------------|-----------------------------------------|--------------|
| Event data                        | Data to pass into the navigation event. | String(list) |

## Example

In this example, the Navigation event view is used with two Text views inside Panel sections.

The Text views use the fire and confirmAndFire methods to
control the Navigation event:

- The On change event handler of the first Text view is set to
if(me.getText() = = "EXIT") ${NavigationEvent1}.fire().
- The On change event handler of the second Text view is set to
if(me.getText() = = "EXIT") ${NavigationEvent1}.confirmAndFire("Are you sure you want to
exit?").

- Typing Exit in the first text box ends the service.
- Typing Exit in the second text box returns an alert because of the
confirmAndFire method.

## Events

- On load: Activated when the page loads.
- On trigger: Activated when a Trigger event is fired, but if this Trigger
event explicitly returns false, the On trigger event will not
be fired.
- On boundary: Activated when there is a Boundary event. If the Boundary
event ends with a Stay-on-page event, the On boundary event is not fired until
all asynchronous processes associated with the Boundary event are complete.

Depending
on the specific event, you can use JavaScript logic to modify the effects of the
view.

## Methods

For detailed information on the available methods for Navigation event, see the Navigation event JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.