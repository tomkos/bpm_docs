<!-- image -->

# The <any> element

```
<xs:element name="person">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="firstname" type="xs:string"/>
      <xs:element name="lastname" type="xs:string"/>
      <xs:any minOccurs="0"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
targetNamespace="http://www.w3schools.com"
xmlns="http://www.w3schools.com"
elementFormDefault="qualified">
<xs:element name="children">
  <xs:complexType>
    <xs:sequence>
      <xs:element name="childname" type="xs:string"
      maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
</xs:element>
</xs:schema>
```

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<persons xmlns="http://www.microsoft.com"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:SchemaLocation="http://www.microsoft.com family.xsd
http://www.w3schools.com children.xsd">
<person>
<firstname>Hege</firstname>
<lastname>Refsnes</lastname>
<children>
  <childname>Cecilie</childname>
</children>
</person>
<person>
<firstname>Stale</firstname>
<lastname>Refsnes</lastname>
</person>
</persons>
```

The XML file above is valid because the schema "family.xsd"
extends the "person" element with an optional element after
the "lastname" element.

From an SDO perspective, an
occurrence of the <any> tag makes the DataObject
Type isOpen() method and the isSequenced() method
return true.  If maxOccurs > 1 on an <any> tag,
it has no effect on the structure of the data object, it is only used as information
during validation of the data object.  Likewise, the occurrence
of multiple <any> tags in a type does not change the structure
of the data object, they will merely be used for validating the location of
open data that was set.

- Creating custom maps using <any> elements

You can use custom code snippets for setting the target business object that contain <any> elements.