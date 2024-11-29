<!-- image -->

# modifySCAImportMQBinding command

The modifySCAImportMQBinding command
changes the JNDI name of one or more of the resources associated with
a WebSphere MQ import
binding.

- A resource of an invalid type is specified.
- A resource is specified that does not exist.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAImportMQBinding
-moduleName moduleName
-import import\_name
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
AdminTask.modifySCAImportMQBinding('[-moduleName MyMod -import Import1 -sendDestination MyDest]')
```