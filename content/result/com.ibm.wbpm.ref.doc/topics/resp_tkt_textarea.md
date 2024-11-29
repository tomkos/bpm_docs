# Text Area (deprecated)

## Restrictions and limitations

The Text Area view has a minimum height of 4em, which for the default font is 56px without the
label and 77px with the label. In the positioning properties, setting the minimum height to less
than these values visually truncates the Text Area instance to make it look partially hidden. If you
change the size of the default font in the theme, you change the truncation threshold
accordingly.

## Data binding

| Binding description                                                                                                                                                                                                                   | Data type   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| The bound data item contains a String value that the view displays. The String can initially be empty. If the visibility of the view is not read only, the view saves to the bound data item any String that the user enters into it. | String      |

## Theme definitions

The design mode of the theme editor contains a simulation of this view. If you hover over the
simulation, it lists the theme definitions that determine the appearance of the view. For
information on the theme editor, see Creating themes.

## Configuration properties

| Configuration property   | Description                                                                                                                                                                                                                                                   | Data type    |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Placeholder hint         | Add a brief description or example of the input required by the user. If the bound data item does not contain a value, users see the hint until they type in the field.                                                                                       | String       |
| Text area type           | Specify whether the text area has plain or rich text. The default value is Plain Text.If you select Rich Text, a palette for rich-text editing provides content-authoring views for standard text formatting, link editing, insertion of graphics, and so on. | TextAreaType |
| Disable HTML encoding    | Select to display the bound data without using HTML encoding.                                                                                                                                                                                                 | Boolean      |