<!-- image -->

# Mapping xsd:any[]

## About this task

<!-- image -->

```
// Variable AnyElemAny is represented as AnyElemAny\_1
  	ServiceManager serviceManager = new ServiceManager();
 	Bofactory bofactory = (BOFactory)serviceManager.locateService("com/ibm/websphere/bo/BOFactory");

 	BOXSDHelper xsdHelper = (BOXSDHelper)serviceManager.locateService("com/ibm/websphere/bo" );
	// Retrieve the values in the xsd:any[] on the source and populate the target

	int instancePropertyCount  = AnyMany.getInstanceProperties().size();

	int definedPropertyCount =  AnyMany.getType().getProperties().size();
// If equal, then the Source BO does not have data corresponding to  xsd:any

	if (instancePropertyCount == definedPropertyCount)
	System.out.println("no open properties found");

	// Iterate through each of the properties and get the value
	// set the target
	Property property = null;
	// target Sequence
	Sequence seq = AnyMany\_1.getSequence();
	Property targetAnyProperty = xsdHelper.getGlobalProperty("http://GlobalElems", "globalElement1", true);
	for (int i = definedPropertyCount; i < instancePropertyCount; i++)
	{
			property = (Property) AnyMany.getInstanceProperties().get(i);
			if (xsdHelper.isElement(property)) {
			Object  data = AnyMany.get(property);
			// set this data on the target
				seq.add(targetAnyProperty,data);
		}
	}
```