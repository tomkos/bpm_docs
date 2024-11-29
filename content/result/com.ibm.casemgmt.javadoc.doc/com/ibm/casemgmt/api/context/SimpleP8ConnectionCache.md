- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Class
- Next Class

- Frames
- No Frames

- All Classes

- Summary:
- Nested |
- Field |
- Constr |
- Method

- Detail:
- Field |
- Constr |
- Method

## Class SimpleP8ConnectionCache

- java.lang.Object
    - com.ibm.casemgmt.api.context.BaseP8ConnectionCache
        - com.ibm.casemgmt.api.context.SimpleP8ConnectionCache

- All Implemented Interfaces:
P8ConnectionCache

public final class SimpleP8ConnectionCache
extends BaseP8ConnectionCache
A basic implementation of P8ConnectionCache that is appropriate to cache the Connection
 for a single user in the context of a thread of execution. It caches
 Connection objects in a map of this instance so it is dedicated to the
 current calling thread.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

SimpleP8ConnectionCache()
Constructs a SimpleP8ConnectionCache instance.
    - Method Summary

### Method Summary

    - Methods inherited from class com.ibm.casemgmt.api.context.BaseP8ConnectionCache
getP8Connection
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait