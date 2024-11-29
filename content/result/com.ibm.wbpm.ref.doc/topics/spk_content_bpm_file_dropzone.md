# BPM File Dropzone

## Configuration properties

<!-- image -->

The content management
configuration properties for the BPM File Dropzone view are shown in the following
table:

| Content management property   | Description                                                          | Data type       |
|-------------------------------|----------------------------------------------------------------------|-----------------|
| Hide in portal                | Prevent the document from displaying in Process Portal.              | Boolean         |
| Upload properties             | Specify the properties that you want to associate with the document. | NameValuePair[] |

The behavior configuration properties for the BPM File Dropzone view are shown in the
following table:

| Behavior configuration property   | Description                                                                                                | Data type   |
|-----------------------------------|------------------------------------------------------------------------------------------------------------|-------------|
| Auto upload                       | Automatically upload dropped files.                                                                        | Boolean     |
| Auto-remove uploaded files        | Remove uploaded files from the dropzone.                                                                   | Boolean     |
| Max file size (MB)                | The maximum file size (in megabytes) for uploads.                                                          | Decimal     |
| File types allowed                | Select a file type, or specify custom to specify your own file type. When empty, all file types are valid. | FileType[]  |
| Add documents to folder           | Adds new documents to the current process folder when the coach is running within the scope of a process.  | Boolean     |

The appearance configuration properties for the BPM File Dropzone view are shown in the
following table:

| Appearance configuration property   | Description                                         | Data type   |
|-------------------------------------|-----------------------------------------------------|-------------|
| Show border                         | Show a border around the file upload area.          | Boolean     |
| Square border corners               | Make the border corners square, instead of rounded. | Boolean     |
| Show thumbnails                     | Show thumbnails of files in the dropzone area.      | Boolean     |

## Events

- On load: Activated when the view is loaded. For example:
me.setAssociatedWithProcessInstance(true)
- On file added: Activated when a file is added to the view. For
example:${DocInfoDlg}.show()
- On file selected: Activated when a file is selected in the view. For
example:${DocInfoDlg}.show()
- On file removed: Activated when a file is removed from the view. For
example:return confirm("Are you sure you want to remove this?")
- On upload complete: Activated when files are successfully uploaded. For
example:${BPMFileList1}.refresh()
- On upload error: Activated when there is an error while uploading files
operations. For example:console.error("Error occurred: " + error)

Depending
on the event, you can use JavaScript logic to modify the effects of the view. For more information
about using events with views, see User-defined events.

## Methods

For detailed information on the available methods for BPM File Dropzone, see the BPM File Dropzone JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.