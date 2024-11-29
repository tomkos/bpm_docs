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
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Interface TreeActionTermDefinition

- All Superinterfaces:
java.io.Serializable

public interface TreeActionTermDefinition
extends java.io.Serializable
This interface is the definition for a tree action term in a decision tree.  These definitions are
 referred to by TreeAction objects within the actual decision tree.  Separating the
 definition from the actual usage allows the definitions to be reused by different nodes in the
 decision tree.  Each TreeActionTermDefinition contains a user presentation string,
 which defines how the term should be presented to the user, and a list of value templates that
 are available to specify templatized action values for this action term.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getUserPresentation()
Get the user presentation for this action term definition.

java.util.List<TreeActionValueTemplate>
getValueTemplates()
Get the list of value templates available for this tree action term.

boolean
isTermNotApplicable()
Determine whether or not the term is "not applicable".

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getUserPresentation
java.lang.String getUserPresentation()
Get the user presentation for this action term definition.
Returns:The user presentation for this action term definition.
    - getValueTemplates
java.util.List<TreeActionValueTemplate> getValueTemplates()
Get the list of value templates available for this tree action term.  The List
 returned is unmodifiable.
Returns:The list of value templates available for this tree action term.  The returned list
 is unmodifiable.
    - isTermNotApplicable
boolean isTermNotApplicable()
Determine whether or not the term is "not applicable".  A "not applicable" term
 means that the action is an invocation of another SCA component.
Returns:true if the term is "not applicable; otherwise false.