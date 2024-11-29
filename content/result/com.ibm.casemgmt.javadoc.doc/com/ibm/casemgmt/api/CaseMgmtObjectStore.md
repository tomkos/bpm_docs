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

## Class CaseMgmtObjectStore

- java.lang.Object
    - com.ibm.casemgmt.api.CaseMgmtObjectStore

- public final class CaseMgmtObjectStore
extends java.lang.Object
Represents an object store that contains a deployed solution in the Case Management system.
 To obtain an instance of CaseMgmtObjectStore, use one of the factory methods, 
 getFetchlessInstance() or fetchInstance().
 
 If an instance is fetched by calling fetchInstance(), the method
 verifies that the identifier used to reference the object store represents a
 valid object store. An exception is thrown if the object store is invalid.
 If getFetchlessInstance() is called, no such verification occurs,
 but an exception may be thrown later if a method is called that requires that 
 the referenced object store is valid.
 
 All of the information returned by CaseMgmtObjectStore is managed by a 
 cache internal to the Case Java API. The same information can be obtained
 whether the instance was obtained in a fetched or a fetchless manner, but 
 calling fetchInstance() performs only an initial check to ensure
 that the referenced object store is valid.

ID status:
ID review by David Newhall

- ======== NESTED CLASS SUMMARY ======== ========== METHOD SUMMARY ===========
    - Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

static class 
CaseMgmtObjectStore.CM8HostConfiguration
Represents information about the CM8 host configured for this
 object store.
    - Method Summary All Methods Static Methods Instance Methods Concrete Methods Modifier and Type Method and Description static CaseMgmtObjectStore fetchInstance (ObjectStoreReference objStoreRef) A factory method that returns an instance of CaseMgmtObjectStore . CaseMgmtObjectStore.CM8HostConfiguration getCM8HostConfiguration () Returns information about the CM8 host configured for this object store. java.lang.String getDisplayName () Returns the display name of the object store. static CaseMgmtObjectStore getFetchlessInstance (ObjectStoreReference objStoreRef) A factory method that returns an instance of CaseMgmtObjectStore . com.filenet.api.util.Id getId () Returns the Id of the object store. IntegrationType getIntegrationType () Returns the integration type of the object store. java.util.Date getLastConfiguredDate () Returns the last configured date of the object store. ObjectStoreReference getObjectStoreReference () Returns an ObjectStoreReference object that represents a reference to the Content Engine object store object. java.lang.String getSymbolicName () Returns the symbolic name of the object store. TargetEnvironmentType getTargetEnvironmentType () Returns the target environment type of the object store.

### Method Summary

| Modifier and Type                        | Method and Description                                                                                                                   |
|------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| static CaseMgmtObjectStore               | fetchInstance(ObjectStoreReference objStoreRef) A factory method that returns an instance of CaseMgmtObjectStore.                        |
| CaseMgmtObjectStore.CM8HostConfiguration | getCM8HostConfiguration() Returns information about the CM8 host configured for this  object store.                                      |
| java.lang.String                         | getDisplayName() Returns the display name of the object store.                                                                           |
| static CaseMgmtObjectStore               | getFetchlessInstance(ObjectStoreReference objStoreRef) A factory method that returns an instance of CaseMgmtObjectStore.                 |
| com.filenet.api.util.Id                  | getId() Returns the Id of the object store.                                                                                              |
| IntegrationType                          | getIntegrationType() Returns the integration type of the object store.                                                                   |
| java.util.Date                           | getLastConfiguredDate() Returns the last configured date of the object store.                                                            |
| ObjectStoreReference                     | getObjectStoreReference() Returns an ObjectStoreReference object that represents a reference to the  Content Engine object store object. |
| java.lang.String                         | getSymbolicName() Returns the symbolic name of the object store.                                                                         |
| TargetEnvironmentType                    | getTargetEnvironmentType() Returns the target environment type of the object store.                                                      |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait