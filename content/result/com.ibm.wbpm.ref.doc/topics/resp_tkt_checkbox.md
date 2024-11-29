# Check Box (deprecated)

| As a check box   | As a pair of radio buttons   | As a switch   |
|------------------|------------------------------|---------------|
|                  |                              |               |

## Data binding

| Binding description                                                                                           | Data type   |
|---------------------------------------------------------------------------------------------------------------|-------------|
| Records the state of the instance, such as selected or not selected if the selection instance is a check box. | Boolean     |

## Theme definitions

The design mode of the theme editor contains a simulation of this view. If you hover over the
simulation, it lists the theme definitions that determine the appearance of the view. For
information on the theme editor, see Creating themes.

## Configuration properties

<!-- image -->

| Configuration property   | Description                                                                                                                                                                                                                                            | Data type       |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Show as                  | Select whether the check box instance displays as a check box, a radio button, or switch.The default value is Checkbox                                                                                                                                 | ShowAsSelection |
| True label               | Set the text for the "true" choice.The default text is "Yes".                                                                                                                                                                                          | String          |
| False label              | Set the text for the "false" choice. The default text is "No".                                                                                                                                                                                         | String          |
| Style > Switch on color  | Set the color of the background for the on or selected position of the check box when it is showing as a switch.                                                                                                                                       | String          |
| Style > Switch off color | Set the color of the background for the off or unselected position of the check box when it is showing as a switch.                                                                                                                                    | String          |
| Style > Text size        | Set the size of the text for the label and the amount of padding around the text. For example, to make the label more readable on smart phones, you can set this configuration option to Large for the small screen size. The default value is Medium. | String          |