<!-- image -->

# How do I get or set anyAttribute values?

You can perform a get on data that was set in an anyAttribute field in the
same manner as any other attribute value, if the name is known. You can perform a get with the XPath
@<name> and it will be resolved. The following example code shows this:

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 xmlns:tns="http://AnyAttrOnlyMixed" 
 targetNamespace="http://AnyAttrOnly">
  <xsd:complexType name="AnyAttrOnly">
    <xsd:sequence>
      <xsd:element name="element" type="xsd:string"/>
    </xsd:sequence>
    <xsd:anyAttribute/>
  </xsd:complexType>
</xsd:schema>

<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	targetNamespace="http://GlobalAttrs">
  <xsd:attribute name="globalAttribute" type="xsd:string"/>
</xsd:schema>

	DataObject dobj = ...

	// Get the global attribute Property that is going to be set
	Property globalProp = boXsdHelper.getGlobalProperty("http://GlobalAttrs", 
	"globalAttribute", false);

	// Set the value on the dobj, just like any other data
	dobj.set(globalProp, "foo");

	// The data can now be accessed by a get call
	System.out.println(dobj.get("@globalAttribute")); // Displays "foo"
```

If the name is unknown using the code, the values can be iterated and accessed one by one as seen
in the How do I tell if my DataObject has an anyAttribute tag? topic.