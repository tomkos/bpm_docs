### Methods

### Parent

### Helpers

<!-- image -->

| Width:           | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                               | String                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Text alignment:  | The alignment of the output text relative to the width of the view. {Default | Left | Center | Right}                                                                              | TextAlignment         |
| Color style:     | The color style of the link. Note\: The color style applies only to the text, not the label. {Default | Normal | Muted | Light-gray | Primary | Info | Success | Warning | Danger} | ParagraphColorStyle   |
| Size:            | The size of the text. Note\: The text size applies to both text and label. {Default | Super-Large | Extra-Large | Larger | Large | Small | Smaller}                                | OutputTextSizeStyle   |
| Text weight:     | The weight of the link text. Note\: The text weight applies only to the text, not the label {Default | Slim | Normal | Semi-bold | Bold}                                           | OutputTextWeightStyle |
| Label placement: | The position of the label. If you select Left, the width of the view changes. {Top | Left}                                                                                         | LabelPlacement        |
| Label width:     | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                  | String                |

| Tab index:               | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10.   | Integer   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Link text:               | Text to set for the link                                                                                                       | String    |
| Prevent multiple clicks: | Prevents the user from clicking the link more than once. Only effective for a Boundary Event link type.                        | Boolean   |
| Link type:               | Set to Boundary Event to emit a boundary event within the service, URL to go to an outside page {Boundary Event | URL}         | LinkType  |
| Link URL:                | Only effective if Link Type is URL                                                                                             | String    |
| Open in same window:     | Open URL in the same window. The link type must be URL.                                                                        | Boolean   |

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

| Name   | Type     | Default   | Description                                                                                                                                                                                                                                                                                                     |
|--------|----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "NORMAL"|H"=Normal | "DEFAULT"|"DEF"|"D"=Default | "MUTED"|"M"=Muted | "LIGHT\_GRAY"|"GRAY"|"LIGHTGRAY"|"LIGHT GRAY"|"LIGHT"|"L"=Light | "PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "ERROR"|"ERR"|"DANGER"|"G"=Danger | "TRANSPARENT"|"T"=Transparent |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description       |
|--------|----------|-----------|-------------------|
| text   | {string} |           | Label for control |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name   | Type      | Default   | Description    |
|--------|-----------|-----------|----------------|
| flag   | {boolean} |           | {true | false} |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type     | Default   | Description        |
|--------|----------|-----------|--------------------|
| url    | {string} |           | Set URL of control |

| Name   | Type     | Default   | Description                                                                                                                                                                                                                   |
|--------|----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "SUPER-LARGE"|"SUPER LARGE"|"SUPER"|"R"=Super large | "EXTRA-LARGE"|"EXTRA LARGE"|"EXTRA"|"X"=Extra large | "LARGER"|"G"=Larger | "LARGE"|"L"=Large | "SMALL"|"S"=Small | "SMALLER"|"M"=Smaller | "DEFAULT"|"DEF"|"D"=Default |

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | tab indices start at 1 and may be set sparsely |

| Name   | Type     | Default   | Description            |
|--------|----------|-----------|------------------------|
| text   | {string} |           | Output text of control |

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

| Name   | Type     | Default   | Description      |
|--------|----------|-----------|------------------|
| width  | {string} |           | Width of control |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |