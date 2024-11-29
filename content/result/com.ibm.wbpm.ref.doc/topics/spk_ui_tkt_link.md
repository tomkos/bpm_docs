# Link

## Data binding

Set or modify the data binding for the view in the General properties tab.
The Link view can be bound to a Boolean variable. If bound, the variable value is
set to true when the link is clicked.

You can use the Link view to link to an outside web page or you can use it to create a
cross-reference to a different view or section within the same page or view, for example, a link
within a table.

## Configuration properties

Under
Configuration, set or modify the appearance and behavior properties for the
view. Under Events, set the formula configuration properties.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                             | Data type   |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Width                               | Specifies the width of the link text in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If no unit type is specified, then px is assumed.                      | String      |
| Text alignment                      | Specifies the alignment of the link text, in relation to the width of the view. The available options are Left, Center, and Right.                                                      | String      |
| Color style                         | Specifies a color style for the link. The colors correspond to variables in the specified theme. This setting applies only to the text and not to the label.                            | String      |
| Size style                          | Specifies the text size. This setting applies to both label and text.                                                                                                                   | String      |
| Text weight                         | Specifies the text weight. This setting applies only to the text and not to the label. Default Slim Normal Semi-Bold Bold                                                               | String      |
| Label placement                     | Specifies the placement of the label in relation to the text. The available options are Top and Left.  Note that a left placement of the label changes the specified width of the link. | String      |
| Label width                         | The width of the label. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed.           | String      |

| Behavior configuration property   | Description                                                                                                                                                                                                                     | Data type   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Tab index                         | The tabbing sequence index. The tab indices start at 1 and can be set sparsely. For example, you can use 1, 5, 10. The Tab index property controls the tabbing sequence when you move between UI areas by pressing the Tab key. | Integer     |
| Link text                         | Provides the text for the link.                                                                                                                                                                                                 | String      |
| Prevent multiple clicks           | Prevents users from clicking the link more than once. This property is applicable only to links of Boundary Event type.                                                                                                         | Boolean     |
| Link type                         | Specifies the type of the link. The available options are: Boundary Event: Emits a boundary event within a service. URL: Links to an outside web page.                                                                          | String      |
| Link URL                          | The URL address for the link. This property is applicable only to links of URL type.                                                                                                                                            | String      |
| Open in same window               | Opens the web page with the same-domain URL address in the same browser window. This property is applicable only to links of URL type, and opens URLs that are in the same domain.                                              | Boolean     |

## Example

1 Add a Link view to your page at the appropriate location, and then set the followingconfiguration properties for the link:
    1. Under Behavior, in the Link text field, type in
Take me to IBM Support, set the Link type to
URL, and then enter https://www.ibm.com/support in the
Link URL. Leave Open in same window clear.
    2. Under Appearance, set Text alignment to
Left, Color style to Muted,
Size style to Large, Text
weight to Slim, and Label placement to
Top.
2. Save your changes.

At run time, the result is a light-gray link that reads "Take me to IBM Support". When clicked,
the link takes you to the IBM Support portal.

## Events

Set or modify the
formula configuration properties and the event handlers for the view in the
Events properties. You can set events to be triggered programmatically or when
a user interacts with the view. For information on how to define and code
events, see User-defined events.

| Formula configuration property   | Description                                                                                                | Data type   |
|----------------------------------|------------------------------------------------------------------------------------------------------------|-------------|
| Text formula                     | The formula or expression for calculating the link text.For more information about formulas, see Formulas. | String      |

The Link view has the following types of event handlers:

- On load: Activated when the page loads. For example:
me.setText("Link to Google")
- On click: Activated when the link is clicked, before leaving the page. If
the evaluated expression returns false, the click does not fire the boundary event.
For example: return me.getText() != ""
- On boundary event: Activated when the flow reaches a stay-on-page event
after the boundary event is fired through the Link view. For more
information, see the context.trigger() property in the The coach view context object
topic. For example: me.setColorStyle("G")

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
More information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for Link, see the Link JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.