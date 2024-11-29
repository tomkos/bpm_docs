### Methods

### Parent

### Helpers

<!-- image -->

| ECM server configuration name:   | The ECM server to use. The default server is the embedded ECM server.                                                          | String   |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------|----------|
| Folder path:                     | The default folder path is the root folder.                                                                                    | String   |
| Document object type ID:         | Specify the object type ID for the documents. The ID must be defined in your ECM server. The default value is "cmis:document". | String   |

| Table style:        | The style of the table.                                                                                                                                                          |                     |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Color style:        | The color style for the table display.                                                                                                                                           |                     |
| Max thumbnail size: | The maximum size (in bytes) to display a thumbnail.                                                                                                                              | Integer             |
| Width:              | The width in pixels (px), percent (%), or em units (em). For example: 500px, 20%, 40em. If "px", "%", or "em" is not appended to the numeric value, the value defaults to "px".  | String              |
| Height:             | The height in pixels (px), percent (%), or em units (em). For example: 500px, 20%, 40em. If "px", "%", or "em" is not appended to the numeric value, the value defaults to "px". | String              |
| Columns:            | The columns to display in the list.                                                                                                                                              | ECMFileListColumn[] |

| Show footer:       | Show the table footer.                                              | Boolean   |
|--------------------|---------------------------------------------------------------------|-----------|
| Show table stats:  | Show table statistics. For example, "Showing 1 to 5 of 59 entries". | Boolean   |
| Show pager:        | Display the pager.                                                  | Boolean   |
| Initial page size: | The initial maximum number of entries shown for each page.          | Integer   |
| Selection mode:    | Determines the selectability of table items.                        |           |

| Allow updates:            | Allow updates to the files in the list.                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean              |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Allow document deletions: | Enable files to be deleted using this control.                                                                                                                                                                                                                                                                                                                                                                                                                | Boolean              |
| Confirm on deletion:      | Show a confirmation dialog box before files are deleted.                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean              |
| Allow revisions display:  | Indicates whether versions are displayed for the files in the list.                                                                                                                                                                                                                                                                                                                                                                                           | Boolean              |
| Show all versions:        | Show all versions of each file in the list.                                                                                                                                                                                                                                                                                                                                                                                                                   | Boolean              |
| Max results:              | The maximum number of files to display. When set, the Max results value indicates the number of documents to be fetched at a time. When no value is set, by default, Max results fetches 10 documents at a time. When more documents than the configured Max results value are displayed, a Load More button appears, which you can click to fetch the next set of Max results documents. The Load More button is not shown when there are no more documents. | Integer              |
| Match rule:               | Select whether articles should be displayed based on any, all, or none of the filter rules defined in the "Filter" section. {None | All Properties | Any Property}                                                                                                                                                                                                                                                                                            | BPMDocumentMatchRule |
| Filter:                   | The properties in the "Filter" table that are used to filter files. These properties are only available if they were assigned when the files were uploaded.                                                                                                                                                                                                                                                                                                   | NameValuePair[]      |
| CMIS query filter:        | A string of text that contains the Content Management Interoperability Services (CMIS) query.                                                                                                                                                                                                                                                                                                                                                                 | String               |
| Search Service:           | Specify the service to use when searching for documents.                                                                                                                                                                                                                                                                                                                                                                                                      |                      |

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

| Name     | Type      | Default   | Description                                                              |
|----------|-----------|-----------|--------------------------------------------------------------------------|
| loadMore | {boolean} |           | Loads more records if any are available in the repository (when 'true'). |

| Name       | Type     | Default   | Description        |
|------------|----------|-----------|--------------------|
| searchText | {string} |           | The search string. |

| Name       | Type     | Default   | Description             |
|------------|----------|-----------|-------------------------|
| recordName | {string} |           | The name of the record. |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description          |
|--------|----------|-----------|----------------------|
| path   | {string} |           | The new folder path. |

| Name   | Type     | Default   | Description    |
|--------|----------|-----------|----------------|
| label  | {string} |           | The new label. |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name     | Type      | Default   | Description                                                               |
|----------|-----------|-----------|---------------------------------------------------------------------------|
| record   | {Object}  |           | The record to select.                                                     |
| selected | {boolean} |           | The selection value (where 'true' is selected and 'false' is deselected). |

| Name       | Type     | Default   | Description      |
|------------|----------|-----------|------------------|
| serverName | {string} |           | The server name. |
| folderpath | {string} |           | The folder path. |

| Name   | Type     | Default   | Description    |
|--------|----------|-----------|----------------|
| title  | {string} |           | The new label. |

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

| Name   | Type      | Default   | Description                                                             |
|--------|-----------|-----------|-------------------------------------------------------------------------|
| col    | {string}  |           | The column name.                                                        |
| asc    | {boolean} |           | Sorts the document list in ascending order in the column (when 'true'). |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |