# Caption box

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                 | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of a caption box in pixels, percent, or em units. For example: 50px or 20% or 0.4em. If only a number is specified without any unit, the number is interpreted as the number of pixels. | String      |
| Label placement                     | Specifies the label placement relative to the contained view: Top, Left, Bottom, or Right.The default label placement is Top.                                                                               | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.                               | String      |
| Label horizontal alignment          | Specifies the horizontal alignment of the label: Left, Center, or Right.The default label horizontal alignment is Top.                                                                                      | String      |
| Label vertical alignment            | Specifies the vertical alignment of the label: Top, Middle, or Bottom.The default label vertical alignment is Top.                                                                                          | Integer     |
| Shrink to content                   | Specifies whether or not the caption box should be shrunk to the size of the contained view. By default, this property is not selected.                                                                     | Boolean     |
| Color style                         | Specifies the color style for the label. The colors correspond to variables in the specified theme.                                                                                                         | String      |
| Label size style                    | Specifies the size of the label.                                                                                                                                                                            | String      |
| Label weight style                  | Specifies the font weight of the label.                                                                                                                                                                     | String      |

## Example

In this example, a Text Area view is nested inside a caption box, and the following appearance
configuration properties are set for the caption box view:

- Label placement is set to Right.
- Label horizontal alignment is set to Right.
- Label vertical alignment: is set to Middle.
- Color style is set to Warning.
- Label size style is set to Large.
- Label weight style is set to Bold.

All the other properties are left with their default settings.

These properties and their values result in a yellow label in large and bold font, placed on the
right of the text area, vertically centered within the caption box.

## Events

| Formula configuration property   | Description                                                                                                                | Data type   |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------|-------------|
| Label formula                    | Specifies the label associated with the view using a formula expression.For more information about formulas, see Formulas. | String      |

- On load: Activated when the view loads.

For example, On load can be used to dynamically specify the label
position using the .setLabelHorizontalAlignment,
.setVerticalAlignment, or .setLabelPlacement
methods.

## Methods

For detailed information on the available methods for Caption box, see the Caption box JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.