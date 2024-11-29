# Tooltip

The Tooltip view is most commonly used to display helpful tips about input views. The Tooltip
view is a container for other views such as Plain text.

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                                                        | Data type   |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Show label                          | Displays a label. If the Tooltip view has a label, it is displayed. If the Tooltip view does not have a label, and it contains another view, the label of the inner view is displayed. If Show label is not selected, neither label is shown. Note: The view Label visibility property is ignored. | Boolean     |
| Label placement                     | The label position.                                                                                                                                                                                                                                                                                | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                                                      | String      |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                                                                                                                       | Integer     |
| Color style                         | The color style for the view. The colors correspond to variables in the specified theme.                                                                                                                                                                                                           | ColorStyle  |
| Horizontal position                 | The horizontal positioning of the tooltip. .                                                                                                                                                                                                                                                       |             |
| Vertical position                   | The vertical positioning of the tooltip.                                                                                                                                                                                                                                                           |             |

The behavior configuration properties for Tooltip are shown in the following table:

| Behavior configuration property   | Description                                                                                                           | Data type   |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------|-------------|
| Show tooltip                      | Displays the tooltip when the page loads.                                                                             | Boolean     |
| Show on hover                     | Displays the tooltip when the user hovers over the related view.                                                      | Boolean     |
| Text as HTML                      | Renders the tooltip text using HTML. If so, you must enter the tooltip text in the Help text box, in the General tab. | Boolean     |

## Example

In this example, there is a Plain text view inside a tooltip, and the following configuration
properties are set for the Tooltip view:

- Events :
    - The Tooltip formula is set to "My tooltip".
- Appearance configuration:

- Show label is not selected.
- Label placement is set to Left.
- Width is set to 50%.
- Color style is set to Default.
- Horizontal position is set to Left.
- Vertical position is set to Top.
- Behavior configuration:

- Show tooltip is selected.
- Show on hover is not selected.
- Text as HTML is selected.

These properties and their values result in a tooltip element which is half the size of the
default Tooltip view size, and that says My tooltip on a black background.
This tooltip element is displayed above a text area, on the left hand side, and is visible as soon
as the page loads.

## Events

| Formula configuration property   | Description                                                                                                 | Data type   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------|-------------|
| Tooltip formula                  | Formula or expression used to calculate the Tooltip text.For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads.
- On click: Activated when the tooltip is clicked.

## Methods

For detailed information on the available methods for Tooltip, see the Tooltip JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.