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

## Class BinaryCustomProperty

- java.lang.Object
    - com.ibm.task.api.BinaryCustomProperty

- All Implemented Interfaces:
java.io.Serializable

public final class BinaryCustomProperty
extends java.lang.Object
implements java.io.Serializable
Describes a custom property that has a binary value.
 
 Custom properties allow a user to add additional properties to an object beyond
 those provided and managed by the Human Task Manager, for example, a JSP.
 
 The binary custom property may be searched for when an additional queryable string is provided.
 The data type should specify the type of the binary value. It is, however, not checked by the Human
 Task Manager.
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

BinaryCustomProperty()
Default constructor needed by deserialization.

BinaryCustomProperty(java.lang.String name,
                    java.lang.String dataType,
                    java.lang.String queryString,
                    byte[] buffer)
Constructor that builds a binary custom property from the passed values;
 the binary custom property value is already serialized.

BinaryCustomProperty(java.lang.String name,
                    java.lang.String dataType,
                    java.lang.String queryString,
                    java.io.Serializable value)
Constructor that builds a binary custom property from the passed values.
    - Method Summary Methods Modifier and Type Method and Description java.lang.String getDataType () Returns the data type of the binary custom property value. java.lang.String getName () Returns the name of the binary custom property. java.lang.String getQueryString () Returns the queryable string that describes the binary custom property. java.io.Serializable getValue () Returns the value of the binary custom property. byte[] getValueAsByteArray () Returns the value of the binary custom property as byte array. void setDataType (java.lang.String dataType) Sets the data type of the binary custom property value. void setName (java.lang.String name) Sets the name of the binary custom property. void setQueryString (java.lang.String queryString) Sets the queryable string that describes the binary custom property. void setValue (java.io.Serializable value) Sets the value of the binary custom property. void setValueFromByteArray (byte[] value) Sets the value of the binary custom property; the value is already serialized.

### Method Summary

| Modifier and Type    | Method and Description                                                                                             |
|----------------------|--------------------------------------------------------------------------------------------------------------------|
| java.lang.String     | getDataType() Returns the data type of the binary custom property value.                                           |
| java.lang.String     | getName() Returns the name of the binary custom property.                                                          |
| java.lang.String     | getQueryString() Returns the queryable string that describes the binary custom property.                           |
| java.io.Serializable | getValue() Returns the value of the binary custom property.                                                        |
| byte[]               | getValueAsByteArray() Returns the value of the binary custom property as byte array.                               |
| void                 | setDataType(java.lang.String dataType) Sets the data type of the binary custom property value.                     |
| void                 | setName(java.lang.String name) Sets the name of the binary custom property.                                        |
| void                 | setQueryString(java.lang.String queryString) Sets the queryable string that describes the binary custom property.  |
| void                 | setValue(java.io.Serializable value) Sets the value of the binary custom property.                                 |
| void                 | setValueFromByteArray(byte[] value) Sets the value of the binary custom property; the value is already serialized. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait