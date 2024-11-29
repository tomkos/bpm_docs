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

## Interface EndpointReference

- public interface EndpointReference
Represents a WS-Addressing endpoint reference.

- =========== FIELD SUMMARY =========== ========== METHOD SUMMARY ===========
    - Field Summary

Fields 

Modifier and Type
Field and Description

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_EIS 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_GENERIC\_JMS 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_HTTP 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_JMS 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_MQ 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_MQJMS 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_NOT\_SET 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_SCA 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_SLSB 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_WEB\_SERVICE 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_1 

static com.ibm.websphere.sca.addressing.BindingType
BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_2
    - Method Summary

Methods 

Modifier and Type
Method and Description

java.lang.String
getAddress()
Returns the endpoint address.

com.ibm.websphere.sca.addressing.BindingType
getBindingType()
Returns the binding type specified with the endpoint reference.

java.lang.String
getImport()
Returns the target import set for the endpoint reference.

java.lang.String
getPort()
Returns the name of the WSDL port associated with this endpoint reference.

javax.xml.namespace.QName
getPortType()
Returns the QName of the WSDL portType associated with this endpoint reference.

commonj.sdo.Sequence
getReferenceParameters()
Returns the endpoint reference parameters..

commonj.sdo.Sequence
getReferenceProperties()
Returns the endpoint reference properties.

javax.xml.namespace.QName
getService()
Returns the QName of the WSDL service associated with this endpoint reference.

void
setAddress(java.lang.String address)
Sets the endpoint address.

void
setBindingType(com.ibm.websphere.sca.addressing.BindingType bindingType)
Specify the binding type for this endpoint reference.

void
setImport(java.lang.String importName)
Sets the target import for the endpoint reference.

void
setPort(java.lang.String name)
Sets the name of the WSDL port associated with this endpoint reference.

void
setPortType(javax.xml.namespace.QName qname)
Sets the QName of the WSDL portType associated with this endpoint reference.

void
setService(javax.xml.namespace.QName qname)
Sets the QName of the WSDL service associated with this endpoint reference.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- BINDING\_TYPE\_NOT\_SET
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_NOT\_SET

- BINDING\_TYPE\_JMS
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_JMS

- BINDING\_TYPE\_MQJMS
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_MQJMS

- BINDING\_TYPE\_GENERIC\_JMS
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_GENERIC\_JMS

- BINDING\_TYPE\_MQ
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_MQ

- BINDING\_TYPE\_WEB\_SERVICE
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_WEB\_SERVICE

- BINDING\_TYPE\_HTTP
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_HTTP

- BINDING\_TYPE\_SCA
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_SCA

- BINDING\_TYPE\_EIS
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_EIS

- BINDING\_TYPE\_SLSB
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_SLSB

- BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_1
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_1

- BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_2
static final com.ibm.websphere.sca.addressing.BindingType BINDING\_TYPE\_WEB\_SERVICE\_SOAP\_1\_2

- Method Detail

### Method Detail

    - getAddress
java.lang.String getAddress()
Returns the endpoint address.
Returns:The address.
    - setAddress
void setAddress(java.lang.String address)
Sets the endpoint address.
Parameters:address - The address.
    - getReferenceProperties
commonj.sdo.Sequence getReferenceProperties()
Returns the endpoint reference properties.
Returns:The collection of reference parameters.
    - getReferenceParameters
commonj.sdo.Sequence getReferenceParameters()
Returns the endpoint reference parameters..
Returns:The collection of reference parameters.
    - getPortType
javax.xml.namespace.QName getPortType()
Returns the QName of the WSDL portType associated with this endpoint reference.
Returns:The QName of the portType.
    - setPortType
void setPortType(javax.xml.namespace.QName qname)
Sets the QName of the WSDL portType associated with this endpoint reference.
Parameters:qname - The QName of the portType.
    - getService
javax.xml.namespace.QName getService()
Returns the QName of the WSDL service associated with this endpoint reference.
Returns:The QName of the service.
    - setService
void setService(javax.xml.namespace.QName qname)
Sets the QName of the WSDL service associated with this endpoint reference.
Parameters:qname - The QName of the service.
    - getPort
java.lang.String getPort()
Returns the name of the WSDL port associated with this endpoint reference.
Returns:The name of the port.
    - setPort
void setPort(java.lang.String name)
Sets the name of the WSDL port associated with this endpoint reference.
Parameters:name - The name of the port.
    - setBindingType
void setBindingType(com.ibm.websphere.sca.addressing.BindingType bindingType)
Specify the binding type for this endpoint reference.
  One may need to specify bindingType when protocol information 
  in the URI is ambiguous, for example a "http://..." URI can 
  be for webservice binding as well as for HTTP binding
Parameters:bindingType - The binding type of the service.
    - getBindingType
com.ibm.websphere.sca.addressing.BindingType getBindingType()
Returns the binding type specified with the endpoint reference.
Returns:The bindng type.
    - setImport
void setImport(java.lang.String importName)
Sets the target import for the endpoint reference.
Parameters:importName - The target import name.
    - getImport
java.lang.String getImport()
Returns the target import set for the endpoint reference.
Returns:target import name