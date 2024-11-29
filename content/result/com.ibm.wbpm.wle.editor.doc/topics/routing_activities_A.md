# Setting up a routing policy (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

Before
you can configure a routing policy, you must declare variables for
your BPD.

## About this task

When you define a policy, the users who receive
the runtime task are determined by the conditions that you specify.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process
definition (BPD).
3. Open the diagram of your BPD and select the activity that
you want to route.  Note: The activity that you choose
must already have an attached service.
4. Go to the Assignments page in the
properties view.
5. From the Assign To list, select Routing
Policy (Deprecated).
6. Under Routing Conditions (If), click Add a column to
select the variable to use to begin specifying conditions. When
defining routing conditions, you create a table in which each column
represents a variable and each row represents a rule.
7. From the displayed list, choose the variable for which
you want to specify a condition.
8. In the first field in row 1, enter the value to compare
to the variable. For example, if you choose a variable
called customer (String) in the preceding step and
that variable holds customer names, enter a customer name in the field.
9. If you want to add another variable to the routing condition,
click Add a column and choose a variable from
the displayed list. Enter the value to compare to the second variable.
The following examples illustrate the syntax for possible
values in the variable columns:
Table 1. Routing
conditions

Enter...
To match...

 "ok"

The exact string, ok (no quotation
marks)

 >100

Any number greater than 100

 <100

Any number less than 100

 !=3

All numbers except 3
10. If you want to establish advanced routing rules, select Adv.
When you establish routing rules, you create specifications that determine
who receives the runtime task, such as only those users who have a
previously defined user attribute. To establish rules,
click Add Rule in the Advanced Assigned To
(Then) section of the Routing properties, and see Deprecated: Defining rules for instructions.
Note: IBM Business Automation Workflow creates
only one set of rules under Advanced Assigned To (Then) for the entire
Routing Conditions table. If you want to remove a rule after you define
it, click Advanced Lane Participant in the Assign
To field in the routing conditions table to display the
rule or rules for that routing condition. Under Advanced
Assigned To (Then), click the bullet before the rule that
you want to remove, and then click Remove.
11. If you do not select Adv, the Assign
To field in the routing table shows the default assignee, Swimlane,
which means that the runtime task is routed to the team assigned to
the swimlane in your BPD. If you have multiple teams defined in your
current process application, you select one of those teams from the
menu.

## What to do next

When you define routing conditions, Business Automation Workflow evaluates
the conditions in the table from top to bottom. Business Automation Workflow implements
the first condition that matches. If no conditions match, Business Automation Workflow assigns
the activity to the default assignee, Swimlane.