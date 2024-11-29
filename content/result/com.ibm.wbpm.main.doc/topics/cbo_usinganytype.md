<!-- image -->

# Using AnyType for complex types

The only differences between anyType and other complex types are in which instance data can be
mapped to or from the field and how this instance data is serialized. Complex types are limited to a
single type: Customer, Address, and so on. The anyType, however, allows any DataObject regardless of
type. If maxOccurs > 1, then each DataObject in the list can of a different type.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	targetNamespace="http://AnyType">
  <xsd:complexType name="AnyType">
    <xsd:sequence>
      <xsd:element name="person" type="xsd:anyType"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>

<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	targetNamespace="http://Customer">
  <xsd:complexType name="Customer">
    <xsd:sequence>
      <xsd:element name="name" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>

<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	xmlns:tns="http://Employee" targetNamespace="http://Employee">
  <xsd:complexType name="Employee">
    <xsd:sequence>
      <xsd:element name="id" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>

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

	// The instance data will be an Employee
	// Displays "Employee"
	System.out.println(anyType.getDataObject("person").getName());
```

Just like anySimpleType, anyType uses xsi:type during serialization to assure that the intended
type of DataObject is maintained when deserialized. When you set to "Customer," the XML would look
like:

```
<?xml version="1.0" encoding="UTF-8"?>
<p:AnyType xsi:type="p:AnyType"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	  xmlns:customer="http://Customer"
    xmlns:p="http://AnyType">
  <person xsi:type="customer:Customer">
    <name>foo</name>
  </person>
</p:AnyType>
```

And when set to "Employee":

```
<?xml version="1.0" encoding="UTF-8"?>
<p:AnyType xsi:type="p:AnyType"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	  xmlns:employee="http://Employee"
    xmlns:p="http://AnyType">
  <person xsi:type="employee:Employee">
    <id>foo</id>
  </person>
</p:AnyType>
```

AnyType also allows for the setting of simple type values through wrapper DataObjects. These
wrapper DataObjects have a single property named "value" (element) that holds the simple type value.
The business object API have been overridden to automatically wrap and unwrap these simple
types and wrapper DataObjects when using the get<Type>/set<Type> APIs. The non-type
casting get/set APIs will not perform this wrapping.

```
DataObject anyType = ...

	// Calling a set<Type> API on an anyType Property causes automatic
	// creation of a wrapper DataObject
	anyType.setString("person", "foo");

	// The regular get/set APIs are not overridden, so they will return
	// the wrapper DataObject
	DataObject wrapped = anyType.get("person");

	// The wrapped DataObject will have the "value" Property
	// Displays "foo"
	System.out.println(wrapped.getString("value"));

	// The get<Type> API will automatically unwrap the DataObject
	// Displays "foo"
	System.out.println(anyType.getString("person"));
```

When the wrapper DataObject is serialized, it will be serialized just like anySimpleType mapping
of Java™
instance classes to XSD types in the xsi:type field. So this setting would serialize as:

```
<?xml version="1.0" encoding="UTF-8"?>
<p:AnyType xsi:type="p:AnyType"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
 xmlns:xsd=" http://www.w3.org/2001/XMLSchema"
 xmlns:p="http://AnyType">
  <person xsi:type="xsd:string">foo</person>
</p:AnyType>
```

If no xsi:type is given or if an incorrect xsi:type is given, then an exception will be thrown.
In addition to automatic wrapping, the wrapper can be manually created for use with the set() API
through BOFactory createDataTypeWrapper(Type, Object), where Type is the SDO simple type of the data
to be wrapped and Object is the data to be wrapped.

```
Type stringType = boType.getType("http://www.w3.org/2001/XMLSchema", "string");
	DataObject stringType = boFactory.createByMessage(stringType, "foo");
```

To determine if a DataObject is a wrapper type, the BOType isDataTypeWrapper(Type) can be
called.

```
DataObject stringType = ...
	boolean isWrapper = boType.isDataTypeWrapper(stringType.getType());
```

For the other complex types, in order to move data from one field to another, the data must be of
the same type. AnyType can contain any complex types, however, so a direct move with no mapping
might not be possible, based on the instance data in the field.

You can use the property Type URI and Name to determine if a property is of type anyType. They
will be "commonj.sdo" and "DataObject". All data is valid to be inserted into an anyType. This leads
to the following mapping rules:

- anyType can always map to anyType.
- any complex type can always map to anyType.
- any simple type can always map to anyType.
- anyType might be able to map to any of the other simple or complex types, depending on
its value in the business object instance. The mapping cannot be determined at design time;
it is determined at run time.