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

## Class JMSDataBindingImplJava

- java.lang.Object
    - com.ibm.ws.sca.databinding.impl.DataBindingImplJava
        - com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplJava

- All Implemented Interfaces:
JMSDataBinding, JMSObjectBinding, commonj.connector.runtime.DataBinding, java.io.Serializable

public class JMSDataBindingImplJava
extends com.ibm.ws.sca.databinding.impl.DataBindingImplJava
implements JMSObjectBinding
A JMS Data Binding implementation that serializes data object into JMS Object Message
 using Java serialization mechanism.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String $sccsid static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | $sccsid                 |
| static java.lang.String | COPYRIGHT               |

    - Fields inherited from class com.ibm.ws.sca.databinding.impl.DataBindingImplJava
fieldDataObject
    - Fields inherited from interface com.ibm.websphere.sca.jms.data.JMSDataBinding
ANY\_MESSAGE, BASE\_MESSAGE, BYTES\_MESSAGE, MAP\_MESSAGE, OBJECT\_MESSAGE, STREAM\_MESSAGE, TEXT\_MESSAGE

- Constructor Summary

Constructors 

Constructor and Description

JMSDataBindingImplJava()

- Method Summary Methods Modifier and Type Method and Description boolean equals (java.lang.Object obj) For now it suffices to check that the two bindings are of the same type. commonj.sdo.DataObject getDataObject () int getMessageType () Returns OBJECT\_MESSAGE which is the only message type supported by JMSDataBindingImplJava. java.lang.Object getObject () Returns the Object created by this DataBinding implementation (in the read method) to the runtime. java.io.Serializable getSerializableObject () Deprecated. getObject() is used instead int hashCode () Any instance of JMSDataBindingImplJava equals each other, so a constant value 37 is returned as hashCode boolean isBusinessException () Queries the DataBinding to determine whether the received message contains a fault (carried within a BusinessException). boolean isObjectType () Used by the runtime to query whether the payload received by the DataBinding is an Object or a DataObject. boolean isPrimitiveType () Deprecated. isObjectType() is used instead void read (javax.jms.Message message) Read message. void setBusinessException (boolean isBusinessException) This method is called by the runtime if the outgoing message contains a BusinessException. void setObject (java.lang.Object data) Sets the Object and changes objectType to true. void setObjectType (boolean isObject) Used by the runtime to indicate to the DataBinding that the input value to be serialized by the write method is an Object (set by setObject ) and not a DataObject (set by setDataObject ). void setPrimitiveType (boolean isPrimitiveType) Deprecated. setObjectType(boolean) is used instead void setSerializableObject (java.io.Serializable data) Deprecated. setObject(Object) is used instead void write (javax.jms.Message message) Write the DataObject into an outgoing JMS Message.

### Method Summary

| Modifier and Type      | Method and Description                                                                                                                                                                                                       |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                | equals(java.lang.Object obj) For now it suffices to check that the two bindings are of the same type.                                                                                                                        |
| commonj.sdo.DataObject | getDataObject()                                                                                                                                                                                                              |
| int                    | getMessageType() Returns OBJECT\_MESSAGE which is the only message type  supported by JMSDataBindingImplJava.                                                                                                                 |
| java.lang.Object       | getObject() Returns the Object created by this DataBinding implementation  (in the read method) to the runtime.                                                                                                              |
| java.io.Serializable   | getSerializableObject() Deprecated.  getObject() is used instead                                                                                                                                                             |
| int                    | hashCode() Any instance of JMSDataBindingImplJava equals each other, so a constant value 37  is returned as hashCode                                                                                                         |
| boolean                | isBusinessException() Queries the DataBinding to determine whether the received  message contains a fault (carried within a  BusinessException).                                                                             |
| boolean                | isObjectType() Used by the runtime to query whether the payload received by  the DataBinding is an Object or a DataObject.                                                                                                   |
| boolean                | isPrimitiveType() Deprecated.  isObjectType() is used instead                                                                                                                                                                |
| void                   | read(javax.jms.Message message) Read message.                                                                                                                                                                                |
| void                   | setBusinessException(boolean isBusinessException) This method is called by the runtime if the outgoing message  contains a BusinessException.                                                                                |
| void                   | setObject(java.lang.Object data) Sets the Object and changes objectType to true.                                                                                                                                             |
| void                   | setObjectType(boolean isObject) Used by the runtime to indicate to the DataBinding that the  input value to be serialized by the write  method is an Object (set by setObject) and not a  DataObject (set by setDataObject). |
| void                   | setPrimitiveType(boolean isPrimitiveType) Deprecated.  setObjectType(boolean) is used instead                                                                                                                                |
| void                   | setSerializableObject(java.io.Serializable data) Deprecated.  setObject(Object) is used instead                                                                                                                              |
| void                   | write(javax.jms.Message message) Write the DataObject into an outgoing JMS Message.                                                                                                                                          |

    - Methods inherited from class com.ibm.ws.sca.databinding.impl.DataBindingImplJava
getAsByteArray, setDataObject, setFromByteArray
    - Methods inherited from class java.lang.Object
clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait
    - Methods inherited from interface commonj.connector.runtime.DataBinding
setDataObject