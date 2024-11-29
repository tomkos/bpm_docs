# Progress bar

The visual display of the Progress bar view gives the user an immediate understanding of how many
tabs, pages, or input fields have been completed. It is most commonly used as a header on web forms
or tabs.

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                               | Data type         |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Color style                         | Specifies a color style for the fill color of the progress bar. The colors correspond to variables in the specified theme. The default color style is Default (gray).                                                                                     | TooltipColorStyle |
| Striped                             | When selected, adds stripes to the progress bar.                                                                                                                                                                                                          | Boolean           |
| Active                              | When selected, and when Striped is also selected, makes the progress bar stripes move.                                                                                                                                                                    | Boolean           |
| Radius                              | Specifies the roundness of the progress bar corners, in either pixel or em units. For example, 15px or 1em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no border radius is specified. | String            |
| Width                               | Specifies the width of the progress bar in pixels, percents, or em units. For example: 800px, or 80% or 50em. If only a number is specified without any unit, the number is interpreted as the number of pixels.                                          | String            |
| Height                              | Specifies the height of the well in pixels, or em units. For example, 15px or 1em. If only a number is specified without any unit, the number is interpreted as the number of pixels. By default, no height is specified.                                 | String            |

| Behavior configuration property   | Description                                                                                          | Data type   |
|-----------------------------------|------------------------------------------------------------------------------------------------------|-------------|
| Max value                         | Specifies the total numeric value of the progress (not to be confused with Width). For example, 100. | Integer     |

## Example

In this example, the following configuration properties are set for the Progress bar view:

- Behavior configuration properties:
    - Max value is set to 100.
- Appearance configuration properties:

- Color style is set to Info.
- Striped is selected.
- Active is selected.
- Radius is set to 1.
- Width is set to 25%.
- Events configuration properties:

- For the On load event, the setProgress method is used to
set the progress bar to 50: me.setProgress(50);

These properties and their values result in a light-blue, striped and animated half-filled
progress bar with rounded corners, that takes 25% of the page width.

## Events

| Formula configuration property   | Description                                                                                    | Data type   |
|----------------------------------|------------------------------------------------------------------------------------------------|-------------|
| Formula                          | Expression to be used to calculate progress.For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads.
- On click: Activated when the progress bar is clicked.

## Methods

- setWidth(): Sets the width of the progress bar.
- getWidth(): Gets the configured size for the progress bar width (including the
unit).
- setHeight(): Sets the height of the progress bar.
- getHeight(): Gets the configured size for the progress bar height (including
the unit).
- setColorStyle(): Sets the color style of the progress bar.
- setRadius(): Sets the radius (roundness) of the progress bar.
- setProgress(): Sets the progress status.
- getProgress(): Gets the progress status.
- setMaximum(): Sets the maximum value of the progress bar.

For more information on how to use these methods, see the Progress bar JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.