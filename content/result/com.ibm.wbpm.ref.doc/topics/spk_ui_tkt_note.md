# Note

## Data binding

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                 | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of a note in pixels, percent, or em units. For example: 50px or 20% or 0.4em. The default unit is pixel, in case no other is specified. | String      |
| Label style                         | Specifies the header style for the note label. Default Heading 1 Heading 2 Heading 3                                                                        | String      |
| Color style                         | Specifies a color style for the view. The colors correspond to variables in the specified theme. The default color style is Default (gray).                 | String      |

## Example

In this example, the following appearance configuration properties are set for the Note view:

- Text formula is set to "Read this note".
- Label style is set to Heading 1.
- Color style is set to Info.

In the General properties tab, the name given to the
Label is Note.

These properties and their values result in a text area on a blue background that displays a blue
level 1 header labeled Note, followed by the message: Read this
note.

## Events

| Formula configuration property   | Description                                                                                              | Data type   |
|----------------------------------|----------------------------------------------------------------------------------------------------------|-------------|
| Text formula                     | Formula or expression used to calculate the note text.For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads.
- On click: Activated when a note is clicked.

## Methods

For detailed information on the available methods for Note, see the Note JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.