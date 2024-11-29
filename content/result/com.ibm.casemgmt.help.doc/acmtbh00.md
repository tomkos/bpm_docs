# Responding to validation errors in the Step Designer

## Symptoms

```
FNRPB6202E: An error occurred during validation.

FNRPB1005E: A network operation was stopped while trying to complete
 the Load Task action.
```

```
Step: [ ERROR ] Step cannot be reached from the launch step.

Step: [ ERROR ] No and-join step found for and-split step

: [ ERROR ] Route from Step to Step is incorrectly nested.

WFC: [ ERROR ] WaitForCondition instruction references work 
class, ACM-SalaryInfo, but no work class of that name 
was found with the transfer flag set in the workflow collection 
or on the server.

WFC: [ WARNING ] WaitForCondition instruction references work 
class, ACM-class\_name, but no work class of that name 
was found with the transfer flag set in the workflow collection. 
Using the definition previously transferred to the server.

WFC 2: [ ERROR ] WaitForCondition instruction references work 
class, ACM-class\_name, but no work class of that name 
was found with the transfer flag set in the workflow collection 
or on the server.

WFC 2: [ WARNING ] WaitForCondition instruction references work 
class, ACM-class\_name, but no work class of that name 
was found with the transfer flag set in the workflow collection. 
Using the definition previously transferred to the server.
```

## Causes

- Editing or deleting a role or property that is used in the task
from the solution. If you save the solution and then later edit or
remove a role or property that is used in a Task, you receive a validation
error when you validate the task again in the Step Designer. Restriction: For best results, do not edit or remove a role
or property that is used in a solution until after you edit the Task
in the Step Designer.
- Creating a step that cannot be reached.
- Defining a step as an AND-split without defining a step as the
AND-join.
- Creating routes that are invalid.
- Creating a task that is dependent on another XPDL file.

## Resolving the problem

1. Click the error text in the status bar
to view the associated message.
2. Complete one of the following steps to resolve the problem:

- If you must edit or delete a role or property that is used in
the task, first edit the task in the Step Designer to remove the property
or role. Then, edit the role or property at the solution level. Open
the task again in the Step Designer if you must use the modified role
or property.
- Ensure that each step in the map can be reached.
- Define an AND-join step for each AND-split step.
- Ensure that the connectors and steps that you defined meet the
requirements for valid workflow routes.
- If your workflow includes a step that is dependent on a step in
another XPDL file, then open the workflow in Process Editor and run
the validation there. If the WCF errors in the Step
Designer are warnings in the Process Editor instead of errors, you
can ignore the errors in the Step Designer. Otherwise, use the Process
Editor validation correction feature to correct the problem.