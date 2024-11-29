# Decimal

## Data binding

Set or modify the data binding for the view in the General properties tab.
The Decimal view can be bound to a Decimal variable.

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.  | String      |
| Size                                | The size of the text in the view.                                                                                                                                             | String      |
| Label placement                     | The label placement for this view. A left placement of the label changes the specified width of the view.                                                                     | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                                                         | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key.                                                                                                     | Integer     |
| Placeholder text                  | The placeholder text that is displayed when no value is entered.                                                                                                                                                                                                                                                                    | String      |
| Numeric formatting                | Determines whether the thousands separator and the decimal separator are based on the current user's locale or specified as custom configuration options. The available options are Auto and Custom.                                                                                                                                | String      |
| Hide thousands separator          | Hides the thousands separator.                                                                                                                                                                                                                                                                                                      | Boolean     |
| Thousands separator               | Separates the thousands in digit grouping. Commas are most commonly used as thousands separators. Based on the user's locale, other symbols (such as periods) or custom characters can be used as thousands separators.                                                                                                             | String      |
| Decimal separator                 | Separates the integral and the fractional parts of a decimal numeral. Periods are most commonly used as decimal separators. Based on the user's locale, other symbols (such as commas) or custom characters can be used as decimal separators.                                                                                      | String      |
| Decimal places                    | The maximum number of decimal places to display.                                                                                                                                                                                                                                                                                    | Integer     |
| Currency                          | The currency that the decimal number is formatted to.  When you specify a value for Currency, the currency format overwrites the values that you have specified for Thousands Separator and Decimal Separator. To specify a custom formatting for the decimal numbers, use the Prefix and Postfix configuration properties instead. | String      |
| Currency symbol                   | The currency symbol whose value overrides the Currency value. To specify a custom formatting for the decimal numbers, use the Prefix and Postfix configuration properties instead.                                                                                                                                                  | String      |
| Prefix                            | A symbol that precedes the numerical input values.                                                                                                                                                                                                                                                                                  | String      |
| Postfix                           | A symbol that succeeds the numerical input values.                                                                                                                                                                                                                                                                                  | String      |

## Example

1. Under General, enter Total as the name of the
decimal view.
2. Under Events, specify the following value for Formula
value: @{Value1} + @{Value2}. This formula takes the input values
from two other decimal views named Value1 and Value2,
and adds them up.
3. Under Appearance, set Size style to
Large, and Label placement to
Top.
4. Under Behavior, set Thousands separator to
, (comma), Decimal separator to
. (period), Decimal places to
2, and Prefix to $.
5. Save your changes.

The result is a decimal field that adds the input values for Value1 and
Value2, is preceded by the $ symbol, and shows two
decimals after the separator. If the input value for Value1 is
$100.00 and the input value for Value2 is
$200.00, the value for your decimal number is displayed as
$300.00

## Events

Set or modify the
formula configuration properties and the event handlers for the view in the
Events properties. You can set events to be triggered programmatically or when
a user interacts with the view. For information on how to define and code
events, see User-defined events.

| Formula configuration property   | Description                                                                                                                                                                               | Data type   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Value formula                    | The formula that specifies how the value is displayed in the view. You can use static String values or formulas or aggregate functions.For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads. For example:
me.setValue(0.00);
- On change: Activated when the value changes. For example:
${Decimal1}.setValue(oldValue); ${Decimal2}.setValue(newValue);
- On focus: Activated when the focus moves to the decimal field. For example:
${Tooltip1}.setTooltipVisible(true)
- On blur: Activated when the view loses the focus. For example:
${Tooltip1}.setTooltipVisible(false);
- On format: Activated when the user applies custom formatting to the input
values. The formatting is based on the return value of the statement. For example:
var neg = me.getValue() < 0; if (neg){return "(" + formattedValue + ")"}

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for Decimal, see the Decimal JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.