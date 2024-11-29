<!-- image -->

# How do I get/set any values?

You can perform a get with the XPath <name>. If the name is unknown,
then the value can be found by checking the instance properties. If there are multiple any tags, or
an any tag with maxOccurs > 1, then the DataObject sequence will have
to be used instead if it is important to determine which any tag the data originated from.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
 xmlns:tns="http://AnyElemAny" 
 targetNamespace="http://AnyElemAny">
  <xsd:complexType name="AnyElemAny">
    <xsd:sequence>
      <!-- Handle all these any one way -->
      <xsd:any maxOccurs="3"/>
      <xsd:element name="marker1" type="xsd:string"/>
      <!-- Handle this any in another -->
      <xsd:any/>
    </xsd:sequence>
  </xsd:complexType>
</xsd:schema>
```

Because the <any/> tag causes the DataObject to be sequenced determining which any value was
set can be done by checking the Sequence for the position of the any properties.

You can determine which any tag the instance data for the following XSD belongs to by using the
following code:

```
DataObject anyElemAny = ...
	Seqeuence seq = anyElemAny.getSequence();
	
	// Until we encounter the marker1 element, all the open data
	// found belongs to the first any tag
	boolean foundMarker1 = false;
	
	for (int i=0; i<seq.size(); i++)
	{
	    Property prop = seq.getProperty(i);
	    
	    // Check to see if the property is an open property
	    if (prop.isOpenContent())
	    {
	        if (!foundMarker1)
	        {
	            // Must be the first any because it occurs
	            // before the marker1 element
	            System.out.println("Found first any data: "+seq.getValue(i)); 
	        }
	        else
	        {
	            // Must be the second any because it occurs
	            // after the marker1 element
	            System.out.println("Found second any data: "+seq.getValue(i));
	         }
	    }
	    else
	    {
	        // Must be the marker1 element
	        System.out.println("Found marker1 data: "+seq.getValue(i));
	        foundMarker1 = true;
	    }
	}
```

Setting an <any/> value is done by creating a global element property and adding that value to
the sequence.

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
	xmlns:tns="http://GlobalElems" 
	targetNamespace="http://GlobalElems">
  <xsd:element name="globalElement1" type="xsd:string"/>
  <xsd:element name="globalElement2" type="xsd:string"/>
</xsd:schema>

	DataObject anyElemAny = ...
	Seqeuence seq = anyElemAny.getSequence();

	// Get the global element Property for globalElement1
	Property globalProp1 = boXsdHelper.getGlobalProperty(http://GlobalElems, 
	"globalElement1", true);

	// Get the global element Property for globalElement2
	Property globalProp2 = boXsdHelper.getGlobalProperty(http://GlobalElems, 
	"globalElement2", true);

	// Add the data to the sequence for the first any
	seq.add(globalProp1, "foo");
	seq.add(globalProp1, "bar");
	
	// Add the data for the marker1
	seq.add("marker1", "separator");  // or anyElemAny.set("marker1", "separator")
	
	// Add the data to the sequence for the second any
	seq.add(globalProp2, "baz");

	// The data can now be accessed by a get call
	System.out.println(dobj.get("globalElement1"); // Displays "[foo, bar]"
	System.out.println(dobj.get("marker1");        // Displays "separator"
	System.out.println(dobj.get("globalElement2"); // Displays "baz"
```