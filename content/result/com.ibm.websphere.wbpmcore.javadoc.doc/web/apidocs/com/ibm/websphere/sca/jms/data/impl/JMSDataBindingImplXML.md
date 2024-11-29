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

## Class JMSDataBindingImplXML

- java.lang.Object
    - com.ibm.ws.sca.databinding.impl.DataBindingImplXML
        - com.ibm.websphere.sca.jms.data.impl.JMSDataBindingImplXML

- All Implemented Interfaces:
JMSDataBinding, JMSDataBindingXML, com.ibm.wsspi.sca.jms.data.JMSDataBindingNativeBytes, commonj.connector.runtime.BindingContext, commonj.connector.runtime.DataBinding, java.io.Serializable

public class JMSDataBindingImplXML
extends com.ibm.ws.sca.databinding.impl.DataBindingImplXML
implements JMSDataBinding, commonj.connector.runtime.BindingContext, JMSDataBindingXML, com.ibm.wsspi.sca.jms.data.JMSDataBindingNativeBytes
JMS Data Binding that converts between SDO and its String XML representation.
See Also:Serialized Form

- =========== FIELD SUMMARY =========== ======== CONSTRUCTOR SUMMARY ======== ========== METHOD SUMMARY ===========
    - Field Summary Fields Modifier and Type Field and Description static java.lang.String $sccsid static java.lang.String COPYRIGHT

### Field Summary

| Modifier and Type       | Field and Description   |
|-------------------------|-------------------------|
| static java.lang.String | $sccsid                 |
| static java.lang.String | COPYRIGHT               |

    - Fields inherited from class com.ibm.ws.sca.databinding.impl.DataBindingImplXML
fieldDataObject
    - Fields inherited from interface com.ibm.websphere.sca.jms.data.JMSDataBinding
ANY\_MESSAGE, BASE\_MESSAGE, BYTES\_MESSAGE, MAP\_MESSAGE, OBJECT\_MESSAGE, STREAM\_MESSAGE, TEXT\_MESSAGE
    - Fields inherited from interface commonj.connector.runtime.BindingContext
BINDING\_COMMUNICATION, BINDING\_COMMUNICATION\_INBOUND, BINDING\_COMMUNICATION\_OUTBOUND, BINDING\_CONFIGURATION, BINDING\_INVOCATION, BINDING\_INVOCATION\_FAULT, BINDING\_INVOCATION\_REQUEST, BINDING\_INVOCATION\_RESPONSE, BINDING\_NAME, BINDING\_REGISTRY, BINDING\_TYPE, BINDING\_TYPE\_EIS, BINDING\_TYPE\_HTTP, BINDING\_TYPE\_JMS, EXPECTED\_TYPE, INTERACTION\_SPEC

- Constructor Summary

Constructors 

Constructor and Description

JMSDataBindingImplXML()

- Method Summary Methods Modifier and Type Method and Description boolean equals (java.lang.Object obj) Check if two JMSDataBindingImplXML's are equal. commonj.sdo.DataObject getDataObject () int getMessageType () Return the Text Message type int hashCode () Any instance of JMSDataBindingImplXML equals each other, so a constant value 31 is returned as hashCode boolean isBusinessException () Queries the DataBinding to determine whether the received message contains a fault (carried within a BusinessException). boolean outputWrappedXML () Used by the runtime to determine whether a doc-lit wrapped input type should be unwrapped before passing it to the data binding, and whether to doc-lit wrap the output type. void read (byte[] nativeBytes, boolean isBusinessException) void read (javax.jms.Message message) Read the contents of the incoming JMS Message into a DataObject. void setBindingContext (java.util.Map bindingContext) This method is used to set a BindingContext map into the data binding. void setBusinessException (boolean isBusinessException) This method is called by the runtime if the outgoing message contains a BusinessException. void write (javax.jms.Message message) Write the DataObject into an outgoing JMS Message.

### Method Summary

| Modifier and Type      | Method and Description                                                                                                                                                                             |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| boolean                | equals(java.lang.Object obj) Check if two JMSDataBindingImplXML's are equal.                                                                                                                       |
| commonj.sdo.DataObject | getDataObject()                                                                                                                                                                                    |
| int                    | getMessageType() Return the Text Message type                                                                                                                                                      |
| int                    | hashCode() Any instance of JMSDataBindingImplXML equals each other, so a constant value 31   is returned as hashCode                                                                               |
| boolean                | isBusinessException() Queries the DataBinding to determine whether the received  message contains a fault (carried within a  BusinessException).                                                   |
| boolean                | outputWrappedXML() Used by the runtime to determine whether a doc-lit wrapped input type  should be unwrapped before passing it to the data binding, and  whether to doc-lit wrap the output type. |
| void                   | read(byte[] nativeBytes,     boolean isBusinessException)                                                                                                                                          |
| void                   | read(javax.jms.Message message) Read the contents of the incoming JMS Message into a  DataObject.                                                                                                  |
| void                   | setBindingContext(java.util.Map bindingContext) This method is used to set a BindingContext map into the data binding.                                                                             |
| void                   | setBusinessException(boolean isBusinessException) This method is called by the runtime if the outgoing message  contains a BusinessException.                                                      |
| void                   | write(javax.jms.Message message) Write the DataObject into an outgoing JMS Message.                                                                                                                |

    - Methods inherited from class com.ibm.ws.sca.databinding.impl.DataBindingImplXML
getAsByteArray, getAsString, read, setDataObject, setEncoding, setFromByteArray, setFromString, write
    - Methods inherited from class java.lang.Object
clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait
    - Methods inherited from interface commonj.connector.runtime.DataBinding
setDataObject