# Defining rules with a routing policy (deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

Using rules, your task assignments can be dynamic,
which ensures that activities are routed to the appropriate individuals.

When defining rules, you can choose from the following rule
types:

| Rule type           | Description                                                                         |
|---------------------|-------------------------------------------------------------------------------------|
| Swimlane            | Routes activities to users based on whether they are the default lane participants. |
| Participant Rule    | Selects users according to group membership.                                        |
| User Attribute Rule | Selects users based on user attributes.                                             |
| Expression Rule     | Selects users who match a particular expression that you provide.                   |

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a business process
definition (BPD).
3. Click an activity in the BPD.
4. In the Properties page, click Assignments.
5. In the Assign To list, select Routing
Policy (Deprecated). The Routing
Conditions (If) section becomes available.
6. Under Routing Conditions (If), click Add
a column, and select the variable for which you want to
add the condition.
7. In the table, select Adv. The Advanced
Assigned To (Then) section is populated.
8. Under Advanced Assigned To (Then),
click all in the following statement:  Advanced
Lane Participants are users who match all of the following
rules:
Choose all or any.
If
you choose all, the runtime task is assigned
to users who match all specified rules. If you choose any,
the runtime task is assigned to users who match at least one of the
specified rules.
If none of the conditions that you specify
are met, IBM Business Automation Workflow assigns
the task to the swimlane for the rule to which this Advanced Assignment
applies.
9 Click Add Decision to choose thetype of rule to add. For example, you can define thefollowing Advanced Lane Participant group (team)rules in the group properties: Advanced Lane Participants areusers who match all of the following rules: The Add Decision... option adds other rules to the list.

For example, you can define the
following Advanced Lane Participant group (team)
rules in the group properties:

Advanced Lane Participants are
users who match all of the following rules:

    - Who belong to the Finance Managers group
    - Who have an attribute Level 1 Loans greater than tw.local.loanAmount
    - Who match expression tw.local.Recipient
10 Supply the necessary information for the specified typeof rule.

- For a Swimlane rule, supply the required
input for the following specification:
Who belong to
lane participant.

Table 2. Input required
for a Swimlane rule

Specification
Action

belong
 Click belong to choose either belong or do
not belong.
- For a Participant Rule, supply the
input that you want for the following specification:
Who belong to
the select team .

Table 3. Input required
for a Participant Rule

Specification
Action

belong
Click belong to choose either belong or do
not belong.

select team
Click select team to choose a team from the library.
- For a User Attribute Rule, supply the
required input for the following specification:
Who have an
attribute select user attributeequal toenter value.

Table 4. Input required for a User Attribute Rule

Specification
Action

select user attribute
Click select user attribute to select a user attribute
definition from the library.

equal to
Click equal to to choose from: equal to, not
equal to, less than, less
than or equal to, greater than,
or greater than or equal to.

enter value
Click enter value to display a field in which you can
enter either anBusiness Automation Workflow variable
or a JavaScript expression that produces the value that you want to
compare. Be sure to surround any strings in the expression with double
quotation marks.
- For an Expression Rule, supply the
required input for the following specification:
Who match expression enter
value.

Table 5. Input required for an
Expression Rule

Specification
Action

match
Click match to choose either match or do
not match.

enter value
Click enter value to display a field in which you can
enter either an Business Automation Workflow variable
or a JavaScript expression that produces the value that you want to
compare. Be sure to surround any strings in the expression with double
quotation marks. The variable or expression must evaluate to a specific
user name.