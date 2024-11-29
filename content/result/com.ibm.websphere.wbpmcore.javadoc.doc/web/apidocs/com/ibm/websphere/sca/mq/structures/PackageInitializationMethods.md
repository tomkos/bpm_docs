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

## Class PackageInitializationMethods

- java.lang.Object
    - com.ibm.websphere.sca.mq.structures.PackageInitializationMethods

- public class PackageInitializationMethods
extends java.lang.Object
The ContextService, introduced for 6.2, is in the session.core component.
 Because the ContextService uses SMO and SMO will use the ContextService,
 there would be a dependency cycle between session.core and smo. To break
 the cycle we need to separate the SMO interface classes from the SMO
 implementation classes. 
 
 The EMF generated code in ServiceMessageObjectFactory and ServiceMessageObjectPackage
 has direct calls to the init() methods in the corresponding implementation
 classes. We need to remove this dependency of the interface classes on the 
 implementation classes, and the two methods in this class are designed to do that.

 These methods are only called once, on package initialization, so efficiency is not
 a major concern.

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Constructor Summary

Constructors 

Constructor and Description

PackageInitializationMethods()
    - Method Summary Methods Modifier and Type Method and Description static boolean isXCI ()

### Method Summary

| Modifier and Type   | Method and Description   |
|---------------------|--------------------------|
| static boolean      | isXCI()                  |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait