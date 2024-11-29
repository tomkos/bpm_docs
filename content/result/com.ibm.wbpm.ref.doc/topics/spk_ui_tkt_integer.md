# Integer

## Data binding

Set or modify the data binding for the Integer view in the General
properties tab. The view is bound to an Integer variable.

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.  | String      |
| Size style                          | The size of the text in the view.                                                                                                                                             | String      |
| Label placement                     | The label placement for this view. Left placement of the label changes the specified width of the view.                                                                       | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                     | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |
| Placeholder text                  | The placeholder text that is displayed when no value is entered.                                                                                                                                                                | String      |
| Numeric formatting                | Determines whether the thousands separator is based on the current user's locale or specified as a custom configuration option. The available options are Auto and Custom.                                                      | String      |
| Hide thousands separator          | Hides the thousands separator. By default, this option is not selected.                                                                                                                                                         | Boolean     |
| Thousands separator               | Separates the thousands in digit grouping. Commas are most commonly used as thousands separators. Based on the user's locale, other symbols (such as periods) or custom characters can be used as thousands separators.         | String      |
| Prefix                            | A symbol that precedes the numerical input values.                                                                                                                                                                              | String      |
| Postfix                           | A symbol that succeeds the numerical input values.                                                                                                                                                                              | String      |

## Example

1. Under Appearance, set Size style to
Default, and Label placement to
Top.
2. Under Behavior, set Thousands separator to
, (comma), and Prefix to
$.
3. Save your changes.

In the result, an input value of 1500 is displayed as
$1,500.

## Events

Set or modify the
formula configuration properties and the event handlers for the view in the
Events properties. You can set events to be triggered programmatically or when
a user interacts with the view. For information on how to define and code
events, see User-defined events.

| Formula configuration property   | Description                                                                                                                                                                               | Data type   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Value formula                    | The formula that specifies how the value is displayed in the view. You can use static String values or formulas or aggregate functions.For more information about formulas, see Formulas. | String      |

The Integer view has the following types of event handlers:

- On load: Activated when the page loads. For example:
me.setValue(0.00);
- On change: Activated when the value changes. For example:
${Decimal1}.setValue(oldValue); ${Decimal2}.setValue(newValue);
- On focus: Activated when the focus moves to the integer field. For example:
${Tooltip1}.setTooltipVisible(true)
- On blur: Activated when the integer field loses the focus. For example:
${Tooltip1}.setTooltipVisible(false);
- On format: Activated when the user applies custom formatting to the input
values. The formatting is based on the return value of the statement. For example:
var neg = me.getValue() < 0; if (neg){return "(" + formattedValue + ")"}

Depending on the specific event, you can use JavaScript logic to modify the effects of the
view. More information on using events with views is found in the topic
User-defined events.

## Methods

For detailed information on the available methods for Integer, see the Integer JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.