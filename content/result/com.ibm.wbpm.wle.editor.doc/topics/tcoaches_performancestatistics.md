# Accessing coach performance statistics

## About this task

<!-- image -->

By analyzing the statistics,
you can evaluate the complexity of your user interface and make the necessary adjustments to ensure
an optimal performance at run time. Based on page content, the statistics can include information
such as the number of views in a coach and the number of view instances that are created at run time
for each item in the bound list. Where applicable, the views that have repeating elements are also
listed. Hover over any entry in the list to display details about that view, which is also shown
selected on the canvas.

The numbers are indicators that let you know when you venture outside
of best practices, warning you of a potential performance decline. Because not all views are equal,
use the numbers as a guideline. For a better estimate of the performance impact, correlate the
numbers with the complexity of the views. For example, 30 Date Time Picker
views can have a heavier impact on performance than 100 Decimal or Integer
views.

To prevent you from mixing different technologies, a
warning icon is displayed on the static analysis toolbar icon whenever you attempt using views from
different toolkits in the same coach. You can click the analysis to obtain more insight about the
issue.

- To disable the design-time WYSIWYG, in the coach, right-click anywhere on the canvas, then click Editor Options > Disable WYSIWYG in the Designer. When WYSIWYG is turned off, the coaches on the canvas no longer respond to changes
that you make to their configuration properties.
- When you have completed the design of your coaches and want to turn the design-time WYSIWYG back
on, right-click on the canvas and click Editor Options > Enable WYSIWYG in the Designer. Enabling the WYSIWYG persists between sessions.

To access the
performance statistics, you must first enable the runtime flag that displays the coach data, as
described later in this topic. Then, as the human service runs, click Show performance
statistics
 in the upper-right corner of the page to display the Performance
section for the first coach that completed running. Click  to display the performance statistics for each coach that completes running, or click
Hide Performance Statistics
 to collapse the section.

- The total number of view instances
- The view instances by view name
- The total number of view types that are created
- The time spent in each view instance

- The total time spent in lifecycle event handlers
- The time spent in event handlers for each type of view
- The time spent in each lifecycle function

<!-- image -->

<!-- image -->

## Procedure

To enable the runtime flag that displays the performance statistics

1. In the designer, click  to run your client-side human service or heritage human service.
2. In the window that opens for your first coach, press F12 to start the web browser debugger or
console.
3. In the expression editor, enter the following line:

localStorage["CoachPerformanceMonitor"] = true;
4. Run the human service again.
5 To disable the performance statistics flag, enter the following line in the expressioneditor: localStorage["CoachPerformanceMonitor"] = false; Tip: Alternatively, you can enable JavaScript debugging for coaches and views. See Enabling tracing for coaches . Another way to set the local storage flag is by specifying thebrowser preferences, as follows: Tip: Regardless of which method you use to set the local storage flag, the browsersetting overrides the debug setting. The debug setting is used only if the local storage flag is notdefined.

```
localStorage["CoachPerformanceMonitor"] = false;
```

    1. In the upper-right corner of the designer, click your user name, and select
Preferences.
    2. Select Show the runtime performance monitor, then click
Save. Note that Show the runtime performance monitor
is a browser setting that is persisted across sessions but is not saved to the user profile in
Workflow Center.