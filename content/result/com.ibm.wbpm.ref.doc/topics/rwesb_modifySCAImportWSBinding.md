<!-- image -->

# modifySCAImportWSBinding command

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAImportWSBinding
-moduleName moduleName
-import import\_name
-endpoint targetEndpointName
[-applicationName applicationName]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.modifySCAImportWSBinding('[-moduleName myModule 
-import myImport -endpoint http://myTargetEndpoint]')
```