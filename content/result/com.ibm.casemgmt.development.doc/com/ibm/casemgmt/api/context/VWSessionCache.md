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

## Interface VWSessionCache

- All Known Implementing Classes:
BaseVWSessionCache, SimpleVWSessionCache

public interface VWSessionCache
Interface that supplies VWSession objects out of a cache.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

filenet.vw.api.VWSession
getVWSession(java.lang.String ceURI,
            java.lang.String connPt)
Retrieves a cached VWSession object for the given CE domain URI
 and connection point name.

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getVWSession
filenet.vw.api.VWSession getVWSession(java.lang.String ceURI,
                                      java.lang.String connPt)
Retrieves a cached VWSession object for the given CE domain URI
 and connection point name. If no VWSession was cached previously,
 a new VWSession object is created and cached as appropriate
 for the concrete implementation of VWSessionCache.

Parameters:
ceURI - a CE domain URI
connPt - a PE connection point name
ID status:
ID review by David Newhall