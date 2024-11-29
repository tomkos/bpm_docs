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

## Class FloatEncoding

- java.lang.Object
    - com.ibm.mq.data.FloatEncoding

- public final class FloatEncoding
extends java.lang.Object
Enumeration-style class giving values for each of the four floating-point
 encodings recognised by WebSphere MQ: undefined, s390, ieee normal and reversed.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static FloatEncoding
IEEE\_NORMAL
Signals that floating-point values use the IEEE format.

static FloatEncoding
IEEE\_REVERSED
Signals that floating-point values use the IEEE format with bytes swapped,
 so that the least significant byte of the mantissa appears first.

static int
MASK
Binary mask yielding the bits which represent the floating-point encoding
 value in a WMQ encoding identifier

static FloatEncoding
S390
Signals that floating-point values use the S390 floating point format

static FloatEncoding
TNS
Signals that floating-point values use the TNS floating point format

static FloatEncoding
UNDEFINED
Signals that floating-point values are of an undefined format
    - Method Summary Methods Modifier and Type Method and Description static FloatEncoding forValue (int encoding) Given a WMQ encoding, returns the relevent FloatEncoding object. int getValue () Returns the value, in a WMQ encoding, of this floating-point encoding java.lang.String toString ()

### Method Summary

| Modifier and Type    | Method and Description                                                                   |
|----------------------|------------------------------------------------------------------------------------------|
| static FloatEncoding | forValue(int encoding) Given a WMQ encoding, returns the relevent FloatEncoding  object. |
| int                  | getValue() Returns the value, in a WMQ encoding, of this floating-point encoding         |
| java.lang.String     | toString()                                                                               |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait