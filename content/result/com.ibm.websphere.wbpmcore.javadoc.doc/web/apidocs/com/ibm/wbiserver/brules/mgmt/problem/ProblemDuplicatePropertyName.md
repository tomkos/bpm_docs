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

## Class ProblemDuplicatePropertyName

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemDuplicatePropertyName

- All Implemented Interfaces:
java.io.Serializable

public class ProblemDuplicatePropertyName
extends Problem
implements java.io.Serializable
Problem class representing the error that a new property is being defined with the same
 name as an existing property on the specified entity.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

ProblemDuplicatePropertyName(Property newProperty,
                            java.lang.Object entityContainingDuplicateProperty)
Constructor for the ProblemDuplicatePropertyName class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.Object getEntityContainingDuplicateProperty () Get the entity that contains the duplicate property. java.lang.String getErrorMessage () Property getNewProperty () Get the new property containing the duplicate name.

### Method Summary

| Modifier and Type   | Method and Description                                                                      |
|---------------------|---------------------------------------------------------------------------------------------|
| java.lang.Object    | getEntityContainingDuplicateProperty() Get the entity that contains the duplicate property. |
| java.lang.String    | getErrorMessage()                                                                           |
| Property            | getNewProperty() Get the new property containing the duplicate name.                        |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait