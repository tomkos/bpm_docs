# Notification

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                 | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Color style                         | Specifies a color style for the view. The colors correspond to variables in the specified theme. The default color style is Default (gray).                                                                 | ColorStyle  |
| Icon                                | Specifies the notification icon name. For example: calendar, clock-o, camera, cloud-upload, bell, info, file-text. See Font Awesome V4.7.0 for a complete list of icons.  By default, no icon is specified. | String      |

## Example

In this example, the following appearance configuration properties are set for the Notification
view:

- Notification formula is set to "Enter comments
below".
- Color style is set to Danger.
- Icon is set to comment.

These properties and their values result in a speech balloon icon beside some text on a red
background that says "Enter comments below".

## Events

| Formula configuration property   | Description                                                                                                   | Data type   |
|----------------------------------|---------------------------------------------------------------------------------------------------------------|-------------|
| Notification formula             | An expression to be used as the value of the notification. For more information about formulas, see Formulas. | String      |

- On load: Activated when the page loads.
- On click: Activated when the notification is clicked.

## Methods

For detailed information on the available methods for Notification, see the Notification JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.