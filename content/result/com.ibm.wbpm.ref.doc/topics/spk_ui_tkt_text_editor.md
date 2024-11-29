# Rich text

## Data binding

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

The appearance configuration properties for Rich text are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                                    | Data type   |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the text area in px (pixels), % (percent), or em units. For example: 50px or 20% or 0.4em. If no unit type is specified, px is assumed. | String      |
| Height                              | Specifies the height of the text field in px (pixels) or em units. If no unit type is specified, px is assumed.                                                | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                               | Data type       |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Tab index                         | Specifies the tabbing sequence index of the view. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key.                     | Integer         |
| Palette colors                    | The default colors that are available in the text color palette. The number of colors is determined by the number of rows and columns. Name: The name of the color is displayed as a tooltip at mouse-over. Value: The hexadecimal representation of the specified color. | NameValuePair[] |
| Palette columns                   | The number of columns for the text color palette. The default number is 8.                                                                                                                                                                                                | Integer         |
| Palette rows                      | The number of rows for the text color palette. The default number is 5.                                                                                                                                                                                                   | Integer         |
| Show status bar                   | Shows or hides the status bar underneath the editor area. The status bar displays the HTML element that is currently edited.                                                                                                                                              | Boolean         |

## Events

- On load: Activated when the page loads. For example:
me.setText("Some default text on load.")
- On change: Activated when the text is changed. For example:
if(newText != oldText){return confirm ("Are you sure you want to change the text area field?");}
- On focus: Activated when the focus moves to the text field. For example:
me.setLabelPlacement("T")
- On blur: Activated when the text field loses the focus. For example:
me.setLabelPlacement("L")
- On input: Activated when the user enters text in the text field. For
example: return potential.length<=10;

## Methods

For detailed information on the available methods for Rich text, see the Rich text JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.