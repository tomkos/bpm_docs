# Cannot validate the case types or deploy a solution after the data type or cardinality of a
solution-level property is changed

## Symptoms

You changed the data type or cardinality of a solution-level property that is used in various
case types, document classes, tasks, or steps in the solution. In Case Builder, you try to validate a case type that reuses the property and
receive an error such as the following message:

```
Errors occurred when the case type was validated: 

t1
Step1: [ ERROR ] Parameter TR\_STP1, whose value is (F\_CaseFolder.TR\_STP1), Array v. non-array mismatch
Step1: [ ERROR ] Parameter definition value type found float, expected boolean
```

If
you try to deploy the updated solution, the deployment fails. When
you click Errors or Logs from
the More Actions option for your solution on
the Manage Solutions page, you see a message
in the deployment log that the solution cannot be deployed because
there are validation errors. For example, you see the following message:

```
FNRPA0034E The solution cannot be deployed because the validation of the XPDL document failed with the following Process Engine error message: 
TR\_t1:Step1:[ ERROR ] Parameter TR\_STP1, whose value is (F\_CaseFolder.TR\_STP1), Array v. non-array mismatch 
TR\_t1:Step1:[ ERROR ] Parameter definition value type found float, expected boolean
FNRPA0162E The TR\_t1 task workflow does not exist.
FNRPA0093E The previous error was caused by: [FNRPE2131090101E]Invalid Work Class name: "TR\_t1".

FNRPA0162E The TR\_t2 task workflow does not exist.
FNRPA0093E The previous error was caused by: [FNRPE2131090101E]Invalid Work Class name: "TR\_t2".
```

## Causes

## Resolving the problem