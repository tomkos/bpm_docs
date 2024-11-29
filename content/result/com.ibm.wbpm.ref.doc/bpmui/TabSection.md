### Methods

### Parent

### Helpers

<!-- image -->

| Color style:   | Color style of the tabs {Default | Primary | Success | Info | Warning | Danger}                               | TabColorStyle   |
|----------------|---------------------------------------------------------------------------------------------------------------|-----------------|
| Tabs style:    | Affects the appearance of the tabs {Default | Simple}                                                         | TabsStyle       |
| Size:          | Size-based styling for this view (default, large, small, extra-small) {Default | Large | Small | Extra-Small} | ButtonSizeStyle |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type       | Default   | Description                                                 |
|--------|------------|-----------|-------------------------------------------------------------|
| index  | {?integer} |           | 0-based pane index. When null current pane text is returned |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type      | Default   | Description                                            |
|--------|-----------|-----------|--------------------------------------------------------|
| index  | {integer} |           | 0-based pane index. Specify -1 to not display any pane |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name    | Type      | Default   | Description                                                                 |
|---------|-----------|-----------|-----------------------------------------------------------------------------|
| visible | {boolean} |           | Visibility flag (true to show the pane, false to hide it)                   |
| index   | {integer} |           | List of 0-based pane index. When null, the index is the current pane index. |

| Name    | Type      | Default   | Description                                                                |
|---------|-----------|-----------|----------------------------------------------------------------------------|
| tabText | {string}  |           | The text to set for the tab                                                |
| index   | {integer} |           | index of tab to set text for. if unspecified, the current tab will be used |

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