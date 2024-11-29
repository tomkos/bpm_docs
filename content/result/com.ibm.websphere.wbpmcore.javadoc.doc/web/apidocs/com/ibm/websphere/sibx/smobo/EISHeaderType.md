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

## Interface EISHeaderType

- public interface EISHeaderType begin-user-doc A representation of the model object 'EIS Header Type '. end-user-doc The following features are supported:

```
public interface EISHeaderType
```

The following features are supported:
 
EIS Interaction Spec
EIS Connection Spec

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

java.lang.Object
getEISConnectionSpec()
Returns the value of the 'EIS Connection Spec' containment reference

java.lang.Object
getEISInteractionSpec()
Returns the value of the 'EIS Interaction Spec' containment reference

void
setEISConnectionSpec(java.lang.Object value)
Sets the value of the 'EIS Connection Spec' containment reference

void
setEISInteractionSpec(java.lang.Object value)
Sets the value of the 'EIS Interaction Spec' containment reference

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

    - getEISInteractionSpec
java.lang.Object getEISInteractionSpec()
Returns the value of the 'EIS Interaction Spec' containment reference.
 

Returns:the value of the 'EIS Interaction Spec' containment reference.See Also:setEISInteractionSpec(Object)
    - setEISInteractionSpec
void setEISInteractionSpec(java.lang.Object value)
Sets the value of the 'EIS Interaction Spec' containment reference.
 

Parameters:value - the new value of the 'EIS Interaction Spec' containment reference. Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getEISInteractionSpec()
    - getEISConnectionSpec
java.lang.Object getEISConnectionSpec()
Returns the value of the 'EIS Connection Spec' containment reference.
 

Returns:the value of the 'EIS Connection Spec' containment reference.See Also:setEISConnectionSpec(Object)
    - setEISConnectionSpec
void setEISConnectionSpec(java.lang.Object value)
Sets the value of the 'EIS Connection Spec' containment reference.
 

Parameters:value - the new value of the 'EIS Connection Spec' containment reference. Note that
              this must be a commonj.sdo.DataObject rather than a simple java.lang.Object.See Also:getEISConnectionSpec()