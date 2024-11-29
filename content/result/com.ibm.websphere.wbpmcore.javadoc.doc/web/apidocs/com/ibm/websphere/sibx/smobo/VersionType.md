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

## Interface VersionType

- public interface VersionType A representation of the model object 'Version Type '. This presents version information pertaining to this message. The version is broken down into version, release and modification. The following features are supported:

```
public interface VersionType
```

The following features are supported:
 
Version
Release
Modification

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

java.math.BigInteger
getModification()
Returns the value of the 'Modification' attribute.

java.math.BigInteger
getRelease()
Returns the value of the 'Release' attribute.

java.math.BigInteger
getVersion()
Returns the value of the 'Version' attribute.

void
setModification(java.math.BigInteger value)
Sets the value of the 'Modification' attribute.

void
setRelease(java.math.BigInteger value)
Sets the value of the 'Release' attribute.

void
setVersion(java.math.BigInteger value)
Sets the value of the 'Version' attribute.

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

    - getVersion
java.math.BigInteger getVersion()
Returns the value of the 'Version' attribute.
Returns:the value of the 'Version' attribute.See Also:setVersion(BigInteger)
    - setVersion
void setVersion(java.math.BigInteger value)
Sets the value of the 'Version' attribute.
Parameters:value - the new value of the 'Version' attribute.See Also:getVersion()
    - getRelease
java.math.BigInteger getRelease()
Returns the value of the 'Release' attribute.
Returns:the value of the 'Release' attribute.See Also:setRelease(BigInteger)
    - setRelease
void setRelease(java.math.BigInteger value)
Sets the value of the 'Release' attribute.
Parameters:value - the new value of the 'Release' attribute.See Also:getRelease()
    - getModification
java.math.BigInteger getModification()
Returns the value of the 'Modification' attribute.
Returns:the value of the 'Modification' attribute.See Also:setModification(BigInteger)
    - setModification
void setModification(java.math.BigInteger value)
Sets the value of the 'Modification' attribute.
Parameters:value - the new value of the 'Modification' attribute.See Also:getModification()