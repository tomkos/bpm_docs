<!-- image -->

# Rule set

The RuleSet class provides methods that support the following:

- Retrieve a list of rule blocks for the rule set
- Retrieve a list of rule templates defined in the rules set

Currently each rule set can only have one rule block, while there can be multiple rule templates
defined in the rule set. The rule block contains the set of rules that will be executed when the
rule set is invoked. The rule block allows for the order of the rules to be modified. A rule block
must have at least one rule defined. The rules (Rule) can be defined as template
instance rules (TemplateInstanceRule) or hard-coded. If an if-then or action rule has been defined
with a template, it can be removed from the rule block. If a new instance of rule was created with a
template, it can be added to the rule block.

If a rule is hard-coded and was not defined with a template, it cannot be modified or removed
from the rule block. The expectation with these rules is that they have been designed to always be
part of the rule set logic and are not to be changed or repeated within the logic.

When a new rule is created with a template, it must have a unique name value. The list of
existing rules can be retrieved and checked first before creating the rule.

For hard-coded if-then and action rules, only the name and presentation can be retrieved. The
presentation is a string which can be used to display information about the rule in client
applications. For if-then or action rules that are defined with a template, the name and
presentation can be retrieved as well as additional information. Specific parameter values can be
retrieved and changed. With a template (RuleSetRuleTemplate) defined in the rule
set, another instance of the rule can be created within the rule set and parameter values can be
set. For example, if you have a rule saying that a customer of a particular status level receives a
discount of a specific amount. This logic could be defined with a single rule template and then
repeated with parameter values changed for the status level (gold, silver, bronze, and so on) and
the discount amount (15%, 10%, 5%, and so on).

The parameters for a rule defined with a template are specific to the instance of the rule. The
template only defines a standard presentation and the number of parameters for the rule. Each rule
defined with a template can have different values as explained in the example on discounts for
different customer status.

- Retrieve a rule by index
- Add a rule that was defined with a template
- Remove a rule defined with a template
- Modify the order of a rule by one place or to a specific index location

- Retrieve the name of the rule
- Retrieve the display name of the rule
- Retrieve the user presentation
- Retrieve the rule block

- Create a rule template instance from this template definition
- Retrieve the parent rule set

- Retrieve the parameters for the rule
- Retrieve the template definition which defined the rule

- Retrieve the template ID
- Retrieve the name
- Retrieve and set the display name
- Retrieve and set the description
- Retrieve the parameters for this template
- Retrieve the user presentation

Figure 1. Class diagram of BusinessRule and related classes

<!-- image -->