### Methods

### Parent

### Helpers

<!-- image -->

| Layout flow:          | Layout of child views. Note\: Do not use Justified when the layout is Inline Scroll or Auto-Wrap. Combining these options may result in unexpected layout behavior. {Horizontal | Horizontal Inline Scroll | Horizontal Tight | Horizontal Auto-wrap | Vertical | Vertical Tight}   | LayoutFlow2         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Horizontal alignment: | Horizontal alignment of child views. Note\: Do not use Justified when the layout is Inline Scroll or Auto-Wrap. Combining these options might result in unexpected layout behavior. {Justified | Left | Center | Right}                                                             | HorizontalAlignment |
| Vertical alignment:   | Controls the vertical alignment of the elements displayed in the layout. Only applies to horizontal layout flows. {Top | Middle | Bottom}                                                                                                                                           | VerticalAlignment   |
| Width:                | The width in px, %, or em.\r\nFor example\: 50px, 20%, 0.4em. If no unit is specified, px is assumed.                                                                                                                                                                               | String              |
| Height:               | Height in px, em\r\nFor example\: 50px, 0.4em. If no unit is specified, px is assumed                                                                                                                                                                                               | String              |

| Async loading:    | Provides a better UI experience for large data sets (at the expense of slower overall row-loading time once the section starts loading). Used only if this section is bound to a list.                    | Boolean   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Async batch size: | The number of rows that are loaded synchronously in an asynchronous batch. This can help tune or optimize synchronous vs. asynchronous loading performance. Used only if this section is bound to a list. | Integer   |

| Responsive sensor:   | (Optional) Id of the Responsive Sensor view containing this Layout. If omitted, the nearest sensor in  the parent chain is used.   | String               |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| Behaviors:           | The behavior of the section based on box factors defined in a responsive sensor.                                                   | ResponsiveBehavior[] |

| Events                | Events               | Events                |
|-----------------------|----------------------|-----------------------|
| On Load:              | me.setWidth("100%"); | Javascript expression |
| On Responsive Update: |                      | string                |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name    | Type     | Default   | Description                |
|---------|----------|-----------|----------------------------|
| obj	The | {object} |           | layout element to be added |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type      | Default   | Description                                   |
|--------|-----------|-----------|-----------------------------------------------|
| index  | {integer} |           | The index of the layout element to be removed |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name   | Type     | Default   | Description                    |
|--------|----------|-----------|--------------------------------|
| height | {string} |           | sets the height of the section |

| Name   | Type     | Default   | Description                        |
|--------|----------|-----------|------------------------------------|
| text   | {string} |           | sets the help text for the section |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name   | Type      | Default   | Description                                          |
|--------|-----------|-----------|------------------------------------------------------|
| obj    | {object}  |           | Object to modify selection of                        |
| flag   | {boolean} |           | Set whether object is selected or not {true | false} |

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

| Name   | Type     | Default   | Description                   |
|--------|----------|-----------|-------------------------------|
| width  | {string} |           | sets the width of the section |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |