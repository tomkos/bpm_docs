<!-- image -->

# Creating decision table templates

## About this task

Decision tables, in which the conditions or actions are
based on templates are dynamically modifiable in the runtime environment.
Base the conditions or actions of a decision table on a template if
you want to give your business analyst the ability to modify the runtime
behavior of the decision table without involving the integration developer.

## Procedure

1. In the decision table editor, choose a cell and click the Converts
an expression of a decision table cell into a template () icon . If you are working with an existing value
in the table, then the system will examine the expression and convert
all literal values into parameters.The value appears
in a small square to indicate that it is a template, and a new template
appears as in the General tab of the properties
area shown in this image:
2 In the Parameters row, you can create a new parameter asfollows:
    1. Click the  icon. A new parameter will
appear.
    2. In the Type column, click Select Type,
and select an appropriate choice from the list.
    3. To add a restriction on how the parameter can be configured,
click None under the Constraint column.
A list showing the available choices will appear.
    4. To specify an upper and a lower limit for the constraint,
click Range, and then use the choices in the
window to build your expression. You can either choose
an existing template which will then prompt you for a value, or you
can compose it yourself by clicking the appropriate operators and
values in sequence.
    5. Alternatively, to specify a list of choices, click Enumeration,
and add an item to the Enumeration Items table in the Constraint tab
in the properties view. The Value is the actual setting,
and Presentation is how it is displayed in an actual rule.
3. In the Presentation row, write a sentence that will appear
in the cell. To insert a parameter that the user can make
changes to, click the triangular icon to launch a menu, and then choose
a parameter from the list.
4. If you want to make changes to this value's implementation,
click the first cell in the Expression row, and use the choices in
the pop-up window to build a new expression.

## Related concepts

- Decision table editor
- Choosing the correct template parameter values

## Related tasks

- Working with conditions in a decision table
- Configuring actions in a decision table
- Working with initialization action rules
- Using an otherwise condition
- Changing the layout of your decision table
- Using templates in your decision table
- Editing a decision table template
- Creating rule set templates
- Creating a new rule from a template in the rule set editor