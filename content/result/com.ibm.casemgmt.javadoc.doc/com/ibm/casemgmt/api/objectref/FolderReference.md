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

## Class FolderReference

- java.lang.Object
    - com.ibm.casemgmt.api.objectref.CEObjectReference<com.filenet.api.core.Folder,ObjectStoreReference>
        - com.ibm.casemgmt.api.objectref.FolderReference

- public class FolderReference
extends CEObjectReference<com.filenet.api.core.Folder,ObjectStoreReference>
Represents a reference to a Content Engine Java API Folder object.
 A FolderReference instance has a parent object reference of type ObjectStoreReference.
 
 A FolderReference can be constructed using a parent ObjectStoreReference and either
 an object ID or path. It can also be constructed with a Content Engine Java API
 ObjectStore object and a path or ID. It can also be constructed with a Content Engine Java API
 Folder object.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

FolderReference(com.filenet.api.core.Folder folder)
Constructs a FolderReference instance using a Content Engine Java API
 Folder object.

FolderReference(com.filenet.api.core.ObjectStore os,
               com.filenet.api.util.Id folderId)
Constructs a FolderReference using an existing Content Engine Java API ObjectStore
 object and a folder ID.

FolderReference(ObjectStoreReference osRef,
               com.filenet.api.util.Id folderId)
Constructs a FolderReference object using a parent ObjectStoreReference
 object and a folder ID.

FolderReference(ObjectStoreReference osRef,
               java.lang.String folderPath)
Constructs a FolderReference object using a parent ObjectStoreReference
 object and a folder path.

FolderReference(com.filenet.api.core.ObjectStore os,
               java.lang.String folderPath)
Constructs a FolderReference using an existing Content Engine Java API ObjectStore
 object and a folder path.
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.Folder fetchCEObject (com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API Folder object. com.filenet.api.core.Folder getFetchlessCEObject () Obtains a fetchless instance of a Content Engine Java API Folder object.

### Method Summary

| Modifier and Type           | Method and Description                                                                                     |
|-----------------------------|------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.Folder | fetchCEObject(com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API Folder object. |
| com.filenet.api.core.Folder | getFetchlessCEObject() Obtains a fetchless instance of a Content Engine Java API Folder object.            |

    - Methods inherited from class com.ibm.casemgmt.api.objectref.CEObjectReference
fetchCEObject, fetchOptionalCEObject, fetchOptionalCEObject, getParentObjectReference
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait