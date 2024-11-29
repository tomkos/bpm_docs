# Integrating with the IBM Case Monitor dashboard

## About this task

The IBM Case Monitor dashboard retrieves data about the solutions that are deployed to a target
object store from the Case Analyzer store that you configure for that object store. In the dashboard, users can switch between
Case Analyzer stores to obtain
information about solutions in different target object stores.

## Procedure

To configure the IBM Case Monitor dashboard:

1. In the Case configuration tool, edit and run the
Register the IBM Case Monitor Widgets Package task.

Important: If you run this task in a cluster environment, you must ensure
that the plug-in is loaded on each node of the cluster. Either restart the cluster to force the
plug-in to be loaded on all nodes or manually load the plug-in on each node by using the IBM Content
Navigator administration client.
2. Optional: 
In IBM Content Navigator, change the refresh interval, time unit, and color scheme for the IBM
Case Monitor Dashboard plug-in. 
The refresh interval determines how often the IBM Case Monitor dashboard is to retrieve
information from the Case Analyzer
store and refresh the chart widgets. By default, the dashboard refreshes the chart widgets every 300
seconds. Setting the refresh time to 60 seconds or less affect performance negatively.
The time unit determines whether time values in the dashboard are displayed in days, hours, or
minutes.
3. Configure a Case Analyzer store for
each target object store that you want to monitor. 
For more information, see Configuring the IBM Case Monitor Dashboard.
4. Fully synchronize the nodes in the IBM Business Automation
Workflow
deployment environment and restart the whole IBM Business Automation
Workflow environment.

- IBM Case Monitor Dashboard pages

The IBM Case Monitor Dashboard includes a set of pages that display the chart widgets. Each page displays the happenings for a specific type of case artifact, such as cases or activities.
- Configuring the IBM Case Monitor Dashboard

The IBM Case Monitor Dashboard is a separate IBM Content Navigator desktop that is included in the IBM Business Automation Workflow installation. To complete the configuration, you must configure a Case Analyzer store and register the plug-in.
- Troubleshooting the IBM Case Monitor Dashboard

You can troubleshoot problems with the IBM Case Monitor Dashboard by appending a debugging parameter to the URL that Is used.