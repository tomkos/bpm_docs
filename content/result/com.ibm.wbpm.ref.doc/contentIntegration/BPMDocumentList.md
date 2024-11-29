### Methods

### Parent

### Helpers

<!-- image -->

| Table style:   | The style of the table.                |                  |
|----------------|----------------------------------------|------------------|
| Color style:   | The color style for the table display. |                  |
| Columns:       | The columns to display in the list.    | FileListColumn[] |

| Show footer:             | Show the table footer.                                                                                                                                       | Boolean    |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Show table stats:        | Show table statistics. For example, "Showing 1 to 5 of 59 entries".                                                                                          | Boolean    |
| Show pager:              | Display the pager.                                                                                                                                           | Boolean    |
| Initial page size:       | The initial maximum number of entries shown for each page.                                                                                                   | Integer    |
| Max file size (MB):      | The maximum file size for uploads.                                                                                                                           | Decimal    |
| File types allowed:      | Select a pre-configured file type from the drop-down list or select "Custom" to specify your own file type. When this field empty, all file types are valid. | FileType[] |
| Add documents to folder: | Add new documents to the current process folder when the coach is running within the scope of a process.                                                     | Boolean    |

| Allow create:                     | Allow the creation of files.                                                                                                                                                                                                                                                                                                                                                                                                                                  | Boolean              |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Allow updates:                    | Allow updates to the files in the list.                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean              |
| Allow document deletions:         | Enable documents to be deleted using this control.                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean              |
| Confirm on deletion:              | Show a confirmation dialog box before files are deleted.                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean              |
| Allow revisions display:          | Indicates whether versions are displayed for the files in the list.                                                                                                                                                                                                                                                                                                                                                                                           | Boolean              |
| Max results:                      | The maximum number of files to display. When set, the Max results value indicates the number of documents to be fetched at a time. When no value is set, by default, Max results fetches 10 documents at a time. When more documents than the configured Max results value are displayed, a Load More button appears, which you can click to fetch the next set of Max results documents. The Load More button is not shown when there are no more documents. | Integer              |
| Associated with process instance: | Display only those files that are associated with the current process instance.                                                                                                                                                                                                                                                                                                                                                                               | Boolean              |
| Match rule:                       | Select whether articles should be displayed based on any, all, or none of the filter rules defined in the "Filter" section. {None | All Properties | Any Property}                                                                                                                                                                                                                                                                                            | BPMDocumentMatchRule |
| Filter:                           | The properties in the "Filter" table that are used to filter files. These properties are only available if they were assigned when the files were uploaded.                                                                                                                                                                                                                                                                                                   | NameValuePair[]      |
| Default upload name:              | The default name of the document that you want to create. To allow a user to edit the name, select the "User editable" check box.                                                                                                                                                                                                                                                                                                                             | String               |
| User editable:                    | Allows the user to edit the default name of the document in the Create Document window. The default name is set in the "Default upload name" option.                                                                                                                                                                                                                                                                                                          | Boolean              |
| Add properties:                   | Add the properties specified in the "Upload properties" table to the document.                                                                                                                                                                                                                                                                                                                                                                                | Boolean              |
| Upload properties:                | Add the properties in the "Upload properties" table to the document (if the Add Properties check box is selected).                                                                                                                                                                                                                                                                                                                                            | NameValuePair[]      |
| Hide in portal:                   | Prevent the BPM document from being displayed in the portal.                                                                                                                                                                                                                                                                                                                                                                                                  | Boolean              |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description    |
|--------|----------|-----------|----------------|
| label  | {string} |           | The new label. |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

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