# Removing a reused process from a solution

## About this task

## Procedure

To remove a reused process from a solution:

1. Open the solution in IBM
FileNet Process Designer.
2. Optional: 
If the reused process is the main
workflow, set another workflow definition as the main workflow by
clicking Action > Set
as Main Workflow.
3. Select the workflow to delete by clicking View > Workflows > workflow
name and then selecting Action > Remove Workflow.

Important: Validation errors occur if you remove a global workflow that is
      referenced by any task workflows. To avoid the errors, you must modify the task workflows so
      that they do not reference the removed global workflow.