### Methods

### Parent

### Helpers

<!-- image -->

| Color style:        | The color-based style for this control.                                                                                                                                                                          |         |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Shape style:        | The shape-based style for this control.                                                                                                                                                                          |         |
| Size style:         | The size-based style for this control.                                                                                                                                                                           |         |
| Outline:            | The color style of the control is the only thing displayed when the cursor is hovered over the control.                                                                                                          | Boolean |
| Icon:               | The icon name, such as "calendar", "clock-o", "camera", "cloud-upload", "bell", "info", and "file-text". For a comprehensive list of icons, see http://fontawesome.io/icons. Note: The "fa-" prefix is optional. | String  |
| Hide Browse button: | Hide the Browse button.                                                                                                                                                                                          | Boolean |
| Hide file name:     | Hide the name of the file.                                                                                                                                                                                       | Boolean |

| Max file size (MB):      | The maximum file size (in megabytes) for uploads.                                                                                                               | Decimal    |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Auto upload:             | Upload selected files automatically. If this option is not selected, use the startUpload() method instead.                                                      | Boolean    |
| File types allowed:      | Select a pre-configured file type from the drop-down list or select "Custom" to specify your own file type. When this field is empty, all file types are valid. | FileType[] |
| Add documents to folder: | Add new documents to the current process folder when the coach is running within the scope of a process.                                                        | Boolean    |

| Upload properties:   | Specifies the matching properties to upload with this document.   | NameValuePair[]   |
|----------------------|-------------------------------------------------------------------|-------------------|
| Hide in portal:      | Prevent the BPM document from being displayed in the portal.      | Boolean           |

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

| Name   | Type     | Default   | Description                                                                                                                                                                                                             |
|--------|----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | The color style. The available styles are: "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"PRI"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|ERROR|ERR"|"G"|"E"=Danger |

| Name       | Type     | Default   | Description                                    |
|------------|----------|-----------|------------------------------------------------|
| documentId | {string} |           | The document ID of the document to be updated. |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| title  | {string} |           | The new name. |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description                                                                    |
|--------|----------|-----------|--------------------------------------------------------------------------------|
| icon   | {string} |           | The new icon. For a list of available icons, see http://fontawesome.io/icons/. |

| Name   | Type     | Default   | Description    |
|--------|----------|-----------|----------------|
| label  | {string} |           | The new label. |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name    | Type      | Default   | Description                                                                            |
|---------|-----------|-----------|----------------------------------------------------------------------------------------|
| outline | {boolean} |           | Displays an outline for the browse button (when 'true'). The default value is 'false'. |

| Name   | Type     | Default   | Description                                                                                                        |
|--------|----------|-----------|--------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | The shape style. The available styles are: "Default"|"D"=Default | "ROUNDED"|"ROUND"|"R"=Rounded | "FLAT"|"F"=Flat |

| Name   | Type     | Default   | Description                                                                                                                                                       |
|--------|----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | The size style. The available styles are: "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large | "EXTRA-SMALL"|"X-SMALL"|"XS"|"X"=X-small |

| Name      | Type       | Default   | Description                        |
|-----------|------------|-----------|------------------------------------|
| propNames | {string[]} |           | The property names.                |
| propVals  | {ANY[]}    |           | The values for each property name. |

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

| Name   | Type   | Default   | Description                |
|--------|--------|-----------|----------------------------|
| file   | {File} |           | The file object to upload. |