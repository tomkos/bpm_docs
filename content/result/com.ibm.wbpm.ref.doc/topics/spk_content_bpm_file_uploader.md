# BPM File Uploader

## Configuration properties

<!-- image -->

The content management
configuration properties for the BPM File Uploader view are shown in the following
table:

| Content management property   | Description                                                          | Data type       |
|-------------------------------|----------------------------------------------------------------------|-----------------|
| Upload properties             | Specifies the matching properties to be uploaded with this document. | NameValuePair[] |
| Hide in portal                | Prevent the document from displaying in Process Portal.              | Boolean         |

The behavior configuration properties for the BPM File Uploader view are shown in the
following table:

| Behavior configuration property   | Description                                                                                                                                                                   | Data type   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Max file size (MB)                | The maximum allowed file size for uploads.                                                                                                                                    | Decimal     |
| Auto upload                       | Uploads selected files automatically. If this option is not selected, use the startUpload() method instead                                                                    | Boolean     |
| File types allowed                | The valid file types. You can select a file type from the drop-down menu, or select Custom to specify your own file type. When this field is empty, all file types are valid. | FileType[]  |
| Add documents to folder           | Adds new documents to the current process folder when the coach is running within the scope of a process.                                                                     | Boolean     |

The appearance configuration properties for the BPM File Uploader view are shown in the
following table:

| Appearance configuration property   | Description                                                                                                                                                                           | Data type   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Color style                         | The color style for this view.                                                                                                                                                        | String      |
| Shape style                         | The shape of this view.                                                                                                                                                               | String      |
| Size style                          | The style of this view.                                                                                                                                                               | String      |
| Outline                             | Outline-only means the view only shows its color-based style when hovered over.                                                                                                       | Boolean     |
| Icon                                | The name of the icon name. For example, calendar, clock-o, camera, cloud-upload, bell, info, or file-text. For a comprehensive list, see The Icons. Note: The fa- prefix is optional. | String      |
| Hide Browse button                  | When true, the browse button is not displayed. When false, it is displayed.                                                                                                           | Boolean     |
| Hide file name                      | When true, the file name is not displayed. When false, it is displayed.                                                                                                               | Boolean     |

## Events

The formula configuration property for the BPM File Uploader view is shown in the following
table:

| Formula configuration property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Data type   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Document name formula            | The expression or formula that is used to set the name of the document to be uploaded. You can set the name by using a static string or you can set it dynamically by using a formula. For example: To use static text, enclose the text in double quotation marks: "Static Document Name" To use a formula to dynamically calculate the name, use the following format: ${Text1}.getText()  For more information about using formulas, see Binding data and configuration options. | String      |

The BPM File Uploader view has the following types of event handlers:

- On load: Activated when the view loads. For
example:me.setAssociatedWithProcessInstance(true)
- On file added: Activated when a file is added to the view. For
example:${DocInfoDlg}.show()
- On file selected: Activated when a file in the view is selected. For
example:${DocInfoDlg}.show()
- On upload complete: Activated when a file uploads successfully. For
example:${BPMFileList1}.refresh()
- On upload error: Activated when an error occurs while uploading a file. For
example:console.error("Error occurred: " + error)

Depending
on the specific event, you can use JavaScript logic to modify the effects of the view. You can find
more information about using events with views in User-defined events.

## Methods

For detailed information on the available methods for BPM File Uploader, see the BPM File Uploader JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.