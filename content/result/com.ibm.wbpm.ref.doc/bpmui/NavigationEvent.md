### Methods

### Parent

### Helpers

<!-- image -->

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name                | Type     | Default   | Description                                                    |
|---------------------|----------|-----------|----------------------------------------------------------------|
| confirmationMessage | {string} |           | Text of the confirmation message                               |
| eventData           | {*}      |           | Additional data (payload) associated with the navigation event |

| Name      | Type   | Default   | Description                                                    |
|-----------|--------|-----------|----------------------------------------------------------------|
| eventData | {*}    |           | Additional data (payload) associated with the navigation event |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type   | Default   | Description                               |
|--------|--------|-----------|-------------------------------------------|
| *      |        |           | eventData Data to add to navigation event |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |