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

## Class CEObjectReference<T extends com.filenet.api.core.IndependentObject,P extends CEObjectReference<?,?>>

- java.lang.Object
    - com.ibm.casemgmt.api.objectref.CEObjectReference<T,P>

- Type Parameters:
T - the class of Content Engine Java API object that this reference
             class refers to. For example, Folder for a folder reference.
P - the object reference class that refers to the parent of the
             type of object this reference class refers to. For example, 
             for a Folder object, the parent object reference would be
             ObjectStoreReference. If the type of object has no parent,
             the Object is used for this parameter.

Direct Known Subclasses:
DomainReference, FolderReference, ObjectStoreReference, TaskReference

public abstract class CEObjectReference<T extends com.filenet.api.core.IndependentObject,P extends CEObjectReference<?,?>>
extends java.lang.Object
Base class that all object reference classes extend. This is a parameterized
 class with parameters for the type of Content Engine Java API object the
 class references as well as the type of reference class that refers 
 to a parent of the object. For example, the parent of a Folder object is
 an ObjectStore object so the parent is identified with an ObjectStoreReference
 object.

ID status:
ID review by David Newhall

- ========== METHOD SUMMARY ===========
    - Method Summary All Methods Instance Methods Abstract Methods Concrete Methods Modifier and Type Method and Description T fetchCEObject () Fetches the Content Engine Java API object this reference object refers to using null for the default property filter. abstract T fetchCEObject (com.filenet.api.property.PropertyFilter propFilt) Fetches the Content Engine Java API object this reference object refers to using a specific property filter. T fetchOptionalCEObject () Fetches the Content Engine Java API object this reference object refers to, but if the object does not exist in the repository, no exception is thrown and null is returned. T fetchOptionalCEObject (com.filenet.api.property.PropertyFilter pf) Fetches the Content Engine Java API object this reference object refers to, but if the object does not exist in the repository, no exception is thrown and null is returned. abstract T getFetchlessCEObject () Obtains a fetchless instance for the Content Engine Java API object this reference object refers to. P getParentObjectReference () Gets the object reference object that refers to the parent of the object this instance refers to.

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                                            |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T                   | fetchCEObject() Fetches the Content Engine Java API object this reference object  refers to using null for the default property filter.                                                                                                           |
| abstract T          | fetchCEObject(com.filenet.api.property.PropertyFilter propFilt) Fetches the Content Engine Java API object this reference object  refers to using a specific property filter.                                                                     |
| T                   | fetchOptionalCEObject() Fetches the Content Engine Java API object this reference object  refers to, but if the object does not exist in the repository,   no exception is thrown and null is returned.                                           |
| T                   | fetchOptionalCEObject(com.filenet.api.property.PropertyFilter pf) Fetches the Content Engine Java API object this reference object  refers to, but if the object does not exist in the repository,   no exception is thrown and null is returned. |
| abstract T          | getFetchlessCEObject() Obtains a fetchless instance for the Content Engine Java API object  this reference object refers to.                                                                                                                      |
| P                   | getParentObjectReference() Gets the object reference object that refers to the parent of the  object this instance refers to.                                                                                                                     |

- Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait