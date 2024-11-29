### Methods

### Parent

### Helpers

<!-- image -->

| Color style:   | The color style for this view.  {Default | Primary | Info | Success | Warning | Danger}   | BadgeColorStyle   |
|----------------|-------------------------------------------------------------------------------------------|-------------------|
| Shape style:   | Determines the shape of the view {Badge | Label | Tag}                                    | BadgeShapeStyle   |

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
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"PRI"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|ERROR|ERR"|"E"=Danger |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name   | Type     | Default   | Description                                                             |
|--------|----------|-----------|-------------------------------------------------------------------------|
| style  | {string} |           | "B"|"Badge"|"Def"|"Default"=badge || "T"|"Tag"=tag || "L"|"Label"=label |

| Name   | Type     | Default   | Description              |
|--------|----------|-----------|--------------------------|
| text   | {string} |           | Text to set in the badge |

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