# Adding workflows that are not associated with activities

## About this task

You can include system functions such as WaitForCondition in which one workflow
calls another workflow that contains information that the first workflow requires for processing
steps. The workflow called or created must not be created in the solution collection. You cannot add
or edit such a workflow by using Case Builder. Instead,
you add or edit this workflow by using IBM®
FileNet® Process Designer.

## Procedure

To add a workflow that is not associated with an activity:

1. In IBM
FileNet Process Designer,
add a new workflow by clicking File > Insert > New Workflow.
2. Specify a name for the workflow on the General page
under the Workflow tab.
3. Define the new workflow according to your business requirements.
For example, add a system step that creates the new workflow in the calling workflow, specify
the new workflow as the base workflow in another workflow, or have an activity create and then wait
for the new workflow.
4. Validate the workflow collection.
5. Insert the workflow into the solution by clicking File > Solution > Edit. Then, select the solution definition.
6. Select the case type.

Important: Do
not select the solution workflow collection.
7. Click File > Insert > Workflow from Repository.
8. Do not select to update the base workflow class.
9. Edit the activity and workflows according to your business requirements.
10. Validate and save the solution.