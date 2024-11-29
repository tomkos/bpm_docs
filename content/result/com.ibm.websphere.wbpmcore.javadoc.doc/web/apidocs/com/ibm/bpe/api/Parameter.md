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

## Class Parameter

- java.lang.Object
    - com.ibm.bpe.api.Parameter

- All Implemented Interfaces:
java.io.Serializable

public final class Parameter
extends java.lang.Object
implements java.io.Serializable
Describes a parameter and its value to set the value of a parameter that is used in
 query table filters and selection criteria.
 Note that system parameters $USER and $LOCALE are resolved when the query is run.
 $LOCALE may be set in the filter options and is modified by the query table runtime
 before the query is executed.
Since:
6.2
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

Parameter()
Default constructor to initialize the parameter options.

Parameter(java.lang.String name,
         java.io.Serializable value)
Constructor that builds a parameter option from the passed values.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getName () Returns the name of the parameter. java.io.Serializable getValue () Returns the value of the parameter. void setParameter (java.lang.String name, java.io.Serializable value) Sets the parameter. java.lang.String toString () Returns a string representation of the Parameter object.

### Method Summary

| Modifier and Type    | Method and Description                                                                          |
|----------------------|-------------------------------------------------------------------------------------------------|
| java.lang.String     | getName() Returns the name of the parameter.                                                    |
| java.io.Serializable | getValue() Returns the value of the parameter.                                                  |
| void                 | setParameter(java.lang.String name,             java.io.Serializable value) Sets the parameter. |
| java.lang.String     | toString() Returns a string representation of the Parameter object.                             |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait