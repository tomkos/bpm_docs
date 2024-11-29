# Collapsible panel

A collapsible panel can contain other views, such as text boxes or other collapsible panels. When
you include more collapsible panels in a group, only one nested panel can be expanded at a time
inside its parent, while the other panels are collapsed.

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                           | Data type   |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Color style                         | Specifies a color style for the collapsible panel. The colors correspond to variables in the specified theme.                                                                                         | String      |
| Width                               | Specifies the width of the collapsible panel. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed. | String      |
| Height                              | Specifies the height of the collapsible panel in px (pixels) or em units. If no unit type is specified, then px is assumed.                                                                           | String      |

| Behavior configuration property   | Description                                                                                                                                                 | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Initially collapsed               | Specifies whether the section is collapsed when the page is loaded.                                                                                         | Boolean     |
| Panel group name                  | Specifies the name of a group of collapsible panels. Within the same group, only one panel can be expanded at a time, while the other panels are collapsed. | String      |

## Example

To create a collapsible section in your UI page, add a Collapsible panel view to the page layout.
In the Configuration properties, under Behavior, set the
Initially collapsed property to false, and then enter
a panel group name, for example G1. Under Appearance,
set Color style to Info, Width
to 50%, and Height to 0.4em.
Save your changes. At run time, the resulting collapsible section is displayed expanded, its header
colored in light blue. To collapse the section, click the small minus (-) icon that is displayed in
the right upper corner of the section header.

## Events

Set
or modify the event handlers for the view in the Events properties. You can set
events to be triggered programmatically or when a user interacts with the view. For information about how to define and code events, see User-defined events.

- On load: Activated when the page loads. For example:
if(me.isExpand()){me.collapse();}
- On expand: Activated when the section is expanded. For example:
me.setColorStyle("S")where "S" (standing for
Success) must be defined in "me.setColorStyle("S")".
- On collapse: Activated when the section is collapsed. For example:
me.setColorStyle("");${CollapsiblePanel1}.expand()

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for Collapsible panel, see the Collapsible panel JavaScript
API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.