# modifySCAModuleProperty command

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAModuleProperty
-moduleName moduleName
-propertyName propertyName 
-newPropertyValue propertyValue
[-applicationName applicationName]
```

## Required parameters

```
-propertyName [groupName]propertyName
```

## Optional parameters

## Example

```
AdminTask.modifySCAModuleProperty(['-moduleName', 'MyModule',  
'-applicationName', 'myApplication', '-propertyName', '[mygroupName]mypropName', 
'-newPropertyValue', 'myNewPropValue'])
```