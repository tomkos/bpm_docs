# Password

## Data binding

Set or modify the data binding for the view in the General properties. The
Password view can be bound to a String variable.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                        | Data type   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the text box for the password in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed. | String      |
| Size                                | Specifies the size style for the view. The following options are available: Default Larger Small                                                                                   | String      |
| Label placement                     | Specifies the label placement for this view. The available options are Top and Left.  Note that a left placement of the label changes the specified width of the view.             | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.      | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                               | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | Specifies the tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |
| Placeholder text                  | Provides the placeholder text that is displayed when no value was entered.                                                                                                                                                                | String      |

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events. The Password view has the following
types of event handlers:

- On load: Activated when the page loads. For example:
me.setText("Some default text on load.")
- On change: Activated when the text changes. For example:
if(newText != oldText){return confirm ("Are you sure you want to change the text field?");}
- On focus: Activated when the focus moves to the text field. For example:
me.setLabelPlacement("T")
- On blur: Activated when the text field loses the focus. For example:
me.setLabelPlacement("L")
- On input: Activated when the user provides the input text. If the
expression returns false, the input is not taken. For example:
return potential.length<=10;

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for Password, see the Password JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.