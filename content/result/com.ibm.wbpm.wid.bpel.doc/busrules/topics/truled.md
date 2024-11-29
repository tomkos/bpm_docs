<!-- image -->

# Creating a rule set

## Procedure

1. In the workbench, switch to the business integration perspective.
2. From the main menu, click File > New > Rule Set.
3. In the New Rule Set window, specify a module (or create
one if necessary by clicking New), a folder
and a name for the new rule set, and click Next.
4. In the select an interface and operation window, browse
to an existing rule group, or click New to
create one. If necessary, use the drop down lists to select
a different interface and operation.
5. Click Finish.

## Results

- Rule set editor

A rule set captures decision-making business logic in the form of a series of if-then statements.
- Adding a variable to a rule set

Variables store the data that are used by a rule set.
- Creating an if-then rule in the rule set editor

An if-then rule determines what action to run according to the condition of the incoming message.
- Creating an action rule in the rule set editor

An action rule determines what action to run no matter what the incoming message is.
- Creating rule set templates

Use a rule set template to define the implementation and parameters for an if-then or action rule. This template can then be used to create new instances of the same rule using different parameters.
- Creating a new rule from a template in the rule set editor

Rules can be created from existing templates. In this way, you can create a similar rule without having to redefine the implementation, and by making changes to the parameters within the constraints specified.
- Letting a web user override the default values in a rule set

In a rule set, there are often situations where you want to allow a web user to override the default output value as programmed. To capture this in a rule set, use the following approach.
- Structuring an ordered rule set for modification

In some rule sets, there may be a tight dependency between the rules and their order of processing.  This is the nature of sequential execution. Here are some suggestions on how to plan for possible changes to an ordered rule set.
- Calling one rule set from another one

Currently, you cannot call one rule set from another directly, you can only call out to operations which exist in another component. To work around this, separate the rule sets into two distinct rule groups, and then invoke one from the other.