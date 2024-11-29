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

## Class StoredQueryProperty

- java.lang.Object
    - com.ibm.bpe.api.StoredQueryProperty

- All Implemented Interfaces:
java.io.Serializable

public final class StoredQueryProperty
extends java.lang.Object
implements java.io.Serializable
Describes a property of a stored query.
 
 Stored query properties allow a user to add user-defined properties to a stored query.
Since:
6.0.2
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

StoredQueryProperty(java.lang.String name,
                   java.lang.String value)
Constructor.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getName () Returns the name of the stored query property. java.lang.String getValue () Returns the value of the stored query property. void setValue (java.lang.String value) Sets the value of the stored query property.

### Method Summary

| Modifier and Type   | Method and Description                                                        |
|---------------------|-------------------------------------------------------------------------------|
| java.lang.String    | getName() Returns the name of the stored query property.                      |
| java.lang.String    | getValue() Returns the value of the stored query property.                    |
| void                | setValue(java.lang.String value) Sets the value of the stored query property. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait