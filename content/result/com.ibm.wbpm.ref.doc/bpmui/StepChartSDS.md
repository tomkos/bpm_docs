### Methods

### Parent

### Helpers

<!-- image -->

| Show area below steps:          | When enabled, area beneath step chart will be filled in (similar to Area Chart)                          | Boolean                   |
|---------------------------------|----------------------------------------------------------------------------------------------------------|---------------------------|
| Background color style:         | Background color {Transparent | Primary | Info | Success | Warning | Danger}                             | ChartBackgroundColorStyle |
| Data series color style:        | The dataseries color style. {Primary | Info | Success | Warning | Danger | Light}                        | ChartSDSColorStyle        |
| Data series custom color style: | The dataseries custom color style.                                                                       | NameValuePair             |
| Show value labels:              | When enabled, datapoint values will be visible above each point.                                         | Boolean                   |
| Show breadcrumbs:               | When enabled, the title shows the current position of the drill-down tree (depending on menu selection). | Boolean                   |
| XY axis color style:            | XY axis color style {None | Light - Labels Only | Dark - Labels Only | Light | Dark}                     | ChartXYAxisStyle          |
| Gridlines style:                | Set style for horizontal gridlines, if any. {None | Light | Dark}                                        | ChartGridLinesStyle       |
| X label rotation:               | X axis label rotation (in degrees)                                                                       | Decimal                   |
| X axis height:                  | X axis height (as integer)                                                                               | Integer                   |
| Border radius:                  | Radius                                                                                                   | String                    |
| Padding:                        | Padding for right, top, left, bottom (in px)                                                             | String                    |
| Height:                         | The height of the chart                                                                                  | Integer                   |

| Chart data mode:        | The method to populate chart data, from a service or from the config option. To populate drill down trees, you must use a service. {From Service | From Config Option}   | ChartDataMode   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Data service:           | Data service that populate the DataSeries.                                                                                                                               |                 |
| Data series:            | Single data series to populate chart                                                                                                                                     | DataSeries      |
| Enable menu:            | Visibility of the menu. Necessary if you have are using a drill-down tree, or if you have added menus.                                                                   | Boolean         |
| Number of Y axis ticks: | The value that you specify is not interpreted as an exact number but is adjusted to the best suitable tick count to provide optimal display.                             | Integer         |
| Y axis tick precision:  | The number of decimal places displayed for Y axis value labels, default is 0.                                                                                            | Integer         |
| Min Y axis value:       | Minimum Y axis value                                                                                                                                                     | Decimal         |
| Max Y axis value:       | The max value on the Y axis                                                                                                                                              | Decimal         |
| Use X axis culling:     | X axis culling                                                                                                                                                           | Boolean         |
| Number of X axis ticks: | The value that you specify is not interpreted as an exact number but is adjusted to the best suitable tick count to provide optimal display.                             | Integer         |
| Show tooltip:           | When enabled, hovering over data points with the mouse will cause a tooltip to appear, containing both the name of the point, as well as its value                       | Boolean         |

| Name     | Type     | Default   | Description                                                                                                     |
|----------|----------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name     | {string} |           | CSS class name(s) to add to the control. Separate class names by a space if more than one class.                |
| replaced | {string} |           | CSS class name(s) to be replaced by the first argument. Separate class names by a space if more than one class. |

| Name   | Type      | Default   | Description                                                                 |
|--------|-----------|-----------|-----------------------------------------------------------------------------|
| value  | {integer} |           | the position of the y-value that you want to add the dashed horizontal line |
| label  | {string}  |           | the label of the line                                                       |

| Name            | Type       | Default   | Description                                                                                                                                                                                            |
|-----------------|------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action          | {String}   |           | An identifier for this action                                                                                                                                                                          |
| menuItemLabel   | {String}   |           | The label of the menu item                                                                                                                                                                             |
| icon            | {String}   |           | (Font Awesome) icon name for the menu item. See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons. Refer to the knowledge center for the latest Font Awesome version. |
| badgeText       | {String}   |           | text/value to show in a badge next to the menu item                                                                                                                                                    |
| onClickFunction | {function} |           | a callback function to be invoked when the menu item is clicked. If omitted, the "on menu action" event will be called when the item is clicked                                                        |

