### Methods

### Parent

### Helpers

<!-- image -->

| Color style:   | The color style for this view.  {Default | Primary | Info | Success | Warning | Danger | Dark}                                                                                                     | ButtonColorStyle    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Ghost style:   | Show the button in the selected color style with no outline and no solid fill. Add a light grey background at hover over.                                                                          | Boolean             |
| Shape style:   | Rounded, flat or square (default) view shape. {Default | Rounded | Flat}                                                                                                                           | ButtonShapeStyle    |
| Size:          | Size-based styling for this view (default, large, small, extra-small) {Default | Large | Small | Extra-Small}                                                                                      | ButtonSizeStyle     |
| Outline only:  | Show the outline and hide the solid fill of the button in the selected color style. Add the solid fill at hover over.                                                                              | Boolean             |
| Icon:          | Icon name, for example: calendar, clock-o, camera, cloud-upload, bell, info, file-text, etc... Check http://fontawesome.io/icons for a comprehensive list. Note: that the "fa-" prefix is optional | String              |
| Width:         | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                               | String              |
| Icon location: | The location of the icon relative to the button text. {Left | Right}                                                                                                                               | InputGroupButtonLoc |

| Tab index:               | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10.   | Integer   |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Prevent multiple clicks: | Prevents the user from clicking the button more than once.                                                                     | Boolean   |

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

| Name   | Type     | Default   | Description                                                                                                                                                                                                      |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"PRI"|"P"=Primary | "INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|ERROR|ERR"|"E"|"G"=Danger | "BLACK"|BLACK|"BLK"|"B"|"B"=Black |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name      | Type      | Default   | Description    |
|-----------|-----------|-----------|----------------|
| ghostMode | {boolean} |           | {true | false} |

| Name   | Type     | Default   | Description             |
|--------|----------|-----------|-------------------------|
| text   | {string} |           | Rollover text to be set |

| Name   | Type     | Default   | Description                                                                                                                                                |
|--------|----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| icon   | {string} |           | See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons. Refer to the knowledge center for the latest Font Awesome version. |

| Name      | Type     | Default   | Description                                                          |
|-----------|----------|-----------|----------------------------------------------------------------------|
| direction | {string} |           | Indicates the direction of the icon alignment (L - left | R - right) |

| Name    | Type      | Default   | Description    |
|---------|-----------|-----------|----------------|
| outline | {boolean} |           | {true | false} |

| Name   | Type     | Default   | Description                                                            |
|--------|----------|-----------|------------------------------------------------------------------------|
| style  | {string} |           | "Default"|"D"=Default | "ROUNDED"|ROUND"|"R"=Rounded | "FLAT"|"F"=Flat |

| Name   | Type     | Default   | Description                                                                                                             |
|--------|----------|-----------|-------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large | "EXTRA-SMALL"|"X-SMALL"|"XS"|"X"=X-small |

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | Tab indices start at 1 and may be set sparsely |

| Name   | Type     | Default   | Description                  |
|--------|----------|-----------|------------------------------|
| text   | {string} |           | Text to be set on the button |

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
| width  | {string} |           | Button width  |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |