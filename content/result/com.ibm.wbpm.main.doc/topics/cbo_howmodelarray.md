<!-- image -->

# How do I work with a model group array?

Since model groups are flattened and not expressed in a DataObject, the properties inside of the
model group become multiple cardinality properties so that their isMany() methods return true if
they are not already true. Their minOccurs and maxOccurs facets become multiplied by that of the
containing model group. Choice will multiply the maxOccurs facet in the same way as the other model
groups, but will always use 0 as the multiplication value for minOccurs because any data in a choice
may not be selected.

For example, the following XSD has a model group array:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
		targetNamespace="http://ModelGroupArray">
  <xsd:complexType name="ModelGroupArray">
    <xsd:sequence minOccurs="2" maxOccurs="5">
      <xsd:element name="element1" type="xsd:string"/>
      <xsd:element name="element2" type="xsd:string" 
			minOccurs="0" maxOccurs="3"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

As stated, element1 and element2 will now be multiple
cardinality so that a get(...) accessor would return a List. Element1 has a
default minOccurs of 1 and a default maxOccurs of 1. Element2 has a minOccurs
of 0 and a maxOccurs of 3. In the following example, their new minOccurs and maxOccurs will be as
follows:

```
DataObject - ModelGroupArray
	Property[0] - element1 - minOccurs=(2*1)=2 - maxOccurs=(5*1)=5
	Property[1] - element2 - minOccurs=(2*0)=0 - maxOccurs=(5*3)=15
```

If the type were Choice:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
		targetNamespace="http://ModelGroupArray">
  <xsd:complexType name="ModelGroupArray">
    <xsd:choice minOccurs="2" maxOccurs="5">
      <xsd:element name="element1" type="xsd:string"/>
      <xsd:element name="element2" type="xsd:string" 
			minOccurs="0" maxOccurs="3"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

Would generate the following minOccurs due to the exclusion of choice that only
element1 can be picked each time or only element2 could be
picked each time, so to pass validation both need to be able to have 0 occurrences:

```
DataObject - ModelGroupArray
	Property[0] - element1 - minOccurs=(0*1)=0 - maxOccurs=(5*1)=5
	Property[1] - element2 - minOccurs=(0*0)=0 - maxOccurs=(5*3)=15
```