| Name            | Type       | Default   | Description                                                                                                                                                                                            |
|-----------------|------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| action          | {String}   |           | An identifier for this action                                                                                                                                                                          |
| menuItemLabel   | {String}   |           | The label of the menu item                                                                                                                                                                             |
| icon            | {String}   |           | (Font Awesome) icon name for the menu item. See {@link http://fontawesome.io/icons Font Awesome} for a comprehensive list of icons. Refer to the knowledge center for the latest Font Awesome version. |
| badgeText       | {String}   |           | text/value to show in a badge next to the menu item                                                                                                                                                    |
| onClickFunction | {function} |           | a callback function to be invoked when the menu item is clicked. If omitted, the "on menu action" event will be called when the item is clicked                                                        |

| Name   | Type      | Default   | Description                                                               |
|--------|-----------|-----------|---------------------------------------------------------------------------|
| value  | {integer} |           | the position of the x-value that you want to add the dashed vertical line |
| label  | {string}  |           | the label of the line                                                     |

| Name       | Type                | Default   | Description                                                                                                         |
|------------|---------------------|-----------|---------------------------------------------------------------------------------------------------------------------|
| seriesName | {(string|string[])} |           | the name(s) of the dataseries that you want to defocus. If no series is specified, all data in chart will be dimmed |

| Name       | Type                | Default   | Description                                                                                                            |
|------------|---------------------|-----------|------------------------------------------------------------------------------------------------------------------------|
| seriesName | {(string|string[])} |           | the name(s) of the dataseries that you want to focus. If no series is specified, all data in chart will be highlighted |

| Name       | Type       | Default   | Description                |
|------------|------------|-----------|----------------------------|
| whether    | {boolean}  |           | to group the series or not |
| seriesName | {string[]} |           | the name of the dataseries |

| Name         | Type      | Default   | Description                                                               |
|--------------|-----------|-----------|---------------------------------------------------------------------------|
| collapseFlag | {boolean} |           | Set to true to collapse the view (equivalent to a view setting of "NONE") |

| Name       | Type                | Default   | Description                                                                                                        |
|------------|---------------------|-----------|--------------------------------------------------------------------------------------------------------------------|
| seriesName | {(string|string[])} |           | the name(s) of the dataseries that you want to show. If no names are specified, all series in chart will be hidden |

| Name   | Type    | Default   | Description                                    |
|--------|---------|-----------|------------------------------------------------|
| event  | {Event} |           | Value change event (usually an onchange event) |

| Name   | Type     | Default   | Description                              |
|--------|----------|-----------|------------------------------------------|
| label  | {string} |           | Label for the line that is to be removed |

| Name     | Type     | Default   | Description                             |
|----------|----------|-----------|-----------------------------------------|
| actionId | {String} |           | Identifier for the action to be removed |

| Name   | Type     | Default   | Description                              |
|--------|----------|-----------|------------------------------------------|
| label  | {string} |           | Label for the line that is to be removed |

| Name   | Type     | Default   | Description                                                                                                                                                                                     |
|--------|----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {string} |           | "DEFAULT"|"DEF"|"D"=Default | "PRIMARY"|"PRI"|"P"=Primary | "LIGHT"|" L"=Light |INFO"|INF"|"I"=Info | "SUCCESS"|"S"=Success | "WARNING"|"WARN"|"W"=Warning | "DANGER"|ERROR|ERR"|"E"|"G"=Danger |

| Name   | Type             | Default   | Description                                                                                                                                                                                                                                                                             |
|--------|------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| style  | {object | array} |           | Specify a name value pair object for single data series and an array of name value pair for multi data series. The name property should specify the series-name or category name in the case of pie and donut charts. The value should specify the color by name, HEX code or RGB code. |

| Name     | Type      | Default   | Description                                                                   |
|----------|-----------|-----------|-------------------------------------------------------------------------------|
| enabled  | {boolean} |           | Enabled/read-only flag (true to enable view, false to disable/make read-only) |
| required | {boolean} |           | Enable/disable required field flag for control                                |

| Name    | Type      | Default   | Description                                                    |
|---------|-----------|-----------|----------------------------------------------------------------|
| visible | {boolean} |           | Label visibility flag (true to show view label, false to hide) |

| Name      | Type   | Default   | Description        |
|-----------|--------|-----------|--------------------|
| queryData | {*}    |           | Updated query data |

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

| Name       | Type                | Default   | Description                                                                                                       |
|------------|---------------------|-----------|-------------------------------------------------------------------------------------------------------------------|
| seriesName | {(string|string[])} |           | the name(s) of the dataseries that you want to show. If no names are specified, all series in chart will be shown |

| Name       | Type       | Default   | Description                                                                           |
|------------|------------|-----------|---------------------------------------------------------------------------------------|
| chartType  | {string}   |           | the chart type in {bar, line, area, spline, area-spline, step, area-step, pie, donut} |
| seriesName | {string[]} |           | the name of the series that you want to transform the chart with                      |

| Name   | Type   | Default                | Description                   |
|--------|--------|------------------------|-------------------------------|
| phase  | {int}  | bpmext.ui.PHASE\_NORMAL | The phase we are currently in |