# Defining Team rules (deprecated)

## Before you begin

This procedure triggers
dynamic group creation, which can be time consuming. You can configure IBM® Business Automation
Workflow to deactivate these triggers.

## Procedure

To define rules, follow these steps.

1. Open the Process Designer desktop
editor.
2. Open the team that you want to edit.
3. Click Add Rule to choose the type
of rule you want. When you define team rules, you have
the following types from which to choose:
Table 1. Rule
types available for defining teams

Rule type
Description

Participant Rule
Enables user selection according to team membership.

User Attribute Rule
Enables user selection that is based on user attributes. To
learn how to create user attribute definitions, see Creating a user attribute definition.

Expression Rule
Enables the selection of users who match a particular expression
that you provide.
4 Supply the necessary information for the type of rule thatyou choose.
    - For a Participant Rule, supply the input that you want for
the following specification:
Who belong to
team select participant.

Table 2. Input
required for a Participant Rule

Expression
Action

belong
Click belong to choose either belong or do
not belong.

select participant
Click select participant to choose an
existing team.
    - For a User Attribute Rule, supply the
input that you want for the following specification.
Note: To
learn how to create user attribute definitions, see Creating a user attribute definition.
Who have an
attribute select user attribute equal to enter value.

Table 3. Input required for a User Attribute
Rule

Expression
Action

select user attribute
Click select user attribute to
select an existing user attribute definition.

equal to
Click equal to to choose from: equal
to, not equal to, less
than, less than or equal to, greater
than, or greater than or equal to.

enter value
Click enter value to display a field
in which you can enter either an IBM Business Automation Workflow variable
or a JavaScript expression that produces the value that you want to
compare. Be sure to surround any strings in the expression with double
quotation marks.

For example, when you select Using
Expression and define a User Attribute Rule, you can enter
an expression that returns a default value when the complex variable
is null and the attribute for the variable otherwise. For example,
if the user attribute is a string, the expression can be:tw.local.processData==null ?
"":tw.local.processData.targetView.complexity
    - For an Expression Rule, supply the input
that you want for the following specification:
Who match expression enter
value.

Table 4. Input required for an Expression
Rule

Expression
Action

match
Click match to choose either match or do
not match.

enter value
Click enter value to display a field
in which you can enter either an Business Automation Workflow variable
or a JavaScript expression that produces the value that you want to
compare. Be sure to surround any strings in the expression with double
quotation marks. The expression must evaluate to a specific user name.