<!-- image -->

# Specifying the rule logic for a rule group

## About this task

## Procedure

1. In the editor of your newly created rule group, click the
operation that you want to associate with the rules.
2. If this is a new operation, then it is unlikely that there
will be rule logic defined for it, and you will have the following
options:

Option
Description

Create Operation Definition
Click here to launch the rule group editor and specify the
rule logic yourself.

Link to Orphan
This option will be available if you have already created
an operation and deleted it. Click here to link to the rule logic
that is still defined for the old operation.

Once you have made your choice, the rule logic window
will appear.
3. Define the Default Rule Logic, by clicking Enter
Rule Logic and either select an existing rule set or decision
table from the list, or create a new one. Note: If you
do not select default rule logic, and the rule logic that you provide
does not cover all the possible cases, a runtime exception will occur
when the current condition is not covered.
4. Create your rule logic (you can create as many as necessary)
by clicking the plus icon () beside the Scheduled
Rule Logic label, and either select an existing rule set
or decision table from the list, or create a new one.

## Related concepts

- Rule group editor
- Using rule set names in a rule group

## Related tasks

- Scheduling rules using the rule group editor
- Customizing algorithms for date and time selection
- Creating custom selectors