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

## Interface DataFactory

- public interface DataFactory
A Factory for creating SDO DataObjects.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
COPYRIGHT 

static DataFactory
INSTANCE
The default DataFactory.
    - Method Summary

Methods 

Modifier and Type
Method and Description

commonj.sdo.DataObject
create(java.lang.Class interfaceClass)
Creates a DataObject supporting the given interface.

commonj.sdo.DataObject
create(java.lang.String uri,
      java.lang.String typeName)
Creates a DataObject of the Type specified by typeName with the given package uri.

commonj.sdo.DataObject
create(commonj.sdo.Type type)
Creates a DataObject of the Type specified.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- INSTANCE
static final DataFactory INSTANCE
The default DataFactory.

- Method Detail

### Method Detail

    - create
commonj.sdo.DataObject create(java.lang.Class interfaceClass)
Creates a DataObject supporting the given interface.
 InterfaceClass is the interface for the DataObject's Type.
Parameters:interfaceClass - is the interface for the DataObject's Type.
Returns:the created DataObject.
Throws:
java.lang.IllegalArgumentException - if the instanceClass does
   not correspond to a Type this factory can instantiate.
    - create
commonj.sdo.DataObject create(java.lang.String uri,
                            java.lang.String typeName)
Creates a DataObject of the Type specified by typeName with the given package uri.
Parameters:uri - The uri of the Package.typeName - The name of the Type.
Returns:the created DataObject.
Throws:
java.lang.IllegalArgumentException - if the uri and typeName does
   not correspond to a Type this factory can instantiate.
    - create
commonj.sdo.DataObject create(commonj.sdo.Type type)
Creates a DataObject of the Type specified.
Parameters:type - The Type.
Returns:the created DataObject.
Throws:
java.lang.IllegalArgumentException - if the Type
   cannot be instantiaed by this factory.