<!-- image -->

# Configuring logging properties using the administrative console

## About this task

- Enable or disable a particular event log.
- Specify the level of detail in a log.
- Specify where log files are stored, how many log files are kept, and a format for log
output.

You can change the log configuration statically or dynamically. Static configuration changes
affect applications when you start or restart the application server. Dynamic or run time
configuration changes apply immediately.

When a log is created, the level value for that log is set from the configuration data. If no
configuration data is available for a particular log name, the level for that log is obtained from
the parent of the log. If no configuration data exists for the parent log, the parent of that log is
checked, and so on, up the tree until a log with a non-null level value is found. When you change
the level of a log, the change is propagated to the children of the log, which recursively
propagates the change to their children, as necessary.

## Procedure

1. Enable logging and set the output properties for a log:
2. In the navigation pane, click Servers > Server Types > WebSphere application
servers.
3. Click the name of the server that you want to work with.
4. Under Troubleshooting, click Logging and tracing.
5. Click Change Log Detail levels.
6 The list of components, packages, and groups displays all the components that are currentlyregistered on the running server; only server events that have been invoked at least once appear onthis list. All server components with event points that can be logged are listed under one of thecomponents that start with the name WBILocationMonitor.LOG.
    - To select events for a static change to the configuration, click the
Configuration tab.
    - To select events for a dynamic change to the configuration, click the
Runtime tab.
7. Select the event or group of events that you want to log.
8. Set the logging level for each event or group of events.

Note: Only the levels FINE, FINER, and FINEST are valid for CEI event logging.
9. Click Apply.
10. Click OK.
11. To have static configuration changes take effect, stop then restart the server.

## Results