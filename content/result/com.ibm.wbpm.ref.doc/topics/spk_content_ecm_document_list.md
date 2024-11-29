# ECM Document List

## Integrating with an Enterprise Content Management server

| Action                    | Description                                            |
|---------------------------|--------------------------------------------------------|
| Update                    | Replaces the file contents and updates its properties. |
| Display document versions | Shows the versions of the document.                    |
| Delete                    | Removes the document.                                  |

To integrate the
ECM Document List view with an Enterprise Content Management (ECM) server, the process application
must have a connection to that server. See Adding an Enterprise Content Management server. For information about
building ECM services, see Building a service that integrates with an ECM system or a BPM store. For additional information, see
the topics under Enabling document support.

## Restrictions and limitations

When you configure the displayed folder for the ECM document list through a script at run time,
it might display the contents of the root folder. You must click Refresh in
the doc list viewer control to display the correct folder.

## Data binding

| Binding description                                                     | Data type       |
|-------------------------------------------------------------------------|-----------------|
| The ECMDocumentInfo binding contains the URL for the selected document. | ECMDocumentInfo |

## Configuration properties

<!-- image -->

The content management
configuration properties for the ECM Document List view are shown in the following
table:

| Content management property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Data type                   |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Allow create                  | Allow users to add a document to the Enterprise Content Management document repository. The default value is false.                                                                                                                                                                                                                                                                                                                                           | Boolean                     |
| Allow updates                 | Boolean indicator of whether files in the list can be updated.                                                                                                                                                                                                                                                                                                                                                                                                | Boolean                     |
| Allow document deletions      | If this option is disabled, files cannot be deleted by using this view.                                                                                                                                                                                                                                                                                                                                                                                       | Boolean                     |
| Confirm on deletion           | Show a confirmation dialog before deleting files.                                                                                                                                                                                                                                                                                                                                                                                                             | Boolean                     |
| Allow revisions display       | Boolean indicator of whether files in the list have their versions that are displayed.                                                                                                                                                                                                                                                                                                                                                                        | Boolean                     |
| Max results                   | The maximum number of files to display. When set, the Max results value indicates the number of documents to be fetched at a time. When no value is set, by default, Max results fetches 10 documents at a time. When more documents than the configured Max results value are displayed, a Load More button appears, which you can click to fetch the next set of Max results documents. The Load More button is not shown when there are no more documents. | Integer                     |
| Filter                        | Properties to filter files on. These properties are assigned at upload (if they are assigned).                                                                                                                                                                                                                                                                                                                                                                | NameValuePair[]             |
| CMIS query filter             | A string of text containing the Content Management Interoperability Services (CMIS) query.                                                                                                                                                                                                                                                                                                                                                                    | String                      |
| Search service                | The service to use when searching for documents.                                                                                                                                                                                                                                                                                                                                                                                                              | ECM Document Search Service |

The content management advanced configuration properties for the ECM Document
List view are shown in the following
table:

| Content management advanced property.   | Description                                                                                | Data type   |
|-----------------------------------------|--------------------------------------------------------------------------------------------|-------------|
| ECM server configuration name           | The ECM server to be used.                                                                 | String      |
| Document object type ID                 | Specify the documentObjectType for the documents. This must be defined in your ECM server. | String      |
| Folder path                             | The default folder path is the root folder.                                                | String      |

The behavior configuration properties for the ECM Document List view are shown
in the following table:

| Behavior configuration property   | Description                                                                                                                                                                                                                                                              | Data type                  |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Show footer                       | Show the footer.                                                                                                                                                                                                                                                         | Boolean                    |
| Show table stats                  | Show table statistics, for example, "Showing 1 to 5 of 59 entries".                                                                                                                                                                                                      | Boolean                    |
| Max file size (MB)                | The maximum file size (in megabytes) for uploads.                                                                                                                                                                                                                        | Decimal                    |
| Show pager                        | Show the pager.                                                                                                                                                                                                                                                          | Boolean                    |
| Initial page size                 | Initial maximum number of entries to be shown per page.                                                                                                                                                                                                                  | Integer                    |
| Default document properties       | Select the variable to use for the default properties of the ECM document. When an ECM document is created, the document list contains the default values for the document properties. The values might be read-only or hidden from users when they create the document. | List of ECMDefaultProperty |
| File types allowed                | Select a file type, or specify custom to specify your own file type. When empty, all file types are valid. For file upload troubleshooting information, see MIME type determination.                                                                                     | FileType[]                 |

The appearance configuration properties for the ECM Document
List view are shown in the following table:

| Appearance configuration property   | Description                         | Data type        |
|-------------------------------------|-------------------------------------|------------------|
| Table style                         | The table style for this view.      | String           |
| Color style                         | The color style for this view.      | String           |
| Columns                             | The columns to display in the list. | FileListColumn[] |

## Events

- On file clicked: Activated when a file is clicked. For
example,console.log(doc.fileName)
- On error: Activated when there is an error while running operations in the
document list. For example,alert("There has been an error: "+message)

Depending
on the specific event, you can use JavaScript logic to modify the effects of the view. More
information on using events with views is found in the topic User-defined events.

## Methods

For detailed information on the available methods for ECM Document List, see the ECM Document List JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.