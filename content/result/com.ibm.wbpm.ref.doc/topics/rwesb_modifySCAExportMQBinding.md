<!-- image -->

# modifySCAExportMQBinding command

The modifySCAExportMQBinding command
changes the JNDI name of one or more of the resources associated with
a WebSphere MQ export
binding.

- A resource of an invalid type is specified.
- A resource is specified that does not exist.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAExportMQBinding
-moduleName moduleName
-export export\_name
[-applicationName applicationName]
[-connectionFactory connectionFactoryName]
[-sendDestination sendDestinationName]
[-receiveDestination receiveDestinationName]
[-activationSpec activationSpecName]
[-listenerPort listenerPortName]
```

## Required parameters

## Optional parameters

## Example

```
AdminTask.modifySCAExportMQBinding('[-moduleName MyMod -export Export1 -sendDestination MyDest]')
```