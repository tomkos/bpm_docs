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

## Interface LinkTemplateData

- All Superinterfaces:
java.io.Serializable

public interface LinkTemplateData
extends java.io.Serializable
Accesses the properties of a link template.
 
 Links are used for synchronization across concurrent activities. They define the
 potential flow of control between two activities in the process. The actual flow
 of control is determined at run time based on the truth value of the transition
 conditions associated with the links.
 
Since:
6.2

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
getDescription()
Returns the description of the link template.

java.lang.String
getName()
Returns the name of the link template.

java.lang.String
getSourceActivityName()
Returns the name of the source activity.

java.lang.String
getTargetActivityName()
Returns the name of the target activity.

boolean
isBusinessRelevant()
States whether the link is business relevant or not.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Returns the name of the link template.
    - isBusinessRelevant
boolean isBusinessRelevant()
States whether the link is business relevant or not. A
 business relevant link can, for example, be logged into the audit trail.
    - getDescription
java.lang.String getDescription()
Returns the description of the link template. If there is no description, null is returned.
    - getSourceActivityName
java.lang.String getSourceActivityName()
Returns the name of the source activity.
    - getTargetActivityName
java.lang.String getTargetActivityName()
Returns the name of the target activity.