<!-- image -->

# Differentiating identically named elements

In the Service Data Object (SDO) framework, elements and attributes are created as properties. In
the following code examples, the XSDs create types that have one property named
foo:

```
<xsd:complexType name="ElementFoo">
  <xsd:sequence>
    <xsd:element name="foo" type="xsd:string" default="elem\_value"/>
  </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="AttributeFoo">
  <xsd:attribute name="foo" type="xsd:string" default="attr\_value"/>
</xsd:complexType>
```

In these cases, you can access the property using the XML Path Language (XPath). However, valid
schema types can have an attribute and element of the same name, as in the following example:

```
<xsd:complexType name="DuplicateNames">
  <xsd:sequence>
    <xsd:element name="foo" type="xsd:string" default="elem\_value"/>
  </xsd:sequence>
  <xsd:attribute name="foo" type="xsd:string" default="attr\_value"/>
</xsd:complexType>
```

In XPath, you must be able to differentiate identically named elements from attributes. This is
achieved by beginning one of the names with an at sign (@). The following snippet shows how to
access the identically named element and attribute:

```
1	DataObject duplicateNames = ...

2	// Displays "elem\_value"
3	System.out.println(duplicateNames.get("foo"));

4	// Displays "attr\_value"
5	System.out.println(duplicateNames.get("@foo"));
```

Use this naming scheme for all methods that take a String value that is an SDO XPath.

- Model group support (all, choice, sequence, and group references)

The SDO specification requires model groups (all, choice, sequence, and group references) to be expanded in place and not describe types or properties.