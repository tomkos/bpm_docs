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

## Class BaseVWSessionCache

- java.lang.Object
    - com.ibm.casemgmt.api.context.BaseVWSessionCache

- All Implemented Interfaces:
VWSessionCache

Direct Known Subclasses:
SimpleVWSessionCache

public abstract class BaseVWSessionCache
extends java.lang.Object
implements VWSessionCache
Abstract base class implementation of VWSessionCache. This base implementation
 handles creating new VWSession objects when needed and calls 
 methods implemented by a subclass to actually retrieve and put the objects in 
 a cache as appropriate. For example, a particular subclass may use an HTTP Session object to
 cache the VWSession objects.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

BaseVWSessionCache()
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description filenet.vw.api.VWSession getVWSession (java.lang.String ceURI, java.lang.String connPt) Returns a cached VWSession object for the given CE domain URI and connection point name.

### Method Summary

| Modifier and Type        | Method and Description                                                                                                                                              |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| filenet.vw.api.VWSession | getVWSession(java.lang.String ceURI,             java.lang.String connPt) Returns a cached VWSession object for the given CE domain URI  and connection point name. |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait