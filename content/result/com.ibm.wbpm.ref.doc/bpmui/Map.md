### Methods

### Parent

### Helpers

<!-- image -->

| Map Type:   | Type of map to display eg\: Roadmap, Satellite, Hybrid {Roadmap | Satellite | Hybrid}                 | MapType   |
|-------------|-------------------------------------------------------------------------------------------------------|-----------|
| Zoom level: | 0 - 19 (Lowest zoom is 0 [whole world], highest is 19 [includes individual buildings when available]) | Integer   |
| Width:      | Width in px, %, em\r\nFor example\: 50px, 20%, 4em. If no unit is specified, px is assumed.           | String    |
| Height:     | Height in px, %, em\r\nFor example\: 50px, 20%, 4em. If no unit is specified, px is assumed           | String    |

| Disable panning:    | Disables map panning                                                                                       | Boolean   |
|---------------------|------------------------------------------------------------------------------------------------------------|-----------|
| Hide Zoom view:     | Hides the zoom view, preventing zooming in and out.                                                        | Boolean   |
| Hide Map Type view: | Prevents the user from changing map type.                                                                  | Boolean   |
| Hide scale view:    | Hides the scale from view                                                                                  | Boolean   |
| Hide rotate view:   | Prevent users from rotating the map                                                                        | Boolean   |
| Show marker:        | This is to indicate whether to show the marker or not (note\: must set longitude and latitude within view) | Boolean   |
| Latitude:           | Latitude to center the map on                                                                              | Decimal   |
| Longitude:          | Longitude to center map on                                                                                 | Decimal   |
| Map source:         | Map Provider eg\: OpenStreetMap and Bing Maps {OpenStreetMap | Bing Maps}                                  | MapSource |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name     | Type     | Default   | Description                                         |
|----------|----------|-----------|-----------------------------------------------------|
| location | {object} |           | the object that includes the latitude and longitude |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name      | Type      | Default   | Description   |
|-----------|-----------|-----------|---------------|
| latitude  | {decimal} |           | the latitude  |
| longitude | {decimal} |           | the longitude |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
|        | {string} |           |               |

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

| Name   | Type     | Default   | Description          |
|--------|----------|-----------|----------------------|
| width  | {string} |           | the width of the map |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |