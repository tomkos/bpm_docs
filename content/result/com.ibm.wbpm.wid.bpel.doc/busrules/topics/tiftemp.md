<!-- image -->

# Creating rule set templates

## About this task

You can create templates for both if-then and action rules
in the same way.

Business rules based on templates are dynamically
modifiable in the runtime environment. The parameters of the rule
can be modified within certain constraints. Base your rule on a template
if you want to give your business analyst the ability to modify the
parameters of a rule without involving the integration developer.

## Procedure

1. In the rule set editor, click either the Add
If-then template (,) or Add
Action template () icon .
A new template appears as shown in this image (note that
the window is slightly different for the action template).
2 In the Parameters row, create a new parameter as follows: Note: If you apply a constraint to a parameter, the runtimeuser of a rule using this template will be able to modify the parameteronly in accordance with that constraint.
    1. Click the  icon. A new parameter will
appear.
    2. In the Type column, click Select Type,
and select an appropriate choice from the list.
    3. To add a restriction on how the parameter can be configured,
click None under the Constraint column.
A list showing the available choices will appear.
    4. To specify an upper and a lower limit for a numeric
parameter, click Range, and then use the choices
in the window to build your expression. You can either
choose an existing template which will then prompt you for a value,
or you can compose it yourself by clicking the appropriate operators
and values in sequence.
    5. To specify a list of choices, click Enumeration,
and add items to the Enumeration Items table in the Constraint tab
in the properties view. The Value is the actual setting,
and Presentation is how it is displayed in an actual rule.
3. In the Presentation row, write a sentence that will describe
the rule to another user. To insert a parameter that the
user can make changes to, click the triangular icon to launch a menu,
and then choose a parameter from the list.
4 Compose the condition as follows:

1. In the If row, click Condition.
A pop-up window appears.
2. Use the choices in the window to build your condition.
5 Set the action as follows:

1. In the Then row, click Action.
A pop-up window appears.
2. Use the choices in the window to set the action.

## Results

## Related concepts

- Rule set editor
- Choosing the correct template parameter values

## Related tasks

- Adding a variable to a rule set
- Creating an if-then rule in the rule set editor
- Creating an action rule in the rule set editor
- Creating a new rule from a template in the rule set editor
- Creating decision table templates
- Using templates in your decision table