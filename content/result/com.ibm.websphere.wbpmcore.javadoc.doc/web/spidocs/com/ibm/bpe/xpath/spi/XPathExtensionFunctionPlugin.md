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

## Interface XPathExtensionFunctionPlugin

- public interface XPathExtensionFunctionPlugin
This interface allows the definition of custom XPath extension functions. These functions can be used in 
  XPath expressions and conditions in a BPEL process.
  

Since:
8.5

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

XPathExtensionFunctionDescriptor[]
getXPathFunctions()
Exposes XPath extension functions to the process runtime environment.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getXPathFunctions
XPathExtensionFunctionDescriptor[] getXPathFunctions()
Exposes XPath extension functions to the process runtime environment.
Returns:An array of XPathExtensionFunctionDescriptor that discribes the custom extension functions.