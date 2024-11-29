# Input group

## Configuration properties

Under Configuration, set or modify the configuration
properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                   | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.  | String      |
| Label placement                     | The label placement for this view. A left placement of the label changes the specified width of the view.                                                                     | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |
| Color style                         | The color style for the view. The colors correspond to variables in the specified theme.                                                                                      | String      |
| Button location                     | The button location relative to the field.                                                                                                                                    | String      |
| Button type                         | You can create the view as a clickable icon, a text field, or a menu. Use the Menu option with a Pop-up Menu view. For more information about this view, see Pop-up menu.     | String      |
| Button info                         | The name of the icon. See Font Awesome V4.7.0 for a complete list of icons.                                                                                                   | String      |

## Example

To create an Input group with a calculator icon next to an Integer input
field , drop an Integer view into an Input group view and set the Input group options as
follows:

- Leave Width blank.
- Set Label placement to Top.
- Set Color style to Primary.
- Set Button location to Left.
- Set Button type to Icon.
- Set Button info to calculator.

## Configuring the Input group in a read-only section

<!-- image -->

```
me.setEnabled(true)
```

## Events

- On load when the page loads, for example
me.setIcon("rocket");
- On button click when an icon used as a button is clicked, for example
${PopupMenu1}.setMenuVisible(!${PopupMenu1}.isMenuVisible())

## Methods

For more information about the available methods, see the Input group JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.

For more information about input views, see Plain text, Text area, Date/time picker, Integer.