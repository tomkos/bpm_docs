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

## Interface JMSObjectBinding

- All Superinterfaces:
commonj.connector.runtime.DataBinding, JMSDataBinding, java.io.Serializable

All Known Implementing Classes:
JMSDataBindingImplJava

public interface JMSObjectBinding
extends JMSDataBinding
A DataBinding represents the mapping between a native data
 format and an SDO DataObject, and vice-versa. 
 This interface is a further extension of
 commonj.connector.runtime.DataBinding based on the
 JMSDataBinding interface. It exposes methods to support the
 transport of java.lang.Objects, as well as DataObjects as
 supported by the parent class.
See Also:DataBinding

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String $sccsid static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | $sccsid                 |
| static java.lang.String | COPYRIGHT               |

- Fields inherited from interface com.ibm.websphere.sca.jms.data.JMSDataBinding
ANY\_MESSAGE, BASE\_MESSAGE, BYTES\_MESSAGE, MAP\_MESSAGE, OBJECT\_MESSAGE, STREAM\_MESSAGE, TEXT\_MESSAGE

- Method Summary Methods Modifier and Type Method and Description java.lang.Object getObject () Returns the Object created by this DataBinding implementation (in the read method) to the runtime. boolean isObjectType () Used by the runtime to query whether the payload received by the DataBinding is an Object or a DataObject. void setObject (java.lang.Object inObject) This method is called by the runtime to prime the DataBinding, prior to the write method being invoked to serialize the Object to an outgoing JMS Message. void setObjectType (boolean isObject) Used by the runtime to indicate to the DataBinding that the input value to be serialized by the write method is an Object (set by setObject ) and not a DataObject (set by setDataObject ).

### Method Summary

| Modifier and Type   | Method and Description                                                                                                                                                                                                       |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| java.lang.Object    | getObject() Returns the Object created by this DataBinding implementation  (in the read method) to the runtime.                                                                                                              |
| boolean             | isObjectType() Used by the runtime to query whether the payload received by  the DataBinding is an Object or a DataObject.                                                                                                   |
| void                | setObject(java.lang.Object inObject) This method is called by the runtime to prime the  DataBinding, prior to the write method being  invoked to serialize the Object to an outgoing JMS Message.                            |
| void                | setObjectType(boolean isObject) Used by the runtime to indicate to the DataBinding that the  input value to be serialized by the write  method is an Object (set by setObject) and not a  DataObject (set by setDataObject). |

    - Methods inherited from interface com.ibm.websphere.sca.jms.data.JMSDataBinding
getMessageType, isBusinessException, read, setBusinessException, write
    - Methods inherited from interface commonj.connector.runtime.DataBinding
getDataObject, setDataObject