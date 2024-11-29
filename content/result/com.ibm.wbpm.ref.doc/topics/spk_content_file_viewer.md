# File Viewer

## Integrating with an Enterprise Content Management server

To integrate the File Viewer coach view with an Enterprise Content Management (ECM) server, the
process application must have a connection to that server. See Adding an Enterprise Content Management server. For
information about building ECM services, see Building a service that integrates with an ECM system or a BPM store. For additional
information, see the topics under Enabling document support.

## Data binding

| Binding description              | Data type       |
|----------------------------------|-----------------|
| Contains the URL for a document. | ECMDocumentInfo |

## Configuration properties

Set or modify configuration properties for the File Viewer view, such as appearance and behavior
properties, in the Configuration properties tab. Set the formula
configuration properties in the Events tab.

<!-- image -->

The behavior configuration properties for the File Viewer view are listed in the following
table:

| Behavior configuration property   | Description                                                            | Data type   |
|-----------------------------------|------------------------------------------------------------------------|-------------|
| Fit content to viewer width       | If this option is enabled, the view fits the content to viewer width.  | Boolean     |
| Fit content to viewer height      | If this option is enabled, the view fits the content to viewer height. | Boolean     |

The appearance configuration properties for the File Viewer view are listed in the following
table:

| Appearance configuration property   | Description                                                                                                                                                                  | Data type   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Controls placement                  | Specifies the placement of views within the viewer panel.                                                                                                                    | String      |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |
| Height                              | The height of the view in px (pixels) or em units. If no unit type is specified, px is assumed.                                                                              | String      |

## Events

Set or modify the
formula configuration properties and the event handlers for the view in the
Events properties. You can set events to be triggered programmatically or when
a user interacts with the view. For information on how to define and code
events, see User-defined events.

- On load: Activated when the page loads. For example,
:me.setValue(0.00);

Depending on the specific event, you can use JavaScript logic to modify the effects of the view.
You can find more information about using events with views in User-defined events.

## Methods

For detailed information on the available methods for File Viewer, see the File Viewer JavaScript API.

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.

## Limitation

There is no configuration option in the File Viewer to set any character encoding to allow the
document content to be displayed in its own encoding.