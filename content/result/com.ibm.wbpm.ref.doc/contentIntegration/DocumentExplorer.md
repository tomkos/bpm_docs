### Methods

### Parent

### Helpers

<!-- image -->

| Instance ID:                | Specify the instance ID for which you want to display a list of associated documents and folders. If the "Folder ID" property is configured, the "Instance ID" property is ignored. If no folder ID or instance ID is specified, the folder ID is derived from the human service context. For client-side human services, the tw.system.processInstance.id and tw.system.processInstance.caseFolderId properties are used for the context. For heritage human services, the tw.system.currentProcessInstance.id and tw.system.currentProcessInstance.caseFolderId properties are used for the context.                                                                                    | String   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| Server name:                | If a folder ID is configured, specify the name of the external ECM server. The server name can be typed into the field. You can also use a variable that represents the server name and add the variable to this field. For an external ECM server name, check the Process App Settings page for the external ECM systems available.If you are working with the internal ECM content repositories - BPM managed store, BPM content store, or BPM document store - constants are available for them; for example, ECMServerNames.IBM\_BPM\_MANAGED\_STORE.                                                                                                                                    | String   |
| Repository name:            | The name of the repository that represents the repository configured with the server set using the 'Server name' configuration. This is optional, and would be used in the context of a Case Configuration, when Case is configured with more than one Target Object store, and 'Server name' is set to a predefined constant of IBM\_TargetObjectStore. The repository name would help in resolving IBM\_TargetObjectStore to the proper Target Object store. From a Case perspective you can set this configuration to the tosName variable.                                                                                                                                              | String   |
| Folder ID:                  | Specify the folder ID for which you want to display a list of associated documents and folders. If this property is configured, the instance ID is ignored. If the "Folder ID" property is not configured, the folder ID is derived from the associated "Instance ID" property. If an instance ID is not specified, the folder ID is derived from the human service context. For client-side human services, the tw.system.processInstance.id and tw.system.processInstance.caseFolderId properties are used for the context. For heritage human services, the tw.system.currentProcessInstance.id and tw.system.currentProcessInstance.caseFolderId properties are used for the context. | String   |
| Display parent case folder: | Display the contents of the parent case instance. This option is only valid for process instances in a case solution that are created through Case Builder. When this option is selected, the Server Name, Instance ID and Folder ID fields are ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                  | Boolean  |

| Table style:         | The style of the table.                                                                                                                                                          |                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Color style:         | The color style for the table display.                                                                                                                                           |                  |
| Width:               | The width in pixels (px), percent (%), or em units (em). For example: 500px, 20%, 40em. If "px", "%", or "em" is not appended to the numeric value, the value defaults to "px".  | String           |
| Height:              | The height in pixels (px), percent (%), or em units (em). For example: 500px, 20%, 40em. If "px", "%", or "em" is not appended to the numeric value, the value defaults to "px". | String           |
| Columns:             | The columns to display in the list.                                                                                                                                              | ExplorerColumn[] |
| View Style:          | The style of the view (Default, Modern).                                                                                                                                         |                  |
| Show column headers: | Select this option to enable viewing the column headers for the 'Default' View style. In the 'Modern' View style, this option gets automatically enabled at runtime.             | Boolean          |

| Show footer:                                    | Show the table footer.                                                                                                                                                                                                                                             | Boolean   |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Show table stats:                               | Show table statistics. For example, "Showing 1 to 5 of 59 entries".                                                                                                                                                                                                | Boolean   |
| Show pager:                                     | Display the pager.                                                                                                                                                                                                                                                 | Boolean   |
| Initial page size:                              | The initial maximum number of entries shown for each page.                                                                                                                                                                                                         | Integer   |
| Confirm on deletion:                            | Show a confirmation dialog box before files are deleted.                                                                                                                                                                                                           | Boolean   |
| Collapsible:                                    | Indicates whether the section can be collapsed.                                                                                                                                                                                                                    | Boolean   |
| Initially collapsed:                            | Indicates whether the section is collapsed when the view opens.                                                                                                                                                                                                    | Boolean   |
| Refresh trigger:                                | Indicates whether the contents of the control can be refreshed. Bind this property to a private variable.When the value of the bound variable changes to "true", the view is refreshed. After the view is refreshed, the value of the variable returns to "false". | Boolean   |
| ECM get related folders service:                | Gets the folder info for the ECM servers listed in the Process Application Settings page.                                                                                                                                                                          | String    |
| Instance status:                                | Determines whether the Document Explorer is editable or read-only. ACTIVE instances are editable. Instances with different status values (COMPLETED, FAILED, TERMINATED, and SUSPENDED) are read-only.                                                             | String    |
| Hide Document Explorer:                         | Hide the Document Explorer control, for example, for a business process definition (BPD).                                                                                                                                                                          | Boolean   |
| View clicked document:                          | Select this option to enable the default viewer for documents when you click their name.                                                                                                                                                                           | Boolean   |
| Enable on custom view event:                    | Enable the execution of a custom script in the 'on custom view' event when the View menu action is selected.                                                                                                                                                       | Boolean   |
| Use document viewer:                            | Select this option to open documents in an in-line document viewer when the View menu action is selected. When this option is clear, documents open in a new window.                                                                                               | Boolean   |
| ECM get default target repository name service: | Gets the default target repository name represented by the predefined ECM constant IBM\_TargetObjectStore.                                                                                                                                                          | String    |

| Last updated doc ID:             | The ID of the document on which a create or update operation was performed.                                                                                                                                                                                                                        | ECMID                |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Default ECM document properties: | Specifies the matching properties to upload with this document.                                                                                                                                                                                                                                    | ECMDefaultProperty[] |
| Add BPM properties:              | By default, properties are not added to new BPM documents. Enabling this configuration option adds the properties defined in the "Upload BPM properties" configuration option. If you want to control when the properties are added to the document, bind this configuration option to a variable. | Boolean              |
| Upload BPM properties:           | Adds the properties specified in the "Upload BPM properties" table to a BPM document (when the "Add BPM properties" option is selected).                                                                                                                                                           | NameValuePair[]      |
| Hide in portal:                  | Prevent the BPM document from being displayed in the portal.                                                                                                                                                                                                                                       | Boolean              |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name           | Type     | Default   | Description                           |
|----------------|----------|-----------|---------------------------------------|
| parentFolderId | {string} |           | The ID of the parent folder.          |
| newFolderName  | {string} |           | The name of the folder to be created. |
| serverName     | {string} |           | The name of the target server.        |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name      | Type      | Default   | Description                                                                                                  |
|-----------|-----------|-----------|--------------------------------------------------------------------------------------------------------------|
| isNewRoot | {boolean} |           | Reloads content from the root folder (when 'true'). If 'false', content is reloaded from the current folder. |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name         | Type      | Default   | Description                               |
|--------------|-----------|-----------|-------------------------------------------|
| folderId     | {string}  |           | The folder ID.                            |
| startRefresh | {boolean} |           | Enables a refresh to start (when 'true'). |

| Name         | Type      | Default   | Description                               |
|--------------|-----------|-----------|-------------------------------------------|
| instanceId   | {string}  |           | The process instance ID.                  |
| startRefresh | {boolean} |           | Enables a refresh to start (when 'true'). |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name    | Type      | Default   | Description                                               |
|---------|-----------|-----------|-----------------------------------------------------------|
| refresh | {boolean} |           | Refreshes the content of Document Explorer (when 'true'). |

| Name         | Type      | Default   | Description                               |
|--------------|-----------|-----------|-------------------------------------------|
| serverName   | {string}  |           | The server name.                          |
| startRefresh | {boolean} |           | Enables a refresh to start (when 'true'). |

| Name   | Type     | Default   | Description    |
|--------|----------|-----------|----------------|
| title  | {string} |           | The new title. |

| Name      | Type      | Default   | Description                                                                                                                                 |
|-----------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| valid     | {boolean} |           | Valid/invalid flag (true to set view valid, false to make it invalid - which typically shows the view with "invalid" styling and indicator) |
| errorText | {string}  |           | Validation error text to show on the invalid-styled view                                                                                    |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name     | Type      | Default   | Description                                                             |
|----------|-----------|-----------|-------------------------------------------------------------------------|
| visible  | {boolean} |           | Visibility flag (true to show view, false to hide)                      |
| collapse | {boolean} |           | Set to true to collapse the control space when visible is set to false. |

| MyView.setVisible(false, false); //Equivalent to MyView.hide()   |
|------------------------------------------------------------------|
| MyView.setVisible(false, true); // Sets visibility to "None"     |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |