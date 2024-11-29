### Methods

### Parent

### Helpers

<!-- image -->

| Width:                            | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                      | String                |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Text alignment:                   | The alignment of the output text relative to the width of the view. {Default | Left | Center | Right}                                                                                     | TextAlignment         |
| Color style:                      | The color style of the output text. Note\: The color style applies only to the text, not the label. {Default | Normal | Muted | Light-gray | Primary | Info | Success | Warning | Danger} | ParagraphColorStyle   |
| Size:                             | The text size. Applies to the text and the label. {Default | Super-Large | Extra-Large | Larger | Large | Small | Smaller}                                                                | OutputTextSizeStyle   |
| Text weight:                      | The text weight. Applies only to the text, not the label. {Default | Slim | Normal | Semi-bold | Bold}                                                                                    | OutputTextWeightStyle |
| Label placement:                  | The position of the label. If you select Left, the width of the view changes. {Top | Left}                                                                                                | LabelPlacement        |
| Label width:                      | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                         | String                |
| Use normal font weight for label: | (Classic theme only) By default, the label font weight is bold. By clicking this option, you'll use the normal font weight as defined in the theme.                                       | Boolean               |

| Allow HTML:   | Display the bound data as HTML formatted text.                                                   | Boolean   |
|---------------|--------------------------------------------------------------------------------------------------|-----------|
| Wrap text:    | Control how text is wrapped to a new line. {Default | Normal | Keep all | Anywhere | Break word} | TextWrap  |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type     | Default   | Description                                                                                                                                                                                                                                                                                |
|--------|----------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "MUTED"|"M"=Muted | "LIGHT\_GRAY"|"GRAY"|"LIGHTGRAY"|"LIGHT GRAY"|"LIGHT"|"L"=Light | "PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "ERROR"|"ERR"|"DANGER"|"G"=Danger | "TRANSPARENT"|"T"=Transparent |

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

| Name   | Type      | Default   | Description   |
|--------|-----------|-----------|---------------|
|        | {boolean} |           |               |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type     | Default   | Description                                                                                                                                                           |
|--------|----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "R","SUPER"=Super large | "X","EXTRA-LARGE"=Extra large | "G","LARGER"=Larger | "L","LARGE"=Large | "S","SMALL"=Small | "M","SMALLER"=Smaller | "D","DEFAULT"=Default |

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