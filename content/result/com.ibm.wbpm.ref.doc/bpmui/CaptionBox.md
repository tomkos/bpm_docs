### Methods

### Parent

### Helpers

<!-- image -->

| Width:                      | Width of the view (%, px)                                                                                         | String                     |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------|
| Label placement:            | Label placement {Top | Left | Bottom | Right}                                                                     | CaptionPlacement           |
| Label width:                | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String                     |
| Label horizontal alignment: | Horizontal alignment to be used (left, center, right) {Left | Center | Right}                                     | TooltipHorizontalAlignment |
| Label vertical alignment:   | Vertical alignment to be used (Top, Middle, Bottom) {Top | Middle | Bottom}                                       | VerticalAlignment          |
| Shrink to content:          |                                                                                                                   | Boolean                    |
| Color style:                | Button color {Default | Normal | Muted | Light-gray | Primary | Info | Success | Warning | Danger}                | ParagraphColorStyle        |
| Label size:                 | The size of the label.  {Default | Super-Large | Extra-Large | Larger | Large | Small | Smaller}                  | OutputTextSizeStyle        |
| Label weight style:         | The weight of the label text. {Default | Slim | Normal | Semi-bold | Bold}                                        | OutputTextWeightStyle      |

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

| Name   | Type     | Default   | Description                |
|--------|----------|-----------|----------------------------|
| label  | {string} |           | label text for the control |

| Name   | Type     | Default   | Description                                                                                                |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "D"=Default | "M"=Muted | "L"=Light-gray | "P"=Primary | "I"=Info | "S"=Success | "W"=Warning | "G"=Danger |

| Name      | Type     | Default   | Description                                                               |
|-----------|----------|-----------|---------------------------------------------------------------------------|
| placement | {string} |           | "T","TOP"=Top | "L","LEFT"=Left | "B","BOTTOM"=Bottom | "R","RIGHT"=Right |

| Name   | Type     | Default   | Description                                                                                                                                                           |
|--------|----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "R","SUPER"=Super large | "X","EXTRA-LARGE"=Extra large | "G","LARGER"=Larger | "L","LARGE"=Large | "S","SMALL"=Small | "M","SMALLER"=Smaller | "D","DEFAULT"=Default |

| Name   | Type      | Default   | Description   |
|--------|-----------|-----------|---------------|
| flag   | {boolean} |           | true | false  |

| Name   | Type     | Default   | Description                                                    |
|--------|----------|-----------|----------------------------------------------------------------|
| style  | {string} |           | "D"=Default | "N"=Normal | "S"=Slim | "M"=Semi-bold | "B"=Bold |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

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
| width  | {string} |           | width of the input group |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |