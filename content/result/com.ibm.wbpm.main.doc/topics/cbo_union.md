<!-- image -->

# Serializing and deserializing unions with xsi:type

The following example XSD shows a union that has the members of an integer and a date.

```
<xsd:simpleType name="integerOrDate">
	<xsd:union memberTypes="xsd:integer xsd:date"/>
</xsd:simpleType>
```

This multiple typing can cause confusion during deserialization and when manipulating the
data.

Business objects support SDO's using xsi:type for serialization and will follow the same
algorithm for determining the type on a deserialization if the xsi:type is not present in the XML
data.

So to guarantee that the data (the number "42" in this example) would be deserialized as an
integer, you can use the xsi:type specified in the input XML. You can also order the member list of
the union in the XSD so that the integer comes before the string. The following example shows how
both methods are implemented:

```
<integerOrString xsi:type="xsd:integer">42</integerOrString>

<xsd:simpleType name="integerOrString">
	<xsd:union memberTypes="xsd:integer xsd:string"/>
</xsd:simpleType>
```

Likewise, if the user wanted the data to be deserialized as a string, then either of the
following changes would cause that behavior:

```
<integerOrString xsi:type="xsd:string">42</integerOrString>

<xsd:simpleType name="integerOrString">
	<xsd:union memberTypes="xsd:string xsd:integer"/>
</xsd:simpleType>
```

Note that if a string type is the first member of the union, it never has any information loss.
It can also hold any data that will always be chosen by the no xsi:type algorithm. If you want to
use a type other than string, you must either use xsi:type in the XML or reorder the member types in
the XSD to give the other members a chance to accept the data.