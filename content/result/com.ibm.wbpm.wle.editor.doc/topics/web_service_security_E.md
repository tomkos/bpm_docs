# Serialization of IBM® Business Automation Workflow objects
for use in web services

When sending complex types as input parameters to web services, Business Automation Workflow often
needs hints as to how to structure the data. These methods are built
on the structure because a structure is, by definition, a Complex
type.

The following methods have been added to the tw.object.Record() object
to assist in forming the SOAP request:

- setSOAPElementName(string elementName)
- setSOAPElementNS(string namespace)
- defineSOAPProperty(string propertyName, string schemaName,
string typeName, boolean isAttribute, string namespace)

## Example

You are passing an object of type NameUpdateRequest as
an argument to a web service. This object is defined in the namespace http://www.lombardisoftware.com/schemas/NameUpdateRequest .
The NameUpdateRequest object contains two properties,
First (string) and Last (string).

Following is example code
to generate the XML that is part of the SOAP call:

```
<# out = new tw.object.Record(); out.setSOAPElementNS("http://www.lombardisoftware.com/schemas/ NameUpdateRequest"); out.setSOAPElementName("NameUpdateRequest"); out.defineSOAPProperty("First", "http://www.w3.org/2001/ XMLSchema", "string", false, ""); out.defineSOAPProperty("Last", "http://www.w3.org/2001/ XMLSchema", "string", false, ""); out.First = "John"; out.Last = "Smith"; #>
```

This generates the following XML element:

```
<NameUpdateRequest xmlns="http://www.lombardisoftware.com/schemas/ NameUpdateRequest"> <first xmlns="">John</first> <last xmlns="">Smith</last> </NameUpdateRequest>
```