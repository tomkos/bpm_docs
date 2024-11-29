# Button

## Data binding

Set or modify the data binding for Button in the General properties tab.
The view is bound to a Boolean variable.

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                   | Data type           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Color style                         | The color style for the button. The colors correspond to variables in the specified theme. The available options are Default, Primary, Success, Danger, Dark.                                 | String              |
| Shape                               | The shape of the button.                                                                                                                                                                      | String              |
| Size                                | The size of the button.                                                                                                                                                                       | String              |
| Outline only                        | The button displays its color-based style only when you hover a cursor over it. By default, this property is not selected.                                                                    | Boolean             |
| Icon                                | The name of the icon that precedes the text on the button. For example: calendar, clock-o, camera, cloud-upload, bell, info, file-text. See Font Awesome V4.7.0 for a complete list of icons. | String              |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed..                 | String              |
| Icon location                       | The location of the icon relative to the button text. The available options are: Left (default) Right                                                                                         | InputGroupButtonLoc |
| Outline only                        | Shows the outline and hides the solid fill of the button in the selected color style. The solid fill is shown at hover over.                                                                  | Boolean             |
| Ghost style                         | Shows the button in the selected color style with no outline and no solid fill. The ghost button appears on a light grey background at hover over.                                            | Boolean             |

| Behavior configuration property   | Description                                                                                                                                                                                                                     | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |
| Prevent multiple clicks           | Prevents users from clicking the button more than once.                                                                                                                                                                         | Boolean     |

## Example

1. Under Formula, specify the button name as a static text enclosed in
double quotation marks, for example "OK".
2. Under Behavior, select Prevent multiple
clicks.
3. Under Appearance, set Color style to
Success, and leave Shape style and Size
style set to Default. For Icon, type in
check.
4. Save your changes.

The result is a rectangular button that reads OK on a green background.
The text on the button is preceded by a check mark.

## Events

Set or modify the
formula configuration properties and the event handlers for the view in the
Events properties. You can set events to be triggered programmatically or when
a user interacts with the view. For information on how to define and code
events, see User-defined events.

| Formula configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                  | Data type   |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Label formula                    | The expression or formula that is used to set the label for the Button view. You can set the label either by using a static string or dynamically by using a formula. For example: Static text enclosed in double quotation marks:"Static Button Text" A formula to dynamically calculate the label:${"Text1"}.getText()  For more information about formulas, see Formulas. | String      |

Button has the following types of event handlers:

- On load: Activated when the coach or page loads. For example:
console.log("Button loaded")
- On click: Activated when the link is clicked, before leaving the page. If
the evaluated expression returns false, the click does not fire the boundary event.
For example: return ${Text1}.isValid();
- On boundary event: Activated when the flow reaches a stay-on-page event
after the boundary event is fired through the Link view.  For more
information, see the context.trigger() property in the The coach view context object
topic. For example: alert("Stay on Page status '" + status + "'")

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for Button, see the Button JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.