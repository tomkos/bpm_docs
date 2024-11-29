<!-- image -->

# Managing locks on sequenced events

- Lock: The lock operation attempts to acquire a lock and stores the lock request in a database.
After a lock is granted, processing resumes for the invocation that requested the lock.
- Unlock: The unlock operation releases the current lock and grants the lock to the next lock
request.

## Listing locks

The esAdmin command can list all active and queued locks in the lock manager,
or only those locks associated with a specific module, component, or method.

- listAll: Lists all active and queued locks in the lock manager.
- listLocks: Lists a subset of the active and queued locks in the lock manager. Specify one ormore of the following parameters to return a filtered list of locks: For example, the following command returns a list of active and queued locks for the CustCompcomponent that is part of the CusMod module. esAdmin listLocks CustMod CustComp
    - moduleName
    - componentName
    - methodName

```
esAdmin listLocks CustMod CustComp
```

|   Lock Id |   Sequence Id |   Owner Id | Module   | Component   | Method     | System Message Id   |
|-----------|---------------|------------|----------|-------------|------------|---------------------|
|   7564504 |             2 |     695376 | CustMod  | CustComp    | createCust | A09- 427BE\_5002     |
|   7564504 |             3 |     232757 | CustMod  | CustComp    | createCust | ADF- 053RT\_5004     |

## Releasing locks

```
esAdmin unlock lockId.
```

lockId is the unique lock ID returned by the esAdmin
listLock or esAdmin listAll command.

This command is useful when you encounter a deadlock; you can release the lock that is deadlocked
and grant it to the next lock request in the queue.

## Deleting locks

If you need to delete one or more locks, first stop the module associated with the lock. Then,
use the esAdmin command to delete the lock from the database.

```
esAdmin deleteLocks moduleName
```

You must restart the module in order for the destinations to resume processing event messages.

Use the esAdmin deleteLocks command with caution. All locks in the specified module are deleted
from the lock manager database.