<!-- image -->

# Mapping an integer value to an <anyType> element

## About this task

<!-- image -->

```
ServiceManager serviceManager = new ServiceManager();
 	Bofactory bofactory = (BOFactory)serviceManager.locateService("com/ibm/websphere/bo/BOFactory");

 	BOXSDHelper xsdHelper = (BOXSDHelper)serviceManager.locateService("com/ibm/websphere/bo" );
	// Retrieve the values in the xsd:any[] on the source and populate the target

	Property anyProp = AnyElem.getInstanceProperty("globalElement1");

	String anyStringData = (String)AnyElem.get(anyProp);
// // Create the wrapper object from the input Data

	Type stringType = boType.getType("http://www.w3.org/2001/XMLSchema", "string");
	DataObject wrappedStringDO = bofactory.createDataTypeWrapper(stringType, anyStringData);
```

```
Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "boolean");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "int");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "float");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "double");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "string");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "byte");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "long");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "short");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "hexBinary");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "datetime");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "decimal");
```