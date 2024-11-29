# modifySCAImportEJBBinding command

## Prerequisites

- In local mode, specify the wsadmin -conntype none option.
- To run in connected mode, you must connect as a cell administrator
that is assigned the CellAdmin role, or a deployment environment administrator
that is assigned the DEAdmin role.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAImportEJBBinding
-moduleName moduleName
-import import\_name
-jndiName jndi\_name
[-applicationName applicationName]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.modifySCAImportEJBBinding('[-moduleName MyMod -import Import1 -jndiName newjndiName]')
```