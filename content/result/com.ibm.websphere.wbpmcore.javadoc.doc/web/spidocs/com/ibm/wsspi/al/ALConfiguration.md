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

## Interface ALConfiguration

- public interface ALConfiguration
ALConfig defines what a configuration object to implement.
 An AL configuration object holds configuration information
  which consists of name, classname and metadata.

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
get(java.lang.String key)
get the value of a key/value pair using the key

java.lang.String
getLocatorName()
get the locatorName of this configuration

java.lang.String
getName()
get the name of this AL configuration

java.util.Set
keySet()
Returns a set view of the keys contained in this ALConfig

void
set(java.lang.String key,
   java.lang.String value)
set a key/value pair to an AL configuration

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - get
java.lang.String get(java.lang.String key)
get the value of a key/value pair using the key
Parameters:key - the key part of a key/value pair
Returns:String  the value part of a key/value pair
    - getName
java.lang.String getName()
get the name of this AL configuration
Returns:String   the name of this configuration
    - getLocatorName
java.lang.String getLocatorName()
get the locatorName of this configuration
Returns:String   the locatorName of this configuration
    - keySet
java.util.Set keySet()
Returns a set view of the keys contained in this ALConfig
Returns:Set   a set view of the keys contained in this map
    - set
void set(java.lang.String key,
       java.lang.String value)
set a key/value pair to an AL configuration
Parameters:key - the key of a metadatavalue - the value of a metadata