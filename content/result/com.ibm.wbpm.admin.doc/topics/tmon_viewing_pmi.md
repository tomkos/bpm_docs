<!-- image -->

# Viewing performance metrics with the Tivoli
Performance Viewer

## Before you begin

- The servers that you want to monitor must be running on the node
- The Performance Monitoring Infrastructure (PMI) is enabled
- The service component event points that you want to monitor have been invoked at least once so
that they can be selected from within the viewer.

## About this task

The Tivoli Performance Viewer (TPV) is a powerful
application that allows you view various details of about the performance of your server. The
section entitled Monitoring performance with Tivoli
Performance Viewer in the WebSphere® Application
Server
documentation contains details about how to use this tool for various purposes, including the
resource for complete instructions on using this program. This section is limited to discussing the
viewing of performance data for events specific to IBM® Business Automation
Workflow.

## Procedure

- View current performance activity
    1. Click Monitoring and Tuning > Performance Viewer > Current Activity in the administrative console navigation tree.
    2. Select Server, then click the name of the server whose activity you want
to monitor.
You can alternatively select the check box for the server whose activity you want to monitor,
then click Start Monitoring. To start monitoring multiple servers at the same
time, select the servers then click Start Monitoring.
    3. Select Performance Modules.
    4. Select the check box next to the name of each performance module that you want to view. 
IBM Business Automation Workflow events that emit performance
statistics, and that have been invoked at least once, are listed under the
WBIStats.RootGroup hierarchy. Expand the tree by clicking
+ next to a node and shrink it by clicking - next to a
node.
    5. Click View Modules. 
A chart or table providing the requested data is displayed on the page. Charts are
displayed by default. Each module has several counters associated with it. These counters are
displayed in a table underneath the data chart or table. Selected counters are displayed in the
chart or table. You can add or remove counters from the chart or table by selecting or clearing the
check box next to them. By default, the first three counters for each module are shown.
You
can select up to 20 counters and display them in the TPV in the Current
Activity mode.
    6. Optional: 
To remove a module from a chart or table, clear the check box next to the module then click
View Modules again.
    7. Optional: 
To view the data in a table, click View Table on the counter selection
table. 
To toggle back to a chart, click View Graph.
    8. Optional: 
To view the legend for a chart, click Show Legend. To hide the legend,
click Hide Legend.
    9. When you have finished monitoring the performance of your events, click Tivoli
Performance Viewer, select the server you were monitoring, and click Stop
Monitoring.
- Log performance statistics While monitoring is active on a server, you can log the data from all the PMI counters that arecurrently enabled and record the results in a TPV log file. You can view the TPV log file for aparticular time period multiple times, selecting different combinations of up to 20 counters eachtime. You have the flexibility to observe the relationships among different performance measures inthe server during a particular period.

While monitoring is active on a server, you can log the data from all the PMI counters that are
currently enabled and record the results in a TPV log file. You can view the TPV log file for a
particular time period multiple times, selecting different combinations of up to 20 counters each
time. You have the flexibility to observe the relationships among different performance measures in
the server during a particular period.

1. Click Start Logging when viewing summary reports or performance
modules.
2. When finished, click Stop Logging.
 By default, the log files are stored in the
profile\_root/logs/tpv directory on the node on which the
server is running. The TPV automatically compresses the log file when it finishes writing to it to
conserve space. There must only be a single log file in each compressed file and it must have the
same name as the compressed file.
3. Click Monitoring and Tuning > Performance Viewer > View Logs in the administrative console navigation tree to view the logs