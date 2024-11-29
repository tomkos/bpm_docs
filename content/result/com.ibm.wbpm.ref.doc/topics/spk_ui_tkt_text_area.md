# Text area

## Data binding

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the text field in pixels, percent, or em units. For example: 50px or 20% or 0.4em. The default unit is pixel, in case no other is specified.           | String      |
| Height                              | Specifies the height of the text field in px (pixels) or em units. If no unit type is specified, px is assumed.                                                               | String      |
| Size                                | Specifies the text size. Applies to both label and text. Default Large Small                                                                                                  | String      |
| Label placement                     | Specifies the placement of the label in relation to the text. Top Left  Note: Labels on the left change the specified width of the view.                                      | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                           | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | Specifies the tabbing sequence index of the view. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |
| Placeholder text                  | Provides the placeholder text that is displayed when no value was entered.                                                                                                                                                                            | String      |
| Validate input                    | The regular expression to use for validating input.                                                                                                                                                                                                   | String      |
| Auto-expand on printing           | Enables printing of the entire content of the text area, beyond the area that is visible on the screen.                                                                                                                                               | Boolean     |

## Events

- On load: Activated when the page loads. For example:
me.setText("Some default text on load.")
- On change: Activated when the text is changed. For example:
if(newText != oldText){return confirm ("Are you sure you want to change the text area field?");}
- On focus: Activated when the focus moves to the text field. For example:
me.setLabelPlacement("T")where "T" (standing for
Top) must be defined in "me.setLabelPlacement("L")".
- On blur: Activated when the text field loses the focus. For example:
me.setLabelPlacement("L")where "L" (standing for
Left) must be defined in "me.setLabelPlacement("L")".
- On input: Activated when the user enters text in the text field. For
example: return potential.length<=10;

## Methods

For detailed information on the available methods for Text area, see the Text area JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.