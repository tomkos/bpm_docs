### Methods

### Parent

### Helpers

<!-- image -->

| Vertical:           | When selected, slider will be vertical, instead of horizontal                                            | Boolean         |
|---------------------|----------------------------------------------------------------------------------------------------------|-----------------|
| Color style:        | The color style of the slider view. {Default | Primary | Info | Success | Warning | Danger}              | BadgeColorStyle |
| Height:             | Slider height, in px or em                                                                               | String          |
| Width:              | The width in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.     | String          |
| Border radius:      | Radius of curvature for corners of the slider bar.                                                       | String          |
| Handle width:       | Width in px or em.\r\nFor example\: 50px, 0.4em. If no unit is specified, px is assumed (avoid using %). | String          |
| Handle radius:      | Radius of curvature for corners of the handle.                                                           | String          |
| Show current value: | Show the current slider value, which can be changed by typing a different value.                         | Boolean         |
| Show limit values:  | Show the minimum and maximum values for the slider range.                                                | Boolean         |

| Minimum:   | Minimum value in slider range                                                                                                | Decimal   |
|------------|------------------------------------------------------------------------------------------------------------------------------|-----------|
| Maximum:   | Maximum value in slider range                                                                                                | Decimal   |
| Step:      | Slider value step size                                                                                                       | Decimal   |
| Tab index: | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10. | Integer   |

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

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | Tab indices start at 1 and may be set sparsely |

| Name   | Type      | Default   | Description             |
|--------|-----------|-----------|-------------------------|
| val    | {numeric} |           | Value to set control to |

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