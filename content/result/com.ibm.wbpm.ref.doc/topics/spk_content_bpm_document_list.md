# BPM Document List

| Action                    | Description                                            |
|---------------------------|--------------------------------------------------------|
| Update                    | Replaces the file contents and updates its properties. |
| Display document versions | Shows the versions of the document.                    |
| Delete                    | Removes the document.                                  |

For additional information, see the topics listed under the topic Enabling document support.

## Restrictions and limitations

None

## Data binding

| Binding description                                                     | Data type       |
|-------------------------------------------------------------------------|-----------------|
| The ECMDocumentInfo binding contains the URL for the selected document. | ECMDocumentInfo |

## Configuration properties

<!-- image -->

| Content management property      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Data type       |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Allow create                     | Allow file creation.                                                                                                                                                                                                                                                                                                                                                                                                                                          | Boolean         |
| Allow updates                    | Allow files in the list to be updated.                                                                                                                                                                                                                                                                                                                                                                                                                        | Boolean         |
| Allow document deletions         | If disabled, documents cannot be deleted through this view.                                                                                                                                                                                                                                                                                                                                                                                                   | Boolean         |
| Confirm on deletion              | Show a confirmation dialog before deleting files.                                                                                                                                                                                                                                                                                                                                                                                                             | Boolean         |
| Allow revisions display          | Show versions of files in the list.                                                                                                                                                                                                                                                                                                                                                                                                                           | Boolean         |
| Max results                      | The maximum number of files to display. When set, the Max results value indicates the number of documents to be fetched at a time. When no value is set, by default, Max results fetches 10 documents at a time. When more documents than the configured Max results value are displayed, a Load More button appears, which you can click to fetch the next set of Max results documents. The Load More button is not shown when there are no more documents. | Integer         |
| Associated with process instance | Display files associated with this process instance only.                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean         |
| Match rule                       | Select whether displayed articles should match any or all of the filter rules.                                                                                                                                                                                                                                                                                                                                                                                | String          |
| Filter                           | Properties to filter files on. These properties are available only if they were assigned when the files were uploaded.                                                                                                                                                                                                                                                                                                                                        | NameValuePair[] |
| Default upload name              | The default name of the document that you want to create. To allow a user to edit the name, select the User editable check box.                                                                                                                                                                                                                                                                                                                               | String          |
| User editable                    | Allows the user to edit the default name of the document in the Create Document window. The default name is set in the Default upload name option.                                                                                                                                                                                                                                                                                                            | Boolean         |
| Add properties                   | Add the properties in the Upload Properties table to the document. The default value is false.                                                                                                                                                                                                                                                                                                                                                                | Boolean         |
| Upload properties                | If you selected Add Properties, the properties you want to associate with the document.                                                                                                                                                                                                                                                                                                                                                                       | NameValuePair[] |
| Hide in portal                   | Prevent the document from displaying in Process Portal.                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean         |

| Behavior configuration property   | Description                                                                                                                                                                          | Data type   |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Show footer                       | Show the footer.                                                                                                                                                                     | Boolean     |
| Show table stats                  | Show table statistics, for example, "Showing 1 to 5 of 59 entries".                                                                                                                  | Boolean     |
| Show pager                        | Show the pager.                                                                                                                                                                      | Boolean     |
| Initial page size                 | Initial maximum number of entries to be shown per page.                                                                                                                              | Integer     |
| Max file size                     | The maximum file size (in megabytes) for uploads.                                                                                                                                    | Decimal     |
| File types allowed                | Select a file type, or specify custom to specify your own file type. When empty, all file types are valid. For file upload troubleshooting information, see MIME type determination. | FileType[]  |
| Add documents to folder           | Adds new documents to the current process folder when the coach is running within the scope of a process.                                                                            | Boolean     |

| Appearance configuration property   | Description                         | Data type        |
|-------------------------------------|-------------------------------------|------------------|
| Table style                         | The table style for this view.      | String           |
| Color style                         | The color style for this view.      | String           |
| Columns                             | The columns to display in the list. | FileListColumn[] |

## Events

- On file clicked: Activated when a file is clicked. For example:
console.log(doc.fileName)
- On revision file clicked: Activated when a revision is clicked. For
example:console.log(doc.fileName)
- On error: Activated when there is an error while executing operations in
the view. For example:alert("There has been an error: "+message)

Depending
on the event, you can use JavaScript logic to modify the effects of the view. For more information
about using events with views, see User-defined events.

## Methods

For detailed information on the available methods for BPM Document List, see the BPM Document List JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.