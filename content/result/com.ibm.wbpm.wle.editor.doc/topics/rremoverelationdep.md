# Removing dependent  relationships between process instances
by using JavaScript

## Removing a dependent relationship

1. Decide whether you want to check the user's authorization.
2. Get the instance ID of the dependent instance.
3. Remove the relationship by using the removeDependentProcessRelationship() method,
which has the following signature:TWProcessInstance.removeDependentProcessRelationship(processInstanceID, checkAuthorization)

processInstanceID
The process instance ID of the dependent process instance.

checkAuthorization
A Boolean value that the method uses to determine whether it should
check the user's authorization. The default is false.

```
TWProcessInstance.removeDependentProcessRelationship(processInstanceID, true);
```

## Removing a dependency relationship

1. Decide whether you want to check the user's authorization.
2. Get the instance ID of the process instance that the current instance
depends on.
3. Remove the relationship by using the removeDependedOnProcessRelationship() method,
which has the following signature:TWProcessInstance.removeDependedOnProcessRelationship(processInstanceID, checkAuthorization);

processInstanceID
The process instance ID of the instance that the current instance
depends on.

checkAuthorization
A Boolean value that the method uses to determine whether it should
check the user's authorization. The default is false.

```
TWProcessInstance.removeDependedOnProcessRelationship(processInstanceID, true);
```