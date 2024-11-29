<!-- image -->

# modifySCAImportSCABinding command

This command
changes the SCA import binding for a particular SCA module. A warning
is issued if you select an export whose interface does not match the
interface of your import. IBM® Business Automation Workflow compares
the WSDL port type names of the import and export. If they are not
the same, a warning is issued. However, if the port type names do
match, IBM Business Automation Workflow assumes
that the operations provided are equivalent and no warning is issued.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAImportSCABinding
-moduleName moduleName
-import import\_name
-targetModule targetModuleName
-targetExport targetExportName
[-applicationName applicationName]
[-targetApplicationName targetApplicationName]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.modifySCAImportSCABinding('-moduleName myModule 
-applicationName myApplication -import myImport
-targetModule myTargetModule 
-targetApplicationName myTargetApplication 
-targetExport myTargetExport')
```