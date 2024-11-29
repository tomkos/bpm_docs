<!-- image -->

# Choosing between a rule set and a decision table

1. If your rules seem to take the form of a large number of unstructured
sentences, then you should probably use a rule set to capture their
business logic.  A rule set is more flexible than the more structured
decision table.
2. If you notice that every rule seems to use the same decision criteria,
then it would be a good idea to use a decision table.  In this case,
the decision criteria that all the rules share in common can be captured
once, and then you can define the parameters for each criteria.
3. If your rules naturally take the form of a table, then you should
probably use a decision table.
4. However, if this table has a large number of holes, where some
decision criteria are not applicable, or where the output values are
undefined, then you should use a rule set.  The structure of the decision
table works well for regularity, but not for exception cases.