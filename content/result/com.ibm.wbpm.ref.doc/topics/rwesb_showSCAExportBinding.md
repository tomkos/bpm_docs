<!-- image -->

# showSCAExportBinding command

- If the binding is a web service binding, the service and port names are displayed.
- If the binding is a JMS binding or an adapter (EIS) binding, the binding type is displayed.
- If the export is of type SCA, no export binding is displayed because none exists; the resources
are configured on the import side only. For example, for an SCA export binding, the output would
be in the following
format:exportBinding:type=SCAExportBinding,exportBinding = null
Although
an SCA export has no export binding, it does have an export interface that allows compatibility
checks with the import interface.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
showSCAExportBinding
-moduleName moduleName
-export export\_name
[-applicationName applicationName]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.showSCAExportBinding('-moduleName myModule -applicationName myApplication -export myExport')
```