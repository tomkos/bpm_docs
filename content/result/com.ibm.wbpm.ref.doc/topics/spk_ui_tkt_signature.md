# Signature

Signature comes with appearance and behavior configuration options.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                         | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Color style                         | Specifies a color style for the signature box. The colors correspond to variables in the specified theme.                                                                                                                           | String      |
| Border width                        | Specifies the thickness of the signature box border in pixels.                                                                                                                                                                      | String      |
| Border radius                       | Specifies the roundness of the signature box corners in pixels.                                                                                                                                                                     | String      |
| Box shadow                          | When selected, adds a background shadow to the signature box.                                                                                                                                                                       | Boolean     |
| Width                               | Specifies the width of the signature box in pixels, percents, or em units. For example: 400px or 50% or 30em. If only a number is specified without any unit, the number is interpreted as the number of pixels.                    | String      |
| Height                              | Specifies the height of the signature box in pixels or em units. For example: 150px or 20em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no height is specified. | String      |

The behavior configuration properties for the Signature view are shown in the following
table:

| Behavior configuration property   | Description                                                                                                          | Data type   |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------|-------------|
| Ink color                         | Specifies the color of the signature in color names, hexadecimal codes, or RGB values. It must be a valid CSS color. | String      |

## Example

In this example, the following behavior and appearance configuration properties are set for the
Signature view:

- Ink color is set to Green.
- Color style is set to Default.
- Border width is set to 5px.
- Border radius is set to 5px.
- Box shadow is selected.
- Width is set to 300px.
- Height is set to 75px.

These properties and their values result in a signature box that looks like the following
figure:

## Events

- On load: Activated when the page loads.
- On change: Activated when there is a change in the Signature view.

## Methods

For detailed information on the available methods for the Signature view, see the Signature JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.