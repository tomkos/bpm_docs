### Methods

### Parent

### Helpers

<!-- image -->

| Table style:   | The style of the table.                                                                                                                                                         |        |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Color style:   | The color style for the table display.                                                                                                                                          |        |
| Width:         | The width in pixels (px), percent (%), or em units (em). For example: 500px, 20%, 40em. If "px", "%", or "em" is not appended to the numeric value, the value defaults to "px". | String |

| Is folder referenced:            | Is folder referenced                                                                      | Boolean   |
|----------------------------------|-------------------------------------------------------------------------------------------|-----------|
| Is file referenced:              | Show files for the reference.                                                             | Boolean   |
| Selection mode:                  | Determines the selectability of table items.                                              |           |
| ECM get related folders service: | Gets the folder info for the ECM servers listed in the Process Application Settings page. |           |

| Folder path:      | The folder path of the server from where the folder or file is referenced.                      | String   |
|-------------------|-------------------------------------------------------------------------------------------------|----------|
| Server name:      | The name of the external content management server from where the folder or file is referenced. | String   |
| Parent folder ID: | The folder ID of the instance where the reference is created.                                   | String   |
| Instance ID:      | The ID of the instance where the reference is created.                                          | String   |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name      | Type     | Default   | Description      |
|-----------|----------|-----------|------------------|
| potential | {string} |           | The filter text. |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name       | Type     | Default   | Description      |
|------------|----------|-----------|------------------|
| serverName | {string} |           | The server name. |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name                     | Type      | Default   | Description                                                      |
|--------------------------|-----------|-----------|------------------------------------------------------------------|
| instanceId               | {string}  |           | The process instance ID for which the reference will be created. |
| parentFolderId           | {string}  |           | The ID of the parent folder where the reference will be created. |
| isFolderReferenceEnabled | {boolean} |           | Enables the use of folder references (when 'true').              |
| isFileReferenceEnabled   | {boolean} |           | Enables the use of document references (when 'true').            |

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