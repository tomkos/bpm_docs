### Methods

### Parent

### Helpers

<!-- image -->

| Default alert color style:   | The default color style used for alerts when no color style is specified. {Primary | Info | Success | Warning | Danger}   | AlertColorStyle   |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------|
| Dark Style:                  | When true, alert colors will be darker                                                                                    | Boolean           |
| No vertical spacing:         | Show no vertical spacing between alerts                                                                                   | Boolean           |
| Animate:                     | When set to true, alerts will slide into view. Otherwise, alerts will simply appear on screen                             | Boolean           |
| Show alert icon:             | The icon shows only for the Carbon theme.                                                                                 | Boolean           |

| Alert topic:              | Alert topics the view should listen for. Use * to listen for alerts with unspecified topics.                                      | String[]   |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------|
| Default auto close delay: | Set how long (in milliseconds) each alert should wait before closing itself.  A value of 0 means the alert will not close itself. | Integer    |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name                 | Type      | Default   | Description                                                                                                                     |
|----------------------|-----------|-----------|---------------------------------------------------------------------------------------------------------------------------------|
| title                | {string}  |           | Alert title                                                                                                                     |
| text                 | {string}  |           | Alert text                                                                                                                      |
| style                | {string}  |           | "S"=Success | "I"=Info | "P"=Primary | "W"=Warning | "D"=Danger                                                                 |
| timeout              | {integer} |           | time (in milliseconds) before alert automatically closes                                                                        |
| id                   | {string}  |           | unique id for this alert                                                                                                        |
| data                 | {ANY}     |           | any extra data to associate with this alert                                                                                     |
| iconSetting.showIcon | {boolean} |           | config option to control showing icon, if the value is not set then use default value (carbon theme only)                       |
| iconSetting.iconName | {string}  |           | config option for setting icon for current instance of alert, if the value is not set then use default value (carbon icon only) |

| Name   | Type      | Default   | Description     |
|--------|-----------|-----------|-----------------|
| show   | {boolean} |           | displaying icon |

| Name   | Type     | Default   | Description            |
|--------|----------|-----------|------------------------|
| id     | {string} |           | ID of the alert to get |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name     | Type     | Default   | Description                                                     |
|----------|----------|-----------|-----------------------------------------------------------------|
| style    | {string} |           | "S"=Success | "I"=Info | "P"=Primary | "W"=Warning | "D"=Danger |
| iconName | {string} |           | A carbon icon name                                              |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

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