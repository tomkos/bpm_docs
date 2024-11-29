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

## Class ObjectStoreReference

- java.lang.Object
    - com.ibm.casemgmt.api.objectref.CEObjectReference<com.filenet.api.core.ObjectStore,DomainReference>
        - com.ibm.casemgmt.api.objectref.ObjectStoreReference

- public class ObjectStoreReference
extends CEObjectReference<com.filenet.api.core.ObjectStore,DomainReference>
Represents a reference to a Content Engine Java API ObjectStore object.
 An ObjectStore instance has a parent object reference of type DomainReference.
 
 An ObjectStoreReference can be constructed using a parent DomainReference and
 a name or ID. The name can be the object store symbolic name or display name.
 
 An ObjectStoreReference can also be constructed using an existing Content Engine 
 Java API ObjectStore object.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

ObjectStoreReference(DomainReference domainRef,
                    com.filenet.api.util.Id osId)
Constructs an ObjectStoreReference instance using a parent DomainReference
 object and an ID.

ObjectStoreReference(DomainReference domainRef,
                    java.lang.String osName)
Constructs an ObjectStoreReference instance using a parent DomainReference
 object and a name.

ObjectStoreReference(com.filenet.api.core.ObjectStore os)
Constructs an ObjectStoreReference instance using an existing Content Engine
 Java API ObjectStore object.
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.ObjectStore fetchCEObject (com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API ObjectStore object. com.filenet.api.core.ObjectStore getFetchlessCEObject () Obtains a fetchless instance of a Content Engine Java API ObjectStore object. java.lang.String getObjectStoreIdentity () Returns the identity as either an ID or a name, however it is represented in the reference.

### Method Summary

| Modifier and Type                | Method and Description                                                                                                 |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.ObjectStore | fetchCEObject(com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API ObjectStore object.        |
| com.filenet.api.core.ObjectStore | getFetchlessCEObject() Obtains a fetchless instance of a Content Engine Java API ObjectStore object.                   |
| java.lang.String                 | getObjectStoreIdentity() Returns the identity as either an ID or a name, however it is represented in   the reference. |

    - Methods inherited from class com.ibm.casemgmt.api.objectref.CEObjectReference
fetchCEObject, fetchOptionalCEObject, fetchOptionalCEObject, getParentObjectReference
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait