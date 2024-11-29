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

## Interface ItemListener

- All Known Implementing Classes:
BPCDetailsHandler

public interface ItemListener
The ItemListener interface is used to declare interest in events concerning selection changes.
 For example, BPCListHandler allows you to register the Item Change Listener through the
 itemListener property:

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

void
itemChanged(java.lang.Object item)
Triggered whenever a new element is selected in the ItemListener event provider.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - itemChanged
void itemChanged(java.lang.Object item)
                 throws ClientException
Triggered whenever a new element is selected in the ItemListener event provider.
Parameters:item - The item that has been selected.
Throws:
ClientException