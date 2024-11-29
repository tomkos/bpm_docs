# Adding a step to an activity

## Before you begin

## Procedure

To add a step to an activity:

1. Drag a step to a swimlane in the canvas.
You add a regular step to a role or workgroup swimlane. You add a property step, a rule step,
a stage step, or a stub step to the System swimlane.
2. Specify the step properties.

For a regular step, you specify properties, such as name, description, deadline, and
workgroups.
For a property step, select the property that is to be updated from the
Property list, then specify how that property is to be set.
For a rule step, edit the Rule Name property to associate the rule step
with a business rule.
For a stage step, select one of the following values from the
Action list to change the state of the current stage:
Advance
Completes the current stage and moves the case to the next stage.
Go to Previous
Returns the case to the previous stage.
Put on Hold
Puts the current stage on hold.
Release
Removes the hold on the current stage.

- Steps

Steps are the actions in a workflow that must be completed for a task. You can create and edit steps, assign the steps to be completed by a role or workgroup, and connect steps into a workflow.
- Assigning properties to a step

You can assign properties, such as name, responses, or a role, to a step for a case worker to complete.
- Adding steps that use case properties in IBM FileNet Process Designer

You can map step properties to a case folder instead of to a workflow.
- Adding data fields that can receive values after a step is completed

You can add data fields to a step, then assign values to the data fields after a step is completed.
- Adding steps in IBM FileNet Process Designer to integrate into activities

FileNet P8 Content Platform Engine supports extended workflow features that the Case Builder does not support. You can edit your solution workflows in IBM FileNet Process Designer, and later continue working in the Step Designer.
- Mapping custom parameters in rule steps to external data sources

If a rule step is associated with a business rule that includes custom rule parameters, you must edit the rule step in Process Designer to map the custom rule parameters to the external data sources.
- Adding a custom page to a step

Instead of displaying a default page to the case worker, you can create custom pages to display in Case Client and assign the custom page to the steps in your workflow.