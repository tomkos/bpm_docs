### Methods

### Parent

### Helpers

<!-- image -->

| Debugging on:   | Sets the debug switch to true when checked.  The switch causes views to log debug information in the console.   | Boolean         |
|-----------------|-----------------------------------------------------------------------------------------------------------------|-----------------|
| Parameters:     | List of parameters which can be accessed by the getParameter() method.                                          | NameValuePair[] |

| Show log:         | Useful when testing on Mobile devices such as the iPad where the browser log is not easy to retrieve in real-time.   | Boolean   |
|-------------------|----------------------------------------------------------------------------------------------------------------------|-----------|
| Last entry first: | Insert new entries at the top of the log window instead of at the end                                                | Boolean   |

| Locale:       | Forced locale                                                               | String   |
|---------------|-----------------------------------------------------------------------------|----------|
| I18N Service: | Specifies the I18N Ajax service that supplies internationalization to views |          |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type     | Default   | Description       |
|--------|----------|-----------|-------------------|
| name   | {string} |           | Name of parameter |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name      | Type      | Default   | Description   |
|-----------|-----------|-----------|---------------|
| debugging | {boolean} |           | Debug flag    |

| Name      | Type     | Default   | Description                                                                        |
|-----------|----------|-----------|------------------------------------------------------------------------------------|
| direction | {string} |           | {AUTO|LTR|RTL} Use AUTO to reset to the default page text direction set by IBM BPM |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |