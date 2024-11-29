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

## Interface LocatorDefinition

- public interface LocatorDefinition
This is the interface that locator definitions need to implement.
 This interface is actually the java representation of the corresponding emf model that gets
 generated when configuration file for the artifactloader is loaded in the memory.
 In the configuration file there is a locator definition for each locator that is available.
 That definition has some properties and in this interface there are get methods specified for those properties.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT
This is copyright for this class / interface
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.util.List
getEnvironments()
Method to find out the environments this locator supports.

java.lang.String
getImplementation()
Method to get the complete instantiable class name of the locator implementation.

java.util.List
getMimes()
Method to find out the supported mimes by this locator.

java.lang.String
getName()
Method to get the name of the locator implementation.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
This is copyright for this class / interface
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getName
java.lang.String getName()
Method to get the name of the locator implementation.
Returns:Returns the name of the locator implementation.
    - getImplementation
java.lang.String getImplementation()
Method to get the complete instantiable class name of the locator implementation.
Returns:Returns the class name of the locator implementation.
    - getMimes
java.util.List getMimes()
Method to find out the supported mimes by this locator.
Returns:Returns the mimes supported by the locator implementation.
    - getEnvironments
java.util.List getEnvironments()
Method to find out the environments this locator supports.
Returns:Returns the list of environments that this locator works in.