# Adding a Decision Table component to a service 
(deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

- The double-dash (-) value in a variable field
indicates that any variable value is considered a match.
- When a rule evaluates to true, the JavaScript expression that
you provide as the action is started. This expression may contain
any valid JavaScript.
- A rule only executes the JavaScript expression once per a rule,
using the JavaScript expression associated with the first condition
that evaluates to true.

The steps in this procedure demonstrate how to add a Decision
Table component to a decision service using example values. For your
own implementation, you might not use the same steps or names.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process definition (BPD).
3. Create a Decision service.
4. Drag the Decision Table component from the component palette
to the service diagram.
5. Click the Properties tab, then enter ExpenseApproval as
the Decision Table component name.
6. Click the Variables tab.
7. Click Add Input to add variables
to the service.
8. Replace Untitled1 in the Name field
with request.
9. Click Select next to Variable Type
and select the type from the list. If
you use the Activity Wizard to create a Decision service, you can
choose existing variables to add as input and output. You should use
the Activity Wizard when you start with an existing activity and want
to quickly create a service to implement the activity. To access the
wizard, right-click an activity and select Activity Wizard from
the list of options.
10. Click Add Private.
11. Replace Untitled1 in the Name field
with approvalRequired .
12. Click Select next to Variable Type
and select the Boolean type from the list.
13. Click the Decisions tab to open
the rules editor.
14. In the rules editor, click the plus sign to add a variable
(column) to the first rule (row).
15. From the list of available variables, select amount from
the request structure.
16. Type >250 as the variable value.
17. In the rules editor, click the plus sign again. Make sure
the first rule (row) is selected because you want to add another variable
(column) to this rule.
18. From the list of available variables, select type from
the request structure.
19. Type "director" as the variable value.
20. In the Action Requirement field
for the first rule (row), type Requires Approval .
21. In the rules editor, click the Action section
to expand it.
22. For the Requires Approval requirement, enter the following
JavaScript for the Action:  tw.local.approvalRequired = true;
23. In the rules editor, click the second row to select it.
Create a new rule stating that employee expenses of more than $60
require approval.
24. In the rules editor, click the third row to select it.
Create a catch-all rule by typing - for both the
amount and type. The - value in a variable
field indicates that any variable value is considered a match.
25. In the Action Requirement field
for the third rule (row), type Auto Approval .
26. In the Action section, enter the
following JavaScript for the Auto Approval action: tw.local.approvalRequired = false;
27. Click the Diagram tab.
28. Use the Sequence Flow tool to connect the Decision Table
 component and the Start and End events.

- Authoring rules using JavaScript in a Decision Table component (deprecated)

 Traditional: 
You can create rules using JavaScript in a Decision Table component.
- Decision Table controls (deprecated)

 Traditional: 
You can use the toolbar options in the conditions editor window to add, remove, or move conditions in the table.
- Specifying variable values using JavaScript (deprecated)

 Traditional: 
You can use JavaScript in rules to set variable values.