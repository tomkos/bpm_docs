# Variable types (deprecated)

## Complex variables for hierarchical data

<!-- image -->

For
more information about creating complex, hierarchical variable types,
see the related topic "Adding process variables to a BPD."

- SQLResult
- XMLDocument
- XMLElement
- XMLNodeList

## Collections (lists) of variables

You can
write rules against collections, or lists of variables, using Business
Action Language (BAL) rule constructs. You can use a variable to retrieve
a collection (list) of objects of a specific type. Use a list parameter
in a business object when then are numerous objects that your rule
must run against, instead of just a single object. For example, if
you are writing a rule about an invoice, and there are multiple line
items in the invoice, then the invoice is actually a collection of
line items. To write a rule against the number of line items (if there
are 10 or more line items, then process this invoice manually), add
a list parameter in a complex variable to your rule.

<!-- image -->

## Predefined variable types

1. Open a process application in Process Designer.
2. Click the indicator next to the Toolkits category to see a list
of toolkit dependencies for the current process application.
3. Click the indicator next to the System Data toolkit to see its
contents.
4. Click the Data category
5. Double-click the Record business object
to open it. The Documentation field provides
information about the business object. The documentation informs you
that a Record is a group of ANY typed variables
and that you do not need to declare the number of ANY typed variables
that you want to go into the Record. So, the Record object is similar
to a Structure object, except you do not need to declare the type
or the number of variables it contains.

For additional information about using variable types in rules, refer to the related topic "Types
of variable definition" in the IBM® Operational Decision
Manager documentation.