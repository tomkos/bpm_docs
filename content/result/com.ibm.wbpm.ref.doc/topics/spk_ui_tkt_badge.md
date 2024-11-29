# Badge

Badge is similar to Icon. It is most commonly used for the following purposes:

- Drawing attention to a specific UI area
- Displaying helpful information
- Serving as a clickable button

## Configuration properties

<!-- image -->

The appearance configuration
properties for Badge are shown in the following table:

| Appearance configuration property   | Description                                                                                      | Data type       |
|-------------------------------------|--------------------------------------------------------------------------------------------------|-----------------|
| Color style                         | Specifies a color style for the view. The colors correspond to variables in the specified theme. | BadgeColorStyle |
| Shape style                         | Specifies the shape styles for the view.                                                         | BadgeShapeStyle |

## Events

| Formula configuration property   | Description                                                                                                                                                                                                                            | Data type   |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Text formula                     | Specifies the expression for the view. You can use the property to set the label for Badge. The text must be enclosed within double quotation marks. For example: "This is a badge" For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads. For
example:me.setColorStyle("I")
- On click: Activated when a badge used as a button is clicked. For
example:${Tooltip1}.setTooltipVisible(!${Tooltip1}.isTooltipVisible())

Depending on the specific event, you can use JavaScript logic to modify the effects of
the view. More information on using events with views is found in the
topic User-defined events.

## Methods

For detailed information on the available methods for Badge, see the Badge JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.