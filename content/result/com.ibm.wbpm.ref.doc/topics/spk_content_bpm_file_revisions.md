# BPM File Revisions

## Configuration properties

<!-- image -->

The appearance
configuration properties for the BPM File Revisions view are shown in the following table:

| Appearance configuration property   | Description                                                                                                                                                                  | Data type   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Table style                         | The table style for this view.                                                                                                                                               | String      |
| Color style                         | The color style for this view.                                                                                                                                               | String      |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |
| Height                              | The height of the view in px (pixels) or em units. If no unit type is specified, px is assumed.                                                                              | String      |

## Events

- On load: Activated when the view loads. For
example:${Data1}.setData(me.getVersionCount())
- On file clicked: Activated when a version of the file is clicked. For
example:window.open(url, '\_blank');
- On refreshed: Activated when the view is refreshed. For
example:console.log("List refreshed")
- On refresh error: Activated when there is an error while the file is
refreshing. For example:alert("There has been an error with the
refresh")

Depending
on the specific event, you can use JavaScript logic to modify the effects of the view. You can find
more information about using events with views in User-defined events.

## Methods

For detailed information on the available methods for BPM File Revisions, see the BPM File Revisions JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.