<!-- image -->

# Substitution groups

Any top-level element can be defined as the head element of a substitution
group. Any other top-level element can then be a member of the substitution
group, and can be substituted for the head element. The substitutable
elements must either be of the same type as the head element, or they
must be derived from the head element.

- 1  StoreName is
a substitutable element whose head element is Name.
- 2  Book is
a substitutable element whose head element is Publication.
- 3  Magazine is
a substitutable element whose head element is also Publication.
- 4  BookStore is
a an element that contains Name and Publication..

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
	targetNamespace="http://SubstitutionGroups"
	xmlns:tns="http://SubstitutionGroups">
	
	<!-- ELEMENT DECLARATIONS -->
	
	<xsd:element name="Name" type="xsd:string" />
	 1 <xsd:element name="StoreName" substitutionGroup="tns:Name" type="tns:MyString" />
	
	<xsd:element name="Publication" type="tns:PublicationType" />
 2 	<xsd:element name="Book" substitutionGroup="tns:Publication" type="tns:BookType" />
 3 	<xsd:element name="Magazine" substitutionGroup="tns:Publication" type="tns:MagazineType" />
		
 4 		<xsd:element name="BookStore">
		<xsd:complexType>
			<xsd:sequence>
				<xsd:element ref="tns:Name" />
				<xsd:element ref="tns:Publication" maxOccurs="unbounded" />
			</xsd:sequence>
		</xsd:complexType>
	</xsd:element>
	
	<xsd:element name="LiteratureStore" substitutionGroup="tns:BookStore" />
	
	

	<!--  TYPE DEFINITIONS -->
	
	<xsd:simpleType name="MyString">
		<xsd:restriction base="xsd:string">
			<xsd:minLength value="3"></xsd:minLength>
			<xsd:maxLength value="10"></xsd:maxLength>
		</xsd:restriction>
	</xsd:simpleType>
	
	<xsd:complexType name="PublicationType">
		<xsd:sequence>
			<xsd:element name="Title" type="xsd:string" />
			<xsd:element name="Author" type="xsd:string" minOccurs="0"
				maxOccurs="unbounded" />
			<xsd:element name="Date" type="xsd:gYear" />
		</xsd:sequence>
	</xsd:complexType>
	
	<xsd:complexType name="BookType">
		<xsd:complexContent>
			<xsd:extension base="tns:PublicationType">
				<xsd:sequence>
					<xsd:element name="ISBN" type="xsd:string" />
					<xsd:element name="Publisher" type="xsd:string" />
				</xsd:sequence>
			</xsd:extension>
		</xsd:complexContent>
	</xsd:complexType>
	
	<xsd:complexType name="MagazineType">
		<xsd:complexContent>
			<xsd:restriction base="tns:PublicationType">
				<xsd:sequence>
					<xsd:element name="Title" type="xsd:string" />
					<xsd:element name="Date" type="xsd:gYear" />
				</xsd:sequence>
			</xsd:restriction>
		</xsd:complexContent>
	</xsd:complexType>

</xsd:schema>
```

<!-- image -->

Note that all the elements that are part of the substitution group
appear under substitution group in the business object editor.
If you click the substitution group, the properties view shows you
the head element of the group. You can map each substitutable element
by creating an XML map or a business object map.

You cannot map substitution group in the editor, and you
cannot create a substitution group in the business object editor.