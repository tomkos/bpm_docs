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

## Class CaseMgmtContext

- java.lang.Object
    - com.ibm.casemgmt.api.context.CaseMgmtContext

- public final class CaseMgmtContext extends java.lang.Object Configures the Case Java API with context about the execution environment. In order to call the Case Java API, two classes must be used to configure the executing environment context: Construct an instance of this class and configure the calling thread using the static method set(CaseMgmtContext) . The set() method returns the currently configured CaseMgmtContext object if there is one. That return value can be used to restore the calling thread to the previous configured object, typically in the finally section of a try/catch/finally block. This is good practice if threads are being reused from a thread pool. ID status: ID review by David Newhall

```
public final class CaseMgmtContext
extends java.lang.Object
```

    1. The logged on user credentials and the user locale. Use the Content
         Engine Java API UserContext class to configure this information.
    2. Additional context specific to the Case Java API is configured using
         this CaseMgmtContext class.

Construct an instance of this class and configure the calling thread
 using the static method set(CaseMgmtContext).  The set()
 method returns the currently configured CaseMgmtContext object if
 there is one. That return value can be used to restore the calling thread
 to the previous configured object, typically in the finally section
 of a try/catch/finally block. This is good practice if threads are
 being reused from a thread pool.

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

CaseMgmtContext(VWSessionCache vwSessCache,
               P8ConnectionCache p8ConnectionCache)
Constructs a CaseMgmtContext object with a concrete implementation
 of VWSessionCache and P8ConnectionCache.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static CaseMgmtContext get () Returns the current CaseMgmtContext instance configured on the calling thread. java.util.Map<java.lang.String,java.lang.Object> getClientContext () Returns a map for the client context if one has been specified through the setClientContext method. DynamicClientContextProvider getDynamicClientContextProvider () Returns the current provider object specified with setDynamicClientContextProvider(), if any. P8ConnectionCache getP8ConnectionCache () Returns the P8ConnectionCache configured on this CaseMgmtContext instance. VWSessionCache getVWSessionCache () Returns the VWSessionCache configured on this CaseMgmtContext instance. static boolean isContextSpecified () Indicates if the context has been specified by calling set(CaseMgmtContext) . static CaseMgmtContext set (CaseMgmtContext ctx) Sets a particular instance of CaseMgmtContext in the calling thread. java.util.Map<java.lang.String,java.lang.Object> setClientContext (java.util.Map<java.lang.String,java.lang.Object> clientCtxMap) Allows a client context to be specified that is used when communicating with an external data service. DynamicClientContextProvider setDynamicClientContextProvider (DynamicClientContextProvider provider) Specifies an object that provides a client context dynamically when processing particular objects.

### Method Summary

| Modifier and Type                                | Method and Description                                                                                                                                                                  |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static CaseMgmtContext                           | get() Returns the current CaseMgmtContext instance configured on the  calling thread.                                                                                                   |
| java.util.Map<java.lang.String,java.lang.Object> | getClientContext() Returns a map for the client context if one has been specified  through the setClientContext method.                                                                 |
| DynamicClientContextProvider                     | getDynamicClientContextProvider() Returns the current provider object specified with setDynamicClientContextProvider(), if any.                                                         |
| P8ConnectionCache                                | getP8ConnectionCache() Returns the P8ConnectionCache configured on this CaseMgmtContext  instance.                                                                                      |
| VWSessionCache                                   | getVWSessionCache() Returns the VWSessionCache configured on this CaseMgmtContext  instance.                                                                                            |
| static boolean                                   | isContextSpecified() Indicates if the context has been specified by calling  set(CaseMgmtContext).                                                                                      |
| static CaseMgmtContext                           | set(CaseMgmtContext ctx) Sets a particular instance of CaseMgmtContext in the calling thread.                                                                                           |
| java.util.Map<java.lang.String,java.lang.Object> | setClientContext(java.util.Map<java.lang.String,java.lang.Object> clientCtxMap) Allows a client context to be specified that is used when communicating  with an external data service. |
| DynamicClientContextProvider                     | setDynamicClientContextProvider(DynamicClientContextProvider provider) Specifies an object that provides a client context dynamically when processing  particular objects.              |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait