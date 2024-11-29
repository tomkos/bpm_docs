<!-- image -->

# showSCAImportMQBinding command

The showSCAImportMQBinding command
displays the attributes of a WebSphere MQ
import binding as a java.util.Hashtable containing
the usage and the JNDI name of each of the resources associated with
this binding.

The format of the output is specified by the javaFormat parameter.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
showSCAImportMQBinding
-moduleName moduleName
-import import\_name
[-applicationName applicationName]
[-javaFormat]
[-showAdvanced]
```

## Required parameters

## Optional parameters

- connection.factory
- send.destination
- listener.port
- callback.destination
- receive.destination
- activation.specification

## Example

```
AdminTask.showSCAImportMQBinding('[-moduleName MyMod -import Import1 -javaFormat true]')
```