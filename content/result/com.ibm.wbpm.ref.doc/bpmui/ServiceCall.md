### Methods

### Parent

### Helpers

<!-- image -->

| Called service:   | The service that runs when this view executes. Takes in the Input Value as an argument for the service, and outputs the result as the bound data of this view.   |         |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Input value:      | The value used as input to the service. If this value changes, the service is automatically invoked with the updated input.                                      | ANY     |
| Auto run:         | Run on start and whenever input data changes                                                                                                                     | Boolean |

| Name   | Type   | Default   | Description                                                                                |
|--------|--------|-----------|--------------------------------------------------------------------------------------------|
| input  | {ANY}  |           | Input data for the AJAX service (type will depend on the binding type of the AJAX service) |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type      | Default   | Description                                   |
|--------|-----------|-----------|-----------------------------------------------|
| flag   | {boolean} |           | Set to true to enable autorun for the service |

| Name   | Type   | Default   | Description    |
|--------|--------|-----------|----------------|
| data   | {*}    |           | the input data |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |