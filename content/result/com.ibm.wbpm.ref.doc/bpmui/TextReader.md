### Methods

### Parent

### Helpers

<!-- image -->

| Width:           | The width of the text box in (%, px, em)                                                                          | String         |
|------------------|-------------------------------------------------------------------------------------------------------------------|----------------|
| Height:          | The height of the text box in (%, px, em)                                                                         | String         |
| Size:            | The text size. {Default | Large | Small}                                                                          | TextSizeStyle  |
| Label placement: | The label placement for the view. {Top | Left}                                                                    | LabelPlacement |
| Label width:     | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String         |

| Max text length:    | Maximum number of characters displayed until the "read more" hint is shown. If not specified or < 1, then 128 characters is assumed by default.   | Integer   |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Read more hint:     | Text displayed for the "read more" hint                                                                                                           | String    |
| Read less hint:     | Text displayed for the "read less" hint                                                                                                           | String    |
| Initially expanded: | When enabled, text reader will be expanded on load                                                                                                | Boolean   |
| Use arrow icons:    | Enables you to use arrow icons that expand and collapse the text area.                                                                            | Boolean   |

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

| Name   | Type      | Default   | Description                           |
|--------|-----------|-----------|---------------------------------------|
| flag   | {boolean} |           | indicating the desired expanded state |

| Name   | Type     | Default   | Description           |
|--------|----------|-----------|-----------------------|
| height | {string} |           | height of the control |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description               |
|--------|----------|-----------|---------------------------|
| label  | {string} |           | label for the text reader |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name   | Type      | Default   | Description                           |
|--------|-----------|-----------|---------------------------------------|
| flag   | {boolean} |           | set the visibility of the text reader |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type     | Default   | Description                        |
|--------|----------|-----------|------------------------------------|
| text   | {string} |           | Text to set for the read less hint |

| Name   | Type     | Default   | Description                        |
|--------|----------|-----------|------------------------------------|
| text   | {string} |           | Text to set for the read more hint |

| Name   | Type     | Default   | Description                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large |

| Name   | Type     | Default   | Description                 |
|--------|----------|-----------|-----------------------------|
| text   | {string} |           | the text in the text reader |

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
| width  | {string} |           | width of the control |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |