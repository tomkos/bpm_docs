# Document Explorer

You can configure the Document Explorer coach view to add, view, or delete individual folders,
and add, view, check out, download, and remove documents. The Document Explorer uses services to
perform these functions.

- Specified directly by identifying the specific folder using the Folder ID
configuration option. If the folder is not on the default content management server, the
Server name configuration option identifies the server that contains the
folder.
- Derived by identifying an instance ID, which has an associated folder and server in the content
management system.
- Derived from the human service context, which has an associated folder in the content management
system.

1. To configure the ECM server, see Adding an Enterprise Content Management (ECM) server.
2. Drag a Document Explorer component to the coach.
3. Select the component.
4 Click Configuration , select Content managementadvanced . To configure the properties, see Configurationproperties and description: After you saved, you can access and manage the documents in the directory from the page.
    - Server name: Enter the ECM server name that you just added.
    - Folder ID: Obtain the ECM Folder ID that you want to manage from
ACCE.

There is an order of precedence to determining the root folder. A value in the folder ID
overrides any value in the instance ID. And any value in the instance ID overrides the use of the
human service context to derive the root folder.

The root folder contains folders and documents (files and their associated properties). The
actual content that any individual user sees in the Document Explorer and what that user can do with
the content depends on the permissions that the user has in the content management system. Assuming
that they have the appropriate permissions, users can add new folders and documents. From the action
menu of a folder or document, users can select an action to perform on that folder or document.

| Action           | Description                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open             | Displays the contents of the folder. The Document Explorer adds a breadcrumb trail so that the user can return to a parent folder.                                  |
| Rename           | Renames the folder.                                                                                                                                                 |
| Delete or remove | Deletes the folder or reference from the ECM server. The Remove option only deletes references from the Document Explorer. The reference remains on the ECM server. |

| Action                      | Description                                                                                                                                              |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| View                        | Displays the contents of the document in the browser or, if the browser does not support the file format, downloads the document.                        |
| Download                    | Downloads the document.                                                                                                                                  |
| Properties                  | Displays the properties that are associated with the document. The document type acts as a template to determine the properties of a specified document. |
| Check out                   | Locks the file. After checking out a file, you can check in a different version of it or change its properties.                                          |
| Check in or cancel check in | Unlocks the file. Use the check-in action to replace the file contents and update its properties. These actions are available only for locked files.     |
| Delete                      | Removes the document from the folder. The document still exists in the content management system.                                                        |

## Integrating with an Enterprise Content Management server

To integrate the Document Explorer view with an Enterprise Content Management (ECM) server, the
process application must have a connection to that server. See Adding an Enterprise Content Management (ECM) server. For information
about building ECM services, see Building a service that integrates with an ECM system or a BPM store. For
additional information, see the topics under Enabling document support.

## Restrictions

This view supports only the Required, Hidden,
and None visibility properties.

## Data binding

| Description                                                     | Data type              |
|-----------------------------------------------------------------|------------------------|
| Each ECMDocumentInfo binding contains the URL for the document. | ECMDocumentInfo (List) |

## Configuration properties

<!-- image -->

The content management
configuration properties for the Document Explorer view are shown in the following
table:

| Content management property     | Description                                                                                                                                                                                                                                                                                               | Data type            |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Last updated doc ID             | The document ID of the document that was created or updated.                                                                                                                                                                                                                                              | ECMID                |
| Default ECM document properties | The matching properties to be uploaded with this document.                                                                                                                                                                                                                                                | ECMDefaultProperty[] |
| Add BPM properties              | By default, properties are not added to new BPM documents. Enabling this configuration option adds the properties that are defined in the Upload BPM properties configuration option. If you want to control when the properties are added to the document, bind this configuration option to a variable. | Boolean              |
| Upload BPM properties           | If you selected Add BPM Properties, these are the properties that you want to associate with the document.                                                                                                                                                                                                | NameValuePair[]      |
| Hide in portal                  | Prevent the document from displaying in Process Portal.                                                                                                                                                                                                                                                   | Boolean              |

The content management advanced configuration properties for the Document
Explorer view are shown in the following
table:

| Content management advanced property   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Data type   |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Instance ID                            | Display the list of documents and folders for the instance ID. If the Folder ID property is configured, the Instance ID configuration is ignored. If neither the Folder ID nor the Instance ID properties are configured, the folder ID is derived from the human service context. For client-side human services, the tw.system.processInstance.id and tw.system.processInstance.processInstanceFolderId properties are used for the context. For heritage human services, the tw.system.currentProcessInstance.id and tw.system.currentProcessInstance.processInstanceFolderId properties are used for the context.                                                         | String      |
| Server name                            | If a folder ID is configured, use the name of the external ECM server. The server name can be typed into the field. You can also use a variable that represents the server name and add the variable to this field. For an external ECM server name, check the Process App Settings page for the external ECM systems available. If you are working with the internal ECM content repositories - BPM managed store, BPM content store, or BPM document store - constants are available for them. For example, ECMServerNames.IBM\_BPM\_MANAGED\_STORE.                                                                                                                           | String      |
| Folder ID                              | Display the list of documents and folders for the folder ID. If this property is configured, the instance ID is ignored. If the Folder ID property is not configured, the folder ID is derived from the associated Instance ID configuration. If an instance ID is not specified, the folder ID is derived from the human service context. For client-side human services, the tw.system.processInstance.id and tw.system.processInstance.processInstanceFolderId properties are used for the context. For heritage human services, the tw.system.currentProcessInstance.id and tw.system.currentProcessInstance.processInstanceFolderId properties are used for the context. | String      |
| Display parent case folder             | Display the contents of the parent case instance. This option is only valid for process instances in a case solution that are created through Case Builder. When this option is selected, the Server Name, Instance ID and Folder ID fields are ignored.                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean     |

The behavior configuration properties for the Document Explorer view are shown
in the following table:

| Behavior configuration property   | Description                                                                                                                                                                                                                                                          | Data type                               |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Show footer                       | Show the footer.                                                                                                                                                                                                                                                     | Boolean                                 |
| Show table stats                  | Show table statistics, for example, "Showing 1 to 5 of 59 entries".                                                                                                                                                                                                  | Boolean                                 |
| Show pager                        | Show the pager.                                                                                                                                                                                                                                                      | Boolean                                 |
| Initial page size                 | Initial maximum number of entries to be shown per page.                                                                                                                                                                                                              | Integer                                 |
| Confirm on deletion               | Show a confirmation dialog before deleting files.                                                                                                                                                                                                                    | Boolean                                 |
| Use document viewer               | Opens documents in an in-line document viewer when the View menu item is selected. If this option is not enabled, documents open in a new window.                                                                                                                    | Boolean                                 |
| Collapsible                       | The Document Explorer view is collapsible.                                                                                                                                                                                                                           | Boolean                                 |
| Initially collapsed               | The Document Explorer view is collapsed when the view opens.                                                                                                                                                                                                         | Boolean                                 |
| Refresh trigger                   | Indicates whether the contents of the view can be refreshed. Bind this property to a private boolean variable. When the value of the bound variable changes to true, the view is refreshed. After the view is refreshed, the value of the variable returns to false. | Boolean                                 |
| ECM get related folders service   | Gets the folder information for the ECM servers that are listed in the Process Application Settings page.                                                                                                                                                            | Default Get Related ECM Folders Service |
| Instance status                   | Determines whether the Document Explorer is editable or read-only. ACTIVE instances are editable. Instances with different status values (COMPLETED, FAILED, TERMINATED, and SUSPENDED) are read-only.                                                               | String                                  |
| Hide Document Explorer            | Hide the Document Explorer view. For example, for a business process definition (BPD).                                                                                                                                                                               | Boolean                                 |
| View clicked document             | Select this option to enable the default viewer for documents when you click their name.                                                                                                                                                                             | Boolean                                 |
| Enable on custom view             | Enable the execution of a custom script in the 'on custom view' event when the View menu action is selected.                                                                                                                                                         | Boolean                                 |
| Use document viewer               | Select this option to open documents in an in-line document viewer when the View menu action is selected. When this option is clear, documents open in a new window.                                                                                                 | Boolean                                 |

The appearance configuration properties for the Document Explorer view are shown
in the following table:

| Appearance configuration property   | Description                                                                                                                                                                  | Data type        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Table style                         | The table style for this view.                                                                                                                                               | String           |
| Color style                         | The color style for this view.                                                                                                                                               | String           |
| Width                               | The width of the view. You can specify the width in px (pixels), % (percent), or em units. For example, 50px, 20%, or 0.4em. If a unit type is not specified, px is assumed. | String           |
| Height                              | The height of the view in px (pixels) or em units. If no unit type is specified, px is assumed.                                                                              | String           |
| Columns                             | The columns to display in the list.                                                                                                                                          | FileListColumn[] |
| View Style                          | The style of the view (Default, Modern).                                                                                                                                     |                  |
| Show column headers                 | Select this option to enable viewing the column headers for the 'Default' View style. In the 'Modern' View style, this option gets automatically enabled at runtime.         | Boolean          |

## Events

- On load: Activated when the view is loaded. For
example,me.getRecordCount();
- On document clicked: Activated when a file is clicked. For
example,console.log(doc.fileName)
- On folder clicked: Activated when a folder is clicked. For
example,console.log("Folder clicked: "+folder.name)
- On delete: Activated when a document or folder is deleted. For
example,console.log("Object is deleted: "+record.name)
- On refreshed: Activated when the view is refreshed. For
example,console.log("List refreshed")
- On error: Activated when there is an error while running operations in the
view. For
example,console.log("There has been an error with the operation : "+error.action)
- On folder rename: Activated when a folder is renamed. For
example,console.log("Folder Renamed: "+folder.name);
- On remove from folder: Activated when an ECM folder or document reference
is removed from a BPM folder. For
example,console.log("Object removed from BPM : "+record.name)
- On document upload complete: Activated when a document is uploaded. For
example,console.log("Uploaded document ID : "+documentId)
- On reference created: Activated when a reference to an external folder or
document is created. For
example,console.log("Reference created : "+reference.referenceName)
- On custom view: Activated when a document is clicked or the View menu
option on the document is clicked. Enables customization to view documents in a custom document
viewer using a custom script. This event is enabled when 'Enable on custom view event' and 'View
Clicked document' configuration options are selected. Additional parameter: doc. For example,
// This would open the document in Navigator viewer only for Case Client.
var docObject = {};
if(doc.id.includes("idd\_")){
  docObject.id = doc.id.split("\_")[1];
}
docObject.caseAction = "documentClicked";
this.context.broadcastMessage(docObject);

Depending
on the event, you can use JavaScript logic to modify the effects of the view. For more information
about using events with views, see User-defined events.

## Methods

For detailed information on the available methods for Document Explorer, see the Document Explorer JavaScript
API.

## Additional resources

For
information about how to create a coach or page, see Building coaches.

For information about standard properties (General,
Configuration, Positioning,
Visibility, and HTML Attributes), see View properties. 
 For information about other UI and content management views,
see UI toolkit and Content Management toolkit.