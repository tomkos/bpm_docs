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

## Class ESBMediationPrimitive

- java.lang.Object
    - com.ibm.wsspi.sibx.mediation.AbstractMediation
        - com.ibm.wsspi.sibx.mediation.esb.ESBMediationPrimitive

- All Implemented Interfaces:
ESBMediation, Mediation

public abstract class ESBMediationPrimitive
extends AbstractMediation
implements ESBMediation
Convenient abstract class for ESB mediation primitive implementors. This 
 provides an implementation of the 
 setSCAServices
 and 
 setRuntimeServices 
 methods of the ESBMediation interface.
 
 This class also provides  
 getSCAServices  and 
 getRuntimeServices methods
 to allow access to the SCA and runtime services set by the engine.
 
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

Constructor and Description

ESBMediationPrimitive()
    - Method Summary Methods Modifier and Type Method and Description RuntimeServices getRuntimeServices () Gets the runtime services for this ESB mediation primitive. SCAServices getSCAServices () Gets the SCA services for this ESB mediation primitive. void setRuntimeServices (RuntimeServices runtimeServices) Sets the runtime services for this ESB mediation primitive. void setSCAServices (SCAServices scaServices) Sets the SCA services for this ESB mediation primitive.

### Method Summary

| Modifier and Type   | Method and Description                                                                                          |
|---------------------|-----------------------------------------------------------------------------------------------------------------|
| RuntimeServices     | getRuntimeServices() Gets the runtime services for this ESB mediation primitive.                                |
| SCAServices         | getSCAServices() Gets the SCA services for this ESB mediation primitive.                                        |
| void                | setRuntimeServices(RuntimeServices runtimeServices) Sets the runtime services for this ESB mediation primitive. |
| void                | setSCAServices(SCAServices scaServices) Sets the SCA services for this ESB mediation primitive.                 |

    - Methods inherited from class com.ibm.wsspi.sibx.mediation.AbstractMediation
getMediationServices, init, setMediationServices
    - Methods inherited from class java.lang.Object
clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait
    - Methods inherited from interface com.ibm.wsspi.sibx.mediation.Mediation
init, mediate, setMediationServices