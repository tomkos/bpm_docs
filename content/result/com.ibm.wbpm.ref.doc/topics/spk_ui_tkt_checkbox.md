# Check box

## Data binding

Set or modify the data binding for Check box in the General properties. The
view is bound to a Boolean variable.

## Configuration properties

Under Behavior, set or modify the configuration properties for Check box.

<!-- image -->

| Appearance configuration property   | Description                                                 | Data type   |
|-------------------------------------|-------------------------------------------------------------|-------------|
| Show validation marker              | Show a validation icon and border when the view is invalid. | Boolean     |

| Behavior configuration property   | Description                                                                                                                                                                                                                     | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events. Check box has the following types
of event handlers:

- On load: Activated when the page loads. For example:
me.setChecked(false);
- On change: Activated when the bound data changes, such as when the box is
selected. For example:
me.isChecked() ? ${Section1}.setVisible(true) : ${Section1}.setVisible(false);

Depending on the specific event, you can use JavaScript logic to modify the effects of the
view. More information on using events with views is found in the topic
User-defined events.

## Methods

For detailed information on the available methods for Check box, see the Check box JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.