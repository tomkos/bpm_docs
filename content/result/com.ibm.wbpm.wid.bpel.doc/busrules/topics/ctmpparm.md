<!-- image -->

# Choosing the correct template parameter values

IBM® Integration
Designer and IBM Workflow
Server use
a different syntax for template parameter values. This inconsistency
does not affect rule set or decision table processing, but
will make it more awkward to edit some business rules in the business
rules manager.

In IBM Integration
Designer,
the value for a float template parameter must take the form '9.99f',
where 9 is any number, and 'f' is a float delimiter. If the 'f' delimiter
is not used in IBM Integration
Designer,
a validation error is added to the rule set.  If the float value is
syntactically correct, the rule can be deployed to the IBM Business Automation
Workflow server,
and executed without error.

In the business process rules manager, a value for a float template
parameter must take the form '99.9'. If you view or edit the rule
set or decision table in the web client, a validation error will be
added for any float value which includes the 'f' delimiter.

This inconsistency is only a problem if you want to modify the
rules and save the new version to the IBM Business Automation
Workflow server.
In this case, you must manually remove the 'f' delimiter from all
float values in the web client before you can save the new version.

## Related tasks

- Creating decision table templates
- Using templates in your decision table
- Creating rule set templates
- Creating a new rule from a template in the rule set editor