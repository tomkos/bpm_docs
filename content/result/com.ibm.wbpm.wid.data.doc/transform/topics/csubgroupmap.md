<!-- image -->

# Substitution group mappings

All elements in the substitution group (the head element and the
substituted elements) must be declared as global elements.  The type
of the substitutable elements must be the same as, or derived from,
the type of the head element. If the type of the substituted element
is the same as the type of the head element you will not have to specify
the type of the substitutable element.

## Alias patterns

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" targetNamespace="http://NameSubstitution" xmlns:p="http://NameSubstitution">

  <xsd:element name="name" type="xsd:string"/>
  <xsd:element name="navn" substitutionGroup="p:name"/>
  <xsd:element name="nombre" substitutionGroup="p:name"/>

  <xsd:complexType name="NameSubstitution">
    <xsd:sequence>
      <xsd:element ref="p:name"/>
	</xsd:sequence>
  </xsd:complexType>
  
</xsd:schema>
```

```
DataObject dobj = ...
	 
	dobj.setString("name", "foo");
	dobj.setString("navn", "foo1");
	dobj.setString("name", "foo2");

	// result should contain foo, foo1 and foo2
result = dobj.get("name");
// result should contain foo1 only 
	result = dobj.get("navn");
	// result should contain foo2 only
	result = dobj.get("nombre");
```

<!-- image -->

```
?xml version="1.0"?>
	<schema xmlns="http://www.w3.org/2001/XMLSchema"  targetNamespace=http://MapTests
	  xmlns:ii="http://MapTests">
	<element name="Library">
	<complexType>
		<sequence>
			<element ref="ii:Publication" maxOccurs="unbounded"/
		</sequence>
	</complexType>
	</element>
	<!--Here is a <complexType> "publication" with 2 derived types:
	"book"     - derived by extension
	"magazine" - derived by restriction
	-->
	<complexType name="publication">
	<sequence>
		<element name="Title" type="string"/>
		<element name="Author" type="string" minOccurs="0"/>
		<element ref="ii:Description"/>
	</sequence>
	</complexType>
	<complexType name="book">
	<complexContent>
		<extension base="ii:publication">
			<attribute name="Section" type="string" use="required"/>
		</extension>
	</complexContent>
	</complexType>
	
	
	<complexType name="magazine">
	<complexContent>
		<restriction base="ii:publication"
			<sequence>
				<element name="Title" type="string"/>
				<element name="Author" type="string" minOccurs="0" maxOccurs="01"/>			<element ref="ii:Description"/>			</sequence>
			</restriction>
	</complexContent>
	</complexType>

	<element name="Publication" type="ii:publication"/>
	<element name="Book"        type="ii:book"     substitutionGroup="ii:Publication"/>
	<element name="Magazine"    type="ii:magazine" substitutionGroup="ii:Publication"/>
	
	<!--Here is a <simpleType> "desc" with 2 derived types:"shortDesc"   - <simpleType> derived by restriction
	"foreignDesc" - <complexType> derived by extension
	<simpleType name="desc">
	<restriction base="string">
		<minLength value="1"/>
	</restriction>
	</simpleType>
	<simpleType name="shortDesc">
	<restriction base="ii:desc">
		<maxLength value="30"/>
	</restriction>
	</simpleType>
	
	
	<complexType name="foreignDesc">
	<simpleContent>
		<extension base="ii:desc">
			<attribute name="Language" type="string" use="required"/>
	</extension>
	</simpleContent>
	</complexType>
	
	
	<element name="Description" type="ii:desc"/>
	<element name="ShortDesc"   type="ii:shortDesc"  substitutionGroup="ii:Description"/><element name="ForeignDesc" type="ii:foreignDesc" substitutionGroup="ii:Description"/>
	</schema>
```

<!-- image -->

<!-- image -->