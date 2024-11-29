<!-- image -->

# Duplicate business objects

## Duplicate XML schema definitions

Multiple
complexType elements that are defined in various XSD files and WSDL
files with the same name and target namespace create duplicate XML
element types. Business objects are saved in XSD files, and during
application design, they are referred to by their related XML element
type and namespace.

Imported XSD and WSDL files can contain
duplicate XML element type schema definitions. At run time, these
duplicate definitions are treated as different Java object types,
even though they are referenced by the same business object type and
namespace.

When you have duplicate business object definitions
that are defined in your application and related libraries, you might
have issues with object comparison at run time. Because interface
settings and other component settings are described by business object
types, a runtime business object instance might reference the wrong
schema definition when matching with an interface input, output, or
fault. You might see similar problems with WSDL interface operation
types. The type matching might fail, even if the two definitions are
identical in the XSD file. When the definitions are different, and
the wrong type is associated with the object, errors might occur during
serializing or deserializing between an XML data stream and a business
object.

You might not notice the duplicates if they are in another
library or module in the application, in a business level application
(BLA), or in shared libraries.

To avoid problems with duplicate
XML element types, ensure that your XSD and WSDL files from different
libraries and applications use unique target namespaces.

```
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://Arrays" xmlns:tns="http://Arrays">
	<xsd:complexType name="IDType">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="id\_type" type="xsd:int"></xsd:element>
		</xsd:sequence>
	</xsd:complexType>
```

## Duplicate business objects and the business object
programming model

- Create the business object by referencing its parent data object
when the child object is not unique.
- Ensure that the parent object is unique.
- Use the correct schemaLocation values in XSD and WSDL files when
you include and import namespaces.

Customer.xsd has an import for {http://address}Address (located
under the root/customer folder of the module)

```
BOFactory.create("http://address", "Address") 
BOType.getType("http://address", "Address")
```

```
DataObject customer = BOFactory.create("http://customer", "Customer");          
address = customer.createDataObject("address");
```

```
DataObject order = BOFactory.create("http://order", "Order");          
orderAddress = order.createDataObject("address");
```