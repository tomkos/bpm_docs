### Methods

### Parent

### Helpers

<!-- image -->

| Width:           | The width of the text box in (%, px, em)                                                                          | String         |
|------------------|-------------------------------------------------------------------------------------------------------------------|----------------|
| Height:          | The height of the text box in (%, px, em)                                                                         | String         |
| Size:            | Set size for the view {Default | Large | Small}                                                                   | TextSizeStyle  |
| Label placement: | The position of the label. If you select Left, the width of the view changes. {Top | Left}                        | LabelPlacement |
| Label width:     | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String         |

| Tab index:               | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10.   | Integer   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Placeholder text:        | The text that is displayed when no value is entered.                                                                           | String    |
| Regular expression:      | Regular expression to use for validating input                                                                                 | String    |
| Auto expand if printing: | Print the entire content of the text area, beyond the area that is visible on the screen.                                      | Boolean   |

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

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description             |
|--------|----------|-----------|-------------------------|
| label  | {string} |           | label for the text area |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name   | Type      | Default   | Description                         |
|--------|-----------|-----------|-------------------------------------|
| flag   | {boolean} |           | set the visibility of the text area |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type     | Default   | Description      |
|--------|----------|-----------|------------------|
| text   | {string} |           | placeholder text |

| Name   | Type     | Default   | Description                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large |

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | tab indices start at 1 and may be set sparsely |

| Name   | Type     | Default   | Description               |
|--------|----------|-----------|---------------------------|
| text   | {string} |           | the text in the text area |

| Name      | Type      | Default   | Description                                                                                                                                 |
|-----------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| valid     | {boolean} |           | Valid/invalid flag (true to set view valid, false to make it invalid - which typically shows the view with "invalid" styling and indicator) |
| errorText | {string}  |           | Validation error text to show on the invalid-styled view                                                                                    |

| Name   | Type     | Default   | Description        |
|--------|----------|-----------|--------------------|
| re     | {string} |           | regular expression |

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