# setWXSDefinitionAsDefault command

Any eXtreme Scale definition
in the cell that was previously set to be default will no longer be
the default. An error is produced if the name you specify for the
definition does not exist.

```
$AdminTask help WXSAdminCommands
```

The setWXSDefinitionAsDefault command
is run using the AdminTask object of the wsadmin scripting client.

## Location

The wsadmin scripting client is
located in the install\_root\bin directory.

## Syntax

```
setWXSDefinitionAsDefault
-name definitionName
```

## Required parameter

## Example

```
AdminTask.setWXSDefinitionAsDefault('[-name mydefName]')
```