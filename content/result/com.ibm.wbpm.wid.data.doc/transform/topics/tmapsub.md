<!-- image -->

# Mapping substitutable elements using an XML map

## Before you begin

Any top-level element can be defined as the head element
of a substitution group. Any other top-level element can then be a
member of the substitution group, and can be substituted for the head
element. The substitutable elements must either be of the same type
as the head element, or they must be derived from the head element
by extension or restriction.

Many of the industrial standard
schemas contain substitution groups. Below is a simple schema sample
with a substitution group, Publication.

```
<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema" targetNamespace="http://SubstitutionGroups/catalog" 
  xmlns:tns="http://SubstitutionGroups/catalog" elementFormDefault="qualified">

<complexType name="BookType">
  <complexContent>
    <extension base="tns:PublicationType">
      <sequence>
        <element name="isbn" type="string"/>
        <element name="publisher" type="string"/>
      </sequence>
    </extension>
  </complexContent>
</complexType>   

<complexType name="MagazineType">
  <complexContent>
    <restriction base="tns:PublicationType">
      <sequence>
        <element name="title" type="string"/>
        <element name="author" type="string"/>
        <element name="date" type="gYear"/>
      </sequence>
    </restriction>
  </complexContent>
</complexType>

 1  <element abstract="true" name="Publication" type="tns:PublicationType"/>
 2  <element name="Book" substitutionGroup="tns:Publication" type="tns:BookType"/>
 3  <element name="Magazine" substitutionGroup="tns:Publication" type="tns:MagazineType"/>
    
 4  <element name="Catalog">
      <complexType>
          <sequence>
            <element ref="tns:Publication" minOccurs="1"/>
          </sequence>
      </complexType>
    </element>  
</schema>
```

- 1  Publication is
the head element.
- 2  Book is
a substitutable element whose head element is Publication.
- 3  Magazine is
a substitutable element whose head element is also Publication.
- 4  Catalog is
a complexType that references Publication

```
<?xml version="1.0" encoding="UTF-8"?>
<tns:Catalog xmlns:tns="http://SubstitutionGroups/catalog" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://SubstitutionGroups/catalog foo.xsd ">
  <tns:Book>
    <tns:title>tns:title</tns:title>
    <tns:author>tns:author</tns:author>
    <tns:date>2001</tns:date>
    <tns:isbn>tns:isbn</tns:isbn>
    <tns:publisher>tns:publisher</tns:publisher>
  </tns:Book>
</tns:Catalog>
```

When there is a head element reference
in the content model of a source or target, all of the members of
a substitution group are available in the XML map editor. The head
element is indicated by the icon

<!-- image -->

Tip: When working with substitution
groups, switch to the Detailed view in the
upper right area of the map editor, as shown in the image above. You
will then see the substitution group elements under the heading Substitution
groups, with the head element at the top of the other
elements in the group.

- If the XML instance contains the element Book,
the mapping defined for Book gets executed.
- If the XML instance contains the element Magazine,
the mapping defined for Publication  gets executed.