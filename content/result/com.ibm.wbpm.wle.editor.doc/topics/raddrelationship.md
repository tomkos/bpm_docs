# Adding an independent relationship between process instances
by using JavaScript

1. Decide whether you want to check user's authorization.
2. Get the instance ID of the process instance to which you want
to add the relationship.
3. Add a relationship by using the addRelatedProcess() method,
which has the following signature:TWProcessInstance.addRelatedProcess(processInstanceId, description, checkAuthorization);
processInstanceId
The ID of the instance to which you want to add the relationship.

Description
A string that describes the relationship. To update
the description, use the relationship.updateDescription() method.

checkAuthorization
A Boolean value that the method uses to determine whether it should
check the user's authorization. The default is false.

The addRelatedProcess() method
returns a Relationship object, which contains the details of the relationship.

```
relation = sourceInstance.addRelatedProcess(processInstanceId, "This is an independent relationship", true);
```