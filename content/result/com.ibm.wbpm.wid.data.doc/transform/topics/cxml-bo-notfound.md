<!-- image -->

# Limitation: Conflicting namespace prefixes between the XML map input and the XML map
definition

If the same prefix is used in both locations to define different namespaces then it can lead to
XML serialization failures when processing the XML map output. This runtime error is reported:
WSXM3106E: Exception while parsing transformed XML: Class '<business object type>' not
found. Problems are generally seen when type casting xs:any or
xs:anyType elements in addition to having the conflicting prefixes.

Example

Suppose that a source document produced has an element s2 whose content is
going to be copied into element t2 in a target document, that is
xs:any or xs:anyType. To allow for the move, the map casts
the type to s2 defined at
http://www.example.org/mapDefinition by using the in namespace prefix
defined in the map definition. The example shows a sample input and output to the map, which would
result in the WSXM3106E error.

```
<?xml version="1.0" encoding="UTF-8"?>
<in:source xmlns:in3="http://www.example.org/mapDefinition"
   xmlns:in="http://myInputNamespace/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<in:s1>s1</in:s1>
<in3:s2>
<in3:c1>c1</in3:c1>
<in3:c2>c2</in3:c2>
</in3:s2>
</in:source>

<?xml version="1.0" encoding="UTF-8"?>
<out:target xmlns:in="http://www.example.org/mapDefinition/"
xmlns:out="http://www.example.org/target/" xmlns:xs4xs="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<t2 xmlns:in3="http://www.example.org/mapDefinition
   xmlns:in="http://myInputNamespace/"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="in:s2">
<in3:c1>c1</in3:c1>
<in3:c2>c2</in3:c2>
</t2>
</out:target>
```

In this example, you can see that the input to the XML map uses the namespace declaration
xmlns:in="http://myInputNamespace/", but the map definition uses the namespace
declaration xmlns:in="http://www.example.org/mapDefinition/", which causes a
conflict. Because of this conflict, the wrong namespace is used when processing the
xsi:type casting that was defined in the XSLT, leading to the XML error.

Solution

Review the map definition and ensure none of the namespace prefixes will conflict with those
namespaces used by the input to the XML map at run time. In the Namespace
section of the map properties, modify the namespace prefixes that the XML map uses. In the above
example, the problem could be avoided by using a prefix that is more unique than in.