<!-- image -->

# Mapping <any> elements to a target using condition on source

## About this task

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd=http://www.w3.org/2001/XMLSchema
 	targetNamespace=http://AnyElem>
	<xsd:complexType name="AnyElem">
  	<xsd:sequence>
		<xsd:any/>
		<xsd:element name="marker1" type="xsd:string"/>
		<xsd:element minOccurs=0 name="Name"/ type="xsd:string></xsd:element> 
	</xsd:seqeunce></xsd:complexType>
	</xsd:schema>
```

```
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://GlobalElems" targetNamespace="http://GlobalElems">
  <xsd:element name="globalElement1" type="xsd:string"/>
</xsd:schema>
```

```
DataObject anyElemAny = ...
	Seqeuence seq = anyElemAny.getSequence();
	// Get the global element Property for globalElement1
	Property globalProp1 = boXsdHelper.getGlobalProperty(http://GlobalElems, "globalElement1", true);
	// Add the data to the sequence for the first any
	seq.add(globalProp1, "foo");
	
	// Add the data for the marker1
	seq.add("marker1", "separator");  // or anyElemAny.set("marker1", "separator")
	
	// The data can now be accessed by a get call
	System.out.println(dobj.get("globalElement1"); // Displays "[foo]"
```

```
ServiceManager serviceManager = new ServiceManager();
	BOXSDHelper xsdHelper = (BOXSDHelper)serviceManager.locateService("com/ibm/websphere/bo" );
// If the Name attribute is set to "David", then set the xsd:any
// on the target 
  String name = AnyElem.getString("Name");
  if (name.equalsIgnoreCase("David"))
	{
		// get the xsd:any on the source
		Property anySourceProp AnyElem.getInstanceProperty("globalElement1");
	   Object data = AnyElem.get(anySourceProp);
    	// Instead of retrieving the target property again - can use     the source  property again
   	Property anytargetProp = xsdHelper.getGlobalProperty("http://GlobalElems", "globalElement1", true);
		AnyElem\_1.set(anytargetProp,data);
```