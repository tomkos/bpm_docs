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

## Class BaseP8ConnectionCache

- java.lang.Object
    - com.ibm.casemgmt.api.context.BaseP8ConnectionCache

- All Implemented Interfaces:
P8ConnectionCache

Direct Known Subclasses:
SimpleP8ConnectionCache

public abstract class BaseP8ConnectionCache
extends java.lang.Object
implements P8ConnectionCache
Abstract base class implementation of the P8ConnectionCache interface.
 This base class creates P8 Connection objects in a default way but calls
 methods implemented by a subclass to cache the Connection objects or
 retrieve the Connection objects out of cache in whatever way is appropriate
 for that subclass. For example, a particular subclass may use 
 an HTTP Session object to cache the Connection objects.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

BaseP8ConnectionCache()
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.Connection getP8Connection (java.lang.String ceURI) Obtains a P8 Connection object for a given Content Engine domain URI.

### Method Summary

| Modifier and Type               | Method and Description                                                                                         |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.Connection | getP8Connection(java.lang.String ceURI) Obtains a P8 Connection object for a given Content  Engine domain URI. |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait