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

## Interface WTXContextType

- public interface WTXContextType begin-user-doc A representation of the model object 'WTX Context Type '. end-user-doc The following features are supported:

```
public interface WTXContextType
```

The following features are supported:
 
Map Server Location
Dynamic Map
Map Instances

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

byte[]
getDynamicMap()
Returns the value of the 'Dynamic Map' attribute.

java.util.List<WTXMapInstanceType>
getMapInstances()
Returns the value of the 'Map Instances' containment reference list.

java.lang.String
getMapServerLocation()
Returns the value of the 'Map Server Location' attribute.

void
setDynamicMap(byte[] value)
Sets the value of the 'Dynamic Map' attribute.

void
setMapServerLocation(java.lang.String value)
Sets the value of the 'Map Server Location' attribute.

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

    - getMapServerLocation
java.lang.String getMapServerLocation()
Returns the value of the 'Map Server Location' attribute.
Returns:the value of the 'Map Server Location' attribute.See Also:setMapServerLocation(String)
    - setMapServerLocation
void setMapServerLocation(java.lang.String value)
Sets the value of the 'Map Server Location' attribute.
Parameters:value - the new value of the 'Map Server Location' attribute.See Also:getMapServerLocation()
    - getDynamicMap
byte[] getDynamicMap()
Returns the value of the 'Dynamic Map' attribute.
Returns:the value of the 'Dynamic Map' attribute.See Also:setDynamicMap(byte[])
    - setDynamicMap
void setDynamicMap(byte[] value)
Sets the value of the 'Dynamic Map' attribute.
Parameters:value - the new value of the 'Dynamic Map' attribute.See Also:getDynamicMap()
    - getMapInstances
java.util.List<WTXMapInstanceType> getMapInstances()
Returns the value of the 'Map Instances' containment reference list.
 The list contents are of type WTXMapInstanceType.
Returns:the value of the 'Map Instances' containment reference list.