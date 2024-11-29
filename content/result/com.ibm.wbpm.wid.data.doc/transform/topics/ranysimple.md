<!-- image -->

# The <anySimpleType> element

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" targetNamespace="http://AnySimpleType">
  <xsd:complexType name="AnySimpleType">
    <xsd:sequence>
      <xsd:element name="foo" type="xsd:anySimpleType"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

```
DataObject anySimpleType = ...
	// Set the data to a String
	stringType.set("foo", "bar");
	// The instance data will always be of the type of date used in the set
	// Displays "java.lang.String"
```