# deleteWXSDefinition command

If the definition cannot be found, an error is shown.
This command deletes the default eXtreme Scale definition
only if it is the only definition in the cell. If there are other
definitions present in the cell, the command will fail, and you must
change the default to another eXtreme Scale definition
before the current one can be deleted.

```
$AdminTask help WXSAdminCommands
```

The deleteWXSDefinition command
is run using the AdminTask object of the wsadmin scripting client.

## Location

The wsadmin scripting client is
located in the install\_root\bin directory.

## Syntax

```
deleteWXSDefinition
-name definitionName
```

## Required parameter

## Example

```
AdminTask.deleteWXSDefinition('[-name MydefName]')
```