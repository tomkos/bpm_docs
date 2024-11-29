# Plain text

## Data binding

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

The appearance configuration properties for Plain text are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.  | String      |
| Size                                | The text size. The size applies to both the label and the text.                                                                                                               | String      |
| Label placement                     | The placement of the label in relation to the text. Labels on the left change the specified width of the view.                                                                | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                     | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |
| Placeholder text                  | The placeholder text that is displayed when no value is entered.                                                                                                                                                                | String      |
| Validate input                    | The regular expression to use for validating input.                                                                                                                                                                             | String      |
| Select text on focus              | Selects all the text in the text field that has the focus.                                                                                                                                                                      | Boolean     |

## Events

| Formula configuration property   | Description                                                                                                                                                                                                                   | Data type   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Text expression                  | Provides the expression or formula that calculates the text in the Plain text view. You can set the text either by using a static string or dynamically by using a formula.For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads. For example:
me.setText("Some default text on load.")
- On change: Activated when the text is changed. For example:
if(newText != oldText){return confirm ("Are you sure you want to change the text field?");}
- On focus: Activated when the focus moves to the text field. For example:
me.setLabelPlacement("T")
- On blur: Activated when the text field loses the focus. For example:
me.setLabelPlacement("L")
- On input: Activated when the user enters text in the text field. For
example: return potential.length<=10;

## Methods

For detailed information on the available methods for Plain text, see the Plain text JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.