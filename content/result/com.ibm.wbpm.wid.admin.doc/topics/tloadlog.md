<!-- image -->

# Loading server console and log files into the Server Logs view

## About this task

## Procedure

1. Click the Server Logs tab to open
the Server Logs view.
2. In the Server Logs view, click the Load Server
Console or Log icon . The Load Server Console or Log window opens.
3 If you want to load server log files into the Server Logsview from one or more directories in your file system, complete thefollowing steps: Note: In the Server Logs view, you can directly load serverlog files from one or more directories in the file system withoutfirst opening the Load Server Console or Log window. Beside the LoadServer Console or Log icon, open the associated menu byclicking the down arrow icon .If you want to load logs that were recently loaded in the Server Logsview, the path and names of the logs may be listed on a menu itemthat you can select to directly reload them. If the logs are not listedon a menu item, you can select the Load from File menuitem. The Load from File window will open to enable you to selectand load one or more logs.
    1. Select Load from file.
    2. Beside the Files field, click Browse.
The Load from File window opens.
    3. In the Filter field, accept the
default filter of .log. This will ensure that
only files with a .log file extension will be displayed in the Select
files list. (Although you can change the filter to specify
another type of file extension, server log files typically have a
.log file extension.)
    4. In the Select files list, select
one or more server log files that you want to load into the Server
Logs view. The Files field displays the paths
and names of the selected server log files and the Total
file size field displays the total combined size of the
selected files.
    5. Click OK to close the Load from
File window.
    6. Click OK to close the Load Server
Console or Log window. The selected server log files are loaded into
a tab in the Server Logs view.

<!-- image -->

4 If you want to load the contents of a server console intothe Server Logs view, complete the following steps: Note: In the Server Logs view, you can load the contents ofthe server console for a running server without first openingthe Load Server Console or Log window. Beside the LoadServer Console or Log icon, click the down arrow icon . From the menu, select Loadfrom Server Console > server\_name (where server\_name isthe name of the server for the console that you want to load). Thecontents of the console for the selected server are loaded into atab in the Server Logs view.

1. Select Load from server console.
2. In the Server field, select the
appropriate server for the server console that you want to load. (If
there are no servers currently running, the Server field
will be empty.)
3. Click OK to close the Load Server
Console or Log window. The contents of the selected server console
are loaded into a new tab in the Server Logs view.

<!-- image -->

5 If you want to load one or more server log files from aserver log directory, complete the following steps: Note: In the Server Logs view, you can directly load serverlog files from a server log directory without first opening the LoadServer Console or Log window. Beside the Load Server Consoleor Log icon, open the associated menu by clicking thedown arrow icon .If you want to load logs that were recently loaded in the Server Logsview, the path and names of the logs may be listed on a menu itemthat you can select to directly reload them. If the logs are not listedon a menu item, you can select the Load from Server LogDirectory > server\_name menu item (where server\_name isthe name of the server for the server logs that you want to load).The Load from Server Log Directory window will open to enable youto select and load one or more logs.

1. Select Load from server log directory.
2. In the Server field, select the
appropriate server for the server logs that you want to load.
3. Beside the Files field, click Browse.
The Load from Server Log Directory window opens.
4. In the list of server logs, select the check box beside
each server log that you want to load.
5. Click OK to close the Load from
Server Log Directory window.
6. Click OK to close the Load Server
Console or Log window. The server log files that you selected are
loaded into a tab in the Server Logs view.

<!-- image -->

## What to do next