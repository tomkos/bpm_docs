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

## Interface BOType

- public interface BOType The BOType interface represents the client programming model interface for the BOType service. The BOType service provides the ability to create the types for business objects that are represented in memory by the commonj.sdo.Type object. DataObjects are defined by the Service Data Object specification and represent a dynamically typed in memory object containing properties. The BOType service supports the creation of a Type object from a Business Object that can be modeled in several different forms, including the following: Note: The getTypeByClass operation is not supported in the initial product release.

```
public interface BOType
```

DataObjects are defined by the Service Data Object specification and
 represent a dynamically typed in memory object containing properties.
 The BOType service supports the creation of a Type object from a 
 Business Object that can be modeled in several different forms,
 including the following:
 
 
as an XML Schema complex type definition,
 as an XML Schema global element definition,
 as a Java interface,
 and as a WSDL message.
 

 Note: The getTypeByClass operation is not supported in the initial
 product release.

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

commonj.sdo.Type
getType(java.lang.String targetNamespace,
       java.lang.String complexTypeName)
Returns the Type associated with the XML Schema complex type
 definition.

commonj.sdo.Type
getTypeByClass(java.lang.Class className)
Deprecated. 
This method is going to be removed.

commonj.sdo.Type
getTypeByElement(java.lang.String targetNamespace,
                java.lang.String globalElementName)
Returns the Type associated with the XML Schema global element
 definition.

commonj.sdo.Type
getTypeByMessage(java.lang.String targetNamespace,
                java.lang.String messageName)
Returns the Type associated with the WSDL message definition.

boolean
isContainmentType(commonj.sdo.Type type)
Returns true if the Type is a complex type or anyType,
 or false if the Type is a simple type or an anySimpleType.

boolean
isDataTypeWrapper(commonj.sdo.DataObject dataObject)
Returns true if the DataObject is a wrapper for a simple type
 or false if the DataObject is not.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - getType
commonj.sdo.Type getType(java.lang.String targetNamespace,
                       java.lang.String complexTypeName)
Returns the Type associated with the XML Schema complex type
 definition.

 BOType boType = (BOType) new ServiceManager().locateService("com/ibm/websphere/bo/BOType");

 Type customerType = boType.getType("http://www.ibm.com/Customer", "CustomerType");

Parameters:targetNamespace - The target namespace of the complex type definition.  Can be
 null to represent the null target namespace.complexTypeName - The name of the complex type.
Returns:The created Type
    - getTypeByElement
commonj.sdo.Type getTypeByElement(java.lang.String targetNamespace,
                                java.lang.String globalElementName)
Returns the Type associated with the XML Schema global element
 definition.

 BOType boType = (BOType) new ServiceManager().locateService("com/ibm/websphere/bo/BOType");

 Type customerType = boType.getTypeByElement("http://www.ibm.com/Customer", "customer");

Parameters:targetNamespace - The target namespace of the complex type definition.  Can be
 null to represent the null target namespace.globalElementName - The name of the global element.
Returns:The created Type
    - getTypeByClass
commonj.sdo.Type getTypeByClass(java.lang.Class className)
Deprecated. This method is going to be removed.
Returns the Type associated with the Java class name.

 BOType boType = (BOType) new ServiceManager().locateService("com/ibm/websphere/bo/BOType");

 DataObject customerType = boType.createTypeByClass(com.ibm.com.Customer.class);

Parameters:iterfaceClass - The Java class that represents the interface
Returns:The created Type
    - getTypeByMessage
commonj.sdo.Type getTypeByMessage(java.lang.String targetNamespace,
                                java.lang.String messageName)
Returns the Type associated with the WSDL message definition.

 BOType boType = (BOType) new ServiceManager().locateService("com/ibm/websphere/bo/BOType");

 Type customerType = boType.createTypeByMessage("http://www.ibm.com/Customer", "customer");

Parameters:targetNamespace - The target namespace of the message definition.  Can be
 null to represent the null target namespace.messageName - The name of the WSDL message
Returns:The created Type
    - isContainmentType
boolean isContainmentType(commonj.sdo.Type type)
Returns true if the Type is a complex type or anyType,
 or false if the Type is a simple type or an anySimpleType.
 
 
 BOType boType = (BOType) new ServiceManager().locateService("com/ibm/websphere/bo/BOType");

 boolean isContaimentType = boType.isContainmentType(myType);

Returns:
    - isDataTypeWrapper
boolean isDataTypeWrapper(commonj.sdo.DataObject dataObject)
Returns true if the DataObject is a wrapper for a simple type
 or false if the DataObject is not.
 
 
 BOType boType = (BOType) new ServiceManager().locateService("com/ibm/websphere/bo/BOType");

 boolean isDataTypeWrapper = boType.isDataTypeWrapper(myDataObject);

Returns: