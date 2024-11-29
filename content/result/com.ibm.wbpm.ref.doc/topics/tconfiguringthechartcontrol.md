# Configuring Chart

## Procedure

1 Add the Chart control to a Coach and then select the plottype: Tip: In some cases, you might find that the chartcontrol does not display labels for data names as expected on horizontalor vertical bar plot type charts. This problem can occur when themajor tick marks are too large and there is not enough space leftfor the labels to display properly. To resolve this problem, try reducingthe size of the major tick marks. When a major tick mark valuehas not been set, it defaults to 10. To reduce the tick mark size,set the value to a smaller number, such as 1.0. For example, usethe following values:
    - On the Configuration tab, select Display options > Plots, click in the Plot Type cell,
and then make a selection, such as Pie plot.

In some cases, you might find that the chart
control does not display labels for data names as expected on horizontal
or vertical bar plot type charts. This problem can occur when the
major tick marks are too large and there is not enough space left
for the labels to display properly. To resolve this problem, try reducing
the size of the major tick marks.

    - Set Vertical bar plot, horizontalAxisMajorTickMarks to 1.0.
    - Ensure that horizontalAxisMinorTickMarks is blank.
    - Set Horizontal bar plot, verticalAxisMajorTickMarks to 1.0.
    - Ensure that verticalAxisMinorTickMarks is blank.
2 Construct a ChartData object for the binding:

- On the Variables tab, add a private variable
and select ChartData as the variable type.
3. Add a server script to the diagram and initialize the ChartData
object using a format similar to the following example:    tw.local.myChartData = {
       plots: [
           {
               series: [
                   {
                       label: "Flavors",
                       data: [
                           { name: "Apple", value: 4 },
                           { name: "Cherry", value: 3 },
                           { name: "Lemon", value: 1 }
                       ]
                   }
               ]
           }
       ]
   };
4. Bind the Chart to the private variable.
5. Optional: Add a Button control to the coach
to manually refresh the data in the Chart control. Bind
the Button control to the Chart Refresh configuration
property in the Chart control. For information about the configuration
property, see Chart control.