<!-- image -->

# Business Rule

Similar to business rule group artifacts, rule sets and decision tables have a name and a target
namespace. The combination of these values must be unique when compared to other rule sets and
decision tables. For example, two rule sets can share the same target namespace value, but must have
different names or a rule set and decision table could have the same name, but have different target
namespace values.

A copy of a business rule can be made from an existing business rule for situations where a
similar rule is required to be scheduled at a specific time with different parameter values for
rules constructed from templates. New rules cannot be fully created from scratch as there must be a
backing Java™ class to provide the implementation for the business rule. The backing Java class is
only created at deploy time. When a new rule is created, it is added to the list of available
targets for the operation which is associated with the original rule. The additional rule is not
persisted however, until the business rule group with which the operation is associated is
published.

The new business rule must have either a different target namespace or name from the original
rule. The display name for the new business rule can remain the same as the original rule as the
combination of the name and namespace provide a key value to identify the business rule. Within the
business rule, the different parameter values which have been defined with a template can be
modified. Scheduling the business rule at a certain time can be done with the
OperationSelectionRecordList or as a default destination with the Operation associated with the
business rule.

The BusinessRule class provides methods that support the following:

- Retrieve the target namespace
- Retrieve the name of the rule set or decision table
- Retrieve and set the display name of the rule set or decision table
- Retrieve the type of the business rule, either rule set or decision table
- Retrieve and set the description for the business rule
- Retrieve the operation that the business rule is associated with.
- Create a copy of the business rule with a different name, target namespace, or both

Figure 1. Class diagram of BusinessRule and related classes

<!-- image -->