# Traditional: Identifying resource issues by using the Performance Monitoring

## Before you begin

## About this task

- The CPU Usage (in percent) of the JVM.
- The JVM heap usage and total memory available.

- The number of managed connections that are in the free pool.
- The percentage of the managed connections pool that is used.

- The number of concurrently active web container threads.
- The number of concurrently active BPM Event Manager threads.

- The number of process instances started in each sampling time
period.
- The number of process instances completed in each sampling time
period.
- The number of tasks received in each sampling time period.
- The number of tasks closed in each sampling time period.

## Procedure

1. Log in to the Process Admin Console using a user ID that
has the administrative user role Monitor.
2. In the Server Admin area of the console, click Performance > Monitoring.
3 If the monitoring is not activated, click the toggle switchto turn the monitoring on. The Configure monitoring windowopens.
    1. For Sampling rate, use the drop-down
to select the sampling resolution.
    2. For Sampling time frame, use
the drop-down to select how long the monitoring data is kept before
being discarded. 
Important: Because the monitoring data is held in
memory, combining a frequent sample rate with a long sampling time
frame might cause memory problems.
    3. Select the application server that you want to monitor.
    4. Click OK to start monitoring. Tip: To
change the monitoring settings, deactivate then reactivate the monitoring
to reopen the Configure monitoring window.
4 When the performance monitoring is active, the dashboard shows the performance graph for theselected resource over a corresponding graph of the process instance and task event rates. You canperform the following actions:

- To update the graphs with the latest data, click Refresh.
- To display a different resource metric, use the drop-down to select a different
metric.
- To zoom both graphs in on a time period of interest, click two data-points in the
performance graph. A message box is displayed indicating that the view is zoomed. Close the message
box to restore the view to display all available data.
- To identify where allocated resources are insufficient, look for resources that become 100%
used.
- To identify possible causal relationships of resource issues, compare the graph that
displays resource statistics against the graph that displays the process instance and task event
statistics for the identical time period. For example, a sudden resource problem might be caused by
one of the recently started process instances.
- To display more information about the process instances and tasks at any point in time,
click on a data point in the process instance graph. You can click on the process instance name to
view it in the Process Inspector, which might help identify processes and tasks that are the cause
of resource issues.
- To export the performance data that is displayed in the current graphs for off-line analysis: The exported file has the prefixPerformance\_Monitoring\_Report\_ . The location of the exported file depends on yourbrowser configuration, which might allow you to select the location or it might use a defaultlocation for downloads. Remember: The sampling time frame defines how long the data isheld in memory before being discarded. This determines how long the data is available to be exportedbefore it is lost.
    - To export the performance data as an Excel file, select the Microsoft Excel
2007 checkbox before clicking Export.
    - To export the performance data in the default comma-separated value format, as a .csv file,
check that the Microsoft Excel 2007 checkbox is not selected, then click
Export.

## Results

## What to do next