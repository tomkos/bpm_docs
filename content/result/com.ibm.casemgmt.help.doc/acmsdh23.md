# Adding a workgroup to an activity

## About this task

Before you add a step that must be completed by members of a specific workgroup, you must have a
step for a case worker to add users to the workgroup. You can create a separate step or you can add
the action to edit the workgroup to the Launch step for the activity. The activity must be a
discretionary activity or else you cannot edit the Launch step. You can also use IBM®
FileNet® Process Designer instead of Step Designer to add a workgroup to a
step.

## Procedure

To add a workgroup to an activity:

1. Click Manage Workgroups, then click Add
Workgroup.
2. Provide a prompt for this workgroup.
A prompt
is displayed in Case Client to
remind the case worker to add members to the workgroup.
3. Click OK.
4. Click Close.
5. Identify the step in your process that must be assigned
to a workgroup.
6 Add the step for the workgroup to complete:
    1. Add a workgroup lane for the new step.
If
there is more than one workgroup defined, change the workgroup in
the Workgroup Property section.
    2. Add a step to the lane.
    3. In the Step Properties section, set the properties as
needed for this step.
    4. Click OK. Then, click Close.
7. Add a connector from the LaunchStep or
the other step where the workgroup members are assigned to the step
that the workgroup must complete.
8. Apply your changes and validate the workflow.

- Adding a step to assign workgroup members

If you include a workgroup in a task, create a step for the case worker to assign members to the workgroup.
- Assigning members to a workgroup in the Launch step

If you include a workgroup in an activity, you can have the case worker assign members to the workgroup in the Launch step.