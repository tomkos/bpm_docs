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

## Interface ESBMediation

- All Superinterfaces: Mediation All Known Implementing Classes: ESBMediationPrimitive public interface ESBMediation extends Mediation Mediation primitive interface for ESB mediation primitives. This interface extends the Mediation interface to support additional services for ESB mediation primitives. ESB mediation primitives have access to two additional services: This interface adds setter methods that allow the engine to supply this mediation primitive with the additional services. ESB mediation primitives do not have to implement ESBMediation if they do not need the extra services.

```
public interface ESBMediation
extends Mediation
```

ESB mediation primitives have access to two additional services:
 
 
SCAServices - Provides useful methods for interacting with the 
   SCA runtime
RuntimeServices - Provides useful methods for interacting with 
   the WebSphere runtime

This interface adds setter methods that allow the engine to supply this
 mediation primitive with the additional services. ESB mediation primitives
 do not have to implement ESBMediation if they do not need the 
 extra services.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description void setRuntimeServices (RuntimeServices runtimeServices) Sets the runtime services. void setSCAServices (SCAServices scaServices) Sets the SCA services.

### Method Summary

| Modifier and Type   | Method and Description                                                         |
|---------------------|--------------------------------------------------------------------------------|
| void                | setRuntimeServices(RuntimeServices runtimeServices) Sets the runtime services. |
| void                | setSCAServices(SCAServices scaServices) Sets the SCA services.                 |

- Methods inherited from interface com.ibm.wsspi.sibx.mediation.Mediation
init, mediate, setMediationServices