<!-- image -->

# Business rules

Using IBM® Integration
Designer,
you can compose integrative business solutions without programming
skills, creating and developing business rules in a graphical programming
environment.

## An example of a business rule

| Customer status   | Quoted price   |
|-------------------|----------------|
| Bronze            | $5             |
| Silver            | $4             |
| Gold              | $3             |

The interaction between conditions and actions determines
the form of your business rules. If the condition is met, the action
is performed. There are two possible forms, rule sets and decision
tables, which are described below.

## Key concepts

- Rule groups
- Rule sets
- Decision tables
- Business roles in the development of business rules
- Templates
- Scheduling

## Rule groups

A rule group is the
highest level implementation component of a business rule. The rule
group acts as a gateway to the business rules since it is exposed
as an SCA component in the runtime environment. The rule group defines
the interface and operation that the business rules will implement.
Rule sets and decision tables which share a common business focus
can be gathered under the umbrella of a single rule group. Rule sets
and decision tables cannot be invoked directly and may only be invoked
through a rule group. One of the most important functions of the rule
group is to define a date and time range during which a specific rule
set or decision table will be used.

## Rule sets

A rule set is a set
of business rules that are evaluated sequentially. There are two kinds
of rule that can be used in a rule set.

An if-then rule set is a set of textual statements
or rules where if is the condition of the rule, and then is
the action.

The first example we discussed used an if-then
rule set:

| Customer status   | Quoted price   | If-then rule                                   |
|-------------------|----------------|------------------------------------------------|
| Bronze            | $5             | If customer has bronze status then price is 5. |
| Silver            | $4             | If customer has silver status then price is 4. |
| Gold              | $3             | If customer has gold status then price is 3.   |

In the runtime environment, each rule is evaluated sequentially,
and each condition that evaluates to true is acted upon, which could
result in more than one action. An example might be a customer loyalty
scheme in which a customer that makes a purchase seven weeks out of
ten receives a free gift, and a customer that makes a purchase in
all ten weeks receives an additional 10% discount voucher for future
use. Customers who made a purchase in all ten weeks evaluate to true
for both conditions and receive both incentives.

## Decision tables

Another form
that a business rule can take is a decision table.

Like
the if-then rule set, the decision table is driven by the interaction
between conditions and actions. However, in a decision table, more
than one condition decides the action. The conditional logic is represented
in a table where the rows and columns intersect to determine the appropriate
action. Each column represents a condition. In a decision table, several
conditions may get evaluated, but only one action is acted on.

For
example, in this example the customer status is represented by the
rows in the table, and the potential amount of money that the customer
spends is represented by the columns. During the transaction, the
customer receives a bigger discount when he or she purchases more
items. The discount depends on the customer's status. The decision
table enforces this business rule behavior through the intersection
of the status (rows) and items purchased (columns). The first column
shows us that the results of each of  intersection is the same as
the if-then rule set: if the customer with bronze status buys less
than 20 items, he pays $5 for each item; if the customer with silver
status buys less than 20 items, she pays $4 for each item; while the
customer with gold status pays $3 for each item.

| Customer status   | Buys less than 20 items   | Buys more than 20 item   | Buys more than 30 items   | Buys more than 40 items   |
|-------------------|---------------------------|--------------------------|---------------------------|---------------------------|
| Bronze            | $5 per item               | $4.50 per item           | $4 per item               | $3.50 per item            |
| Silver            | $4 per item               | $3.50 per item           | $3 per item               | $2.50 per item            |
| Gold              | $3 per item               | $2.50 per item           | $2 per item               | $1.50 per item            |

Here are a few concepts that are unique to decision
tables:

## Business roles in the development of business
rules

Because business rules are developed and maintained
by several users, you need to create roles that indicate the different
ways that different users create, implement, and modify business rules,
and how those users interact while working with a business rule.

Figure 1. How two different roles interact in working
with a business rule

<!-- image -->

## Templates

One of the responsibilities
of the business analyst is to keep business rules relevant. This is
especially necessary when a business environment must be dynamic to
meet ever-changing business needs. For example, your company might
have to periodically adjust sale prices to match the competition's
prices. After deployment, you might still need to modify your prices
or other properties. It is rarely feasible or cost effective to get
an integration developer to make each adjustment.

In order to
create business rules that are dynamically modifiable at run time
the business rules must be based on templates. Decision tables can
also be made dynamically modifiable at run time by basing the conditions
or actions of the decision table on templates.

A template defines
what parts of a deployed business rule can be modified by an authorized
user. The template uses parameters and constraints to provide dynamicity.
Parameters and constraints define which values can be modified and
by how much.

- Range constraints
- Range constraints apply to numeric parameters that are used in
rules. An authorized user may adjust a parameter but the parameter
must be held within a certain numeric range. For example you know
that your product costs 100 to manufacture so your range of prices
might be between 105 and 500.

- Enumeration constraints
- Enumeration constraints are in a list that is either numeric
or textual. The authorized user must choose from one of the options
in the list. For example, the user could upgrade a customer's credit
rating from silver to gold.

Figure 2. An example of a template constraining a
business rule

<!-- image -->

In this example, Vendor A
can use a business rule template to adjust the price of the item to
beat Vendor B's pricing. However, when Vendor B tries to do something
similar, the constraint on the business rule template will not allow
it. The constraint does not permit a lower price than the one that
is currently in place.

## Scheduling

When changes to
the business rules are mandated and expected, you can design rules
and deploy them to the server so that they become active when they
are needed. This functionality is important when, for example, business
analysts have to be prepared for changes to governmental tax regulations
that will not go into affect until the first of the year, or (as shown
in the following example), when a special price is put into effect
for one special day only.

Figure 3. An example of how a business
rule can be created for later use

<!-- image -->