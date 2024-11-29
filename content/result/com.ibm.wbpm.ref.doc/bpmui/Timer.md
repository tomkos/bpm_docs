### Methods

### Parent

### Helpers

<!-- image -->

| Timeout value (msecs.):   | Specify the number of milliseconds before this timer "pops".                                   | Integer   |
|---------------------------|------------------------------------------------------------------------------------------------|-----------|
| Repeatable:               | When enabled, the timer will repeat until stopped based on the interval set in the timeout     | Boolean   |
| Initially stopped:        | When true the timer does not start running until specifically started with the start() method. | Boolean   |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type      |   Default | Description            |
|--------|-----------|-----------|------------------------|
| ticks  | {integer} |         0 | Number of ticks to set |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name   | Type      | Default   | Description                                             |
|--------|-----------|-----------|---------------------------------------------------------|
| flag   | {boolean} |           | {true | false} Set to true to make the timer repeatable |

| Name    | Type      | Default   | Description                    |
|---------|-----------|-----------|--------------------------------|
| timeout | {integer} |           | Milliseconds until timer ticks |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |