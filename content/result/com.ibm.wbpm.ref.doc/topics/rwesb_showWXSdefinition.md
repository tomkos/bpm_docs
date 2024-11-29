# showWXSDefinition command

The list includes information about whether a definition
is the default. An error is produced if the name you specify for the
definition does not exist.

```
$AdminTask help WXSAdminCommands
```

The showWXSDefinition command
is run using the AdminTask object of the wsadmin scripting client.

## Location

The wsadmin scripting client is
located in the install\_root\bin directory.

## Syntax

```
showWXSDefinition
-name definitionName
```

## Required parameter

## Example

```
AdminTask.showWXSDefinition('[-name mydefName]')
```