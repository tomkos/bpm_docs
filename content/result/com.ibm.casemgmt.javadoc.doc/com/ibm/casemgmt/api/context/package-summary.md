- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes

# Package com.ibm.casemgmt.api.context

See: Description

- Interface Summary 

Interface
Description

P8ConnectionCache

Interface that supplies P8 Connection objects out of a cache.

VWSessionCache

Interface that supplies VWSession objects out of a cache.
- Class Summary 

Class
Description

BaseP8ConnectionCache

Abstract base class implementation of the P8ConnectionCache interface.

BaseVWSessionCache

Abstract base class implementation of VWSessionCache.

CaseMgmtContext

Configures the Case Java API with context about the execution
 environment.

DynamicClientContextProvider

Allows the client context to be generated based on a particular object being processed,
 currently a particular LaunchStep or WorkItem object.

SimpleP8ConnectionCache

A basic implementation of P8ConnectionCache that is appropriate to cache the Connection
 for a single user in the context of a thread of execution.

SimpleVWSessionCache

A basic implementation of VWSessionCache that is appropriate to cache the VWSession
 for a single user in the context of a thread of execution.

## Package com.ibm.casemgmt.api.context Description

The logged-on user credentials and the user locale. Use the Content
         Engine Java API UserContext class to configure this information.
Additional context specific to the Case Java API is configured
         using the CaseMgmtContext class in this package.

- Overview
- Package
- Class
- Tree
- Deprecated
- Index
- Help

- Prev Package
- Next Package

- Frames
- No Frames

- All Classes