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

## Class DomainReference

- java.lang.Object
    - com.ibm.casemgmt.api.objectref.CEObjectReference<com.filenet.api.core.Domain,CEObjectReference<?,?>>
        - com.ibm.casemgmt.api.objectref.DomainReference

- public class DomainReference
extends CEObjectReference<com.filenet.api.core.Domain,CEObjectReference<?,?>>
Represents a reference to a Content Engine Java API Domain object.
 A DomainReference instance does not have a parent object reference.
 The getParentObjectReference method returns null.
 
 A DomainReference can be constructed using a domain connection URI
 in which case a Content Engine Java API Connection object is obtained
 from the execution context configured using CaseMgmtContext and
 P8ConnectionCache.
 
 A DomainReference can also be constructed using an existing Domain
 object.

ID status:
ID review by David Newhall

- ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Constructor Summary

Constructors 

Constructor and Description

DomainReference(com.filenet.api.core.Domain domain)
Constructs a DomainReference instance using an existing
 Content Engine Java API Domain object.

DomainReference(java.lang.String ceUri)
Constructs a DomainReference instance using a Content Engine
 domain connection URI.
    - Method Summary All Methods Instance Methods Concrete Methods Modifier and Type Method and Description com.filenet.api.core.Domain fetchCEObject (com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API Domain object. com.filenet.api.core.Connection getConnection () Returns the Connection object that was obtained when this instance was constructed. com.filenet.api.core.Domain getFetchlessCEObject () Obtains a fetchless instance of a Content Engine Java API Domain object.

### Method Summary

| Modifier and Type               | Method and Description                                                                                     |
|---------------------------------|------------------------------------------------------------------------------------------------------------|
| com.filenet.api.core.Domain     | fetchCEObject(com.filenet.api.property.PropertyFilter pf) Fetches a Content Engine Java API Domain object. |
| com.filenet.api.core.Connection | getConnection() Returns the Connection object that was obtained when this  instance was constructed.       |
| com.filenet.api.core.Domain     | getFetchlessCEObject() Obtains a fetchless instance of a Content Engine Java API Domain object.            |

    - Methods inherited from class com.ibm.casemgmt.api.objectref.CEObjectReference
fetchCEObject, fetchOptionalCEObject, fetchOptionalCEObject, getParentObjectReference
    - Methods inherited from class java.lang.Object
equals, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait