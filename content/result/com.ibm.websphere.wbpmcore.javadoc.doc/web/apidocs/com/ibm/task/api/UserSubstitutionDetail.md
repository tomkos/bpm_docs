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

## Class UserSubstitutionDetail

- java.lang.Object
    - com.ibm.task.api.UserSubstitutionDetail

- All Implemented Interfaces:
java.io.Serializable

public class UserSubstitutionDetail
extends java.lang.Object
implements java.io.Serializable
Handles the absence and substitution details of a user.
Since:
7.0
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT\_ 

static java.lang.String
NL
    - Constructor Summary

Constructors 

Constructor and Description

UserSubstitutionDetail()
Default constructor to initialize the user absence and substitution details.

UserSubstitutionDetail(java.util.List substitutes,
                      java.util.Calendar startDate,
                      java.util.Calendar endDate)
Constructor that creates a user substitution details object from the passed values.
    - Method Summary Methods Modifier and Type Method and Description java.util.Calendar getEndDate () Returns the end date of the user's absence period. java.util.Calendar getStartDate () Returns the start date of the user's absence period. java.util.List getSubstitutes () Returns the user IDs of the substitutes. void setEndDate (java.util.Calendar endDate) Sets the end date for the user's absence period. void setStartDate (java.util.Calendar startDate) Sets the start date for the user's absence period. void setSubstitutes (java.util.List substitutes) Sets the substitutes of the user. java.lang.String toString () Returns a string representation of the UserSubstitutionDetail object.

### Method Summary

| Modifier and Type   | Method and Description                                                                        |
|---------------------|-----------------------------------------------------------------------------------------------|
| java.util.Calendar  | getEndDate() Returns the end date of the user's absence period.                               |
| java.util.Calendar  | getStartDate() Returns the start date of the user's absence period.                           |
| java.util.List      | getSubstitutes() Returns the user IDs of the substitutes.                                     |
| void                | setEndDate(java.util.Calendar endDate) Sets the end date for the user's absence period.       |
| void                | setStartDate(java.util.Calendar startDate) Sets the start date for the user's absence period. |
| void                | setSubstitutes(java.util.List substitutes) Sets the substitutes of the user.                  |
| java.lang.String    | toString() Returns a string representation of the UserSubstitutionDetail object.              |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait