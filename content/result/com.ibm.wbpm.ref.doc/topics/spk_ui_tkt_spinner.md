# Spinner

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

The appearance configuration properties for the Spinner view are shown in the following
table:

| Appearance configuration property   | Description                         | Data type   |
|-------------------------------------|-------------------------------------|-------------|
| Size                                | The size of the spinning indicator. | String      |

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

The Spinner view has the following types of event handlers:

- On close: Activated when the spinner window is closed. For example:
${Output\_Text1}.setText("Document has finished loading");where
Output\_Text1 is the control ID of the output text.
- On show: Activated when the spinner window is opened. For
example:me.setLabel("Loading document...");
- On load: Activated when the page loads. For example:
me.show();

## Methods

For detailed information on the available methods for the Spinner view, see the Spinner JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.