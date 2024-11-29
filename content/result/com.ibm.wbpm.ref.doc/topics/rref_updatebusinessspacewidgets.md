# updateBusinessSpaceWidgets command

This command updates widget
binary files, catalog files, endpoint files, templates, and help plug-ins
for widgets that have been previously installed and configured for Business Space.

- [ear\widgets\_name.ear] one or more EAR files.
- [catalog\catalog\_name.xml]
- [endpoints\*.xml] widget endpoints
- [templates\*.zip] Templates must be in a compressed file and follow
IBM Lotus Mashups template format.
- [help\eclipse\plugins\*]

The updateBusinessSpaceWidgets command
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
updateBusinessSpaceWidgets 
-serverName WebSphere\_Portal\_server\_name
 -nodeName WebSphere\_Portal\_node\_name
	-clusterName cluster\_name
 [-widgets widget\_path]
 [-endpoints endpoint\_path]
 [-catalogs catalog\_path]
 [-templates template\_path]
 [-helpplugins help\_path]
 [-noWidgets true|false]
 [-noEndpoints true|false]
 [-noCatalogs true|false]
 [-noTemplates true|false]
[-noHelp true|false]
[-save true|false]
```

## Parameters

## Examples

```
wsadmin -user admin -password admin -lang jython 

wsadmin>AdminTask.updateBusinessSpaceWidgets( [ '-clusterName', 'cluster\_name',
'-widgets', 'widget\_path' ] )
```

```
wsadmin -user admin -password admin -lang jython 

wsadmin>AdminTask.updateBusinessSpaceWidgets( [ '-nodeName', 'node\_name',
'-serverName', 'server\_name', '-widgets', 'widget\_path' ] )
```

Manual
steps are required for updating templates and spaces after running
the installBusinessSpaceWidgets or updateBusinessSpaceWidgets command.
For more information, see Heritage Process Portal or dashboard theme fails to load.