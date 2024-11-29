<!-- image -->

# When to use business rules

The IBM® Integration
Designer tools
have been designed so that users can easily compose integrative business
solutions without programming skills. To this end, you can easily
create and develop business rules in an intuitive graphical programming
environment.

In general, you should use business rules to make a decision when
any of the following conditions are met:

- you want to change the results at run time, on a running server
instead of hard-coded logic in your solution.
- the decision itself naturally takes on the form of a table
- the decision itself naturally takes on the form of a series of
textual if-then statements.

If you want to modify the business rule dynamically you must base
your rule on a template. Basing rules on templates gives you more
dynamicity at run time and allows you to modify settings without involving
an integration developer.

If your decision logic analyzes a collection of data or loops over
a set of data, you should probably structure the decision in a sequential
process, and call out to a rule set whenever there is configurable
data.