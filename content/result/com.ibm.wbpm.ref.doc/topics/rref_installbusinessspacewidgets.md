# installBusinessSpaceWidgets command

The installBusinessSpaceWidgets command
installs, deploys, and registers designated widgets contained in a
compressed file or an enterprise archive (EAR) file. If widgets are
already deployed, the installBusinessSpaceWidgets command
refreshes the binary and registration information.

- [ear\widgets\_name.ear] one or more EAR files.
- [catalog\catalog\_name.xml]
- [endpoints\*.xml] widget endpoints
- [templates\*.zip] Templates must be in a compressed file and follow
IBM Lotus Mashups template format.
- [help\eclipse\plugins\*]

The installBusinessSpaceWidgets command
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
installBusinessSpaceWidgets 
-serverName WebSphere\_Portal\_server\_name
 -nodeName WebSphere\_Portal\_node\_name
 -clusterName cluster\_name
 -widgets widget\_path
 [-save true|false]
```

## Parameters

- The full path for the directory that contains the compressed files
or the EAR files that contain the widgets. If you specify a directory,
all widgets will be installed for all compressed files and EAR files
in that directory.
- The full path to an individual compressed file that contains the
widgets.
- The full path to an individual EAR file that contains the widgets.

## Examples

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.installBusinessSpaceWidgets( [ '-nodeName', 'node\_name',
'-serverName', 'server\_name', '-widgets',
'install\_root/BusinessSpace/registryData/product\_name/widgets/MyWidget.zip' ] )
```

```
wsadmin -conntype SOAP -port 8880 -host ProcessServer01.mycompany.com -user admin -password admin -lang jython 

wsadmin>AdminTask.installBusinessSpaceWidgets( [ '-clusterName', 'cluster\_name',
'-widgets', 'X:/WPS/Temp' ] )
```

Manual steps are
required for updating Business Space templates and spaces after running
the installBusinessSpaceWidgets or updateBusinessSpaceWidgets command.
For more information, see Heritage Process Portal or dashboard theme fails to load.