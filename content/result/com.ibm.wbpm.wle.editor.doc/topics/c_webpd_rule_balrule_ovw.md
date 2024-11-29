# Business rule parts and structure in the Process Designer

1. definitions part
2. if (conditions) part
3. then (actions) part
4. else (optional actions) part

## Definitions

The definitions part of a rule
gives you more control over your business rules when you set variables
at the beginning of your rule. Variables help you identify and then
reference an occurrence of a business term by a convenient name. Use
variables to make your business rules less ambiguous and easier to
understand.

Define a variable by giving it a name of your choice
and then setting a value for the variable. This value can be a number
(or an arithmetic expression whose result is a number), text, or a
predefined business term that already exists in your rule (for example,
customer). Once you have set a variable, it becomes available in all
the parts of the current rule. The variable is valid only in the rule
in which it is defined.

This is a very basic illustration of the
definitions part of a rule. For more information about complex versions
of the definition part, such as multiple occurrences of a value, or
adding a where clause to a definition to apply
further restrictions on the variables, refer to the related section
in the IBM® Operational Decision
Manager knowledge
center, "BAL constructs -- definitions." A related link is provided.

## Conditions

## Actions

```
set applicant\_list to applicant\_list;
```