<!-- image -->

# modifySCAImportJMSBinding command

The modifySCAImportJMSBinding command changes the JNDI name of one or more of
the resources associated with a JMS import binding.

- The module has no binding of the type specified.
- A resource of an invalid type is specified.
- A resource is specified that does not exist.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAImportJMSBinding
-moduleName moduleName
-import import\_name
-type JMS | MQJMS | generic
[-applicationName applicationName]
[-connectionFactory connectionFactoryName]
[-connectionFactoryFailedEventReplay connectionFactoryName]
[-connectionFactoryResponse connectionFactoryName]
[-sendDestination sendDestinationName]
[-activationSpec activationSpecName]
[-listenerPort listenerPortName]
```

## Required parameters

## Optional parameters

- The type parameter is set to generic
- The type parameter is set to MQJMS and a Version 6
application has been deployed to the runtime environment.

- The type parameter is set to JMS
- The type parameter is set to MQJMS and a Version 7
application has been deployed to the runtime environment.

- The type parameter is set to generic
- The type parameter is set to MQJMS and a Version 6
application has been deployed to the runtime environment.

## Example

```
AdminTask.modifySCAImportJMSBinding('[-moduleName MyMod 
-import Import1 -type JMS -sendDestination MyDest]')
```