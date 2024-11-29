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

## Class SimpleVWSessionCache

- java.lang.Object
    - com.ibm.casemgmt.api.context.BaseVWSessionCache
        - com.ibm.casemgmt.api.context.SimpleVWSessionCache

- All Implemented Interfaces:
VWSessionCache

public final class SimpleVWSessionCache
extends BaseVWSessionCache
A basic implementation of VWSessionCache that is appropriate to cache the VWSession
 for a single user in the context of a thread of execution. It caches
 VWSession objects in a map of this instance so it dedicated to the
 current calling thread.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

SimpleVWSessionCache()
Constructs a SimpleVWSessionCache instance.
    - Method Summary

### Method Summary

    - Methods inherited from class com.ibm.casemgmt.api.context.BaseVWSessionCache
getVWSession
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait