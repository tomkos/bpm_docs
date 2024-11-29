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

## Interface ImportBinding

- All Known Subinterfaces:
EISImportBinding, EjbImportBinding, SCAImportBinding, WebServiceImportBinding

public interface ImportBinding
Interface that represent the binding information on a SCA import.
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
getBindingType()
Method returns the type of the import binding.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getBindingType
java.lang.String getBindingType()
Method returns the type of the import binding.
Returns:String
     Type of the import binding.