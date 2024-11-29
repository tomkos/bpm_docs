# Radio button

## Data binding

Set or modify the data binding for the Radio button view in the General
properties. The view is bound to a Boolean variable.

## Configuration properties

Under
Configuration, set or modify the behavior properties for the view.

| Appearance configuration property   | Description                                                 | Data type   |
|-------------------------------------|-------------------------------------------------------------|-------------|
| Show validation marker              | Show a validation icon and border when the view is invalid. | Boolean     |

| Behavior configuration property   | Description                                                                                                                                                                                                                               | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | Specifies the tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |
| Value when selected               | Specifies the value that the binding is set to when the radio button is selected.                                                                                                                                                         | String      |
| Group name                        | Specifies the name of the group this radio button belongs to. Within the same group, only one radio button can be selected at a time, while the other buttons are clear.                                                                  | String      |

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

- On load: Activated when the page loads. For example:
if (me.isSelected()) ${Data1}.setValue(me.getSelectedValue())
- On selected: Activated when the radio button is selected. For example:
${Data1}.setValue(me.getSelectedValue())

## Methods

For detailed information on the available methods for Radio button, see the Radio button JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.