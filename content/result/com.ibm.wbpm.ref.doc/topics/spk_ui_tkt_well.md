# Well

## Configuration properties

<!-- image -->

The appearance configuration
properties for Well are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                                                                                                                                          | Data type         |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Color style                         | Specifies a color style for the view. The colors correspond to variables in the specified theme.                                                                                                                                                                     | TooltipColorStyle |
| Color darkness                      | Specifies the darkness of the selected color: None, Dark, or Darker. By default, the darkness is set to None.                                                                                                                                                        | String            |
| Icon                                | Specifies the notification icon name. For example: calendar, clock-o, camera, cloud-upload, bell, info, file-text. See Font Awesome V4.7.0 for a complete list of icons.  By default, no icon is specified.                                                          | String            |
| Icon size                           | Specifies the size of the icon in either pixel or em units. For example, 43px or 30em. If only a number is specified without any unit, the number is interpreted as the number of pixels.                                                                            | String            |
| Icon position                       | Specifies the position of the icon within the Well view: Bottom-Right, Bottom-Left, Top-Right, or Top-Left.                                                                                                                                                          | String            |
| Vertical alignment                  | Specifies the vertical alignment of child views: Top, Middle, or Bottom. By default, the vertical alignment is set to Top.                                                                                                                                           | String            |
| Padding                             | Specifies the padding to be added around the well, in either px (pixel), % (percent) or em units. For example, 25px or 10em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no padding is specified. | String            |
| Border radius                       | Specifies the roundness of the well corners, in either px (pixel), % (percent) or em units. For example, 15px or 1em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no border radius is specified.  | String            |
| Width                               | Specifies the width of the well in pixels, percent, or em units. For example: 800px or 80% or 50em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no width is specified.                            | String            |
| Height                              | Specifies the height of the well in pixels or em units. For example: 300px or 20em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no height is specified.                                           | String            |

## Example

- Color style is set to Warning.
- Icon is set to gear.
- Icon size is set to 300px.
- Icon position is set to Bottom-Right.
- Border radius is set to 20.
- Height is set to 300px

These properties and their values result in a yellow 300-pixel high Well container with rounded
borders, holding a Text view at the top. A 300-pixel gear icon is displayed in the bottom right
corner of the Well view.

## Events

- On load: Activated when the page loads.
- On click: Activated when the Well view is clicked.

## Methods

For detailed information on the available methods for Well, see the Well JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.