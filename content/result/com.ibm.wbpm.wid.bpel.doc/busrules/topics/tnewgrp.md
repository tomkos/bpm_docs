<!-- image -->

# Creating a rule group

## About this task

## Procedure

1. In the workbench, switch to the business integration
perspective.
2. From the main menu, click File > New > Rule Group.
3. In the New Rule Group window, specify a module (or create
one if necessary by clicking New), a folder
and a name for the new rule group, and click Next.
4. In the select an interface window, browse to an existing
interface or click New to create one. If
you create a new interface here, you will have to create an operation
using the interface editor before you can use it in the rule group.

## Results

- Rule group editor

A rule group controls the timing and implementation of business rules.
- Specifying the rule logic for a rule group

The rule logic is either a rule set or a decision table that is invoked at the designated time by the rule group.
- Scheduling rules using the rule group editor

The rule group editor can be used to schedule the running of a specific rule for a specific date and time.
- Customizing algorithms for date and time selection

When you want to specialize the date and time selection criteria, you can create your own custom algorithm.
- Creating custom selectors

Selectors can be used to determine dynamically, at run time, between two or more possible invocations. The decision is driven by selection criteria that you can customize to your needs.
- Using rule set names in a rule group

Each operation in a rule group contains a rule logic table, which maps a set of date ranges to a rule set or decision table. To avoid confusion, it is always a good practice to use rule set and decision table names which are unique within the operation. If the same name is used twice, it is more difficult to see that there are actually two different rule logics.