<!-- image -->

# Business objects and XML Schema definitions (XSDs)

This topic uses the example of a basic XSD to show the relationship
between a business object and an XSD. For detailed information, see Supported XSD and WSDL artifacts.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	targetNamespace="http://Arrays" xmlns:tns="http://Arrays">
	<xsd:complexType name="IDType">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="id\_type" type="xsd:int"></xsd:element>
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="NameType">
		<xsd:sequence>
			<xsd:element minOccurs="0" name="name\_type" type="xsd:string">
			</xsd:element>
		</xsd:sequence>
	</xsd:complexType>
	<xsd:complexType name="EmployeeType">
		<xsd:sequence>
			<xsd:element name="id" type="tns:IDType" maxOccurs="unbounded" />
			<xsd:element name="name" type="tns:NameType" maxOccurs="unbounded" />
		</xsd:sequence>
	</xsd:complexType>
</xsd:schema>
```

When the above XSD is imported or saved in the XML Schema editor,
three business objects are created, one for each complexType defined
in the XSD. The business objects are created in the Data
Types  category in the Business Integration view.

A field is created for each element in the business object. EmployeeType has
two fields, id  of type IDType,
and name of type NameType .

The attributes of each element are shown in the Properties view
of the field. The Properties view of field id shows
that the field is an array, as indicated by the maxOccurs="unbounded"
attribute in the XSD.

<!-- image -->