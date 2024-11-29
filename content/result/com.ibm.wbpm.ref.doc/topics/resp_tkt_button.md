# Button (deprecated)

<!-- image -->

The button also includes an icon if one has been specified using the Icon
configuration property. You can change the color and text size with predetermined values based on
the theme.

## Data binding

| Binding description                                  | Data type   |
|------------------------------------------------------|-------------|
| Records whether the user clicks the button instance. | Boolean     |

## Theme definitions

The design mode of the theme editor contains a simulation of this view. If you hover over the
simulation, it lists the theme definitions that determine the appearance of the view. For
information on the theme editor, see Creating themes.

## Configuration properties

<!-- image -->

| Configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Data type   |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Icon                     | The URL of the icon file or the path to the managed icon file. The button displays the image at full size. Changing the height and width of the button in its Positioning properties does not affect the image size. Because the button does not resize the image, use an appropriately sized image for the button. If you want to use a larger image, use the Image view instead and set the view instance to fire a boundary event when users select it. The default value is no URL. | URL         |
| Icon description         | A description of the icon that makes it accessible for users and technologies that cannot see the icon.                                                                                                                                                                                                                                                                                                                                                                                 | String      |
| Allow multiple clicks    | Select this option if the user can repeat the button action, such as adding something for each click. Do not select this option if the event is to occur only once, such as a bill payment confirmation.The default value is False (not selected)                                                                                                                                                                                                                                       | Boolean     |
| Style > Theme color type | Set the color of the button defined in the theme for a particular type. In the Classic theme in the System Data toolkit, the colors are: Dark blue for primary (default) White for alternate Light blue for info Green for success Yellow for warning Red for alert  The button definitions (see the theme definitions table) refer to specific color values either directly or through another variable or by a formula.                                                               | String      |
| Style > Text size        | Set the size of the text on the button and the amount of padding between the text and the borders of the button. For example, to make the text more readable on smart phones, you can set this configuration option to Large for the small screen size. The default value is Medium.                                                                                                                                                                                                    | String      |