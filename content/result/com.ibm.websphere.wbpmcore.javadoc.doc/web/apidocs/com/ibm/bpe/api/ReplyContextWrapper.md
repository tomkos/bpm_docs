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

## Class ReplyContextWrapper

- java.lang.Object
    - com.ibm.bpe.api.ReplyContextWrapper

- All Implemented Interfaces: java.io.Serializable, java.lang.Cloneable public final class ReplyContextWrapper extends java.lang.Objectimplements java.io.Serializable, java.lang.Cloneable Wraps the reply context passed to the process engine. When the process engine is accessed through its EJB interface: The ReplyContextWrapper class defers deserialization until the wrapped ReplyContext is accessed. This allows the process engine to set the appropriate class loader. Since: 5.0 See Also: Serialized Form

```
public final class ReplyContextWrapper
extends java.lang.Object
implements java.io.Serializable, java.lang.Cloneable
```

When the process engine is accessed through its EJB interface:

Invocation parameters are automatically deserialized by the application server.
Invocation parameters are deserialized before the process engine sets the appropriate class loader.

 The ReplyContextWrapper class
 defers deserialization until the wrapped ReplyContext is accessed.
 This allows the process engine to set the appropriate class loader.

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

ReplyContextWrapper()
Default constructor needed by deserialization.

ReplyContextWrapper(byte[] buffer)
Constructor that stores the passed serialized object.

ReplyContextWrapper(ReplyContext object)
Constructor that stores the passed object.
    - Method Summary Methods Modifier and Type Method and Description java.lang.Object clone () Creates and returns a copy of this object. static ReplyContextWrapper fromByteArray (byte[] buffer) Factory method that creates a ReplyContextWrapper from a byte array. ReplyContext getObject () Returns the wrapped object.

### Method Summary

| Modifier and Type          | Method and Description                                                                            |
|----------------------------|---------------------------------------------------------------------------------------------------|
| java.lang.Object           | clone() Creates and returns a copy of this object.                                                |
| static ReplyContextWrapper | fromByteArray(byte[] buffer) Factory method that creates a ReplyContextWrapper from a byte array. |
| ReplyContext               | getObject() Returns the wrapped object.                                                           |

- Methods inherited from class java.lang.Object
equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait