### Methods

### Parent

### Helpers

<!-- image -->

| Label placement:      | The label position. {Top | Left}                                                                                  | LabelPlacement   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|------------------|
| Label width:          | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String           |
| Width:                | Width of the QRCode view                                                                                          | String           |
| Height:               | Height of the QRCode view                                                                                         | String           |
| Background image URL: | The background image URL for the QR view.                                                                         | String           |

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

| Name   | Type     | Default   | Description        |
|--------|----------|-----------|--------------------|
| height | {string} |           | backgroundImageURL |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description                                            |
|--------|----------|-----------|--------------------------------------------------------|
| level  | {string} |           | "L"=Level L | "M"="Level M | "Q"=Level Q | "H"=Level H |

| Name   | Type     | Default   | Description               |
|--------|----------|-----------|---------------------------|
| height | {string} |           | the height of the control |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description              |
|--------|----------|-----------|--------------------------|
| label  | {string} |           | the label of the control |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name   | Type      | Default   | Description                 |
|--------|-----------|-----------|-----------------------------|
| flag   | {boolean} |           | the visibility of the label |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type     | Default   | Description     |
|--------|----------|-----------|-----------------|
| QRCode | {string} |           | the QRCode text |

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

| Name   | Type     | Default   | Description              |
|--------|----------|-----------|--------------------------|
| width  | {string} |           | the width of the control |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |