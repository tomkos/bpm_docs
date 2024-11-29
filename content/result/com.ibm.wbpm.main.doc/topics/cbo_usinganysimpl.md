<!-- image -->

# Using AnySimpleType for simple types

The only differences between anySimpleType and the other simple types are in which instance data
can be mapped to or from the field and how this instance data is serialized.

If a string type were to have a set(...) method called on it, the data would first be converted
to a string, and the original data type would be lost:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	targetNamespace="http://StringType">
  <xsd:complexType name="StringType">
    <xsd:sequence>
      <xsd:element name="foo" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>

	DataObject stringType = ...

	// Set the data to a String
	stringType.set("foo", "bar");

	// The instance data will always be type String, regardless of the data set
	// Displays "java.lang.String"
	System.out.println(stringType.get("foo").getClass().getName());

	// Set the data to an Integer
	stringType.set("foo", new Integer(42));

	// The instance data will always be type String, regardless of the data set
	// Displays "java.lang.String"
	System.out.println(stringType.get("foo").getClass().getName());
```

If anySimpleType were to have a set(...) method called on it, the original data would not be
lost.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	targetNamespace="http://AnySimpleType">
  <xsd:complexType name="AnySimpleType">
    <xsd:sequence>
      <xsd:element name="foo" type="xsd:anySimpleType"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>

	DataObject anySimpleType = ...

	// Set the data to a String
	anySimpleType.set("foo", "bar");

	// The instance data will always be of the type of data used in the set
	// Displays "java.lang.String"
	System.out.println(anySimpleType.get("foo").getClass().getName());

	// Set the data to an Integer
	anySimpleType.set("foo", new Integer(42));

	// The instance data will always be of the type of data used in the set
	// Displays "java.lang.Integer"
	System.out.println(anySimpleType.get("foo").getClass().getName());
```

This data type is also preserved across serialization and deserialization by xsi:type.
Consequently, any time you serialize an anySimpleType element, it will have an xsi:type that matches
that defined in the SDO specification based on its Java™ type:

In the following example, you serialize the business object so that the data would look like
this:

```
<?xml version="1.0" encoding="UTF-8"?>
<p:StringType xsi:type="p:StringType"
 xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance
 xmlns:xsd=http://www.w3.org/2001/XMLSchema 
 xmlns:p="http://StringType">
  <foo xsi:type="xsd:int">42</foo>
<p:StringType></p:StringType>
```

The xsi:type will be used during deserialization to load the data as the appropriate Java instance
class. If no xsi:type is specified, the default deserialization type will be string.

For the other simple types, determining how the data can be mapped is a constant. For
instance, a boolean can always map to a string. AnySimpleType can contain any of the simple types,
however, so whether a mapping is possible is based on the instance data in the field.

Use the property Type URI and Name to determine if a property is of type anySimpleType. They will
be commonj.sdo and Object. To determine if data is valid to be inserted into
anySimpleType, check to see if it is not an instance of a DataObject. Data that can be
represented as a string and that is not a DataObject can be set in an anySimpleType field.

This leads to the following mapping rules:

- anySimpleType can always map to anySimpleType.
- any other simple type can always map to anySimpleType.
- anySimpleType can always map to string because all simple types must be able to be converted
into a string.
- anySimpleType might be able to map to any of the other simple types, depending on its
value in the business object. The mapping cannot be determined at design time; it is
determined at run time.