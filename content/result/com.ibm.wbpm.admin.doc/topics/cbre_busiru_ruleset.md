<!-- image -->

# Rule sets

If the condition is met, the action is performed. This may result in more than one action being
performed by the rule set. The order of rule processing is determined by the order of the rule
statements in the if/then rule set. Therefore, when you modify or add a rule, you need to be sure
that it is in the correct sequence.

- An if/then rule determines what action to take according to the condition of the incoming
message.
- An action rule determines what action to take no matter what the incoming message is.

A condition in a rule contains a condition expression, which could be a simple string or an
and, or, or not.

You create new rule sets or modify existing rule sets in the business rules manager using
templates defined for that rule set. The templates provide the structure that determines how the
rule set functions. Rule templates are not shared between rule sets.

- Creating rule set entries

You create a new rule set entry by copying an existing rule set entry and modifying its values.
- Creating rules within rule sets from templates

You create a new rule within a rule set using the rule templates associated with that rule set.
- Modifying rules within rule sets using templates

You modify a rule in a rule set using templates associated with that rule set.