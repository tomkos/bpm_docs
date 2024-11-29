# Decimal (deprecated)

<!-- image -->

If you want the Decimal control to contain an monetary amount, set its
Currency configuration property to the currency or specify the ISO-4217 code
for that currency in the Other Currency field. By default, the
Currency field is set to Other and the
Other Currency field is empty, which means that the Decimal control does not
contain a monetary amount.

## Restrictions and limitations

## Data binding

| Binding description                                                                                                                        | Data type   |
|--------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Contains the number that this control displays. The bound data can be empty and the Decimal control saves the number that the user enters. | Decimal     |

## Configuration properties

<!-- image -->

| Configuration property    | Description                                                                                                                                                                                                                                                                                                                                                                                                        | Data type   |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Currency                  | If the field is being used for a monetary value, select the ISO 4217 currency. Setting a currency causes the Decimal control to use the appropriate symbol and formatting for that currency. The default is Other.                                                                                                                                                                                                 | String      |
| Other Currency            | If you set Currency to Other, leave this field empty for non-monetary values or specify the ISO 4217 three letter currency code to set formatting and symbol.                                                                                                                                                                                                                                                      |             |
| Currency Symbol           | Override the currency symbol that is set by the Currency or Other Currency properties with the specified symbol. The default is to not override the symbol.This field is for handling changes that countries make in the symbols for their currency. For example, in 2010, India changed the sign for their rupee. To display the HTML character for the Indian rupee, in the Currency Symbol field, type &#8377;. |             |
| Hide Thousands Separators | Select this option to hide the delimiter characters that are used to separate thousands. For example, select this option to display ten thousand as 10000 instead of 10 000 or 10,000. The default is to show the separators.                                                                                                                                                                                      | Boolean     |
| Decimal Places            | Set the maximum number of places beyond the decimal character. The default is 2 places (0.00). A value of 0 means no places (0). A negative value means that there is no restriction on the number of places.Restriction: See IEEE 754 for information about the maximum number of decimal places.                                                                                                                 | Integer     |
| Minimum Value             | Set the minimum value that the Decimal control can contain. By default, there is no restriction on the minimum value.                                                                                                                                                                                                                                                                                              | Decimal     |
| Maximum Value             | Set the maximum value that the Decimal control can contain. By default, there is no restriction on the maximum value.                                                                                                                                                                                                                                                                                              | Decimal     |
| Step Size                 | Set the number by which the value increases or decreases when the user presses the up or down arrow keys or clicks the spin control. The control gains the spin control when specify a step size.                                                                                                                                                                                                                  | Decimal     |

## Example: Adding a non-listed
currency

1. Add a Decimal control to the layout of a coach or coach view.
2. Open its configuration properties page. The Currency option
is set to Other by default. Because the bitcoin
is not in the list of currencies that are contained by the Currency option,
the Other value is the one that you want.
3. In the Other Currency option, type the
ISO-4217 code for the bitcoin. Specifying a currency code in the Currency
option or the Other Currency option converts the Decimal control from
displaying numbers to displaying a monetary amount.
4. In the Currency Symbol, if you are using
an alternative to the symbol specified by ISO-4217 for the bitcoin,
type that symbol.