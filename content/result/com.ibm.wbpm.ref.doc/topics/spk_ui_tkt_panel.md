# Panel

You can also use the Panel view with the Panel header and Panel footer views.

## Configuration properties

<!-- image -->

The appearance configuration
properties for the Panel view are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                                                                                                 | Data type   |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Icon                                | Specifies the notification icon name. For example: calendar, clock-o, camera, cloud-upload, bell, info, file-text. See Font Awesome V4.7.0 for a complete list of icons.  By default, no icon is specified.                 | String      |
| Color style                         | Specifies the color style for the view. The colors correspond to variables in the specified theme.                                                                                                                          | ColorStyle  |
| Light color                         | Sets the fill color to a lighter shade, and changes the text title to the color selected in Color style.                                                                                                                    | Boolean     |
| Full body color                     | When selected, fills the body with color, instead of only the header.                                                                                                                                                       | Boolean     |
| Width                               | Specifies the width in pixels, percent, or em units. For example: 50px or 0.4em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no width is specified.      | Integer     |
| Body height                         | Specifies the body height in pixels or em units, not including the header or footer. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no height is specified. | Integer     |

The footer configuration properties for the Panel view are shown in the
following
table:

| Footer configuration property   | Description                                                                    | Data type   |
|---------------------------------|--------------------------------------------------------------------------------|-------------|
| Footer text                     | Allows you to add a footer to the panel and specifies the text for the footer. | String      |

## Example

In this example, the following configuration properties are set for the Panel view:

- The appearance configuration is as follows:
    - Icon is set to rocket.
    - Color style is set to Warning.
    - Light color and Full body color are left
unchecked.
    - Width is set to 50%.
    - Body height is set to 350px.
- The footer configuration is as follows:

- Footer is set to "The text will be in the Panel
footer".

These properties and their values result in 350-pixel high and 50-percent wide yellow bordered
panel containing various other views, with a rocket icon inside a header on a yellow background, and
a footer at the bottom of the panel that says The text will be in the Panel
footer

## Events

- On load: Activated when the page loads.
- On icon click: Activated when the Panel Icon is clicked.

Depending
on the specific event, you can use JavaScript logic to modify the effects of the
view.

## Methods

For detailed information on the available methods for Panel, see the Panel JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.