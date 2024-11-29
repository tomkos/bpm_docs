# Document Reference

## Configuration properties

<!-- image -->

The content management
configuration properties for the Document Reference view are shown in the following
table:

| Content management property   | Description                                                                                     | Data type   |
|-------------------------------|-------------------------------------------------------------------------------------------------|-------------|
| Folder path                   | The folder path of the server name from where the folder or file is referenced.                 | String      |
| Server name                   | The name of the external content management server from where the folder or file is referenced. | String      |
| Parent folder ID              | The folder ID of the instance where the reference is created.                                   | String      |
| Instance ID                   | The ID of the instance where the reference is created.                                          | String      |

The behavior configuration properties for the Document Reference view are shown in the
following table:

| Behavior configuration property   | Description                                                                                      | Data type                               |
|-----------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------|
| Is folder referenced              | If the property is set to false, folders are not shown for the reference.                        | Boolean                                 |
| Is file referenced                | If the property is set to false, files are not shown for the reference.                          | Boolean                                 |
| Selection mode                    | The selection mode for items in the table.                                                       | String                                  |
| ECM get related folders service   | Gets the folder information for the ECM servers listed in the Process Application Settings page. | Default Get Related ECM Folders Service |

The appearance configuration properties for the Document Reference view are shown in the
following table:

| Appearance configuration property   | Description                                                                                                                                                                  | Data type   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Table style                         | The table style for this view.                                                                                                                                               | String      |
| Color style                         | The color style for this view.                                                                                                                                               | String      |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String      |

## Events

- On reference created: Activated when a reference is created. For example:
console.log("Reference created: "+reference.referenceName
- On cancel: Activated when a reference creation is canceled. For
example:console.log("Reference dialog is closed.")
- On error: Activated when there is an error while creating a reference. For
example:alert("Creating reference failed")

Depending
on the event, you can use JavaScript logic to modify the effects of the view. For more information
about using events with views, see User-defined events.

## Methods

For detailed information on the available methods for Document Reference, see the Document Reference JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.