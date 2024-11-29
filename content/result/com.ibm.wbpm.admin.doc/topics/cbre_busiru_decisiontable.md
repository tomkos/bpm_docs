<!-- image -->

# Decision tables

Like the if/then rule set, the decision table is driven by the interaction of conditions and
actions. The main difference is that in a decision table, the action is decided by more than one
condition, and more than one action can be associated with each set of conditions. If the conditions
are met, then the corresponding action or actions are performed.

## Templates

You use templates to modify decision table values in the business process rules manager. The
templates are designed in IBM® Integration
Designer and
contained in the business rule definition. The templates determine which aspects of a decision table
you can modify and provide a list of valid values to choose from. You create new rows or columns in
the table or new actions based on the templates defined for that decision table, and you modify
existing conditions or actions that were created with the template. Decision table templates are not
shared between decision tables.

## Initialization action rules

Decision tables support the use of an initialization action rule, which runs before the decision
table is started and allows for preprocessing, such as for creating business objects or setting
initial values. You can modify an initialization action rule in the business process rules manager,
provided that the business rule definition was designed in IBM Integration
Designer with an initialization action.

Although only one initialization action rule can be created from a single template, the action
rule can have multiple action expressions in it, so it can perform multiple actions. If an
initialization rule template is defined for a particular decision table, it can only be used in that
table.

## Otherwise conditions

The otherwise condition is a special condition that will be entered by default if no
other condition in the decision table is applicable.

The otherwise condition will only display in the business process rules manager if
it is included in the decision table definition that was designed in IBM Integration
Designer. You cannot add or remove it dynamically in
the business process rules manager.

However, you can incorporate actions defined with templates for the otherwise
condition. The otherwise condition can be used zero or one time for any condition being
checked.

Figure 1. Decision table

<!-- image -->

The example shows that gold customers spending $500 - $1999 get an 8% discount while silver
customers spending $500 - $2000 get a 3% discount. Gold customers spending $2000 or more get a 10%
discount while silver customers spending $2000 or more get a 5% discount. Gold customers spending
less than $500 get a 2% discount while silver customers spending less than $500 get a 0%
discount.

- Creating decision table entries

You create a new decision table entry by copying an existing decision table entry and modifying its values.
- Special actions menu

The Decision Table page has a Special actions menu to edit the values in a decision table or modify the structure and variables of a template.
- Modifying decision table entries

You edit a decision table by directly entering the new value into the appropriate input field or by selecting a value from the field's list box options.
- Modifying template values of decision tables

You modify the structure and values of a decision table template by using the Special actions menu and by directly entering values into the appropriate input fields.