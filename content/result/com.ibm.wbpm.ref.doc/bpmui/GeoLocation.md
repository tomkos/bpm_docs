### Methods

### Parent

### Helpers

<!-- image -->

| Monitoring mode:   | When true the geolocation of the device is continuously monitored, when false the Timeout option determines how often the location is updated.\r\nNote\: This option can impact battery life {Once on Load | Continuous | Initially Stopped}   | GeoMonitoringMode   |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| High accuracy:     | Enable high accuracy location detection. Note\: This option can impact battery life for mobile devices                                                                                                                                         | Boolean             |
| Timeout:           | When true, specifies the timeout interval in ms.  The default is 6000, i.e. 6 seconds                                                                                                                                                          | Integer             |
| Max age of data:   | The maximum age (in milliseconds) of the geolocation data. The default is 0 ms.                                                                                                                                                                | Integer             |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type      | Default   | Description          |
|--------|-----------|-----------|----------------------|
| lat1   | {decimal} |           | the first latitude   |
| lon1   | {decimal} |           | the first longitude  |
| lat2   | {decimal} |           | the second latitude  |
| lon2   | {decimal} |           | the second longitude |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name                | Type      | Default   | Description                                                                            |
|---------------------|-----------|-----------|----------------------------------------------------------------------------------------|
| data                | {Object}  |           | Value of bound data. The type of this parameter must match the type of the bound data. |
| createPseudoBinding | {boolean} |           | If set to true, creates a pseudo binding if there is no current binding.               |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |