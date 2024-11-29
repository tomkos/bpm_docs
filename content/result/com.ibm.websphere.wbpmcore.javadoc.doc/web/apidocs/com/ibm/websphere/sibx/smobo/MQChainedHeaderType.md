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

## Interface MQChainedHeaderType

- All Superinterfaces: MQControl public interface MQChainedHeaderType extends MQControl A representation of the model object 'MQ Chained Header Type '. The following features are supported:

```
public interface MQChainedHeaderType
extends MQControl
```

The following features are supported:
 
Value
Opaque
Rfh
Rfh2

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static java.lang.String
$sccsid 

static java.lang.String
COPYRIGHT
    - Method Summary Methods Modifier and Type Method and Description MQOpaqueHeader getOpaque () Returns the value of the 'Opaque ' containment reference. MQRFH getRfh () Returns the value of the 'Rfh ' containment reference. MQRFH2 getRfh2 () Returns the value of the 'Rfh2 ' containment reference. java.lang.Object getValue () Returns the value of the 'Value ' containment reference. void setOpaque (MQOpaqueHeader value) Sets the value of the 'Opaque ' containment reference. void setRfh (MQRFH value) Sets the value of the 'Rfh ' containment reference. void setRfh2 (MQRFH2 value) Sets the value of the 'Rfh2 ' containment reference. void setValue (java.lang.Object value) Sets the value of the 'Value ' containment reference.

### Method Summary

| Modifier and Type   | Method and Description                                                                |
|---------------------|---------------------------------------------------------------------------------------|
| MQOpaqueHeader      | getOpaque() Returns the value of the 'Opaque' containment reference.                  |
| MQRFH               | getRfh() Returns the value of the 'Rfh' containment reference.                        |
| MQRFH2              | getRfh2() Returns the value of the 'Rfh2' containment reference.                      |
| java.lang.Object    | getValue() Returns the value of the 'Value' containment reference.                    |
| void                | setOpaque(MQOpaqueHeader value) Sets the value of the 'Opaque' containment reference. |
| void                | setRfh(MQRFH value) Sets the value of the 'Rfh' containment reference.                |
| void                | setRfh2(MQRFH2 value) Sets the value of the 'Rfh2' containment reference.             |
| void                | setValue(java.lang.Object value) Sets the value of the 'Value' containment reference. |

- Methods inherited from interface com.ibm.websphere.sca.mq.structures.MQControl
getCodedCharSetId, getEncoding, getFormat, isSetCodedCharSetId, isSetEncoding, setCodedCharSetId, setEncoding, setFormat, unsetCodedCharSetId, unsetEncoding