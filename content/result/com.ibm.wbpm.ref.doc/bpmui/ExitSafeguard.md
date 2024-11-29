### Methods

### Parent

### Helpers

<!-- image -->

| Challenge on exit by default:   | When true a challenge is presented to the user if they attempt to close the browser window                                                | Boolean   |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Exit challenge message:         | Additional message to display when challenging an exit. All browsers display a challenge, but some will not show this additional message. | String    |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type     | Default   | Description             |
|--------|----------|-----------|-------------------------|
| msg    | {string} |           | Message to be displayed |

| Name   | Type      | Default   | Description                              |
|--------|-----------|-----------|------------------------------------------|
| flag   | {boolean} |           | Set to true to challenge exit by default |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |