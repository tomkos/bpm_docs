# Chart

A data point is one name-value pair that
represents a unit of business data or a point on a graph. For example,
in the pair <"2010", 5657>, "2010" is the name of
the data point and 5657 is the value. On a graph, a data
point is represented as a slice for pie plots, a bar for bar plots,
or one point for line plots and area plots. ChartDataPoint is the
equivalent business data object that the Chart control uses. A
ChartDataPoint object has a string name and decimal value parameter
used to hold a single unit of business data.

A data
series is a list of multiple data points. On bar plots, each
data point in the series is a bar and has the same color. On line
plots, each data point in the series is a point and the points are
connected by a line. Each data series has a label so that it can be
added to the legend. ChartDataSeries is the equivalent business data
object that the Chart control uses. The
ChartDataSeries object represents a data series, has a string label
(which is displayed in the legend when applicable), and contains a
list of data.

A plot is composed of multiple data
series that must be displayed the same way. If a single bar plot had
four data series, the four data series would be displayed as four
groups of bars. Pie plots can display only one data series at a time.
ChartDataPlot is the equivalent business data object used by the Chart
control. The ChartDataPlot object has only one parameter - series (a
list of ChartDataSeries) - that represents a plot.

A chart is
made up of one or more plots. Most charts have a single plot. For
example, a pie chart is a chart with only one plot - a pie plot. However,
a chart can have multiple plots, such as a line plot displayed on
top of a vertical bar plot. ChartData is the equivalent business data
object used by the Chart control. The ChartData object gets bounds
to the Chart control and has one parameter - plots (a
list of ChartDataPlots).

| Binding          | Description                                                                           |
|------------------|---------------------------------------------------------------------------------------|
| data (ChartData) | Contains multiple ChartDataPlot objects that are displayed in the chart (overlapping) |

| Instance configuration label   | Description                                                                                                                                                                                                                                                                                                                                                    | Definition configuration option                     | Default value                        |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|--------------------------------------|
| Title                          | The title is displayed above the chart.                                                                                                                                                                                                                                                                                                                        | title (String)                                      | (empty)                              |
| Width                          | The width of the chart in pixels.                                                                                                                                                                                                                                                                                                                              | width (Decimal)                                     | (empty)                              |
| Height                         | The height of the chart in pixels. The height of the chart title is not accounted for in this value.                                                                                                                                                                                                                                                           | height (Decimal)                                    | (empty)                              |
| Theme                          | The style applied to the chart.                                                                                                                                                                                                                                                                                                                                | theme (ChartThemeSelection)                         | Default                              |
| Custom theme                   | The custom style applied to the chart when Theme is set to Custom.                                                                                                                                                                                                                                                                                             | customTheme (String)                                | (empty)                              |
| Legend                         | Where the legend is displayed on the chart                                                                                                                                                                                                                                                                                                                     | legendPosition (ChartLegendPositionSelection)       | None                                 |
| Stack bar plots                | Displays bars and columns in stacks instead of side by side                                                                                                                                                                                                                                                                                                    | stackBarAndColumnCharts (Boolean)                   | False (not selected)                 |
| Stack line plots               | Displays line plots in stacks instead of overlapping them                                                                                                                                                                                                                                                                                                      | stackLineCharts (Boolean)                           | False (not selected)                 |
| Stack area plots               | Displays area plots in stacks instead of overlapping them                                                                                                                                                                                                                                                                                                      | stackAreaCharts (Boolean)                           | False (not selected)                 |
| Force categorical data         | In line charts and area charts, displays numeric values as category labels that are evenly distributed across the X-axis or Y-axis.For example, if the numeric data [1979, 5; 1980, 15] represents the number of widgets sold in a specific year, for display purposes, you might enable this option so that each year is evenly spaced apart across the axis. | forceCategoricalData (Boolean)                      | False (not selected)                 |
| Display options                | The types of plots that are displayed and the configurations.                                                                                                                                                                                                                                                                                                  | displayOptions (ChartDisplayOptions)                | (empty list)                         |
| Localization Service           | The service that is used to retrieve the localized strings for use with this Coach View.                                                                                                                                                                                                                                                                       | localizationService (dashboards Localized Messages) | Dashboards Localized Messages Loader |
| On click                       | The segment that the user clicked in the chart.                                                                                                                                                                                                                                                                                                                | lastClickedSegment (ChartClickEvent)                | (empty list)                         |
| Chart refresh                  | Refreshes the chart. Typically, you update the variable that this chart is bound to before you refresh the chart to display the updated data. After the chart is refreshed, this option resets to deselected.                                                                                                                                                  | triggerChartReset (Boolean)                         | False (not selected)                 |

This view does not use the visibility property.

When multiple plots are being rendered on
a single chart, you must enable the Display Horizontal
Axis and Display Vertical Axis options
for each plot. To prevent overlapping, enable the Flip
Horizontal and Flip Vertical options.

```
tw.local.myChartData = { //the ChartData object
       plots: [
           { //a ChartDataPlot object
               series: [
                   { //a ChartDataSeries object
                       label: "Size (oz)",
                       data: [
                           { name: "Small", value: 6 }, //a ChartDataPoint object
                           { name: "Medium", value: 8 }, //another ChartDataPoint object
                           { name: "Large", value: 12 } //another ChartDataPoint object
                   ]
                   },
                   { //another ChartDataSeries object
                       label: "Sugar (g)",
                       data: [
                           { name: "Small", value: 12 }, //a ChartDataPoint object
                           { name: "Medium", value: 16 }, //another ChartDataPoint object
                           { name: "Large", value: 24 } //another ChartDataPoint object
                       ]
                   }
               ]
           },
           { //another ChartDataPlot object
               series: [
                   { //a ChartDataSeries object
                       label: "Satisfaction",
                       data: [
                           { name: "Small", value: 65 }, //a ChartDataPoint object
                           { name: "Medium", value: 80 }, //another ChartDataPoint object
                           { name: "Large", value: 82 } //another ChartDataPoint object
                       ]
                   }
               ]
           }
       ]
   };
```

- Configuring Chart

To use Chart, you must first configure it.
- Applying a custom theme to a chart

Applying a custom theme to a chart can be useful, for example, when you want to comply with a style guide or use specific colors that are not included with the default theme.
- Enable charts to return information

To enable charts to return information about clicked segments, use on-click events.
- Defining tooltips

You can define a tooltip for a row that is added to the Display options table in the Chart control configuration options. Tooltips are displayed when a user hovers over a data point in the chart.