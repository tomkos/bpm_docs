<!-- image -->

# Programming model

Sharing of the model was deemed critical for not only ease of future maintenance, but for a
consistent programming model for the end user. Sharing this model required compromises between the
needs of desktop tools and runtime execution and authoring -- all have clear sets of requirements to
meet for their respective environments and these requirements at times conflicted with each other.
The artifacts described as part of the overall programming model represent a balance in meeting the
requirements of these different environments.

Modification of business rules is limited to only those items that are defined with templates in
the rule sets and decision tables as well as the operation selection table (effective dates and
targets). Creation of new rule sets and decision tables is only supported through the copy of an
existing rule set or decision table. The business rule group component itself is not eligible for
dynamic authoring in the runtime with the exception of the user defined properties and description
values. Changes that need to be made to the component (for example, adding a new operation) must be
done using IBM Integration Designer and then redeployed or reinstalled in the server.

- Business Rule Group

The BusinessRuleGroup class represents the business rule group component.  The BusinessRuleGroup class can be considered the root object which contains rule sets and decision tables.
- Business Rule Group Properties

The properties on business rule groups are intended to be used for management of business rule groups. Properties set on business rule groups can be used in queries to return only a subset of business rule groups which are to be displayed and then modified.
- Operation

Operations are starting points for reaching individual rule sets and decision tables to modify. The operations of a business rule group match the operations listed in the WSDL which is associated with the business rule group component.
- Business Rule

 The RuleSet and DecisionTable classes are based off a generic BusinessRule class with methods that provide information that is available on both rule sets and decision tables.
- Rule set

A rule set is one type of business rule. Rule sets are typically used when multiple rules may need to be executed based on different conditional values. Rule sets are composed of a rule block and rule templates. The rule block (RuleBlock) contains the different if-then and action rules which make up the logic of the rule set.
- Decision table

Decision tables are another type of business rule which can be managed and modified. Decision tables are typically used when there are a consistent number of conditions which must be evaluated and a specific set of actions to be issued when the conditions are met.
- Templates and Parameters

Templates in rule sets and decision tables are based off of a common definition. Templates have parameters and a user presentation. The template parameter values are defined to allow for changes to be made to the rule once it has been deployed.
- Validation

Many of the main objects have a validate method which allows for the artifacts to be checked for correctness and completeness before publishing the artifacts.
- Tracking Changes

For all objects, a hasChanges method is available to check if there have been any modifications which have occurred to the object and any containing objects.
- BusinessRuleManager

The BusinessRuleManager class is the main class for working with the business rule groups, rule sets and decision tables.
- Exception Handling

Exceptions can occur when validation is called on an artifact or when an artifact is published. When a validation error occurs, the ValidationException is thrown with a list of problems. If there is a problem during publishing due to another transaction publishing the same artifacts, a ChangeConflictException is thrown. Anytime another transaction is detected as changing an artifact, the ChangeConflictException exception is thrown.
- Authorization

The classes do not support any level of authorization. It is up to the client application using the classes to add its own form of authorization.