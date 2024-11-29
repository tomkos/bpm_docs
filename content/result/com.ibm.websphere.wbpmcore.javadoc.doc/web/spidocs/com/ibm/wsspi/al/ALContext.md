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

## Class ALContext

- java.lang.Object
    - com.ibm.wsspi.al.ALContext

- All Implemented Interfaces:
com.ibm.ws.al.ralclient.RALClientConstants

public class ALContext
extends java.lang.Object
implements com.ibm.ws.al.ralclient.RALClientConstants
The AL Context
 provides the dynamic api of setting/adding/removing remote AL configuarations

- ======== NESTED CLASS SUMMARY ======== =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

static class 
ALContext.ContainerReferenceClassLoader
The classloader for AL repository support
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.ws.al.ralclient.RALClientConstants
EXTADMINNAME, EXTAPPNAME, EXTDEPLOYMENTMANAGER, EXTSECURITY, EXTSERVER, RALSVRMBEANNAME, WCCM\_ALCONFIGURATIONS\_NAME, WCCM\_ALCONFIGURATIONS\_TYPE, WCCM\_PROP\_NAMEATTRIBUTE\_NAME, WCCM\_PROP\_VALUEATTRIBUTE\_NAME, WCCM\_RALCONFIG\_PROP\_NAME, WCCM\_RALCONFIG\_PROP\_TYPE, WCCM\_RALSECURITY\_NAME, WCCM\_RALSECURITY\_TYPE, WCCM\_RALSERVER\_ATTR\_PASSWORD, WCCM\_RALSERVER\_ATTR\_SECURITYENABLE, WCCM\_RALSERVER\_ATTR\_USER, WCCM\_ROOT\_CONFIGOBJ\_NAME

- Constructor Summary

Constructors 

Constructor and Description

ALContext()

- Method Summary Methods Modifier and Type Method and Description static void add (ALConfiguration config) add an instance of ALConfig to the current thread's ALContext. static void addClForBOCacheClean (java.util.List<java.lang.ClassLoader> clList) Add the ClassLoader list for BO Cache cleanup for this thread static void cleanRALCache (ALConfiguration config) clean the corresponding ALConfiguration from the cache. static void cleanRALCache (java.util.Collection<ALConfiguration > configs) clean the corresponding collections of ALConfiguration from the cache.The operation need to happen after setContext/ unset() pair static void cleanupClForBOCacheClean () Clean up the the ClassLoader list for BO Cache cleanup for this thread static void clearBOCache () Clear BO cache static java.util.List<java.lang.ClassLoader> getClForBOCacheClean () Get the ClassLoader list for BO Cache cleanup for this thread static java.lang.String getContainerReference () Returns the ContainerReference id in external form from the current context on this thread. static void remove (ALConfiguration config) remove an instance of ALConfig from the current thread's ALContext. static void setClForBOCacheClean (java.util.List<java.lang.ClassLoader> clList) Set the ClassLoader list for BO Cache cleanup for this thread static void setContainerReference (java.lang.String externalForm) Sets ContainerReference as current context for this thread. static void setContext (ALConfiguration config) set AL context to an instance of ALConfig. static void setContext (java.util.Collection<ALConfiguration > configs) set AL context to a list of ALConfig. static void setContext (java.lang.String tempName, java.lang.String appName) This is a easy of use wrapper method. static void unset () unset the current thread's AL context

### Method Summary

| Modifier and Type                            | Method and Description                                                                                                                                                                          |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static void                                  | add(ALConfiguration config) add an instance of ALConfig to the current thread's ALContext.                                                                                                      |
| static void                                  | addClForBOCacheClean(java.util.List<java.lang.ClassLoader> clList) Add the ClassLoader list for BO Cache cleanup for this thread                                                                |
| static void                                  | cleanRALCache(ALConfiguration config) clean the corresponding ALConfiguration from the cache.                                                                                                   |
| static void                                  | cleanRALCache(java.util.Collection<ALConfiguration> configs) clean the corresponding collections of ALConfiguration from the cache.The operation  need to happen after setContext/ unset() pair |
| static void                                  | cleanupClForBOCacheClean() Clean up the the ClassLoader list for BO Cache cleanup for this thread                                                                                               |
| static void                                  | clearBOCache() Clear BO cache                                                                                                                                                                   |
| static java.util.List<java.lang.ClassLoader> | getClForBOCacheClean() Get the ClassLoader list for BO Cache cleanup for this thread                                                                                                            |
| static java.lang.String                      | getContainerReference() Returns the ContainerReference id in external form from the current context on this thread.                                                                             |
| static void                                  | remove(ALConfiguration config) remove an instance of ALConfig from the current thread's ALContext.                                                                                              |
| static void                                  | setClForBOCacheClean(java.util.List<java.lang.ClassLoader> clList) Set the ClassLoader list for BO Cache cleanup for this thread                                                                |
| static void                                  | setContainerReference(java.lang.String externalForm) Sets ContainerReference as current context for this thread.                                                                                |
| static void                                  | setContext(ALConfiguration config) set AL context to an instance of ALConfig.                                                                                                                   |
| static void                                  | setContext(java.util.Collection<ALConfiguration> configs) set AL context to a list of ALConfig.                                                                                                 |
| static void                                  | setContext(java.lang.String tempName,           java.lang.String appName) This is a easy of use wrapper method.                                                                                 |
| static void                                  | unset() unset the current thread's AL context                                                                                                                                                   |

    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait