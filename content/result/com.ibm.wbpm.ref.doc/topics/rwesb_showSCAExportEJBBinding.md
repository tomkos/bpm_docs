<!-- image -->

# showSCAExportEJBBinding command

## Prerequisites

- In local mode, specify the wsadmin -conntype none option.
- To run in connected mode, you must connect as a cell administrator
that is assigned the CellAdmin role, or a deployment environment administrator
that is assigned the DEAdmin role.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
showSCAExportEJBBinding
-moduleName moduleName
-export export\_name
[-applicationName applicationName]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.showSCAExportEJBBinding('[-moduleName MyMod -export Export1]')
```