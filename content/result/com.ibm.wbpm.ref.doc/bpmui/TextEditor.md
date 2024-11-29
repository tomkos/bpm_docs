### Methods

### Parent

### Helpers

<!-- image -->

| Width:   | The width in px, %, or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.   | String   |
|----------|---------------------------------------------------------------------------------------------------------|----------|
| Height:  | Height in px, % or em\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.        | String   |

| Tab index:       | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10.                                                                                                                                                                                                                                                                                                   | Integer         |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Palette colors:  | Default colors to populate text color palette with. Should be one less than the total number of spots in the palette (as determined by the number of rows and columns) in order to accomodate space for the option of removing colors. Name should represent the name of the color, and will be displayed as a tooltip when mousing over the color, while value should be the hexadecimal representation of the desired color. | NameValuePair[] |
| Palette columns: | The number of columns in the default text color palette. The default is 8                                                                                                                                                                                                                                                                                                                                                      | Integer         |
| Palette rows:    | The number of rows in the default text color palette. The default is 5.                                                                                                                                                                                                                                                                                                                                                        | Integer         |
| Show status bar: | Shows the status bar underneath the editor area, which displays the current html element being edited                                                                                                                                                                                                                                                                                                                          | Boolean         |

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

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| height | {string} |           | Editor height |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description               |
|--------|----------|-----------|---------------------------|
| label  | {string} |           | Label for the text editor |

| Name   | Type      | Default   | Description                            |
|--------|-----------|-----------|----------------------------------------|
| flag   | {boolean} |           | Set to true to make the label visible. |

| Name   | Type      | Default   | Description                    |
|--------|-----------|-----------|--------------------------------|
| vis    | {boolean} |           | Set to true to show status bar |

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | Tab indices start at 1 and may be set sparsely |

| Name   | Type     | Default   | Description                  |
|--------|----------|-----------|------------------------------|
| text   | {string} |           | Text to be set in the editor |

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

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| width  | {string} |           | editor width  |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |