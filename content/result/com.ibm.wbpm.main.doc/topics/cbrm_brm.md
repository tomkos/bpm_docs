<!-- image -->

# BusinessRuleManager

The BusinessRuleManager has methods which allow for retrieving business rule
groups by name, target namespace, or custom properties. It also has a method for publishing changes
which have been made to business rule groups, rule sets, or decision tables.

The BusinessRuleManager class provides methods that support the following:

- Retrieve all of the business rule groups
- Retrieve business rule groups of a specific target namespace
- Retrieve business rule groups of a specific name
- Retrieve business rule groups of a specific name and target namespace
- Retrieve business rule groups which contain a specific property
- Retrieve business rule groups which contain specific properties
- Publish business rule groups

Figure 1. Class diagram for BusinessRuleManager and package

<!-- image -->

## Rule Group Component Query

- Business rule group component target name space
- Business rule group component name
- Property name
- Property value

Each property name can only be defined once per business rule group component.

The query function supported by this class is a small subset of the full SQL language. The user
does not provide the SQL statement, but rather provides the values as parameters for a single
property or a tree structure containing the information for a multi-property query in the form of
nodes. There are logical operator nodes and property query nodes which all implement the
QueryNode interface. The logical operator nodes specify the boolean operators (AND,
OR, NOT). These are created through the QueryNodeFactory. As part of the creation
of these logical operator nodes, the left and right operators must be specified with additional
QueryNode classes. These nodes can either be a property query node or another
logical operator node. If a property query node is passed, it will contain the property name, value
and operator (EQUAL (==), NOT\_EQUAL (!=), LIKE, or NOTLIKE). The overall QueryNode
is parsed by the class and a query is performed on the underlying data in persistent storage.

Wildcard searches are supported when the LIKE and NOTLIKE operators are used. Both the '%' and
'\_' characters are supported in wildcard searches. The '%' character is used when there are an
infinite number of characters which are not known or should not be considered when searching. For
example if a search was to be performed for all business rule groups that have a property with a
name of Department and value that begins with North, the value would be
specified as North%. Another example, suppose that all Departments with a
value ending in Region was required. The value would be
%Region. The '%' character can also be used in the middle of a string. For
example, if there were business rule groups with properties that had values of
NorthCentralRegion, NorthEastRegion, and
NorthWestRegion, a value of North%Region could be
specified.

The '\_' character is used when there is a single character which is unknown or should not be
considered when searching. For example, if a search for all business rule groups with Department
properties with values of Dept1North, Dept2North,
Dept3North, and Dept4North was required, a value of
Dept\_North could be specified and all 4 of the business rule groups with
these properties will be returned. The '\_' character can be used multiple times in a search value
with each instance indicating a single character to ignore. The '\_' character can be used at the
beginning or end of a value. For example if two characters were to be ignored in a value, two '\_'
could be used such as Dept\_\_outh.

In order to treat '%' and '\_' as literal characters and not wildcards a '\' escape character must
be specified preceding the '%' or '\_'. For example if the property name was
%Discount, in order to use this in a query, \%Discount
would need to be specified. If the '\' character is to be used as a literal character, another '\'
escape character must be used such as Orders\\Customer. If a single '\'
character is found without a following '%', '\_', or '\', an IllegalArgumentException will be
thrown.

Wildcard characters can only be used on the left operator (property value). Wildcard characters
cannot be used in property name.

During searches on the value of a specific property or a search for values which do not match a
property, the absence of a property causes the artifact to be ignored from consideration in the
search. For example, if there are 3 business rule groups (A, B, and C) and only two (A and B) have a
property named Department with different values (either
Accounting or Shipping) a search for all business rule
groups which do not have a Department property of
Accounting will only return the business rule group which has the
Department property defined but does not equal
Accounting (business rule group B). The business rule group (C) which does
not have the Department property, will not be returned as it does not have
the property defined in any way.

When using properties for searching, there are two special properties named
IBMSystemName and IBMSystemTargetNameSpace which can
be used for searching based on the name and namespace of an artifact. These values can also be
retrieved with the getName and getTargetNameSpace methods.

```
List getBRGsByTNS (string tNSName, Operator op, int skip, int threshold)
List getBRGByName(string Name, Operator op, int skip, int threshold)
List getBRGsByTNSAndName (string tNSName, Operator, tNSOp, string
	name, Operator nameOp, int skip, int threshold)
List getBRGsBySingleProperty (string propertyName, string propertyValue,
	Operator op, int skip, int threshold)
List getBRGsByProperties (QueryNode queryTree, int skip, int threshold)
```

The 'skip' and 'threshold' parameters provide the user the capability of fetching a partial
result list up to the specified threshold. A value of zero for both of these parameters will return
the full result list. The cursor is not maintained in the result set from a query call. If a skip
value is used, it is possible that additions or deletions could have been made to the result set
such that a subsequent request will return business rule groups which were in an earlier result
set.

Figure 2. Class diagram for QueryNodeFactory and related classes

<!-- image -->

The nodes in the tree allow the user to specify a search expression using the boolean operators,
wild cards (% and escape) and the property/value pair. The operator is only valid for the values,
the operator for the property is always equals (==).

## Publishing

Publishing of business rule changes is done at the business rule group component level. The user
can publish 1…n business rule group components. Before a publish operation is performed, a validate
action is performed on the business rule group and the different objects contained in the business
rule group (operation selection table, rule sets, decision table, and so on). Each publish request
will occur within a single transaction and if any exceptions are encountered during validation or
database publishing the transaction is rolled back and no changes for any business rule group are
published to the repository. This allows changes that are dependent on each other within a single
component (for example, operation selection table and a rule set) or dependencies between components
to occur within one atomic operation.

At publishing time, a check will be made to ensure that the items which are to be published have
not been changed by another transaction. To reduce the possibilities of a conflict, the publish
method will give the user the ability to choose to publish all artifacts whether they are changed or
not or only those artifacts that were changed within the business rule group. The default behavior
will be to publish all artifacts. If the option is set to publish all artifacts and another
transaction had changed the artifacts in the meantime, a ChangeConflictException
will be thrown. Specifying to only publish those artifacts which have changed will reduce the chance
of conflict. Publishing only those artifacts that were changed could result in two users pushing
changes to the repository for two different artifacts within a business rule group (for example, two
rule sets) which could introduce incompatible changes within the business rule group. Because this
potential situation, this option should be used with caution.