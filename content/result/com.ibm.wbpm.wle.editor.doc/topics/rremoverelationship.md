# Removing an independent relationship between process instances
by using JavaScript

To remove an independent relationship between
two process instances, complete the following steps.

1. Decide if you want to check the user's authorization.
2. Get the instance ID of the instance with which you have the independent
relationship that you want to remove.
3. Remove the relationship using the removeRelatedProcessRelationship() method,
which has the following signature:TWProcessInstance.removeRelatedProcessRelationship(processInstanceId, checkAuthorization)

processInstanceId
The ID of the instance with which the relationship exists.

checkAuthorization
A boolean value that the method uses method to determine whether
it should check the user's authorization. The default is false.

```
TWProcessInstance.removeRelatedProcessRelationship(processInstanceId, true);
```