<!-- image -->

# modifySCAExportJMSBinding command

The modifySCAExportJMSBinding command changes the JNDI name of one or more of
the resources associated with a JMS export binding.

- The module has no binding of the type specified.
- A resource of an invalid type is specified.
- A resource is specified that does not exist.

## Location

Start the wsadmin scripting client from the install\_root/profiles/deployment\_manager\_profile/bin directory.

## Syntax

```
modifySCAExportJMSBinding
-moduleName moduleName
-export export\_name
-type JMS | MQJMS | generic
[-applicationName applicationName]
[-connectionFactory connectionFactoryName]
[-connectionFactoryResponse connectionFactoryName]
[-connectionFactoryFailedEventReplay connectionFactoryName]
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
AdminTask.modifySCAExportJMSBinding('[-moduleName MyMod 
-export Export1 -type JMS -sendDestination MyDest]')
```