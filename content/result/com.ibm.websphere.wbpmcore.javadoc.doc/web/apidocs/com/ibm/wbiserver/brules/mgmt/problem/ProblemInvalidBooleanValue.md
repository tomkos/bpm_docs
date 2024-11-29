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

## Class ProblemInvalidBooleanValue

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemInvalidBooleanValue

- All Implemented Interfaces:
java.io.Serializable

public class ProblemInvalidBooleanValue
extends Problem
implements java.io.Serializable
Problem class representing the error that the specified string value is not a valid value
 for a boolean parameter.  Only the strings "true" and "false" (all lower case) are allowed
 as boolean values.
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

ProblemInvalidBooleanValue(java.lang.String value,
                          Parameter parameter)
Constructor for the ProblemInvalidBooleanValue class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () Parameter getParameter () Get the parameter to which the value was being associated. java.lang.String getValue () Get the value that caused the error.

### Method Summary

| Modifier and Type   | Method and Description                                                    |
|---------------------|---------------------------------------------------------------------------|
| java.lang.String    | getErrorMessage()                                                         |
| Parameter           | getParameter() Get the parameter to which the value was being associated. |
| java.lang.String    | getValue() Get the value that caused the error.                           |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait