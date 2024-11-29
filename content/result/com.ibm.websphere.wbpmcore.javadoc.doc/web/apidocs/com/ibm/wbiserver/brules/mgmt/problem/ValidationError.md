- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum ValidationError

- java.lang.Object
    - java.lang.Enum<ValidationError>
        - com.ibm.wbiserver.brules.mgmt.problem.ValidationError

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<ValidationError>

public enum ValidationError
extends java.lang.Enum<ValidationError>
An enum used to identify validation errors that are detected.

- =========== ENUM CONSTANT SUMMARY =========== =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

BUS\_RULE\_NOT\_IN\_AVAILABLE\_TARGET\_LIST
This error indicates that the new business rule being set as a target is
 not in the available targets list for the operation.

CANNOT\_CHG\_HARD\_CODED\_ACTION\_VALUE\_TO\_TEMPLATE
This error indicates that an attempt was made to change a hard-coded
 action value to a template instance.

CASE\_EDGE\_CHILD\_NODE\_MISSING
The child node is missing from a case edge.

CASE\_EDGE\_VALUE\_DEFINITION\_MISSING
The value definition is missing from a case edge.

CASE\_EDGES\_ARE\_MISSING
A condition node has no case edges.

DUPLICATE\_PROPERTY\_NAME
This error indicates that an attempt was made to add a new property to a
 business rule group but the new property has the same name as an existing
 property.

END\_DATE\_NOT\_SET
This error indicates that the end date in an
 OperationSelectionRecord is not set.

INCORRECT\_TEMPLATE
The template associated with the specified template instance expression is not available
 to the part of the decision table to which it is being added.

INVALID\_ACTION\_VALUE\_TEMPLATE
This error indicates that the action value template associated being used
 to define the value for an action is not in the list of available
 templates for that action.

INVALID\_ATTEMPT\_TO\_SET\_VALUE\_TEMPLATE\_INSTANCE
An attempt was made to set a value template instance into part of a decision table that
 currently does not have a value template instance.

INVALID\_BOOLEAN\_VALUE
This error indicates that the specified string does not represent a valid
 boolean value.

INVALID\_CONDITION\_VALUE\_TEMPLATE
This error indicates that the condition value template associated with a
 case edge being added to a condition node is not contained within the
 condition term definition for that condition node.

NO\_TEMPLATES\_AVAILABLE\_FOR\_NEW\_ACTION\_NODES
There are no templates available to fill in new action nodes.

OP\_SEL\_RECORD\_HAS\_NO\_OPERATION
This error indicates that an operation selection record is not associated
 with an operation.

OPERATION\_CONTAINS\_NO\_TARGETS
This error indicates that the operation has no default business rule
 target and also has no business rule targets qualified by date ranges.

OVERLAPPING\_RANGES
This error indicates that the date ranges of two operation selection
 records overlap.

PARM\_NOT\_DEFINED\_IN\_TEMPLATE
This error indicates that an instance of a template was being created and
 one of the parameter values specified was for a parameter that is not
 defined on the template being instantiated.

PARM\_VALUE\_LIST\_CONTAINS\_UNEXPECTED\_VALUE
This error indicates that the parameter value list specified when
 creating an instance of a template contains a value that does not
 correspond to any parameter in that template.

REQUIRED\_PARM\_NOT\_SPECIFIED
This error indicates that a required parameter was not specified.

ROOT\_NODE\_IS\_MISSING
A tree block is missing its root node.

RULE\_BLOCK\_CONTAINS\_NO\_RULES
This error indicates that the rule block contains no rules.

RULE\_NAME\_ALREADY\_IN\_USE
This error indicates that the new rule name is already in use for another
 rule in the rule block.

START\_DATE\_AFTER\_END\_DATE
This error indicates that the start date of a date range is after the end
 date.

START\_DATE\_NOT\_SET
This error indicates that the start date in an
 OperationSelectionRecord is not set.

TARGET\_BUS\_RULE\_NOT\_SET
This error indicates that the target business rule in an
 OperationSelectionRecord is not set.

TEMPLATE\_NOT\_ASSOCIATED\_WITH\_RULESET
This error indicates that the template for the new template instance rule
 being added to a ruleset is not associated with that ruleset.

TEMPLATE\_PARM\_NOT\_SPECIFIED
This error indicates that a value was not specified for a template
 parameter.

TNS\_AND\_NAME\_ALREADY\_IN\_USE
This error indicates that the target name space and name specified for a
 new ruleset or decision table is already in use for an existing ruleset
 or decision table.

TREE\_ACTION\_NULL
Tree action is null.

TREE\_ACTION\_TERM\_IS\_MISSING
A tree action term is missing in a tree block.

TREE\_CONDITION\_IS\_MISSING
A tree condition is missing in a tree block.

TYPE\_CONVERSION\_ERROR
This error indicates that the specified string value could not be
 converted to the data type of the parameter.

VALUE\_TEMPLATE\_INSTANCE\_IS\_MISSING
A tree action should have a value template instance but it is missing.

VALUE\_VIOLATES\_PARAMETER\_CONSTRAINTS
This error indicates that the specified value violates a constraint
 associated with the parameter.

WRONG\_NUMBER\_OF\_PARAMETER\_VALUES
The number of parameter values doesn't match the number of parameters.

WRONG\_OPERATION\_FOR\_OP\_SELECTION\_RECORD
This error indicates that an attempt was made to add an operation
 selection record to an operation selection record list but the operation
 associated with the selection record is not the same as the operation
 containing the operation selection record list.
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description static ValidationError valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static ValidationError [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type        | Method and Description                                                                                |
|--------------------------|-------------------------------------------------------------------------------------------------------|
| static ValidationError   | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.        |
| static ValidationError[] | values() Returns an array containing the constants of this enum type, in the order they are declared. |

    - Methods inherited from class java.lang.Enum
clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait