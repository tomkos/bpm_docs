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

## Interface P8ConnectionCache

- All Known Implementing Classes:
BaseP8ConnectionCache, SimpleP8ConnectionCache

public interface P8ConnectionCache
Interface that supplies P8 Connection objects out of a cache.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

com.filenet.api.core.Connection
getP8Connection(java.lang.String ceURI)
Retrieves a Connection object for a particular CE domain
 URI out of the cache.

- ============ METHOD DETAIL ==========
    - Method Detail

### Method Detail

- getP8Connection
com.filenet.api.core.Connection getP8Connection(java.lang.String ceURI)
Retrieves a Connection object for a particular CE domain
 URI out of the cache. If the object is not yet cached, a new
 Connection object will be created and cached as appropriate
 for the concrete implementation of P8ConnectionCache.

Parameters:
ceURI - a CE domain URI
ID status:
ID review by David Newhall