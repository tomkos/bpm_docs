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

## Interface MQHeader

- All Superinterfaces: MQControl public interface MQHeader extends MQControl begin-user-doc A representation of the model object 'MQ Header '. end-user-doc The following features are supported: See Also: WMQStructuresPackage.getMQHeader()

```
public interface MQHeader
extends MQControl
```

The following features are supported:
 
Value

- ========== METHOD SUMMARY ===========
    - Method Summary Methods Modifier and Type Method and Description java.lang.Object getValue () Returns the value of the 'Value ' containment reference void setValue (java.lang.Object value) Sets the value of the 'Value ' containment reference

### Method Summary

| Modifier and Type   | Method and Description                                                               |
|---------------------|--------------------------------------------------------------------------------------|
| java.lang.Object    | getValue() Returns the value of the 'Value' containment reference                    |
| void                | setValue(java.lang.Object value) Sets the value of the 'Value' containment reference |

- Methods inherited from interface com.ibm.websphere.sca.mq.structures.MQControl
getCodedCharSetId, getEncoding, getFormat, isSetCodedCharSetId, isSetEncoding, setCodedCharSetId, setEncoding, setFormat, unsetCodedCharSetId, unsetEncoding