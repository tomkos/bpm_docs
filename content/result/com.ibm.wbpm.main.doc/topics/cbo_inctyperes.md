<!-- image -->

# Differentiating identically named properties

Address1.xsd:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:complexType name="Address">
    <xsd:sequence>
      <xsd:element minOccurs="0" name="city" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>

Address2.xsd:
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <xsd:complexType name="Address">
    <xsd:sequence>
      <xsd:element minOccurs="0" name="state" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

Business objects do not support duplicate names for any global XSD structures (such as
complexType, simpleType, element, attribute, and so on) through the BOFactory.create() APIs. These
duplicate global structures can still be created as the child to other structures if the proper APIs
are used, as shown in the following examples

Customer1.xsd:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 xmlns:tns="http://Customer1"
 targetNamespace="http://Customer1">
  <xsd:import schemaLocation="./Address1.xsd"/>
  <xsd:complexType name="Customer">
    <xsd:sequence>
      <xsd:element minOccurs="0" name="address" type="Address"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

Customer2.xsd:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 xmlns:tns="http://Customer2"
 targetNamespace="http://Customer2">
  <xsd:import schemaLocation="./Address2.xsd"/>
  <xsd:complexType name="Customer">
    <xsd:sequence>
      <xsd:element minOccurs="0" name="address" type="Address"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

When populating both of the Customer address fields and then calling BOFactory.create() to make
the Address, the resulting child business object types can be incorrectly set. You can avoid this by
calling the createDataObject(address) API on the Customer DataObject. This will be guaranteed
to produce a child of the correct type because business objects will follow the import's
schemaLocation.

```
DataObject customer1 = ...

	// Incorrect way to create Address child
	// This may create a type of Address1.xsd Address or maybe Address2.xsd Address
	DataObject incorrect = boFactory.create("", "Address");
	customer1.set("address", incorrect);

	// Correct way to create Address child
	// This is guaranteed to create a type of Address1.xsd Address
	customer1.createDataObject("address");
```