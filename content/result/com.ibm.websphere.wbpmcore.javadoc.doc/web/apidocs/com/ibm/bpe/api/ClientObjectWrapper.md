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

## Class ClientObjectWrapper

- java.lang.Object
    - com.ibm.bpe.api.ClientObjectWrapper

- All Implemented Interfaces: java.io.Serializable, java.lang.Cloneable public final class ClientObjectWrapper extends java.lang.Objectimplements java.io.Serializable, java.lang.Cloneable Wraps messages and variables passed between the caller and the process engine. When the process engine is accessed through its EJB interface: The ClientObjectWrapper class defers deserialization until the wrapped message or variable is accessed. This allows the process engine to set the appropriate class loader. Since: 5.0 See Also: Serialized Form

```
public final class ClientObjectWrapper
extends java.lang.Object
implements java.io.Serializable, java.lang.Cloneable
```

When the process engine is accessed through its EJB interface:

Invocation parameters are automatically deserialized by the application server.
Messages and variables are deserialized before the process engine sets the appropriate class loader.

 The ClientObjectWrapper class
 defers deserialization until the wrapped message or variable is accessed.
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

ClientObjectWrapper()
Default constructor needed by deserialization.

ClientObjectWrapper(java.lang.Object object)
Constructor that stores the passed object, the message.
    - Method Summary Methods Modifier and Type Method and Description java.lang.Object clone () Creates and returns a copy of this object. static ClientObjectWrapper fromByteArray (byte[] buffer, boolean unwrapSimpleTypes) Factory method that creates a ClientObjectWrapper from a byte array. java.lang.Object getObject () Returns the wrapped object, the message. java.lang.Object getObject (boolean unwrapSimpleTypes) Returns the wrapped object, the message.

### Method Summary

| Modifier and Type          | Method and Description                                                                                                                    |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.Object           | clone() Creates and returns a copy of this object.                                                                                        |
| static ClientObjectWrapper | fromByteArray(byte[] buffer,              boolean unwrapSimpleTypes) Factory method that creates a ClientObjectWrapper from a byte array. |
| java.lang.Object           | getObject() Returns the wrapped object, the message.                                                                                      |
| java.lang.Object           | getObject(boolean unwrapSimpleTypes) Returns the wrapped object, the message.                                                             |

- Methods inherited from class java.lang.Object
equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait