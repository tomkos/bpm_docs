<!-- image -->

# Using the Sequence object to set data order

One example of order significance in XSDs is mixed content. If the text data appears before or
after an element, it may have different meaning than if it occurs in a different location. For these
situations, SDO generates an object known as a Sequence, which is used to set the data in an ordered
fashion.

SDO Sequences should not be confused with XSD sequences. XSD sequences are just model groups that
are flattened out before SDO model generation. The presence of an XSD sequence does not relate to
the presence of an SDO Sequence.

The following conditions in an XSD cause an SDO Sequence to be generated:

A complexType with mixed content:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 xmlns:tns="http://MixedContent" 
 targetNamespace="http://MixedContent">
  <xsd:complexType name="MixedContent" mixed="true">
    <xsd:sequence>
      <xsd:element name="element1" type="xsd:string" minOccurs="0"/>
      <xsd:element name="element2" type="xsd:string" minOccurs="0"/>
      <xsd:element name="element3" type="xsd:string" minOccurs="0"/>
    </xsd:sequence>
  </xsd:complexType>
  <xsd:element name="MixedContent" type="tns:MixedContent"/>
</xsd:schema>
```

A schema that has 1 or more <any/> tags:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 xmlns:tns="http://AnyElemAny" 
 targetNamespace="http://AnyElemAny">
  <xsd:complexType name="AnyElemAny">
    <xsd:sequence>
      <xsd:any/>
      <xsd:element name="marker1" type="xsd:string"/>
      <xsd:any/>
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

A model group array (an all, choice, sequence, or group reference with maxOccurs > 1):

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	targetNamespace="http://ModelGroupArray">
  <xsd:complexType name="ModelGroupArray">
    <xsd:sequence maxOccurs="3">
      <xsd:element name="element1" type="xsd:string"/>
      <xsd:element name="element2" type="xsd:string"/>
	</xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

An <all/> tag of maxOccurs <= 1 that contains more than one element:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	targetNamespace="http://All">
  <xsd:complexType name="All">
    <xsd:all>
      <xsd:element name="element1" type="xsd:string"/>
      <xsd:element name="element2" type="xsd:string"/>
    </xsd:all>
  </xsd:complexType>
</xsd:schema>
```

Specific information about using <any/> and sequence together will be discussed in the topic
listed under Related Information on this page. The general information that follows in the
remainder of this section will describe how to work with the other Sequence conditions, but will
still apply to <any/> as well.

- How do I know if my DataObject has a sequence?

There are two simple APIs to choose from that can determine if a DataObject is sequenced: DataObject noSequence and DataObject withSequence.
- Why do I need to know a DataObject has a Sequence?

If you are working on a DataObject that has a Sequence, it is important to know the order in which the data is set. Because of this, care must be taken in the order in which the values are set.
- How do I work with mixed content?

For mixed content, Sequence has a specific API for adding text: addText(...).
- How do I work with a model group array?

A model group array is created when a model group has a value for maxOccurs > 1.