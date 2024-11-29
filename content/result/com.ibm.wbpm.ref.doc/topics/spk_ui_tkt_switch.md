# Switch

## Data binding

Set or modify the data binding for the view in the General properties. The
view should be bound to a Boolean variable. The data type is Boolean.

## Configuration properties

<!-- image -->

The appearance configuration
properties for Switch are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                         | Data type         |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Color style                         | Specifies a color style for the view. The colors correspond to variables in the specified theme.                                                                                                                                                                                                                                                                                                                                    | TooltipColorStyle |
| Shape Style                         | Specifies one of the following shape styles for the switch: Default (rounded) Square (square) Modern (slider)  The default shape style is Default (rounded).                                                                                                                                                                                                                                                                        | SwitchShapeStyle  |
| Size style                          | Specifies one of the following size styles for the switch: Default (medium) Large Small   The default size style is Default (medium).                                                                                                                                                                                                                                                                                               | SwitchSizeStyle   |
| Label type                          | Specifies whether text or an icon is used as a label to indicate the On and Off positions of the switch. The default value is Text.                                                                                                                                                                                                                                                                                                 | SwitchLabelType   |
| On label                            | Specifies the label to use when the switch is in the On position. By default, no label value is specified.If you are using text for the label, type the text that you want to use to indicate the On position. If you are using an icon for the label, you can choose from a variety of icons that graphically indicate the On position by browsing the Font Awesome V4.7.0 web site. (The Font Awesome prefix fa- is optional.)    | String            |
| Off label                           | Specifies the label to use when the switch is in the Off position. By default, no label value is specified.If you are using text for the label, type the text that you want to use to indicate the Off position. If you are using an icon for the label, you can choose from a variety of icons that graphically indicate the Off position by browsing the Font Awesome V4.7.0 web site. (The Font Awesome prefix fa- is optional.) | String            |

## Events

- On load: Activated when the page loads. For example:
me.setChecked(${Checkbox}.isChecked()) where Checkbox is the
view ID of the Check Box.
- On change: Activated when a change is detected.
${Section2}.setVisible(me.isChecked()) where Section2 is the
control ID of a Section view.

## Methods

For detailed information on the available methods for Switch, see the Switch JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.