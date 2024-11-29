# Area chart SDS

## Restrictions and limitations

## Configuration

Under Configuration,
set or modify the appearance and behavior properties for the view.

<!-- image -->

| Appearance configuration property   | Description                                                                                                                                                                                                                                                                    | Data type     |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Smooth line                         | Smooths out the curve connecting the data points.                                                                                                                                                                                                                              | Boolean       |
| Background color style              | The color style for the background color.                                                                                                                                                                                                                                      | String        |
| Data series color style             | The color style for the data series.                                                                                                                                                                                                                                           | String        |
| Data series custom color style      | Customize the color style for the data series.  In the NameValuePair, Name is the series name and Value is the color specified as name, hexadecimal code, or RGB code. For example, red, #ff0000, rgb(255, 0, 0).  The property takes precedence over Data series color style. | NameValuePair |
| Show value labels                   | Display data point values above each point in the chart.                                                                                                                                                                                                                       | Boolean       |
| Show breadcrumbs                    | When this option is enabled, the title shows the current position of the tree that the user can drill down into (depending on the menu selection).                                                                                                                             | Boolean       |
| Point size                          | The size of the dot that marks the value. Default: 2.5 pixels.                                                                                                                                                                                                                 | Decimal       |
| XY Axis color style                 | The color style for the X and Y axes.                                                                                                                                                                                                                                          | String        |
| Gridlines style                     | The style for the horizontal gridlines.                                                                                                                                                                                                                                        | String        |
| X label rotation                    | The rotation in degrees for the X-axis label.                                                                                                                                                                                                                                  | Decimal       |
| X axis height                       | The height of the X axis.                                                                                                                                                                                                                                                      | Integer       |
| Border radius                       | The radius of the chart.                                                                                                                                                                                                                                                       | String        |
| Padding                             | The padding for the right, top, left, and bottom of the chart (in pixels).                                                                                                                                                                                                     | String        |
| Height                              | The height of the chart.                                                                                                                                                                                                                                                       | Integer       |

| Behavior configuration property   | Description                                                                                                                                                                                                            | Data type                                                             |
|-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Chart data mode                   | Select whether to populate chart data from a service or from the configuration option. Note that trees users can drill down into are available only by populating through a service flow with appropriate Ajax access. | String                                                                |
| Data service                      | A service that populates the data series.                                                                                                                                                                              | Service Flow                                                          |
| Data series                       | The seriesName is the name for the data series and dataPoints is the list of data points to include in the data series.                                                                                                | String for the seriesName and DataPoint[] for the list of dataPoints. |
| Enable menu                       | Enables the visibility of the menu. The menu is required if you have a tree that users can drill down into, or if you added menus.                                                                                     | Boolean                                                               |
| Number of Y axis ticks            | The number of ticks on the Y axis. The value that you specify is not interpreted as an exact number but is adjusted to the best suitable tick count to provide optimal display.                                        | Integer                                                               |
| Y axis tick precision             | The number of decimal places to display for Y-axis value labels. The default number of decimal places is 0.                                                                                                            | Integer                                                               |
| Min Y axis value                  | The minimum value on the Y axis.                                                                                                                                                                                       | Decimal                                                               |
| Max Y axis value                  | The maximum value on the Y axis.                                                                                                                                                                                       | Decimal                                                               |
| Use X axis culling                | Show only the number of X-axis data tick counts, which is determined by the value of the Max X tick count property.                                                                                                    | Boolean                                                               |
| Number of X axis ticks            | The number of ticks on the X axis. The value that you specify is not interpreted as an exact number but is adjusted to the best suitable tick count to provide optimal display.                                        | Integer                                                               |
| Show tooltip                      | When this option is enabled, hovering over data points in the chart with the mouse causes a tooltip to appear. The tooltip shows both the name of the point and its value.                                             | Boolean                                                               |

## Events

- On load: Activated when the page loads. For example:
me.defocusSeries("Brand1")
- On refreshed: Activated when the chart is refreshed. For example:
me.focusSeries("Brand1")
- On click: Activated when the chart is clicked. For example:
me.transform("donut", ["Brand1","Brand2"])
- On menu action: Activated when there is a menu action. For example:
console.log("Running menu action '" + action.name + "' on " +
me.getSelectedDataPoint().label + " with value of " +
me.getSelectedDataPoint().value)

## Keyboard navigation

- Press Tab until the chart that you want is highlighted.
- Press Tab to get focus inside the chart.
- Use the right, left, up or down arrow keys to navigate within the chart. Note: To navigate the
chart as described, you must use the JAWS screen reader.

## Methods

## Additional resources

For information about how to create a coach or page, see Building coaches. 
For information about standard properties
(General, Configuration,
Positioning, Visibility, and HTML
Attributes), see View properties.