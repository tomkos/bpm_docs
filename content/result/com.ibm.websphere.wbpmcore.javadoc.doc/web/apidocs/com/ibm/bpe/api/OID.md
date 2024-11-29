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

## Interface OID

- All Superinterfaces:
java.lang.Comparable, java.io.Serializable

All Known Subinterfaces:
ACOID, AIID, ATID, BCID, EHTID, ESIID, ESTID, ICIID, PIID, PTID, TKIID, TKTID, VTID, WBID

public interface OID
extends java.io.Serializable, java.lang.Comparable
Interface for an object identifier.
 
 An object identifier uniquely identifies an object. It is created when the
 associated object is created and stays with the object during its lifetime.
 It is never reused.
 
 The object identifier can be retrieved using the getID() method of the
 associated object.
Since:
5.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static byte
OBJECT\_META\_TYPE\_A 

static byte
OBJECT\_META\_TYPE\_B 

static byte
OBJECT\_META\_TYPE\_C 

static byte
OBJECT\_META\_TYPE\_D
    - Method Summary

Methods 

Modifier and Type
Method and Description

int
compareTo(java.lang.Object o)
Compares the object identifer with the object identifier of the specified object.

byte
getObjectMetaType()
Returns information about the object meta type of the associated object.

boolean
isPersistent()
Returns information about the persistence of the associated object.

byte[]
toByteArray()
Returns a byte array representation of the object identifier.

java.lang.String
toString()
Returns a String representation of the object identifier.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- OBJECT\_META\_TYPE\_A
static final byte OBJECT\_META\_TYPE\_A
See Also:Constant Field Values

- OBJECT\_META\_TYPE\_B
static final byte OBJECT\_META\_TYPE\_B
See Also:Constant Field Values

- OBJECT\_META\_TYPE\_C
static final byte OBJECT\_META\_TYPE\_C
See Also:Constant Field Values

- OBJECT\_META\_TYPE\_D
static final byte OBJECT\_META\_TYPE\_D
See Also:Constant Field Values

- Method Detail

### Method Detail

    - toString
java.lang.String toString()
Returns a String representation of the object identifier.
 
 There is no maximum length of a String representation.
 The length can vary from object type to object type and
 even for objects of the same object type.

Overrides:
toString in class java.lang.Object
    - toByteArray
byte[] toByteArray()
Returns a byte array representation of the object identifier.
 
 There is no maximum length of a byte array representation.
 The length can vary from object type to object type but
 is constant for objects of the same object type.
    - isPersistent
boolean isPersistent()
Returns information about the persistence of the associated object.
 
 Returns true when the associated object is persistent.
 Returns false when the associated object is transient.
    - getObjectMetaType
byte getObjectMetaType()
Returns information about the object meta type of the associated object.
Returns:a constant value out of OBJECT\_META\_TYPE\_A ... OBJECT\_META\_TYPED
    - compareTo
int compareTo(java.lang.Object o)
Compares the object identifer with the object identifier of the specified object.
 
 Returns zero when the object identifiers are equal.
 Returns a negative integer when this object identifier is less than the specified one.
 Returns a positive integer when this object identifier is greater than the specified one.
 
 Although object identifiers can be compared, no ordering semantics can be deduced.

Specified by:
compareTo in interface java.lang.Comparable