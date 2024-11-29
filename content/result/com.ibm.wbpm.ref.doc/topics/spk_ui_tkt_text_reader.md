# Text reader

## Data binding

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

The appearance configuration properties for Text reader are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the view in pixels, percent, or em units. For example: 50px or 20% or 0.4em. If no unit type is specified, px is assumed.                              | String      |
| Height                              | Specifies the height of the view in px (pixels) or em units. If no unit type is specified, px is assumed.                                                                     | String      |
| Size                                | Specifies the size of the label and text. Default Large Small                                                                                                                 | String      |
| Label placement                     | Specifies the placement of the label in relation to the text. Top Left  Note: Labels on the left change the specified width of the view.                                      | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

| Behavior configuration property   | Description                                                                                                                                                                                             | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Max text length                   | Specifies the maximum number of characters that are displayed until the Read More hint is shown. If no number is specified or the number is lesser than 1, the default value of 128 characters is used. | Integer     |
| Read more hint                    | The placeholder text that is displayed for the Read More hint.                                                                                                                                          | String      |
| Read less hint                    | The placeholder text that is displayed for the Read Less hint.                                                                                                                                          | String      |
| Initially expanded                | Specifies whether the text section is expanded when the page is loaded.                                                                                                                                 | Boolean     |
| Use arrow icons                   | Enables you to use arrow icons that expand and collapse the text area.                                                                                                                                  | Boolean     |

## Events

- On load: Activated when the page loads. For example:
if (${DeviceSensor}.getDeviceInfo().isIPhone) {me.setExpanded(false);} else {me.setExpanded(true);}
- On click: Activated when the view is clicked. For example:
me.toggleExpanded()
- On expand: Activated when the user expands the text. For example:
${TextReader2}.setExpanded(false)
- On collapse: Activated when the user collapses the text. For example:
${TextReader2}.setExpanded(true)

## Methods

For detailed information on the available methods for Text reader, see the Text reader JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.