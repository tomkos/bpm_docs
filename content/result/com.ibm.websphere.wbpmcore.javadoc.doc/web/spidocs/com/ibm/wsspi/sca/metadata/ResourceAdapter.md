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

## Interface ResourceAdapter

- public interface ResourceAdapter
Interface that represent the resource adapter information of a resource adapter binding.
Since:
7.5.1.0

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
getName()
Method returns the name of the resource adapter.

java.util.Map<java.lang.String,java.lang.String>
getProperties()
Method returns the properties of the resource adapter.

java.lang.String
getType()
Method returns the type of the resource adapter.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Method returns the name of the resource adapter.
Returns:String
     Name of the resource adapter.
    - getType
java.lang.String getType()
Method returns the type of the resource adapter.
Returns:String
     Type of the resource adapter.
    - getProperties
java.util.Map<java.lang.String,java.lang.String> getProperties()
Method returns the properties of the resource adapter.
Returns:Map
     Properties of the resource adapter.