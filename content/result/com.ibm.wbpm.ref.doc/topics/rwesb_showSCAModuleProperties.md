# showSCAModuleProperties command

```
[groupName]propertyName=value:type
```

```
propertyName=value:type
```

## Prerequisites

The following conditions must be met:

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
showSCAModuleProperties
-moduleName moduleName
[-applicationName applicationName]
[-showPropertyTypes true | false ]
[-groupName groupName]
```

## Required parameters

## Example

```
AdminTask.showSCAModuleProperties('-moduleName MyModule 
-applicationName myApplication')
```