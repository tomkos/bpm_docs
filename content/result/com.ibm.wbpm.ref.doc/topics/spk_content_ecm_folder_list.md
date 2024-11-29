# ECM Folder List

## Configuration properties

<!-- image -->

The content management
configuration properties for the ECM Folder List view are shown in the following
table:

| Content management property   | Description                                                 | Data type   |
|-------------------------------|-------------------------------------------------------------|-------------|
| Allow document deletions      | If disabled, documents cannot be deleted through this view. | Boolean     |
| Confirm on deletion           | Show a confirmation dialog before deleting files.           | Boolean     |

The content management advanced configuration properties for the ECM Folder List view are
shown in the following
table:

| Content management advanced property   | Description                                 | Data type   |
|----------------------------------------|---------------------------------------------|-------------|
| ECM server configuration name          | The ECM server to be used.                  | String      |
| Folder path                            | The default folder path is the root folder. | String      |

The behavior configuration properties for the ECM Folder List view are shown in the
following table:

| Behavior configuration property   | Description                                                         | Data type   |
|-----------------------------------|---------------------------------------------------------------------|-------------|
| Show footer                       | Show the footer.                                                    | Boolean     |
| Show table stats                  | Show table statistics, for example, "Showing 1 to 5 of 59 entries". | Boolean     |
| Show pager                        | Show the pager.                                                     | Boolean     |
| Initial page size                 | Initial maximum number of entries to be shown per page.             | Integer     |
| Selection mode                    | The selection mode for items in the table.                          | String      |
| Hide drill-up                     | Hides the folder drill-up table entry.                              | Boolean     |

The appearance configuration properties for the ECM Folder List view are shown in the
following table:

| Appearance configuration property   | Description                                                                                                                                                                  | Data type           |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Table style                         | The table style for this view.                                                                                                                                               | String              |
| Color style                         | The color style for this view.                                                                                                                                               | String              |
| Max thumbnail size                  | The maximum size (in bytes) for a thumbnail to be displayed.                                                                                                                 | Integer             |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String              |
| Height                              | The height of the view in px (pixels) or em units. If no unit type is specified, px is assumed.                                                                              | String              |
| Columns                             | The columns to display in the list.                                                                                                                                          | ECMFileListColumn[] |

## Events

- On load: Activated when a file loads. For
example:console.log(me.getFolderCount())
- On folder clicked: Activated when a folder is clicked. For
example:window.open(url, '\_blank');
- On folder deleted: Activated when a folder is deleted. For
example:console.log('Folder Deleted.');
- On refreshed: Activated when the folder list is refreshed. For
example:console.log("Folder List refreshed")
- On error: Activated when there is an error while refreshing. For
example:alert("There has been an error : "+message)
- On row selected: Activated when a user selects the folder: For
example:console.log("Folder Selected")

Depending
on the specific event, you can use JavaScript logic to modify the effects of the view. You can find
more information about using events with views in User-defined events.

## Methods

For detailed information on the available methods for ECM Folder List, see the ECM Folder List JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.