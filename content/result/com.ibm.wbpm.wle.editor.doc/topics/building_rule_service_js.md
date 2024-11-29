# Authoring rules using JavaScript in a Decision Table component 
(deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

The following steps describe how to create a sample business
rule using the Decision Table editor and JavaScript. The rule in the
sample is used to determine whether approval is required for certain
employee expenses. The sample is a single-function rule that can be
called from any other service. For your own implementation, you might
not use the same steps or names.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process definition (BPD).
3. Create a Decision service.
4. Drag a Decision Table component from the palette to the
Decision service diagram, and edit the component parameters as described
in the related topic "Adding a Decision Table component to a service."
5. Click the Decisions tab to open
the rules editor.
6. In the rules editor, click the plus sign to add a variable
(column) to the first rule (row).
7. From the variables displayed, pick the amount variable
from the request structure.
8. Type >250 as the value.
9. In the rules editor, click the plus sign again. Make sure
the first rule (row) is selected because you want to add another variable
(column) to this rule.
10. From the variables displayed, pick the type variable
from the request structure.
11. Type "director" as the value.
12. In the Action Requirement field
for the first rule (row), type Requires Approval.
13. In the rules editor, click the Action section
to expand it.
14. For the Requires Approval requirement, enter the following
JavaScript code for the Action: tw.local.approvalRequired
= true; The rules editor includes the rule shown
in the following image:
15. In the rules editor, click the second row to select it.
Create a new rule so that expenses of more than $60 for employees
requires approval.
16. In the rules editor, click the third row to select it.
Create your catch-all condition by typing - for both
the amount and type. The - value in a
variable field indicates that any variable value is considered a match.
17. In the Action Requirement field
for the third rule (row), type Auto Approval.
18. In the Action section, enter the
following JavaScript for the Auto Approval action: tw.local.approvalRequired
= false; The rules editor includes the rules shown
in the following image:  For more information
about specifying variable values using JavaScript, refer to the related
topic "Specifying variable values using JavaScript."
19. Click the Diagram tab.
20. Use the Sequence Flow tool to connect the Decision Table
 component and the Start and End events.
21. Name the Decision Table component and save your work.

## What to do next

You can now nest this Decision service in any other service
within your process application that requires this logic. Be sure
to adjust the input and output variables as required for each implementation.

For more information about the controls in the decisions
editor window, such as the up and down arrows, refer to the related
topic "Decision Table controls."