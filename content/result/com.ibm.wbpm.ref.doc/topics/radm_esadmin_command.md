<!-- image -->

# esAdmin command-line utility

The esAdmin command can list and delete
all locks currently managed by the lock manager. When listing locks,
you can list all locks or a small subset that is filtered based on
the module, component, or method. This command can also be used to
release an active lock in a deadlock situation; after the lock is
released, it is granted to the next queued request.

## Syntax

```
esAdmin
-h hostName
-p soapPortNumber
-username username
-password password
method

Methods:
listAll
listLocks [moduleName] [componentName] [methodName]
deleteLocks [moduleName] 
unlock lockID
```

## Parameters

## Example

```
esAdmin listLocks Order
```

|   Lock Id |   Sequence Id |   Owner Id | Module   | Component   | Method      | System Message Id   |
|-----------|---------------|------------|----------|-------------|-------------|---------------------|
|   7564504 |             2 |     695376 | Order    | OrderComp   | createOrder | A09- 427BE\_5002     |
|   7564504 |             3 |     232757 | Order    | OrderComp   | createOrder | ADF- 053RT\_5004     |

```
esAdmin -username administrator1 -password adminpassword -p 9060 unlock 754830988
```