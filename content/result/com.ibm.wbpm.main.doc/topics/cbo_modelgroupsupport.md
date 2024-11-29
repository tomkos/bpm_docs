<!-- image -->

# Model group support (all, choice, sequence, and group references)

Basically, this means that any of those structures that are within the same containing structures
are "flattened". This "flattening" puts all the child structures at the same level, which can
produce duplicate naming issues in an SDO whose structure is derived from the flattened data. When
an XSD does not flatten the groups, there is still a separation of duplicates that are contained by
different parents.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 targetNamespace="http://MultipleGroup">
  <xsd:complexType name="MultipleGroup">
    <xsd:sequence>
      <xsd:choice>
        <xsd:element name="option1" type="xsd:string"/>
        <xsd:element name="option2" type="xsd:string"/>
      </xsd:choice>
      <xsd:element name="separator" type="xsd:string"/>
      <xsd:choice>
        <xsd:element name="option1" type="xsd:string"/>
        <xsd:element name="option2" type="xsd:string"/>
      </xsd:choice>
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

Since the multiple occurrences of option1 and option2 are contained in different choice blocks
and even have a separating element between them, XSD and XML have no problem distinguishing between
them. But when SDO flattens these groups, all the option properties are now under the same container
of MultipleGroup.

Even without duplicate names, there is also the semantic issue that the flattening of these
groups cause. Take the following XSD for example:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 targetNamespace="http://SimpleChoice">
  <xsd:complexType name="SimpleChoice">
    <xsd:sequence>
      <xsd:choice>
        <xsd:element name="option1" type="xsd:string"/>
        <xsd:element name="option2" type="xsd:string"/>
      </xsd:choice>
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

Asking the user to rename duplicate names or add special annotations to XSDs is impractical
because in many cases, like standards and industry schemas, the user does not control the XSDs they
are working with.

To create consistency for all properties, business objects include a method to access each
individual occurrence of the duplicate named properties through XPath. Following the business
object framework naming convention, any duplicate property names encountered have the next
unused digit appended to their name So for example, the following XSD:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 targetNamespace="http://TieredGroup">
  <xsd:complexType name="TieredGroup">
    <xsd:sequence>
      <xsd:choice minOccurs="0">
        <xsd:sequence>
          <xsd:element name="low" minOccurs="1" 
					maxOccurs="1" type="xsd:string"/>
          <xsd:choice minOccurs="0">
            <xsd:element name="width" minOccurs="0" 
						maxOccurs="1" type="xsd:string"/>
            <xsd:element name="high" minOccurs="0" 
						maxOccurs="1" type="xsd:string"/>
          </xsd:choice>
        </xsd:sequence>
        <xsd:element name="high" minOccurs="1" 
				maxOccurs="1" type="xsd:string"/>
        <xsd:sequence>
          <xsd:element name="width" minOccurs="1" 
					maxOccurs="1" type="xsd:string"/>
          <xsd:element name="high" minOccurs="0" 
					maxOccurs="1" type="xsd:string"/>
        </xsd:sequence>
        <xsd:sequence>
          <xsd:element name="center" minOccurs="1" 
					maxOccurs="1" type="xsd:string"/>
          <xsd:element name="width" minOccurs="0" 
					maxOccurs="1" type="xsd:string"/>
        </xsd:sequence>
      </xsd:choice>
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

The preceding XSD produces the following DataObject model:

```
DataObject - TieredGroup
	Property[0] - low - string
	Property[1] - width - string
	Property[2] - high - string
	Property[3] - high1 - string
	Property[4] - width1 - string
	Property[5] - high2 - string
	Property[6] - center - string
	Property[7] - width2 - string
```

Where width, width1, and width2
are the names of the properties named width starting from the first one in the XSD going down,
likewise with high, high1, high2.

These new property names are just the names used for reference and XPath and do not affect
serialized content. The "true" names of each of these properties that appear in the serialized XML
are the values given in the XSD. So for the XML instance:

```
<?xml version="1.0" encoding="UTF-8"?>
<p:TieredGroup xsi:type="p:TieredGroup"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:p="http://TieredGroup">
  <width>foo</width>
  <high>bar</high>
</p:TieredGroup>
```

In order to access those properties you would use the following code:

```
DataObject tieredGroup = ...

	// Displays "foo"
	System.out.println(tieredGroup.get("width1"));

	// Displays "bar"
	System.out.println(tieredGroup.get("high2"));
```