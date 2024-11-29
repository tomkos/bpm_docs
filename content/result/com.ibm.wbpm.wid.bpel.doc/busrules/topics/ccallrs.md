<!-- image -->

# Calling one rule set from another one

For example, suppose you want rulesetA to call rulesetB. Here is
how you would set it up:

1. Put rulesetA in rulegroupA.
2. Put rulesetB in rulegroupB.
3. Create a reference in rulegroupA with the same interface as rulegroupB.
4. In the assembly editor, wire rulegroupB to the reference in rulegroupA.
5. In rulesetA, add an invoke rule and select the rulesetB operation
in the rulegroupB reference.

When you invoke an operation that returns the operation output
as the output of the decision table, the invoke output variable type
must match the decision table output. If they do not match, code assist
returns an empty list because there is no business object that matches
the output type of the operation. For example, an invoke operation
must return a value of "Country" if the decision table is already
configured to output a value of "Country."