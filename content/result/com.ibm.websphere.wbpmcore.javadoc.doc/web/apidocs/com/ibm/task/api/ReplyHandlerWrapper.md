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

## Class ReplyHandlerWrapper

- java.lang.Object
    - com.ibm.task.api.ReplyHandlerWrapper

- All Implemented Interfaces: java.io.Serializable, java.lang.Cloneable public final class ReplyHandlerWrapper extends java.lang.Objectimplements java.io.Serializable, java.lang.Cloneable Wraps the reply handler passed to the Human Task Manager. When the Human Task Manager is accessed through its EJB interface, then: The ReplyHandlerWrapper defers deserialization of the reply handler implementation until the wrapped ReplyHandler object is accessed. This allows the Human Task Manager to set the appropriate class loader. Since: 6.0 See Also: Serialized Form

```
public final class ReplyHandlerWrapper
extends java.lang.Object
implements java.io.Serializable, java.lang.Cloneable
```

When the Human Task Manager is accessed through its EJB interface, then:

Invocation parameters are automatically deserialized by the application server.
Invocation parameters are deserialized before the Human Task Manager sets the appropriate class loader.

 The ReplyHandlerWrapper
 defers deserialization of the reply handler implementation until the wrapped ReplyHandler object is accessed.
 This allows the Human Task Manager to set the appropriate class loader.

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

ReplyHandlerWrapper()
Default constructor needed by deserialization.

ReplyHandlerWrapper(ReplyHandler object)
Constructor that stores the passed object.
    - Method Summary Methods Modifier and Type Method and Description java.lang.Object clone () Creates and returns a copy of this object. static ReplyHandlerWrapper fromByteArray (byte[] buffer) Factory method that creates a ReplyHandlerWrapper from a byte array. ReplyHandler getObject () Returns the wrapped object.

### Method Summary

| Modifier and Type          | Method and Description                                                                            |
|----------------------------|---------------------------------------------------------------------------------------------------|
| java.lang.Object           | clone() Creates and returns a copy of this object.                                                |
| static ReplyHandlerWrapper | fromByteArray(byte[] buffer) Factory method that creates a ReplyHandlerWrapper from a byte array. |
| ReplyHandler               | getObject() Returns the wrapped object.                                                           |

- Methods inherited from class java.lang.Object
equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait