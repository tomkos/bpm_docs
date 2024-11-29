<!-- image -->

# Decision table editor

Like the rule set, a business rule that takes the form of a decision
table is driven by the interaction between conditions and actions.
The main difference being that, in a decision table, the action is
decided by more than one condition. The conditional logic is represented
as a table where the rows and columns intersect to determine the appropriate
action.

In the decision table editor, the rule is presented in a tabular
format that you can edit as needed. The editor is divided into several
distinct areas, each with its own individual use as shown here.

<!-- image -->

The decision table in this screen capture is an example of how
an interest rate for a mortgage can be calculated by considering both
a customer's salary and credit rating. When this business rule executes,
the initialization action rule (in section 2) begins by taking the
input values and assigning them to the output values. This is done
so that the business process that calls this decision table can continue
to work with the original values. The light gray conditions area of
the table (section 6) shows the multiple conditions that will interact
to determine the customer's interest rate. The row along the top represents
the customer's salary, and the column on the left, the customer's
credit rating. The intersection of the values that are passed into
each of these two conditions specify the action (section 7) that will
determine the customer's interest rate. For example, if a customer's
salary is greater than 500, and the credit rating is 5, then they
will receive the lowest interest rate of 5.0f.

## The individual areas of the decision table

1 The interface area
    - This area displays the interface that is currently being referenced,
as well as the inputs and outputs that you can use in the decision
table.
    - 
2 The Initialize area

- Use this area to configure an initialization action rule (an
operation that will take place when data first enters a decision table),
as well as create a template for one.
- 
3 The initialize tool bar Icon Description Add an initialization action rule Create a template from this action rule.

- Use the icons in the Initialize tool bar to perform the following
functions:

| Icon   | Description                              |
|--------|------------------------------------------|
|        | Add an initialization action rule        |
|        | Create a template from this action rule. |

4 The Table area

- This area displays the table that shows the conditions and the
actions that make up this business rule.
- 
5 The decision table tool bar Icon Description Add a new condition Add a new condition value Add a new action Change the orientation of the condition (thiswill not impact the runtime execution). Create a template for one of the expressionsin this table

- Use the icons in the decision table tool bar to perform the following
functions:

| Icon   | Description                                                                           |
|--------|---------------------------------------------------------------------------------------|
|        | Add a new condition                                                                   |
|        | Add a new condition value                                                             |
|        | Add a new action                                                                      |
|        | Change the orientation of the condition (this will not impact the runtime execution). |
|        | Create a template for one of the expressions in this table                            |

6 The conditions area

- The conditions area appears in light gray. Use this area of the
decision table to define the multiple conditions that will evaluate
the incoming inputs in order to fire a corresponding action.
7 The actions area

- The actions area appears to the right and below the conditions
area (in this particular configuration of the decision table layout).
Use this area of the decision table to define the actions that will
fire when the conditions intersect.
8 The properties area

- This area displays properties that are relevant to the object
that is currently selected in the editor. Click the tabs to the left
of this view to toggle through the pages. Some pages display properties
in tabular format, and you can add or modify these properties by clicking
the appropriate cell and then interacting with the graphical interface
that appears.
- The contents of the page will differ on the activity or object
chosen. In all cases, you can type F1 to launch a dedicated help window.

## Working with the decision table editor

- Add a condition or a condition value
- Add an action
- Add an initialization action rule
- Using an otherwise condition
- Change the layout of your decision table
- Work with templates

## Related concepts

- Rule group editor
- Rule set editor

## Related tasks

- Working with conditions in a decision table
- Configuring actions in a decision table
- Working with initialization action rules
- Using an otherwise condition
- Changing the layout of your decision table
- Creating decision table templates
- Using templates in your decision table
- Editing a decision table template