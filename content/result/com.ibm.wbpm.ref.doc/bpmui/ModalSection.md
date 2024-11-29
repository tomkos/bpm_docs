### Methods

### Parent

### Helpers

<!-- image -->

| Modal placeholder width:   | Width of modal "well" in which the modal content is displayed (in px, em, %). \r\nNote\: If a modal width is specified, what is contained in it should always be sized to 100% width, otherwise the modal section may not close reliably when the dark area is clicked.   | String           |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Show buttons:              | Show the buttons in the modal.                                                                                                                                                                                                                                            | Boolean          |
| Text on primary button:    | The text on the button that allows you to confirm the action in the modal. For example, Save or OK.                                                                                                                                                                       | String           |
| Text on secondary button:  | The text on the button that allows you to dismiss the action in the modal. For example, Close or Cancel.                                                                                                                                                                  | String           |
| Color style:               | The color style of the primary button. {Default | Primary | Info | Success | Warning | Danger | Dark}                                                                                                                                                                     | ButtonColorStyle |

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

| Name   | Type      | Default   | Description                                                                                                                                                                                               |
|--------|-----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flag   | {boolean} |           | sets the boolean for whether a user can close the modal section by clicking outside of the modal section.  If true, user can close the modal section by clicking outside of the modal section (gray area) |

| Name   | Type     | Default   | Description                                                                                                                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"PRI"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|ERROR|ERR"|"E"|"G"=Danger |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name    | Type      | Default   | Description                                                                     |
|---------|-----------|-----------|---------------------------------------------------------------------------------|
| enabled | {boolean} |           | Enabled/read-only flag (true to enable button, false to disable/make read-only) |

| Name   | Type     | Default   | Description           |
|--------|----------|-----------|-----------------------|
| str    | {string} |           | Primary button's text |

| Name   | Type     | Default   | Description             |
|--------|----------|-----------|-------------------------|
| str    | {string} |           | Secondary button's text |

| Name   | Type      | Default   | Description                       |
|--------|-----------|-----------|-----------------------------------|
| value  | {boolean} |           | True for showing the button group |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name   | Type      | Default   | Description                                |
|--------|-----------|-----------|--------------------------------------------|
| flag   | {boolean} |           | true to show the section, false to hide it |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |