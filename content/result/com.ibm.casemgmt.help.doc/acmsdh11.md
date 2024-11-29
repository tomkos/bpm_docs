# Building new FileNet P8 processes to complete
activities

## About this task

Each workflow contains a Launch Step swimlane. For activities that start automatically or
manually, you cannot edit the steps in the Launch Step swimlane. For discretionary activities, you
can edit the steps in the Launch Step swimlane. For example, you can assign a workgroup to the
Launch Step for the case worker to assign the workgroup members.

You cannot add steps to the Launch Step swimlane. Supported steps that were added to the workflow
by IBM
FileNet Process Designer that do not have a workgroup or role associated are
shown in the Launch Step swimlane. You cannot delete the Launch Step swimlane.

After a step is initially assigned to a swimlane,
you can move it to another swimlane only by updating the Swimlane step
property. A step that you move to a different swimlane retains all connectors.

You add details
for each step, including who completes the step, which attachments are required, what data is
necessary, what responses the participant can choose, deadlines, and other step properties.

You can add a stage step to move the case to handle the lifecycle of case stages. A
stage step can be used to move the case to the next stage, put the current stage on hold, release
the hold on the current stage, or restart the previous stage.

You can add a rule step to the
System swimlane to determine process routing or update case properties based on a business rule.
Before you create a rule step, you must define the business rule that you want to associate with the
rule step.

You can add a property step to the System swimlane to set the value of a case or
activity property. For example, you want to offer a 20% discount when the transaction amount is more
than $1,000. You create an activity and specify a precondition that the activity runs only if the
Transaction\_Amount property is more than 1000. In the activity, you add a property step to set the
Product\_Discount property to 0.2. Alternatively, you can use the property step to set the
Product\_Discount property to the value of another property, such as Discount\_Allowed.

You can
add a placeholder step, or stub step, to the System swimlane for component, submap, or system
steps.

To add data fields to a step, use IBM
FileNet Process Designer.

## Procedure

To build a workflow by using FileNet P8
IBM
FileNet Process Designer:

1. From the Activities page, click the Edit steps icon
to display the step designer for an activity.
2. Optional: 
Click Manage Workgroups to
add a workgroup that can include users or groups.
You must
create a workgroup before creating a workgroup swimlane. A case worker
can specify the workgroup members later.
3 From the Palette , add swimlanes. By default, roles and workgroups are assigned to swimlanes inalphabetical order. You can change the role or workgroup for a swimlanein the Role Property or Workgroup Property section.
    - To create a swimlane for a specific role that is defined in
this solution, drag Role Lane to the canvas.
    - To create a swimlane for a specific workgroup that is defined in this activity, drag
Workgroup Lane to the canvas.
4. To create a new step, drag Step to
a specific swimlane in the canvas.
5. Select the step and specify properties for the step in
the Step Properties section, then click OK.
You can specify a step name, description for the step, the instructions
that are displayed to the case worker for this step, a deadline for
completing the step, case worker responses to the step, and other
step properties. 

You can also specify the case properties, attachments,
or data fields, and the workgroup that the step is assigned to, in
the Step Properties section.
6. Create routes in the workflow from one step to another.
You can define a name and description. Select the appropriate
response or no condition.
7. Apply your changes and validate the workflow.
You
can also specify the case properties, response, attachments, or data
fields, and the workgroup that the step is assigned to, in the Step
Properties section.
The steps and routes are validated
and a message is displayed in the status bar. Correct any errors before
proceeding. 

Important:  The validation tool performs syntactic
validation only.
8. To save the workflow, the activity, and the solution, click Save.

Attention: If you add a swimlane, but you do not add any steps to the swimlane, the
swimlane will not be saved when you save the workflow.

- Adding a workgroup to an activity

Workgroups provide a way to assign work to particular users. A case worker defines the users or groups in the workgroup in the Case Client.
- Adding attachments to an activity

You can add attachments to activities for the documents that a case worker needs for completing an activity. For example, a case worker might need a claim application document, a policy document, and damage photographs to process an insurance claim.
- Adding a swimlane to an activity

You add swimlanes to an activity to divide the work among roles and workgroups. You add steps to swimlanes.
- Adding a step to an activity

You can add steps or stub steps that must be completed to complete the activity. You can add a rule step to determine process routing or update case properties. You can add a property step to set the value of a case or activity property. You can add a stage step to move the current stage to another state.
- Creating routes in a workflow

To create routes in a workflow, you draw connectors between steps that define the order in which steps must be completed.
- Adding workflows that are not associated with activities

If you want to include a workflow that does not require action by a case worker, you can add a workflow in your case type that is not associated with an activity.