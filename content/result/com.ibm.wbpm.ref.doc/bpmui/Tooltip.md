### Methods

### Parent

### Helpers

<!-- image -->

| Show label:          | Displays a label. If the Tooltip coach view has a label, it is displayed. Otherwise, the label of the coach view that is contained inside the Tooltip coach view is displayed. Note: The coach view Label visibility property is ignored.   | Boolean                    |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|
| Label placement:     | The placement of the label {Top | Left}                                                                                                                                                                                                     | LabelPlacement             |
| Label width:         | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                                                           | String                     |
| Width:               | The width of the envelope that wraps the contained view.                                                                                                                                                                                    | String                     |
| Color style:         | The color style of the tooltip. {Default | Primary | Info | Success | Warning | Danger}                                                                                                                                                     | TooltipColorStyle          |
| Horizontal position: | Horizontal positioning of the tooltip {Left | Center | Right}                                                                                                                                                                               | TooltipHorizontalAlignment |
| Vertical position:   | The vertical positioning of the tooltip. {Top | Bottom}                                                                                                                                                                                     | TooltipVerticalAlignment   |
| Size:                | Size-based styling for this view (default, large, extra-small) {Default | Large | Extra-Small}                                                                                                                                              | TooltipSizeStyle           |

| Show tooltip:   | When enabled, tooltip will be visible at load                                | Boolean   |
|-----------------|------------------------------------------------------------------------------|-----------|
| Show on hover:  | When enabled, tooltip will be displayed when user hovers over contained view | Boolean   |
| Text as HTML:   | Include HTML in the tooltip                                                  | Boolean   |

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

| Name   | Type     | Default   | Description                                                                                                                                                              |
|--------|----------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "ERROR"|"ERR"|"DANGER"|"E"|"G"=Danger |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name     | Type   | Default   | Description                                                                                      |
|----------|--------|-----------|--------------------------------------------------------------------------------------------------|
| (string) |        |           | style "Default"|"DEF"|"D"=Default | "LARGE"|"L"=Large | "EXTRA-SMALL"|"X-SMALL"|"XS"=Extra-Small |

| Name   | Type     | Default   | Description         |
|--------|----------|-----------|---------------------|
| text   | {string} |           | text of the tooltip |

| Name    | Type      | Default   | Description               |
|---------|-----------|-----------|---------------------------|
| visible | {boolean} |           | visibility of the tooltip |

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

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |