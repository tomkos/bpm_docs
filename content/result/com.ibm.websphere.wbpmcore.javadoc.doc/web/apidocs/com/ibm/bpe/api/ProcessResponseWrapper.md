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

## Class ProcessResponseWrapper

- java.lang.Object
    - com.ibm.bpe.api.ProcessResponseWrapper

- All Implemented Interfaces: java.io.Serializable public final class ProcessResponseWrapper extends java.lang.Objectimplements java.io.Serializable Wraps the output message returned by a microflow and its associated custom client settings. The ProcessResponseWrapper class servers two major purposes: Since: 5.1 See Also: Serialized Form

```
public final class ProcessResponseWrapper
extends java.lang.Object
implements java.io.Serializable
```

The ProcessResponseWrapper class servers two major purposes:

It defers deserialization of the message passed from the process engine to a client
 until the message is accessed.
 This allows the client program to set the appropriate class loader.
It serves as a container so that the message can be returned together with its custom client settings.

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

ProcessResponseWrapper()
Default constructor needed by deserialization.

ProcessResponseWrapper(java.lang.Object message,
                      CustomClientSettings setting)
Constructor that stores the passed objects.
    - Method Summary Methods Modifier and Type Method and Description static ProcessResponseWrapper fromByteArray (byte[] buffer, CustomClientSettings setting) Factory method that creates a ProcessResponseWrapper from a byte array and custom client setting. CustomClientSettings getClientUISettings () Returns the custom client settings associated to the message. java.lang.Object getMessage () Returns the wrapped object, the message.

### Method Summary

| Modifier and Type             | Method and Description                                                                                                                                                    |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static ProcessResponseWrapper | fromByteArray(byte[] buffer,              CustomClientSettings setting) Factory method that creates a ProcessResponseWrapper from a byte array and custom client setting. |
| CustomClientSettings          | getClientUISettings() Returns the custom client settings associated to the message.                                                                                       |
| java.lang.Object              | getMessage() Returns the wrapped object, the message.                                                                                                                     |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait