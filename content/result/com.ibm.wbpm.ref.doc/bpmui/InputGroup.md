### Methods

### Parent

### Helpers

<!-- image -->

| Width:           | Width of the view (%, px)                                                                                                                   | String               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Label placement: | The position of the label. {Top | Left}                                                                                                     | LabelPlacement       |
| Label width:     | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                           | String               |
| Color style:     | The color of the button. {Default | Primary | Info | Success | Warning | Danger}                                                            | TooltipColorStyle    |
| Button location: | The position of the button relative to the attached view. {Left | Right}                                                                    | InputGroupButtonLoc  |
| Button type:     | The style of button to attach to the contained view. You can use the Menu option only to specify a single menu option. {Icon | Text | Menu} | InputGroupButtonKind |
| Button info:     | Set either the displayed text used with the Text and Menu kind options or the icon name for Icon kind.                                      | String               |

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

| Name      | Type     | Default   | Description                         |
|-----------|----------|-----------|-------------------------------------|
| placement | {string} |           | "L"|"LEFT"=Left | "R"|"RIGHT"=right |

| Name   | Type     | Default   | Description                                                                                                                                                           |
|--------|----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "ERROR"|"ERR"|"DANGER"|"G"=Danger |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description                                                                                                                                                                                    |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| icon   | {string} |           | See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons (note the "fa-" prefix is optional). Refer to the knowledge center for the latest Font Awesome version. |

| Name   | Type     | Default   | Description                |
|--------|----------|-----------|----------------------------|
| label  | {string} |           | label text for the control |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type     | Default   | Description                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large |

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
| width  | {string} |           | width of the input group |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |