### Methods

### Parent

### Helpers

<!-- image -->

| Color style:   | Color-based styling for this view {Default | Primary | Info | Success | Warning | Danger}            | TooltipColorStyle   |
|----------------|------------------------------------------------------------------------------------------------------|---------------------|
| Striped:       | Set stripes on the progress bar.                                                                     | Boolean             |
| Active:        | Make the stripes within the progress bar move (only has an effect when Striped is true).             | Boolean             |
| Radius:        | The roundness of the corners of the progress bar                                                     | String              |
| Width:         | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String              |
| Height:        | Height in px, em\r\nFor example\: 50px, 0.4em. If no unit is specified, px is assumed                | String              |

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

| Name   | Type     | Default   | Description                                                                                                                                             |
|--------|----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|"G"=Danger |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
|        | {string} |           | height        |

| Name   | Type      | Default   | Description                                                                                                                                    |
|--------|-----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| value  | {decimal} |           | Maximum value of bar (what constitutes 100%). Note that it is possible for progress to be set past this value, though it will not be apparent. |

| Name   | Type      | Default   | Description     |
|--------|-----------|-----------|-----------------|
| value  | {decimal} |           | Progress of bar |

| Name   | Type     | Default   | Description                                  |
|--------|----------|-----------|----------------------------------------------|
| radius | {string} |           | Radius of curvature for progress bar corners |

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

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
|        | {string} |           | width         |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |