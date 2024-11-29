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

## Interface CorrelationSetInstanceData

- All Superinterfaces:
java.io.Serializable

public interface CorrelationSetInstanceData
extends java.io.Serializable
Provides information about correlation set instances.
Since:
7.0

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getCorrelationSetName()
Returns the name of the correlation set.

java.util.List
getCorrelationSetProperties()
Returns the properties that are contained in a correlation set instance.

boolean
isInitialized()
Indicates whether the correlation set is initialized,

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getCorrelationSetName
java.lang.String getCorrelationSetName()
Returns the name of the correlation set.
Returns:The name of the correlation set.
    - getCorrelationSetProperties
java.util.List getCorrelationSetProperties()
Returns the properties that are contained in a correlation set instance.
Returns:A list of correlation property instances - refer to CorrelationPropertyInstanceData.
    - isInitialized
boolean isInitialized()
Indicates whether the correlation set is initialized,
Returns:True when the correlation set is initialized else false.