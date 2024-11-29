<!-- image -->

# Structuring an ordered rule set for modification

For example, suppose you have a rule set which calculates the interest
rate for a loan, given the loan amount.

It may look like this:

- Rule 1: primeRate = 5
- Rule 2: if amount < 1000 rate = primeRate;
- Rule 3: if amount >= 1000 rate = primeRate + 1
- Rule 4: if amount >= 5000 rate = primeRate + 2

In this situation, the behavior of the rule set will change significantly
if you reorder the rules, and may even break.  Caution should be taken
when you reorder these rules in the web client, and the logic must
be correct before you publish the changes. The best practice is to
make the modifications in the tools environment, test them, and
then copy those changes to the runtime system.

That being said, it is more likely that new rules will be added
using a template in the web client. Caution should be taken to make
sure that the new rule is inserted correctly in the rule set.  If
the web user is skilled, they may be able to position the new rule
correctly.  If not, you can take these precautions to avoid error:

1. Add a comment to the rule set which describes the general structure
of the rule set, so that it is easier for the web user to make changes
to it.
2. Add comments to each template which clearly describe where the
template instance should be located within the rule set.  You can
do this by referencing existing rules in the rule set, and indicating
that the template should be placed before or after them.
3. Keep the rule set simple.  If possible, limit the actual decision
count in the rule set to one.  In other words, make one decision,
not many.
4. Use the default pattern.  In this pattern, we suggest you
assign the default value at the start, and then put the special
case rules later.  Your web users will come to learn this pattern.
5 Structure your special case rules so that they are mutually independent. For example, the rule set above would be more robust if rules 2 through4 had the following form: This rule could also be converted into a template which hasplug-gable values for each parameter in yellow.
    - if amount >= min and amount < max rate = primeRate + someValue
6. If it is difficult to create mutually exclusive rules, then you
should order the special case rules in ascending or descending order.
 This gives the web user a pattern which is easy to follow.