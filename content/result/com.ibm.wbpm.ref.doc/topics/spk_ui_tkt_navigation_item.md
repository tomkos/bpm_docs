# Navigation item

## Configuration properties

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                            | Data type           |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Icon name                           | The icon name. To use icons for navigation items, see http://fontawesome.io/icons for a list of icon keywords. Note that the "fa-" prefix is optional. | String              |
| Icon location                       | The location of the icon relative to the navigation item text. Left Right                                                                              | InputGroupButtonLoc |

| Behavior configuration property   | Description                                                                                                                                               | Data type          |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Prevent multiple clicks           | Prevents the user from clicking the navigation item button more than once.                                                                                | Boolean            |
| Navigation menu item type         | Specifies the type of navigation item, which can be either a link to an internal app page or an external link. Internal app link External URL             | NavigationItemType |
| Associated page                   | The page identifier for the internal app link. If the navigation item represents a subflow UI, you can also add it here to highlight the navigation item. | PageId[]           |
| Target URL                        | The valid URL of the external link that your navigation item points to.                                                                                   | String             |

## Events

- On load: Activated when the page loads. For
example:console.log(“Navigation item loaded”);
- On click: Activated when the navigation item is clicked. For
example:me.setText(“New navigation item label”);
- On boundary event: Activated when the flow reaches a stay-on-page event
after the boundary event is fired through the Link view. For
example:alert("Stay on Page status '" + status + "'")

Depending on the specific event, you can use JavaScript logic to modify the effects of the
view. More information on using events with views is found in the topic
User-defined events.

## Methods

For detailed information on the available methods for Navigation item, see the Navigation item JavaScript
API..

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.