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

## Class ProblemTNSAndNameAlreadyInUse

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemTNSAndNameAlreadyInUse

- All Implemented Interfaces:
java.io.Serializable

public class ProblemTNSAndNameAlreadyInUse
extends Problem
implements java.io.Serializable
Problem class representing the error that the target name space and name specified for the
 new ruleset or decision table is already in use.
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

ProblemTNSAndNameAlreadyInUse(java.lang.String targetNameSpace,
                             java.lang.String name)
Constructor for the ProblemTNSAndNameAlreadyInUse class.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getErrorMessage () java.lang.String getName () Get the name that is already in use. java.lang.String getTargetNameSpace () Get the target name space that is already in use.

### Method Summary

| Modifier and Type   | Method and Description                                                 |
|---------------------|------------------------------------------------------------------------|
| java.lang.String    | getErrorMessage()                                                      |
| java.lang.String    | getName() Get the name that is already in use.                         |
| java.lang.String    | getTargetNameSpace() Get the target name space that is already in use. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait