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

## Class IntegerEncoding

- java.lang.Object
    - com.ibm.mq.data.IntegerEncoding

- public final class IntegerEncoding
extends java.lang.Object
Enumeration-style class giving values for each of the three integer encodings
 recognised by WebSphere MQ: undefined, normal and reversed.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static int
MASK
Binary mask yielding the bits which represent the integer encoding
 value in a WMQ encoding identifier

static IntegerEncoding
NORMAL
Signals that integer values are encoded with the most significant byte
 first.

static IntegerEncoding
REVERSED
Signals that integer values are encoded with the least significant byte
 first.

static IntegerEncoding
UNDEFINED
Signals that integer values are of an undefined format
    - Method Summary Methods Modifier and Type Method and Description static IntegerEncoding forValue (int encoding) Given a WMQ encoding, returns the relevent IntegerEncoding object. int getValue () Returns the value, in a WMQ encoding, of this integer encoding java.lang.String toString ()

### Method Summary

| Modifier and Type      | Method and Description                                                                     |
|------------------------|--------------------------------------------------------------------------------------------|
| static IntegerEncoding | forValue(int encoding) Given a WMQ encoding, returns the relevent IntegerEncoding  object. |
| int                    | getValue() Returns the value, in a WMQ encoding, of this integer encoding                  |
| java.lang.String       | toString()                                                                                 |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait