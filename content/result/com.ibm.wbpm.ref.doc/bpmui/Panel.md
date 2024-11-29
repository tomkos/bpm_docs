### Methods

### Parent

### Helpers

<!-- image -->

| Icon:            | Icon name, for example: calendar, clock-o, camera, cloud-upload, bell, info, file-text, etc... Check http://fontawesome.io/icons for a comprehensive list. (Note that the "fa-" prefix is optional)   | String          |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Color style:     | Color-based styling for this view (default, info, success, warning, danger, transparent) {Default | Primary | Success | Info | Warning | Danger | Transparent}                                        | PanelColorStyle |
| Light color:     | Sets the fill color to a lighter shade, and changes title text to color selected in color style                                                                                                       | Boolean         |
| Full body color: | Fills the body with color when selected, instead of just the title                                                                                                                                    | Boolean         |
| Width:           | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                                  | String          |
| Body height:     | Height in px, %, em\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed                                                                                                         | String          |

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

| Name   | Type     | Default   | Description                                                                                                                                                                             |
|--------|----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|"G"=Danger | "TRANSPARENT"|"T"=Transparent |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name     | Type      | Default   | Description                                                         |
|----------|-----------|-----------|---------------------------------------------------------------------|
| content  | {string}  |           | The content of the footer                                           |
| htmlFlag | {boolean} |           | {true | false} set to true if footer includes html, false otherwise |

| Name   | Type      | Default   | Description    |
|--------|-----------|-----------|----------------|
| flag   | {boolean} |           | {true | false} |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type     | Default   | Description                                                                                                                                                |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| icon   | {string} |           | See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons. Refer to the knowledge center for the latest Font Awesome version. |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name   | Type      | Default   | Description    |
|--------|-----------|-----------|----------------|
| flag   | {boolean} |           | {true | false} |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| title  | {string} |           | Section title |

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
| width  | {string} |           | Section width |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |