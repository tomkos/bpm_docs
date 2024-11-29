# Integer (deprecated)

## Restrictions and limitations

## Data binding

| Binding description                                                                                                                                                                                                                      | Data type   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| The bound data item contains an Integer value that the view displays. The Integer can initially be empty. If the visibility of the view is not read only, the view saves to the bound data item any number that the user enters into it. | Integer     |

## Theme definitions

The design mode of the theme editor contains a simulation of this view. If you hover over the
simulation, it lists the theme definitions that determine the appearance of the view. For
information on the theme editor, see Creating themes.

## Configuration properties

| Configuration property    | Description                                                                                                                                                                                                                                                                                | Data type   |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Hide thousands separators | Select to hide the delimiters that separate thousands. For example, display ten thousand as 10000 instead of 10 000 or 10,000.                                                                                                                                                             | Boolean     |
| Minimum value             | Set the minimum value that this field can contain. The default is no minimum value.                                                                                                                                                                                                        | Integer     |
| Maximum value             | Set the maximum value that this field can contain. The default is no maximum value.                                                                                                                                                                                                        | Integer     |
| Step size                 | To incrementally increase or decrease the value, set how much the value changes when users press the up or down arrow keys or click the spin view.                                                                                                                                         | Integer     |
| Placeholder hint          | Add a brief description or example of the input required by the user. If the bound data item does not contain a value, users see the hint until they type in the field.                                                                                                                    | String      |
| Style > Text size         | Set the size of the text in the view, the size of the label text, and the amount of padding around the text. For example, to make the text and label more readable on smart phones, you can set this configuration option to Large for the small screen size. The default value is Medium. | String      |