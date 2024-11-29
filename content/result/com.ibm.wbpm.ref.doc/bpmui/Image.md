### Methods

### Parent

### Helpers

<!-- image -->

| Border radius:   | Radius of curvature for the image corners.                                                           | String   |
|------------------|------------------------------------------------------------------------------------------------------|----------|
| Width:           | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String   |
| Height:          | Height in px, em\r\nFor example\: 50px, 0.4em. If no unit is specified, px is assumed.               | String   |

| Prevent multiple clicks:   | Prevent the user from clicking the image more than once.                                                                                | Boolean   |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Image URL type:            | URL type. Note: For images that are not hosted on the local server, use External. {Web | External}                                      | URLType   |
| Image app acronym:         | The acronym of the process app or toolkit that contains the image.                                                                      | String    |
| Default image URL:         | If the view is not bound, this is the URL for the image.                                                                                | String    |
| Default image URL type:    | If the view is not bound this is the URL type. Note: For images that are not hosted on the local server, use External. {Web | External} | URLType   |
| Default image app acronym: | The default acronym of the process app or toolkit that contains the image.                                                              | String    |

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

| Name   | Type     | Default   | Description             |
|--------|----------|-----------|-------------------------|
| height | {string} |           | the height of the image |

| Name   | Type     | Default   | Description                              |
|--------|----------|-----------|------------------------------------------|
| img    | {string} |           | Image url                                |
| type   | {string} |           | "External" | "Web" | "Server" | "Design" |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| radius | {string} |           | Border radius |

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

| Name   | Type     | Default   | Description            |
|--------|----------|-----------|------------------------|
| width  | {string} |           | the width of the image |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |