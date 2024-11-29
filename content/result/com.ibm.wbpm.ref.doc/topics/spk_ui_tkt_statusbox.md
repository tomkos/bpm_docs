# Status box

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                         | Data type   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the status box in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed. | String      |
| Color style                         | Specifies a color style for the view. The colors correspond to variables in the specified theme.                                                                    | String      |
| Status style                        | Specifies the shading style based on the color style that you selected: None (light) Default (light) Dark (dark) Simple (no shade)                                  | String      |
| Float status                        | Specifies whether the status box is floating or fixed. If Float status is clear, the status bar moves other elements out of its way.                                | Boolean     |

| Behavior configuration property   | Description                                                            | Data type   |
|-----------------------------------|------------------------------------------------------------------------|-------------|
| Show status                       | Specifies whether the status box is displayed when the page is loaded. | Boolean     |
| Show validation errors            | Specifies whether the status includes validation errors.               | Boolean     |
| Status as HTML                    | Specifies whether the status includes HTML.                            | Boolean     |

## Events

Set or modify the
formula configuration properties and the event handlers for the view in the
Events properties. You can set events to be triggered programmatically or when
a user interacts with the view. For information on how to define and code
events, see User-defined events.

| Formula configuration property   | Description                                                                                                                                                                                                                   | Data type   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Text expression                  | Provides the expression or formula that calculates the text in the Status box view. You can set the text either by using a static string or dynamically by using a formula.For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads. For example:
me.setStatusText("Status Text is Loaded"); me.setStatusVisible(true);
- On click: Activated when the status box is clicked. For example:
me.setStatusVisible(false);

## Methods

For detailed information on the available methods for Status box, see the Status box JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.