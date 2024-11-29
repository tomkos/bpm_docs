# Configuring activities for inline completion (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

| Task Type         | Usage                                                                                                                                                                                                                                                                                                                                      | Inputs                                                                                                                     | Outputs                                     |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| Simple Approval   | Use when the task requires the business user to indicate an approval or rejection based on the task narrative and the task details that are exposed in the task list.                                                                                                                                                                      | None.                                                                                                                      | approved Type: Boolean comment Type: String |
| Simple Completion | Use when the task requires the business user to indicate task completion based on the task narrative and the task details that are exposed in the task list. For example, in a simple completion task the user might only need to indicate that they have reviewed the task narrative and the exposed task details, and include a comment. | None.                                                                                                                      | comment Type: String                        |
| Simple Choice     | Use when the task requires the business user to choose between a list of options.                                                                                                                                                                                                                                                          | choices Type: String, List. By default these choices are tw.resource.SimpleChoice.Approve, tw.resource.SimpleChoice.Reject | decision Type: String comment Type: String  |

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open the business process definition (BPD) in the Designer view.
3. Select the task that you would like to configure for inline completion.
4. In the Implementation tab of the Properties view, select User Task as the task
type.
5. Select the predefined Human Service that corresponds with the type of inline task that
you are creating: Simple Approval,Simple Completion or
Simple Choice. 

Note: When the user is completing a Simple Approval task, they must enter a comment
if they select the reject option.
6 If you are creating a Simple Choice task, you can modify the choices presented to theuser, and provide additional choices. These options will each appear as a button in the Process Portal task list.
    1. Ensure that you have enabled the Business Automation Workflow Advanced Features by
going to File > Preferences > IBM BPM > Capabilities.
The check box for Business Automation Workflow Advanced
Features should be selected.
    2. In the Variables tab of the BPD, create a private variable to
represent the different options that are presented to the user.
    3. Because the variable will contain a list of strings, assign it type
String and select the Is List check box.
    4. Under Default Value, select the Has Default check box.
    5. The list of options, which appear as button labels in the Process Portal interface, are added
as string values for the autoObject[n] parameters. When you first select
Has Default for your variable, the script appears as follows:

var autoObject = new tw.object.listOf.toolkit.TWSYS.String();
autoObject[0] = "";
autoObject
For each option that is presented to the user, add an autoObject[n]
parameter and a string value. For example, if you are creating inline completion buttons for
computer configuration, you might have the
following:var autoObject = new tw.object.listOf.toolkit.TWSYS.String();
autoObject[0] = "Single Core";
autoObject[1] = "Dual Core";
autoObject[2] = "Quad Core";
autoObject
7. Click Save or Finish Editing.
8. In the Data Mapping tab, the inputs and outputs required by the predefined service are
already added. Map the relevant variables that are specific to your process to the data required by
the predefined service. For example, if you created a simple choice task drawing from a list of
options defined in a private variable, then you must map this variable to the choices(List
of String) variable associated with the Simple Choice service.