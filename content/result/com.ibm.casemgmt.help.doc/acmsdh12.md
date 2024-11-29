# Steps

## Regular steps

Case workers see steps as work items in the Case Client.

- A description of the work item.
- Instructional text for the case worker to complete the work item. Case workers can click
View Instructions in their toolbar to view these instructions.
- Responses that the case worker can choose for the work item. For example, you can define
responses such as approve or reject.
- Whether the work item can be reassigned by a case worker to another case worker. If you select
false, the case worker cannot reassign the step.
- A deadline for completing the work item.

A step can include an event with a condition, a deadline, or an action that a user with a
specific role must complete. A step can depend on the completion of prior or concurrent steps.

A step can be required. The action resulting from a step can be a process, a notification, or
other action. An action can have a deadline with different results if the deadline is met or not
met.

Workgroups provide a way to assign work to particular users instead of to
any user in a role. The users or groups in the workgroup are defined in the Case Client. When users are processing a work item, they see these
workgroups in the Properties widget and are able to select users and groups to assign to the
workgroup. For example, you might have a workgroup named Reviewers, but you do not know who the
reviewers are when you are designing the solution. Instead, it is a decision made by the case worker
in the Case Client. When the case worker views the case in the
Properties widget, he or she can assign users to the Reviewers group.

You specify only a name for the
attachment that acts as a place holder for an array of attachments. The actual attachment is defined
as a workflow property in IBM®
FileNet® Process Designer.

You can build expressions to evaluate conditions for routing decisions in IBM
FileNet Process Designer. The Step Designer only creates and edits routing based on
responses. You can also use expressions to update property values.

You can use Process Designer's Expression builder to define case properties in
workflow expressions such as step parameters, route conditions, or assignments. For example, you can
specify F\_CaseFolder.SolutionPrefix\_AccountNumber for a step parameter
expression.

## Property steps

You can add a property step to set the value of a case or task property. For
example, you want to offer a 20% discount when the transaction amount is more than $1,000. You
create a task and specify a precondition that the task runs only if the Transaction\_Amount property
is more than 1000. In the task, you add a property step to set the Product\_Discount property to 0.2.
Alternatively, you can use the property step to set the Product\_Discount property to the value of
another property, such as Discount\_Allowed.

## Rule steps

You can add a rule step to determine process routing or update case properties based
on a business rule. Before you create a rule step, you must define the business rule that you want
to associate with the rule step.

## Stage steps

You can add a stage step to the case to handle the lifecycle of case stages. A stage
step can be used to move the case to the next stage, put the current stage on hold, release the hold
on the current stage, or restart the previous stage.

## Steps that you can add by using IBM
FileNet Process Designer

You can create and edit submaps in IBM
FileNet Process Designer. A submap step represents
a call from the current workflow map to another map in the same workflow
definition. Submap steps are displayed as read-only steps in Step
Designer.

## Optional step properties

Depending on your
business requirements, you can specify optional properties for a step.

You can create and edit data fields in IBM
FileNet Process Designer. Data fields that are
exposed on a step are displayed as read-only items for the Parameters property
for a step in Step Designer.

- Tasks do not share case data. The solution properties and document
types are templates that can be shared by tasks, but the case data
and documents in a running task (case work item) are not inherited
or shared with another task.
- The steps in one task cannot wait for steps in a different task
to complete.
- A task cannot create another task.