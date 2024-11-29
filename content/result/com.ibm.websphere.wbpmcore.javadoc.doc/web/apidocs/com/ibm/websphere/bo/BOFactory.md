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

## Interface BOFactory

- public interface BOFactory The BOFactory interface represents the client programming model interface for the BOFactory service. The BOFactory service provides the ability to create business objects and business documents that are represented in memory by the commonj.sdo.DataObject and com.ibm.websphere.bo.BOXMLDocument objects. DataObjects are defined by the Service Data Object specification and represent a dynamically typed in memory object containing properties. The BOFactory service supports the creation of a DataObject whose type information can be modeled in several different forms, including the following: Note: The createByClass operation is not supported in the initial product release.

```
public interface BOFactory
```

DataObjects are defined by the Service Data Object specification and
 represent a dynamically typed in memory object containing properties. The
 BOFactory service supports the creation of a DataObject whose type
 information can be modeled in several different forms, including the
 following:
 
 
as an XML Schema complex type definition,
 as an XML Schema global element definition,
 as a Java interface,
 and as a WSDL message.
 
 
 Note: The createByClass operation is not supported in the initial product
 release.

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

commonj.sdo.DataObject
create(java.lang.String targetNamespace,
      java.lang.String complexTypeName)
Creates a DataObject from an XML Schema complex type definition.

commonj.sdo.DataObject
createByClass(java.lang.Class iterfaceClass)
Deprecated. 
This method is going to be removed.

commonj.sdo.DataObject
createByElement(java.lang.String targetNamespace,
               java.lang.String globalElementName)
Creates a DataObject from an XML Schema global element definition.

commonj.sdo.DataObject
createByMessage(java.lang.String targetNamespace,
               java.lang.String messageName)
Creates a DataObject from a WSDL message definition.

commonj.sdo.DataObject
createByType(commonj.sdo.Type type)
Creates a DataObject from a commonj.sdo.Type.

commonj.sdo.DataObject
createDataTypeWrapper(commonj.sdo.Type dataType,
                     java.lang.Object value)
Creates a DataObject wrapper for a simple data type.

BOXMLDocument
createXMLDocument(java.lang.String targetNamespace,
                 java.lang.String globalElementName)
Creates a BOXMLDocument from an XML Schema global element definition.

- ============ FIELD DETAIL =========== ============ METHOD DETAIL ==========
    - Field Detail

### Field Detail

- COPYRIGHT
static final java.lang.String COPYRIGHT
See Also:Constant Field Values

- Method Detail

### Method Detail

    - create
commonj.sdo.DataObject create(java.lang.String targetNamespace,
                            java.lang.String complexTypeName)
Creates a DataObject from an XML Schema complex type definition.
 

 BOFactory boFactory = (BOFactory) new ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");

 DataObject customer = boFactory.create("http://www.ibm.com/Customer", "CustomerType");

Parameters:targetNamespace - The target namespace of the complex type definition. Can be
            null to represent the null target namespace.complexTypeName - The name of the complex type.
Returns:The created DataObject
    - createByElement
commonj.sdo.DataObject createByElement(java.lang.String targetNamespace,
                                     java.lang.String globalElementName)
Creates a DataObject from an XML Schema global element definition.
 

 BOFactory boFactory = (BOFactory) new ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");

 DataObject customer = boFactory.createByElement("http://www.ibm.com/Customer", "customer");

Parameters:targetNamespace - The target namespace of the complex type definition. Can be
            null to represent the null target namespace.globalElementName - The name of the global element.
Returns:The created DataObject
    - createByType
commonj.sdo.DataObject createByType(commonj.sdo.Type type)
Creates a DataObject from a commonj.sdo.Type. The Type can be created
 using the BOType service.
 

 BOFactory boFactory = (BOFactory) new ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");

 BOType boType = (BOType) new ServiceManager().locateService("com/ibm/websphere/bo/BOType");

 Type customerType = boType.create("http://www.ibm.com/Customer", "CustomerType");

 DataObject customer = boFactory.createFromType(customerType);

Parameters:type - The Type object representing the type information of the
            Business Object.
Returns:The created DataObject
    - createByClass
commonj.sdo.DataObject createByClass(java.lang.Class iterfaceClass)
Deprecated. This method is going to be removed.
Creates a DataObject from a Java class name.
 

 BOFactory boFactory = (BOFactory) new ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");

 DataObject customer = boFactory.create(com.ibm.com.Customer.class);

Parameters:iterfaceClass - The Java class that represents the interface
Returns:The created DataObject
    - createByMessage
commonj.sdo.DataObject createByMessage(java.lang.String targetNamespace,
                                     java.lang.String messageName)
Creates a DataObject from a WSDL message definition.
 

 BOFactory boFactory = (BOFactory) new ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");

 DataObject customer = boFactory.createByMessage("http://www.ibm.com/Customer", "customer");

Parameters:targetNamespace - The target namespace of the message definition. Can be null to
            represent the null target namespace.messageName - The name of the WSDL message
Returns:The created DataObject
    - createXMLDocument
BOXMLDocument createXMLDocument(java.lang.String targetNamespace,
                              java.lang.String globalElementName)
Creates a BOXMLDocument from an XML Schema global element definition.
 

 BOFactory boFactory = (BOFactory) new ServiceManager().locateService("com/ibm/websphere/bo/BOFactory");

 BOXMLDocument customerDocument = boFactory.createXMLDocument("http://www.ibm.com/Customer", "customer");

Parameters:targetNamespace - The target namespace of the message definition. Can be null to
            represent the null target namespace.globalElementName - The name of the global element definition
Returns:The DataObject created.
    - createDataTypeWrapper
commonj.sdo.DataObject createDataTypeWrapper(commonj.sdo.Type dataType,
                                           java.lang.Object value)
Creates a DataObject wrapper for a simple data type.
The main use case for wrappers is setting simple-typed values for
 xsd:anyType properties. Wrappers can also be used to set
 values of derived types into properties of the base type in order to
 produce xsi:type annotations in the serialized XML. For
 example, a wrapper can be used to set an xsd:token value
 into an xsd:anySimpleType property.
The returned DataObject has a single property named value
 at index 0, which contains the wrapped value. If the value parameter
 is not an instance of the data type's instance class, the implementation
 will attempt to convert it to a value of the instance class.
The type information of the returned DataObject is not specified
 beyond the value property. Use BOType.isDataTypeWrapper(DataObject)
 to determine whether a given DataObject is a wrapper.

 BOFactory boFactory = (BOFactory) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOFactory");

 BOType boType = (BOType) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOType");

 
 Type stringType = boType.getType("http://www.w3.org/2001/XMLSchema", "string");

 DataObject stringType = boFactory.createDataTypeWrapper(stringType, "foo");

Parameters:dataType - The type of the value object to create a wrapper for.value - The value that will be wrapped by the DataObject
Returns:The created DataObject