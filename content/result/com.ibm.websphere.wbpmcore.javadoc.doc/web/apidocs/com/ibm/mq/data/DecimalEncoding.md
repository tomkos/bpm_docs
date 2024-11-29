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

## Class DecimalEncoding

- java.lang.Object
    - com.ibm.mq.data.DecimalEncoding

- public final class DecimalEncoding
extends java.lang.Object
Enumeration-style class giving values for each of the three decimal encodings
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
Binary mask yielding the bits which represent the decimal encoding
 value in a WMQ encoding identifier

static DecimalEncoding
NORMAL
Signals that decimal values are encoded as packed decimal, with the most
 significant byte first.

static DecimalEncoding
REVERSED
Signals that decimal values are encoded as packed decimal, with the most
 significant byte last.

static DecimalEncoding
UNDEFINED
Signals that decimal values are of an undefined format
    - Method Summary Methods Modifier and Type Method and Description static DecimalEncoding forValue (int encoding) Given a WMQ encoding, returns the relevent DecimalEncoding object. int getValue () Returns the value, in a WMQ encoding, of this decimal encoding java.lang.String toString ()

### Method Summary

| Modifier and Type      | Method and Description                                                                     |
|------------------------|--------------------------------------------------------------------------------------------|
| static DecimalEncoding | forValue(int encoding) Given a WMQ encoding, returns the relevent DecimalEncoding  object. |
| int                    | getValue() Returns the value, in a WMQ encoding, of this decimal encoding                  |
| java.lang.String       | toString()                                                                                 |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait