# createWXSDefinition command

```
$AdminTask help WXSAdminCommands
```

The createWXSDefinition command
is run using the AdminTask object of the wsadmin scripting client.

## Prerequisites

- If the server is not running, use the -conntype
none option.

## Location

The wsadmin scripting client is
located in the install\_root\bin directory.

## Syntax

```
createWXSDefinition
-name definitionName
-catalogServiceEndpoints  defcatalogServiceEndpoints
-gridName defgridName
[-description defDescription]
[-securityEnabled true | false]
[-credentialGenerator UserPassword | WSToken]
[-authAlias AUTHALIAS]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.createWXSDefinition('[-name mydefName -description "my description" 
    -catalogServiceEndpoints localhost:2089 -gridName Mygrid -securityEnabled true -credentialGenerator UserPassword -authAlias NEW\_AUTH\_ALIAS]')
```