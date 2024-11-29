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

## Interface SCAServices

- public interface SCAServices
Provides SCA related services to ESB mediation primitives. Makes available 
 the name of the SCA component and SCA module hosting the flow in which this
 ESB mediation primitive participates. The SCA Component 
 meta-data object is also available.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getComponentName()
Gets the name of the SCA component hosting this ESB mediation primitive.

java.lang.String
getModuleName()
Gets the name of the SCA module hosting this ESB mediation primitive.

com.ibm.websphere.sca.scdl.Component
getParentComponent()
Returns the parent SCA component of this ESB mediation primitive.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- $sccsid
static final java.lang.String $sccsid
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getComponentName
java.lang.String getComponentName()
Gets the name of the SCA component hosting this ESB mediation primitive.
Returns:the name of the SCA component
    - getModuleName
java.lang.String getModuleName()
Gets the name of the SCA module hosting this ESB mediation primitive.
Returns:the name of the SCA module
    - getParentComponent
com.ibm.websphere.sca.scdl.Component getParentComponent()
Returns the parent SCA component of this ESB mediation primitive.
Returns:the parent SCA component