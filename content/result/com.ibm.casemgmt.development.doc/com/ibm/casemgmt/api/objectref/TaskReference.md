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

## Class TaskReference

- java.lang.Object
    - com.ibm.casemgmt.api.objectref.CEObjectReference<com.filenet.api.core.CmTask,ObjectStoreReference>
        - com.ibm.casemgmt.api.objectref.TaskReference

- public class TaskReference
extends CEObjectReference<com.filenet.api.core.CmTask,ObjectStoreReference>
Represents a reference to a Content Engine Java API CmTask object.
 A TaskReference has a parent object reference of type ObjectStoreReference.
 
 A TaskReference can be constructed using a parent ObjectStoreReference and
 an ID.  It can also be constructed with an existing Content Engine Java API
 CmTask object.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

TaskReference(com.filenet.api.core.CmTask task)
Constructs a TaskReference instance using a Content Engine Java API
 CmTask object.

TaskReference(ObjectStoreReference osRef,
             com.filenet.api.util.Id taskId)
Constructs a TaskReference object using a parent ObjectStoreReference
 object and a task object ID.
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.CmTask fetchCEObject (com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API CmTask object. com.filenet.api.core.CmTask getFetchlessCEObject () Obtains a fetchless instance of a Content Engine Java API CmTask object.

### Method Summary

| Modifier and Type           | Method and Description                                                                                     |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.CmTask | fetchCEObject(com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API CmTask object. |
| com.filenet.api.core.CmTask | getFetchlessCEObject() Obtains a fetchless instance of a Content Engine Java API CmTask object.            |

    - Methods inherited from class com.ibm.casemgmt.api.objectref.CEObjectReference
fetchCEObject, fetchOptionalCEObject, fetchOptionalCEObject, getParentObjectReference
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait