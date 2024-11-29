# BPM File List

## Configuration properties

<!-- image -->

The content management
configuration properties for the BPM File List view are shown in the following
table:

| Content management property      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Data type       |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Allow updates                    | Allow files in the list to be updated.                                                                                                                                                                                                                                                                                                                                                                                                                        | Boolean         |
| Allow document deletions         | If disabled, documents cannot be deleted through this view.                                                                                                                                                                                                                                                                                                                                                                                                   | Boolean         |
| Confirm on deletion              | Show a confirmation dialog before deleting files.                                                                                                                                                                                                                                                                                                                                                                                                             | Boolean         |
| Display version                  | Show versions of files in the list.                                                                                                                                                                                                                                                                                                                                                                                                                           | Boolean         |
| Show all versions                | Show all versions of each file.                                                                                                                                                                                                                                                                                                                                                                                                                               | Boolean         |
| Max results                      | The maximum number of files to display. When set, the Max results value indicates the number of documents to be fetched at a time. When no value is set, by default, Max results fetches 10 documents at a time. When more documents than the configured Max results value are displayed, a Load More button appears, which you can click to fetch the next set of Max results documents. The Load More button is not shown when there are no more documents. | Integer         |
| Associated with process instance | Display files associated with this process instance only.                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean         |
| Match rule                       | Select whether displayed articles should match any or all of the filter rules.                                                                                                                                                                                                                                                                                                                                                                                | String          |
| Filter                           | Properties to filter files on. These properties are available only if they were assigned when the files were uploaded.                                                                                                                                                                                                                                                                                                                                        | NameValuePair[] |

The behavior configuration properties for the BPM File List view are shown in the
following table:

| Behavior configuration property   | Description                                                         | Data type   |
|-----------------------------------|---------------------------------------------------------------------|-------------|
| Show footer                       | Show the footer.                                                    | Boolean     |
| Show table stats                  | Show table statistics, for example, "Showing 1 to 5 of 59 entries". | Boolean     |
| Show pager                        | Show the pager.                                                     | Boolean     |
| Initial page size                 | Initial maximum number of entries to be shown per page.             | Integer     |

The appearance configuration properties for the BPM File List view are shown in the
following table:

| Appearance configuration property   | Description                                                                                                                                                                  | Data type        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Table style                         | The table style for this view.                                                                                                                                               | String           |
| Color style                         | The color style for this view.                                                                                                                                               | String           |
| Max thumbnail size                  | The maximum size (in bytes) for a thumbnail to be displayed.                                                                                                                 | Integer          |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String           |
| Height                              | The height of the view in px (pixels) or em units. If no unit type is specified, px is assumed.                                                                              | String           |
| Columns                             | The columns to display in the list.                                                                                                                                          | FileListColumn[] |

## Events

- On load: Activated when the view is loaded. For example:
me.getDocumentCount()
- On file clicked: Activated when a file is clicked. For
example:console.log(doc.fileName)
- On document deleted: Activated when a file is deleted. For
example:console.log("File Deleted")
- On refreshed: Activated when the view is refreshed. For
example:console.log("List refreshed")
- On error: Activated when there is an error while refreshing or deleting in
the file list. For
example:alert("There has been an error with the refresh")
- On update requested: An inline event logic to be called when the user
clicks the update icon. Alternatively, the name of a function to be called when the event is fired.
For example:console.log("Document update request: "+doc.fileName)
- On version display requested: Activated when the document version icon is
clicked. For example:alert("Update document: "+doc.fileName)

Depending
on the event, you can use JavaScript logic to modify the effects of the view. For more information
about using events with views, see User-defined events.

## Methods

For detailed information on the available methods for BPM File List, see the BPM File List JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.