# Decimal (deprecated)

## Limitations

If the user types in content that is not a valid number, the bound data item is null when the
user triggers a boundary event such as clicking a button. If the flow returns to the coach, the view
is empty. Any other views bound to the same data item are also empty.

## Data binding

| Binding description                                                                                                                                                                                                                     | Data type   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| The bound data item contains a Decimal value that the view displays. The Decimal can initially be empty. If the visibility of the view is not read only, the view saves to the bound data item any number that the user enters into it. | Decimal     |

## Theme definitions

The design mode of the theme editor contains a simulation of this view. If you hover over the
simulation, it lists the theme definitions that determine the appearance of the view. For
information on the theme editor, see Creating themes.

## Configuration properties

| Configuration property    | Description                                                                                                                                                                                                                                                                                | Data type                 |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Currency                  | If the field is for a monetary value, select an ISO 4217 currency to set the symbol and formatting for the field. The default value is Other.                                                                                                                                              | CurrencyCodeSelectionType |
| Other currency            | If the field is for a monetary value, specify an ISO 4217 three-letter currency code to set the symbol and formatting for the field. This applies when the currency option is set to Other.                                                                                                | String                    |
| Currency symbol           | Override the currency symbol set by Currency or Other                                                                                                                                                                                                                                      | String                    |
| Hide thousands separators | Select to hide the delimiters that separate thousands. For example, display ten thousand as 10000 instead of 10 000 or 10,000. The default is not selected (False).                                                                                                                        | Boolean                   |
| Decimal places            | Set the maximum number of decimal places to show. The default is 2 decimal places. For no limit on the number of decimal places, set this option to a negative number.                                                                                                                     | Integer                   |
| Minimum value             | Set the minimum value that this field can contain. The default is no minimum value.                                                                                                                                                                                                        | Decimal                   |
| Maximum value             | Set the maximum value that this field can contain. The default is no maximum value.                                                                                                                                                                                                        | Decimal                   |
| Step size                 | To incrementally increase or decrease the value, set how much the value changes when the user presses the up or down arrow keys or clicks the spin view.                                                                                                                                   | Decimal                   |
| Placeholder hint          | Add a brief description or example of the input required by the user. If the bound data item does not contain a value, users see the hint until they type in the field.                                                                                                                    | String                    |
| Style > Text size         | Set the size of the text in the view, the size of the label text, and the amount of padding around the text. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large for the small screen size. The default value is Medium. | String                    |