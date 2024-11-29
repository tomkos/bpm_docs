- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Enum Constants |
- Field |
- Method

- Detail:
- Enum Constants |
- Field |
- Method

## Enum ErrorCategory

- java.lang.Object
    - java.lang.Enum<ErrorCategory>
        - com.ibm.casemgmt.api.constants.ErrorCategory

- All Implemented Interfaces:
java.io.Serializable, java.lang.Comparable<ErrorCategory>

public enum ErrorCategory
extends java.lang.Enum<ErrorCategory>
Represents an error category of an exception. Error categories offer a way to check
 for various types of errors programatically. An error category represents a predictable
 identification of a type of error, as opposed to a more user-oriented error message ID.
 Error message IDs may be different, depending on the scenario that generated the error,
 even though the general nature of the error, represented by an error category, is the same.
 
 Each error category can itself have other categories. A specific category will automatically
 have a more general category. In this way some error checking code can check if an exception 
 has a specific category or a general category depending on what kind of detail it is checking.
 
 All error categories have, either directly or indirectly through one or more other levels of
 categories, the category GENERAL\_ERROR.  The GENERAL\_ERROR category
 does not have any other category.
 
 Several categories such as BAD\_REQUEST or <NOT\_FOUND can correspond 
 directly to HTTP response codes such as 400 Bad Request or 404 Not Found.
 A custom web application, such as one exposing a RESTful interface to a browser-based client, 
 can choose to directly map these categories to the corresponding HTTP response code. It can 
 also check for more specific error categories and choose a response code appropriate to 
 the context in which the error occurred.

ID status:
ID review by David Newhall

- =========== ENUM CONSTANT SUMMARY =========== ========== METHOD SUMMARY ===========
    - Enum Constant Summary

Enum Constants 

Enum Constant and Description

BAD\_REQUEST
Indicates that a bad request was made.

CASE\_NOT\_FOUND
Indicates that the specified case object was not found.

CASE\_TYPE\_NOT\_FOUND
Indicates that the specified case type was not found.

DUPLICATE\_LAUNCH
Indicates that duplicate information was supplied to launch the workflow associated with
 a new task more than once.

FORBIDDEN
Indicates that some operation was forbidden, possibly due to insufficient
 access privileges.

GENERAL\_ERROR
Indicates a general error.

ILLEGAL\_ARGUMENT
Indicates that an illegal argument was supplied to a method of an object.

INCORRECT\_STATE
Indicates that an object was not in the correct state to perform the desired operation.

NOT\_FOUND
Indicates that some object was not found.

NOT\_IMPLEMENTED
Indicates that some operation is not implemented.

OBJECT\_STORE\_NOT\_FOUND
Indicates that the specified object store was not found.

PAGE\_PHYSICAL\_ID\_NOT\_FOUND
Indicates that a physical page ID was not found.

PRECONDITION\_FAILED
Indicates that the appropriate precondition was not met to perform some operation.

REINIT\_STATUS\_NOT\_FOUND
Indicates that the status object used to track a reinitialization operation 
 of a development environment was not found.

SOLUTION\_FOLDER\_NOT\_FOUND
Indicates that the specified solution folder was not found.

TASK\_NOT\_FOUND
Indicates that the specified task object was not found.

TASK\_TYPE\_NOT\_FOUND
Indicates that the specified task type was not found.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description ErrorCategory findFirstCategory (ErrorCategory ... potentialCats) Finds the first category in a list of other categories that this category is associated with. java.util.List<ErrorCategory > getIncludedCategories () Returns the first-level list of other categories that this category has. boolean hasCategory (ErrorCategory otherCat) Indicates if this category is associated with another category. static ErrorCategory valueOf (java.lang.String name) Returns the enum constant of this type with the specified name. static ErrorCategory [] values () Returns an array containing the constants of this enum type, inthe order they are declared.

### Method Summary

| Modifier and Type             | Method and Description                                                                                                                           |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ErrorCategory                 | findFirstCategory(ErrorCategory... potentialCats) Finds the first category in a list of other categories that this category  is associated with. |
| java.util.List<ErrorCategory> | getIncludedCategories() Returns the first-level list of other categories that this category has.                                                 |
| boolean                       | hasCategory(ErrorCategory otherCat) Indicates if this category is associated with another category.                                              |
| static ErrorCategory          | valueOf(java.lang.String name) Returns the enum constant of this type with the specified name.                                                   |
| static ErrorCategory[]        | values() Returns an array containing the constants of this enum type, in the order they are declared.                                            |

    - Methods inherited from class java.lang.Enum
compareTo, equals, getDeclaringClass, hashCode, name, ordinal, toString, valueOf
    - Methods inherited from class java.lang.Object
getClass, notify, notifyAll, wait, wait, wait