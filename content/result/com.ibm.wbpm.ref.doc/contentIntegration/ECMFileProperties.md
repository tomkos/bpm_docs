### Methods

### Parent

### Helpers

<!-- image -->

| ECM server configuration name:   | The ECM server to use. The default server is the embedded ECM server.                                                                                                                                                                                                    | String               |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Default document type:           | The document type for the first use. The default document type is "cmis:document".                                                                                                                                                                                       | String               |
| Default document properties:     | Select the variable to use for the default properties of the ECM document. When an ECM document is created, the document list contains the default values for the document properties. The values might be read-only or hidden from users when they create the document. | ECMDefaultProperty[] |

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

| Name   | Type     | Default   | Description           |
|--------|----------|-----------|-----------------------|
| id     | {string} |           | The document type ID. |

| Name   | Type     | Default   | Description      |
|--------|----------|-----------|------------------|
| id     | {string} |           | The document ID. |

| Name   | Type     | Default   | Description        |
|--------|----------|-----------|--------------------|
| name   | {string} |           | The document name. |

| Name   | Type     | Default   | Description           |
|--------|----------|-----------|-----------------------|
| id     | {string} |           | The document type ID. |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name                     | Type       | Default   | Description                                    |
|--------------------------|------------|-----------|------------------------------------------------|
| defaultPropertyValueList | {Object[]} |           | The list of properties with the default value. |

| Name       | Type     | Default   | Description      |
|------------|----------|-----------|------------------|
| serverName | {string} |           | The server name. |

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