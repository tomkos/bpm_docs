# Slider

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

The appearance configuration properties for the Slider view are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                             | Data type   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Vertical                            | When selected, it displays the slider vertically rather than horizontally.                                                                              | Boolean     |
| Color style                         | Specifies a color style for the slider. The colors correspond to variables in the specified theme.                                                      | String      |
| Height                              | Specifies the slider height in px (pixels) or em units. If no unit type is specified, px is assumed.                                                    | String      |
| Width                               | Specifies the width of the slider in pixels, percent, or em units. For example: 50px or 20% or 0.4em. If no unit type is specified, px is assumed.      | String      |
| Border radius                       | Specifies the radius of the curvature for the corners of the slider bar.                                                                                | String      |
| Handle width                        | Specifies the width of the handle in pixels (px) or em units. For example: 50px or 0.4em. If no unit is specified, px is assumed (% should be avoided). | String      |
| Handle radius                       | Specifies the radius of the curvature for the corners of the handle.                                                                                    | String      |
| Show current value                  | Shows the current slider value, which can be changed by typing a different value.                                                                       | Boolean     |
| Show limit values                   | Shows the minimum and maximum values for the slider range.                                                                                              | Boolean     |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                   | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Minimum                           | Specifies the minimum value in the slider range.                                                                                                                                                                                                              | Decimal     |
| Maximum                           | Specifies the maximum value in the slider range.                                                                                                                                                                                                              | Decimal     |
| Step                              | Specifies the step value for the slider.                                                                                                                                                                                                                      | Decimal     |
| Tab index                         | Specifies the tabbing sequence index of the form control. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |

## Events

| Formula configuration property   | Description                                                                                                                                                                                        | Data type   |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Value formula                    | Specifies the formula or expression to use when the slider values are automatically calculated for the view. No formula is specified by default.For more information about formulas, see Formulas. | String      |

- On load: Activated when the view loads. For example:
me.setValue(50)
- On change: Activated when the slider value is changed. For example:
if (newVal > 50) {${icon}.setIcon("smile-o");} else {${icon}.setIcon("frown-o");}

## Methods

For detailed information on the available methods for the Slider view, see the Slider JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.