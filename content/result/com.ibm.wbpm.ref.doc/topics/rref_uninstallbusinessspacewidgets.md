# uninstallBusinessSpaceWidgets command

- [ear\widgets\_name.ear] one or more EAR files.
- [catalog\catalog\_name.xml]
- [endpoints\*.xml] widget endpoints
- [templates\*.zip] Templates must be in a compressed file and follow
IBM Lotus Mashups template format.
- [help\eclipse\plugins\*]

The uninstallBusinessSpaceWidgets command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- Run the command on the deployment manager node.
- Run the command in the connected mode; that is,
do not use the wsadmin -conntype none option.
- You must connect with a user ID that has WebSphere® Application Server administrator
privileges.

## Location

Start the wsadmin scripting client from the profile\_root/bin directory.

## Syntax

```
uninstallBusinessSpaceWidgets 
-serverName WebSphere\_Portal\_server\_name
 -nodeName WebSphere\_Portal\_node\_name
 -clusterName cluster\_name
 -widgets widget\_path
 [-save true|false]
```

## Parameters

- the full path for the directory that contains the compressed files
or the widget EAR files that contain the widgets. If you specify a
directory, all widgets will be installed for all compressed files
and EAR files in that directory.
- the full path to an individual compressed file that contains the
widgets.
- the full path to an individual EAR file that contains the widgets.

## Example

```
wsadmin -user admin -password admin -lang jython 

wsadmin>AdminTask.uninstallBusinessSpaceWidgets( [ '-clusterName',
'cluster\_name', '-widgets', 'X:/WPS/Temp' ] )
```