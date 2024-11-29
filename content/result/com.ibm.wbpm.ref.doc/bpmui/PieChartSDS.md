### Methods

### Parent

### Helpers

<!-- image -->

| Background color style:         | Background color {Transparent | Primary | Info | Success | Warning | Danger}               | ChartBackgroundColorStyle   |
|---------------------------------|--------------------------------------------------------------------------------------------|-----------------------------|
| Data series color style:        | The palette used for charted data. {Default | Primary | Info | Success | Warning | Danger} | ChartDataSeriesColorStyle   |
| Data series custom color style: | The dataseries custom color style.                                                         | NameValuePair[]             |
| Show breadcrumbs:               | Visibility of breadcrumbs                                                                  | Boolean                     |
| Legend placement:               | Where to place the legend, relative to the chart {None | Bottom-Center | Middle-Right}     | ChartLegendPlacement        |
| Border radius:                  | Radius of the chart (in px)                                                                | String                      |
| Padding:                        | Padding (left top right bottom)                                                            | String                      |
| Height:                         | Height (in px)                                                                             | Integer                     |

| Chart data mode:   | The method to populate chart data, from a service or from the config option. To populate drill down trees, you must use a service. {From Service | From Config Option}   | ChartDataMode   |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
| Data service:      | A service used to populate the chart.                                                                                                                                    |                 |
| Data series:       | Single data series to populate chart                                                                                                                                     | DataSeries      |
| Enable menu:       | Visibility of the menu. Necessary if you are using a drill-down tree, or if you have added menus.                                                                        | Boolean         |
| Show tooltip:      | When enabled, hovering over data will display a tooltip with the label and value of the data contained in that section.                                                  | Boolean         |

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