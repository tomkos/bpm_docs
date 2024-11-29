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

## Class ProblemStartDateAfterEndDate

- java.lang.Object
    - com.ibm.wbiserver.brules.mgmt.problem.Problem
        - com.ibm.wbiserver.brules.mgmt.problem.ProblemStartDateAfterEndDate

- All Implemented Interfaces:
java.io.Serializable

public class ProblemStartDateAfterEndDate
extends Problem
implements java.io.Serializable
Problem class representing the error that the start date is after the end date.
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

ProblemStartDateAfterEndDate(java.util.Date startDate,
                            java.util.Date endDate)
Constructor for the ProblemStartDateAfterEndDate class.
    - Method Summary Methods Modifier and Type Method and Description java.util.Date getEndDate () Get the end date involved in the error. java.lang.String getErrorMessage () java.util.Date getStartDate () Get the start date involved in the error.

### Method Summary

| Modifier and Type   | Method and Description                                   |
|---------------------|----------------------------------------------------------|
| java.util.Date      | getEndDate() Get the end date involved in the error.     |
| java.lang.String    | getErrorMessage()                                        |
| java.util.Date      | getStartDate() Get the start date involved in the error. |

    - Methods inherited from class com.ibm.wbiserver.brules.mgmt.problem.Problem
getErrorType
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait