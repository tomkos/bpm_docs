<!-- image -->

# Server Logs view

In the Business Integration perspective, you can open
the Server Logs view by simply clicking the Server Logs tab.
(If the Server Logs tab is not visible, you
can open the Server Logs view by selecting Window > Show
View > Server Logs.) The Server Logs view is shown in
the following figure:

- 1 Welcome tab
- 2 Server console and log tabs
- 3 Toolbar

At the bottom of the Server Logs view, there is also a
status area that returns messages relating to the server console and
log records.

These three areas are described in the following
sections.

## Welcome tab

The Welcome tab is the home
page of the Server Logs view. It provides an overview of the Server
Logs view and introduces you to some of the key tasks that you can
perform in the view, such as:

- Loading the contents of server consoles or server logs into the
Server Logs view
- Filtering server console or server log records in the Server Logs
view
- Enabling or disabling cross-component tracing for servers
- Loading invocation records into the integration test client

## Server console and log tabs

The server console
and log tabs display the records of server consoles and server logs
that you have loaded into the Server Logs view.

You can also right-click any record and select Properties to
open a Properties window that displays the time, thread ID and
contents for the record. You can choose to view the contents in the
default translated format (for easier reading and assimilation) or
you can view the contents in the raw native format in which they were
originally generated. Also, if you open the Properties window for
an FFDC record or an invocation record, such as a Start, Fail, or
End invocation record, the Properties window will contain an additional Data field
that displays the invocation data that was passed between components.

## Toolbar

The toolbar in the Server Logs view
consists of several icons that are used to initiate numerous tasks.
The toolbar icons and their associated tasks are described in the
following table:

| Icon   | Task                                                                                                                                                                                                                                                                          |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        | Loads the contents of server consoles or log files into the Server Logs view.                                                                                                                                                                                                 |
|        | Filters the records that are displayed in the tabs of server consoles or log files. (Additional information about filtering is found in the "Record filtering" section below.)                                                                                                |
|        | Loads invocation records into the integration test client.                                                                                                                                                                                                                    |
|        | Expands nested invocation records that are currently collapsed.                                                                                                                                                                                                               |
|        | Collapses nested invocation records that are currently expanded.                                                                                                                                                                                                              |
|        | Pages up through records one page at a time.                                                                                                                                                                                                                                  |
|        | Pages down through records one page at a time.                                                                                                                                                                                                                                |
|        | Skips directly to a specified page number.                                                                                                                                                                                                                                    |
|        | Refreshes the records either manually or automatically.                                                                                                                                                                                                                       |
|        | Removes all of the records in a server console tab.                                                                                                                                                                                                                           |
|        | Toggles between enabling and disabling the automatic scrolling of records whenever a server console or log tab is refreshed and new records are appended to the bottom of the tab.                                                                                            |
|        | Displays a menu that enables you to accomplish the following tasks: Enable or disable cross-component tracing. Search for a string in the server console or log records. Sort server console or log records by column in ascending or descending order. Open the Welcome tab. |

## Record filtering

As described in the "Toolbar"
section, you can click the Select Records to Display icon
() to open and select
menu items that filter the records in server console or log tabs.

By
default, any invocation records are displayed in hierarchical format
and have check boxes that enable you to select them for direct loading
into the integration test client. Although you can choose to display
records in a flattened format rather than a hierarchical format, the
invocation records will not have check boxes and you will not be able
to select them for direct loading into the integration test client.

The
following table lists and describes the menu items for filtering records:

| Menu Item                         | Submenu Item (If Any)                               | Description                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All Record Types (Hierarchical) > | with only Server State and Error Contents           | Filters the contents of the consoles and logs to display server state and error contents as well as SystemOut records. If cross-component trace was enabled, invocation records may have been generated and any records appearing within invocations are displayed in hierarchical format. All other records are displayed in flattened format.                           |
|                                   | with only Server State, Error, and Warning Contents | Filters the contents of the consoles and logs to display server state, error, and warning contents as well as SystemOut records. If cross-component trace was enabled, invocation records may have been generated and any records appearing within invocations are displayed in hierarchical format. All other records are displayed in flattened format.                 |
|                                   | with All Contents                                   | Filters the contents of the consoles and logs to display all contents as well as SystemOut records. If cross-component trace was enabled, invocation records may have been generated and any records appearing within invocations are displayed in hierarchical format. All other records are displayed in flattened format.                                              |
| All Record Types (Flattened) >    | with only Server State and Error Contents           | Filters the contents of the consoles and logs to display server state and error contents as well as SystemOut records. If cross-component trace was enabled, invocation records may have been generated. However, all records are displayed in flattened format.                                                                                                          |
|                                   | with only Server State, Error, and Warning Contents | Filters the contents of the consoles and logs to display server state, error, and warning contents as well as SystemOut records. If cross-component trace was enabled, invocation records may have been generated. However, all records are displayed in flattened format.                                                                                                |
|                                   | with All Contents                                   | Filters the contents of the consoles and logs to display all contents as well as SystemOut records. If cross-component trace was enabled, invocation records may have been generated. However, all records are displayed in flattened format.                                                                                                                             |
| Invocation Types >                | with only Server State and Error Contents           | If cross-component trace was enabled, invocation records may have been generated. This menu item filters the contents of the consoles and logs to display only those records that appear within invocations and displays the records in hierarchical format. Displays server state and error contents as well SystemOut records.                                          |
|                                   | with only Server State, Error, and Warning Contents | If cross-component trace was enabled, invocation records may have been generated. This menu item filters the contents of the consoles and logs to display only those records that appear within invocations (including SystemOut records) and displays the records in hierarchical format.  Displays server state, error, and warning contents as well SystemOut records. |
|                                   | with All Contents                                   | If cross-component trace was enabled, invocation records may have been generated. This menu item filters the contents of the consoles and logs to display only those records that appear within invocations (including SystemOut records) and displays the records in hierarchical format. Displays all contents as well as SystemOut records.                            |
| Invocation Start Types            |                                                     | Filters the contents of the consoles and logs to display only Start records for an invocation, such as Start invoke, Start component, and Start import records.                                                                                                                                                                                                           |
| Invocation End Types              |                                                     | Filters the contents of the consoles and logs to display only End records for an invocation, such as End invoke, End component, and End import records.                                                                                                                                                                                                                   |
| Invocation Failure Types          |                                                     | Filters the contents of the consoles and logs to display only Fail records for an invocation, such as Fail invoke, Fail component, and Fail import records.                                                                                                                                                                                                               |
| Exception Types                   |                                                     | Filters the contents of the consoles and logs to display only exception records.                                                                                                                                                                                                                                                                                          |
| FFDC Types                        |                                                     | Filters the contents of the consoles and logs to display only first failure data capture (FFDC) records.                                                                                                                                                                                                                                                                  |