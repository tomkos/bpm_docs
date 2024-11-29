# Pop-up menu

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                          | Data type   |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Show label                          | Provides the label of the pop-up view. When Show label is selected, the pop-up menu displays the label of the contained view. By default, the label of the contained view is hidden. | Boolean     |
| Label placement                     | Specifies the label position: Top Left                                                                                                                                               | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.        | String      |
| Horizontal alignment                | Specifies the horizontal position of the pop-up menu relative to the contained view. Left Right                                                                                      | String      |
| Vertical alignment                  | Specifies the vertical position of the pop-up menu relative to the contained view. Top Bottom                                                                                        | String      |
| Shadow                              | Adds a shadow to the pop-up menu frame.                                                                                                                                              | Boolean     |
| Width                               | Specifies the width of the envelope that wraps the view.                                                                                                                             | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Data type      |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Pin menu                          | Prevents the pop-up menu from closing automatically when a menu item is clicked or when the view loses the focus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Boolean        |
| Menu items                        | Specifies the items in the menu: Command (String) The command that runs when this menu item is selected. Item type (String) Specifies the menu item type: Label Separator Section Header     Icon (String) The icon that you want to add to the specified menu item. Leave blank for no icon. Item text (String) The text to display for the specified menu item (not applicable to separators). Badge shape (String) The badge shape you want to use. None Square Rounded   Badge color (String) The color style to use for the badge. The colors correspond to variables in the specified theme. Badge text (String) The text that is added to the badge. | MenuItemSpec[] |

## Example

1. Under Appearance, set Label placement to
Top, Color style to Warning,
Button location to Left, Button
type to Menu, and Button info to
Click to see Menu Items.
2. Under Events, in On button click, enter the
following line of
code:${Popup\_Menu1}.setMenuVisible(!${Popup\_Menu1}.isMenuVisible{})

1. Under Appearance, set Label placement to
Top, Horizontal alignment to
Left, Vertical alignment to
Bottom, select Shadow, and set
Width to 25%.
2. Under Behavior, select Pin menu.
3 For Menu items , click plus (+) to add three rows to the table, each withthe following values:
    - Row 1: For Command, enter 1, set Item
type to Label, for Item text, enter
Item 1, set Badge shape to
Rounded, Badge color to
Primary, and for Badge text enter
1.
    - Row 2: For Command, enter 2, set Item
type to Label, for Item text, enter
Item 2, set Badge shape to
Rounded, Badge color to Info,
and for Badge text enter 2.
    - Row 3: For Command, enter 3, set Item
type to Label, for Item text, enter
Item 3, set Badge shape to
Rounded, Badge color to
Success, and for Badge text enter
3.

<!-- image -->

## Events

- On load: Activated when the page loads. For
example:me.setMenuVisible(true)
- On item click: Activated when an item is clicked. Applicable only for
labels, not applicable for section headers. For
example:${Text1}.setLabelPosition(command) //sets the label position of the Text1 control to the value of command
//the value of command is set in the menu item command property

## Methods

For detailed information on the available methods for Pop-up menu, see the Pop-up menu JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.