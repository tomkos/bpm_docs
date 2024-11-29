# Adding workflow groups to a step in IBM
FileNet Process Designer can cause validation
errors in Step Designer

## Symptoms

In IBM
FileNet Process Designer, when you add
a workflow group and assign it to a step, the workflow validates in IBM
FileNet Process Designer. When you return to Step
Designer in Case Builder, the
workflow causes validation errors.

## Causes

When you add a workflow group in IBM
FileNet Process Designer, and assign the group
to a new step, the workflow can be validated in IBM
FileNet Process Designer. However, the workflow
group is not added to the XPDL file immediately. When you try to validate
the same workflow in Step Designer, you see a validation error for
exposing the workflow group and for adding the group to the step.

## Resolving the problem

To validate the new workflow in Step Designer, save
and close the solution in Case Builder.
Reopen the solution and validate the workflow in Step Designer. The
workflow validates successfully.