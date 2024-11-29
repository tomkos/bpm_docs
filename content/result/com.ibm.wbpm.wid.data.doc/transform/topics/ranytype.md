<!-- image -->

# The <anyType> element

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" targetNamespace="http://AnyType">
  <xsd:complexType name="AnyType">
    <xsd:sequence>
      <xsd:element name="person" type="xsd:anyType"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" targetNamespace="http://Customer">
  <xsd:complexType name="Customer">
    <xsd:sequence>
      <xsd:element name="name" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://Employee" targetNamespace="http://Employee">
  <xsd:complexType name="Employee">
    <xsd:sequence>
      <xsd:element name="id" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

```
DataObject anyType = ...
DataObject customer = ...
DataObject employee = ...
	// Set the person to a Customer
anyType.set("person", customer);
	// The instance data will be a Customer
	// Displays "Customer"
	System.out.println(anyType.getDataObject("person").getName());
	// Set the person to an Employee
	anyType.set("person", employee);
```

<anyType> also allows for the setting of
simple type values through wrapper data objects.  These wrapper data objects
have a single Property named "value" (element) that holds the simple type
value.

The SDO APIs have been overridden to automatically wrap and unwrap
these simple types and wrapper data objects when using the get<Type>/set<Type>
APIs.  The custom code samples below will show how to create the wrapper objects
when trying to set an <anyType> in a data object.  The
wrapper classes to set the <anyType> only need to be created
when the data content being used is a simple type. Regular complex types can
be set directly on the <anyType> using the
SDO set call.

- Mapping an integer value to an <anyType> element

You can map an integer value to an <anyType> element.