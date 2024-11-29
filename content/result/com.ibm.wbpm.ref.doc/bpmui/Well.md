### Methods

### Parent

### Helpers

<!-- image -->

| Color style:        | Color-based styling for this view {Default | Primary | Info | Success | Warning | Danger}                                                                                                           | TooltipColorStyle   |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Color darkness:     | Darkness of configured color style {None | Dark | Darker}                                                                                                                                           | WellColorDarkness   |
| Icon:               | Icon name, for example: calendar, clock-o, camera, cloud-upload, bell, info, file-text, etc... Check http://fontawesome.io/icons for a comprehensive list. (Note that the "fa-" prefix is optional) | String              |
| Icon size:          | Font size of the icon in px or em.\r\nFor example\: 35px, 0.4em. If no unit is specified, px is assumed                                                                                             | String              |
| Icon position:      | Icon position within well {Bottom-Right | Bottom-Left | Top-Right | Top-Left}                                                                                                                       | WellIconPosition    |
| Vertical alignment: | Vertical alignment of child views {Top | Middle | Bottom}                                                                                                                                           | VerticalAlignment   |
| Padding:            | Padding around well                                                                                                                                                                                 | String              |
| Border radius:      | Radius of curvature for corners.                                                                                                                                                                    | String              |
| Width:              | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                                | String              |
| Height:             | Height in px, %, em\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed                                                                                                       | String              |

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

| Name   | Type     | Default   | Description                                                                                                                                                          |
|--------|----------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | PRIMARY"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "ERROR"|"ERR"|"DANGER"|"G"=Danger |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| height | {string} |           | Well height   |

| Name   | Type     | Default   | Description                                                                                                                                                |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| icon   | {string} |           | See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons. Refer to the knowledge center for the latest Font Awesome version. |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| size   | {string} |           | Icon size     |

| Name   | Type     | Default   | Description                |
|--------|----------|-----------|----------------------------|
| radius | {string} |           | Corner radius of curvature |

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
| width  | {string} |           | Well width    |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |