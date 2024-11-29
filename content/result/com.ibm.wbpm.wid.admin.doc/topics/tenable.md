<!-- image -->

# Enabling or disabling cross-component tracing

## Before you begin

## About this task

To enable or
disable cross-component tracing:

## Procedure

1 If you want to enable or disable cross-component tracingfrom the Server Logs view, complete the following steps:
    1. Click the Server Logs tab to
open the Server Logs view.
    2. In the Server Logs view, ensure that at least one server
console or server log tab is open and selected for the running server
where you want to enable or disable cross-component tracing. (By default,
the contents of a server console are automatically loaded into a new
tab in the Server Logs view whenever a server is started. However,
you can also manually load the contents of a server console or server
log files into a tab by following the instructions in the topic "Loading
server console or log files.")
    3. Click the View Menu icon . A menu opens.
    4. From the Cross-Component Trace State menu,
select one of the following menu items: Disabled, Enabled,
or Enabled with Data Snapshot (recommended).
The lower right corner of the Server Logs view displays the new cross-component
trace state on the server.
2 If you want to enable or disable cross-component tracingfrom the administrative console of a server, complete the followingsteps:

1. Click the Servers tab to open
the Servers view.
2. In the Servers view, right-click the running server
where you want to enable or disable cross-component tracing and then
select Administration > Run Administrative Console.
The login page of the administrative console opens.
3. In the User ID and Password field,
type the user ID and password that you specified when you installed IBM® Integration
Designer.
4. Click Login. The Welcome page
of the administrative console opens.
5. In the left frame of the Welcome page, expand Troubleshooting and
click the Cross-Component Trace link. The Cross-Component
Trace page opens.
6. In the Configuration column of
the Cross-Component Trace configuration table, select disable, enable,
or enable with data snapshot. This setting
is only used when the server is started or restarted. The setting
applies to all sessions of the server.
7. In the Runtime column of the
Cross-Component Trace configuration table, select disable, enable,
or enable with data snapshot (recommended).
This setting is only used when the server is running. The setting
only applies to a single session of the server.
8. Click OK and then click the Save link.
9. Close the administrative console.