### Methods

### Parent

### Helpers

<!-- image -->

| Show label:           | Show the view's label.                                                                                            | Boolean                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|-------------------------|
| Label placement:      | The location of the label relative to the rest of the view.  {Top | Left}                                         | LabelPlacement          |
| Label width:          | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String                  |
| Horizontal alignment: | The horizontal alignment of the menu relative to the contained view. {Left | Right | Auto}                        | MenuHorizontalAlignment |
| Vertical position:    | The menu position relative to the contained view. {Bottom | Top | Auto}                                           | MenuVerticalAlignment   |
| Drop shadow:          | Add a shadow to the menu frame.                                                                                   | Boolean                 |
| Width:                | Width of "envelope" wrapping the contained view/element.                                                          | String                  |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type       | Default   | Description                                                          |
|--------|------------|-----------|----------------------------------------------------------------------|
| item   | {MenuItem} |           | Item to set in control (see method description for object structure) |

| Name   | Type   | Default   | Description                                                                                                                      |
|--------|--------|-----------|----------------------------------------------------------------------------------------------------------------------------------|
| index  | {any}  |           | when numeric this is the Index of menu item to get, when a string it is the Command associated with the menu item to be returned |

| Name   | Type   | Default   | Description                                                                                                                                             |
|--------|--------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| when   | {any}  |           | a string it is the Command associated with the menu item whose index is to be returned, when an object it is the menuitem whose index is to be returned |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type      | Default   | Description             |
|--------|-----------|-----------|-------------------------|
| index  | {integer} |           | Index of item to remove |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name      | Type     | Default   | Description                         |
|-----------|----------|-----------|-------------------------------------|
| alignment | {string} |           | "LEFT"|"L"=Left | "RIGHT"|"R"=Right |

| Name   | Type     | Default   | Description   |
|--------|----------|-----------|---------------|
| label  | {string} |           | Label to set  |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T","TOP"=Top | "L","LEFT"=Left |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type         | Default   | Description             |
|--------|--------------|-----------|-------------------------|
| items  | {MenuItem[]} |           | Items to set in control |

| Name   | Type      | Default   | Description                               |
|--------|-----------|-----------|-------------------------------------------|
| text   | {string}  |           | Badge text to set                         |
| index  | {integer} |           | Index of item badge text is being set for |

| Name   | Type      | Default   | Description                                                                                                                                                |
|--------|-----------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| icon   | {string}  |           | See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons. Refer to the knowledge center for the latest Font Awesome version. |
| index  | {integer} |           | Index of item icon is being set for                                                                                                                        |

| Name   | Type      | Default   | Description                          |
|--------|-----------|-----------|--------------------------------------|
| vis    | {boolean} |           | Set to true to make the menu visible |

| Name    | Type     | Default   | Description                                                  |
|---------|----------|-----------|--------------------------------------------------------------|
| element | {object} |           | The DOM element relative to which the popup menu should open |

| Name      | Type      | Default   | Description                                                                                                                                 |
|-----------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------|
| valid     | {boolean} |           | Valid/invalid flag (true to set view valid, false to make it invalid - which typically shows the view with "invalid" styling and indicator) |
| errorText | {string}  |           | Validation error text to show on the invalid-styled view                                                                                    |

| Name      | Type     | Default   | Description                         |
|-----------|----------|-----------|-------------------------------------|
| alignment | {string} |           | "TOP"|"T"=Top | "BOTTOM"|"B"=Bottom |

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