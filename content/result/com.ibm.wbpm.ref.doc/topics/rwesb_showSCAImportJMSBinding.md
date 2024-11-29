<!-- image -->

# showSCAImportJMSBinding command

The showSCAImportJMSBinding command
displays the attributes of a JMS import binding as a java.util.Hashtable containing
the usage and the JNDI name of each of the resources associated with
this binding.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
showSCAImportJMSBinding
-moduleName moduleName
-import import\_name
[-applicationName applicationName]
[-javaFormat]
[-showAdvanced]
```

## Required parameters

## Optional parameters

- connection.factory
- response.connection.factory
- failed.event.replay.connection.factory
- send.destination
- receive.destination
- activation.specification
- listener.port

## Example

```
AdminTask.showSCAImportJMSBinding('[-moduleName MyMod -import Import1 -javaFormat true]')
```