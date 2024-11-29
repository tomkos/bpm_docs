### Methods

### Parent

### Helpers

<!-- image -->

| Item lookup mode:          | Method used to populate the selection list.  {Start Empty | Items From Service | Items From Static List | Items From Config Option}                                                                                                                                                                                                                                          | SelectItemsLookupMode   |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| List items service:        | Provides the selection list based on the service input data value when the Item lookup mode is Items From Service.                                                                                                                                                                                                                                                           |                         |
| Service input data:        | Provides the input data to the service that populates the selection list when the Item lookup mode is Items From Service.                                                                                                                                                                                                                                                    | ANY                     |
| Ignore input data changes: | Disable the automatic service call when the service input data changes.                                                                                                                                                                                                                                                                                                      | Boolean                 |
| Item input data:           | A business object list that populates the selection list when the Item lookup mode is Items From Config Option.                                                                                                                                                                                                                                                              | ANY[]                   |
| Static list:               | Enter the static selection list. The strings that you enter in the value property are displayed in the selection list. When the user makes a selection, the string that is in the corresponding name property is mapped to the value property of the output object. Note: Do not specify a variable here. For a variable list, use the Items From Config Option lookup mode. | NameValuePair[]         |
| Item selection data:       | In the optionDisplayProperty field, set the business object property to display in the selection list and to take as the selection value. If unset, the defaults are: optionValueProperty, name and optionDisplayProperty, value.                                                                                                                                            | SelectDataMapping       |
| Output business data:      | When the view is bound to a complex type, the property that the user selects is passed to the property specified in optionDisplayProperty and to the property that is bound to the view.                                                                                                                                                                                     | SelectDataMapping       |
| Enable clearing selection: | Show an option to clear the selection in the list.                                                                                                                                                                                                                                                                                                                           | Boolean                 |

| Size:            | Size-based styling for this view {Default | Large | Small}                                                        | TextSizeStyle   |
|------------------|-------------------------------------------------------------------------------------------------------------------|-----------------|
| Width:           | The width in px, %, or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.             | String          |
| Label placement: | The position of the label. If you select Left, the width of the view changes.  {Top | Left}                       | LabelPlacement  |
| Label width:     | The width of the label in px, % or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed. | String          |

| Tab index:          | The tabbing sequence index of the form view. Indices start at 1, and can be set sparsely. For example, you can use 1, 5, 10.   | Integer   |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------|
| Placeholder:        | The text that is displayed before a selection is made.                                                                         | String    |
| Typeahead behavior: | Enable the typeahead behavior to filter the items in the list while typing.                                                    | Boolean   |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name        | Type     | Default   | Description                |
|-------------|----------|-----------|----------------------------|
| value       | {ANY}    |           | The value of the selection |
| displayText | {string} |           | The text to be displayed   |

| Name    | Type   | Default   | Description                   |
|---------|--------|-----------|-------------------------------|
| itemVal | {ANY}  |           | Value of item to get text for |

| slct.getItemText("option1")    // returns "Option 1" (for a selection item with value="option1" and name="Option 1")   |
|------------------------------------------------------------------------------------------------------------------------|
| slct.getItemText(slct.getSelectedItem())    // returns the text of the currently selected item                         |

| Name   | Type      | Default   | Description                            |
|--------|-----------|-----------|----------------------------------------|
| index  | {integer} |           | Index of item/option in select control |

| Name   | Type     | Default   | Description                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type   | Default   | Description                                                                |
|--------|--------|-----------|----------------------------------------------------------------------------|
| input  | {ANY}  |           | Data to be passed to the AJAX Service retrieving the items for the control |

| Name   | Type   | Default   | Description                            |
|--------|--------|-----------|----------------------------------------|
| value  | {ANY}  |           | Value of item/option in select control |

| Name   | Type      | Default   | Description                            |
|--------|-----------|-----------|----------------------------------------|
| index  | {integer} |           | Index of item/option in select control |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name     | Type     | Default   | Description               |
|----------|----------|-----------|---------------------------|
| helptext | {string} |           | Help text for the control |

| Name   | Type      | Default   | Description                                  |
|--------|-----------|-----------|----------------------------------------------|
| idx    | {integer} |           | Index to set                                 |
| value  | {ANY}     |           | Value of item/option in select control       |
| text   | {string}  |           | The display text to show for the item/option |

| Name   | Type     | Default   | Description                                  |
|--------|----------|-----------|----------------------------------------------|
| value  | {ANY}    |           | Value of item/option in select control       |
| text   | {string} |           | The display text to show for the item/option |

| Name   | Type     | Default   | Description                     |
|--------|----------|-----------|---------------------------------|
| label  | {string} |           | Label for single select control |

| Name      | Type     | Default   | Description                     |
|-----------|----------|-----------|---------------------------------|
| placement | {string} |           | "T"|"TOP"=Top | "L"|"LEFT"=Left |

| Name   | Type      | Default   | Description    |
|--------|-----------|-----------|----------------|
| flag   | {boolean} |           | {true | false} |

| Name       | Type     | Default   | Description           |
|------------|----------|-----------|-----------------------|
| labelWidth | {string} |           | Control's label width |

| Name   | Type   | Default   | Description                             |
|--------|--------|-----------|-----------------------------------------|
| value  | {ANY}  |           | Value to set currently selected item to |

| Name   | Type   | Default   | Description                             |
|--------|--------|-----------|-----------------------------------------|
| value  | {ANY}  |           | Value to set currently selected item to |

| Name   | Type   | Default   | Description                    |
|--------|--------|-----------|--------------------------------|
| data   | {ANY}  |           | Default input data for service |

| Name   | Type     | Default   | Description                                                                  |
|--------|----------|-----------|------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"NORMAL"|"D"=Default | "SMALL"|"S"=Small | "LARGE"|"L"=Large |

| Name     | Type      | Default   | Description                                    |
|----------|-----------|-----------|------------------------------------------------|
| tabIndex | {integer} |           | Tab indices start at 1 and may be set sparsely |

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

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |