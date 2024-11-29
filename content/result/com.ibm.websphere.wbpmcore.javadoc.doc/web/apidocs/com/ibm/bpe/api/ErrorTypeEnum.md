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

## Class ErrorTypeEnum

- java.lang.Object
    - com.ibm.bpe.api.ErrorTypeEnum

- All Implemented Interfaces: java.io.Serializable public final class ErrorTypeEnum extends java.lang.Objectimplements java.io.Serializable This enumeration class defines symbolic constants for error types that are found during validation of objects created spontaneously (ad-hoc). Possible values are: Since: 6.0.2 See Also: Serialized Form

```
public final class ErrorTypeEnum
extends java.lang.Object
implements java.io.Serializable
```

    - INFO
    - WARNING
    - ERROR

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static ErrorTypeEnum
ERROR 

static ErrorTypeEnum
INFO 

static ErrorTypeEnum
WARNING
    - Method Summary Methods Modifier and Type Method and Description static ErrorTypeEnum newErrorTypeEnum (int errorType) Factory method to create an ErrorTypeEnum object. java.lang.String toString () Returns a string representation of the ErrorTypeEnum object.

### Method Summary

| Modifier and Type    | Method and Description                                                            |
|----------------------|-----------------------------------------------------------------------------------|
| static ErrorTypeEnum | newErrorTypeEnum(int errorType) Factory method to create an ErrorTypeEnum object. |
| java.lang.String     | toString() Returns a string representation of the ErrorTypeEnum object.           |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait