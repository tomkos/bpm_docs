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

## Class AbstractMediation

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.AbstractMediation

- All Implemented Interfaces:
Mediation

Direct Known Subclasses:
ESBMediationPrimitive

public abstract class AbstractMediation
extends java.lang.Object
implements Mediation
Convenient abstract class for mediation primitive implementors. This provides
 an implementation of the 
 setMediationServices
 and 
 init methods of the Mediation interface.
 The init method simply provides a no-op implementation which 
 mediation primitive programmers may override to perform initialization.
 
 This class also provides a 
 getMediationServices method
 to allow access to the mediation services set by the engine.
 
 At a minimum, extenders of this class must implement the 
 mediate method of the 
 Mediation interface.

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

Modifier
Constructor and Description

protected 
AbstractMediation()
Explicitly defined protected default constructor.
    - Method Summary Methods Modifier and Type Method and Description MediationServices getMediationServices () Gets the mediation services for this mediation primitive. void init () Basic no-op implementation of init. void setMediationServices (MediationServices mediationServices) Sets the mediation services for this mediation primitive.

### Method Summary

| Modifier and Type   | Method and Description                                                                                              |
|---------------------|---------------------------------------------------------------------------------------------------------------------|
| MediationServices   | getMediationServices() Gets the mediation services for this mediation primitive.                                    |
| void                | init() Basic no-op implementation of init.                                                                          |
| void                | setMediationServices(MediationServices mediationServices) Sets the mediation services for this mediation primitive. |

- Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait

- Methods inherited from interface com.ibm.wsspi.sibx.mediation.Mediation
mediate