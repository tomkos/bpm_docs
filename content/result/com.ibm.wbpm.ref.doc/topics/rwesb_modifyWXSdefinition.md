# modifyWXSDefinition command

```
$AdminTask help WXSAdminCommands
```

The modifyWXSDefinition command
is run using the AdminTask object of the wsadmin scripting client.

## Location

The wsadmin scripting client is
located in the install\_root\bin directory.

## Syntax

```
modifyWXSDefinition
-name definitionName 
[-newName newdefName]
[-description defDescription]
[-catalogServiceEndpoints defcatalogServiceEndpoints]
[-gridName defgridName]
[-securityEnabled true | false]
[-credentialGenerator UserPassword | WSToken]
[-authAlias AUTHALIAS]
```

## Required parameter

## Optional parameters

## Example

```
AdminTask.modifyWXSDefinition('[-name MydefName -newName newdefName 
    -description "my new description" -catalogServiceEndpoints localhost:9084 -gridName newgridName -securityEnabled true -credentialGenerator UserPassword -authAlias NEW\_AUTH\_ALIAS]')
```