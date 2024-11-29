<!-- image -->

# Mapping with XSD wildcards

## About this task

To create a business object map using XSD wildcards, follow
these steps

## Procedure

1. Select the wildcard field from the source.
2. Draw a connection to the target.

## Results

| Source                                             | Target is xsd:any   | Target is xsd:anyType   | Target is xsd:anySimpleType   | Target is a regular complex type   | Target is a regular simple type   |
|----------------------------------------------------|---------------------|-------------------------|-------------------------------|------------------------------------|-----------------------------------|
| xsd:any (complex type in the runtime instance)     | Supported           | Supported               |                               | Supported                          |                                   |
| xsd:any (simple type in the runtime instance)      | Supported           | Supported               | Supported                     |                                    | Supported                         |
| xsd:anyType (complex type in the runtime instance) | Supported           | Supported               |                               | Supported                          |                                   |
| xsd:anyType (simple type in the runtime instance)  | Supported           | Supported               | Supported                     |                                    | Supported                         |
| xsd:anySimpleType                                  | Supported           | Supported               | Supported                     |                                    | Supported                         |
| Regular complex type                               | Supported           | Supported               |                               | Supported                          |                                   |
| Regular simple type                                | Supported           | Supported               | Supported                     |                                    | Supported                         |

```
if (<<input parameter variable>> instanceof Integer)
{
	Integer intObject = (Integer)<<input parameter variable>>;
	int intValue = intObject.intValue();
	
	int newValue = intValue + 100;
	
	<<output parameter variable>> = newValue;
}
```

```
if (<<input parameter variable>> instanceof DataObject)
{
	DataObject dObject = (DataObject) <<input parameter variable>>;
	String value = (String)dObject.get("field");
	
	ServiceManager serviceManager = new ServiceManager();
	BOFactory bofactory = (BOFactory)serviceManager.locateService("com/ibm/websphere/bo/BOFactory");
	DataObject outObject = (DataObject)bofactory.create("http://anytest", "ComplexAny");
	outObject.set("field", value.substring(0, 2));
	
	
	<<output parameter variable>> = outObject;
}
```

```
commonj.sdo.Sequence seq = <<input BO variable>>.getSequence();
for (int i = 0; i < seq.size(); i++)
{
	commonj.sdo.Property prop = seq.getProperty(i);
	if (prop.isOpenContent())
	{
		Object xsdAnyValue = seq.getValue(i);
}
}
```

```
commonj.sdo.Sequence seq = <<output BO variable>>.getSequence();
com.ibm.websphere.bo.BOXSDHelper boXSDHelper = (BOXSDHelper) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOXSDHelper");
commonj.sdo.Property property = boXSDHelper.getGlobalProperty("http://anytest", "IntegerAny", true);
seq.add(property, new Integer(123));
```

```
String newString = ((String)<<input parameter variable>> ).substring(0,2);
<<output parameter variable>> = newString;
```

```
String newString = ((String) <<input parameter variable>> ).substring(0,2);

com.ibm.websphere.bo.BOType boType = (com.ibm.websphere.bo.BOType)serviceManager.locateService("com/ibm/websphere/bo/BOType");

Type stringType = boType.getType("http://www.w3.org/2001/XMLSchema", "string");
DataObject stringWrapper = bofactory.createDataTypeWrapper(stringType,newString);
<<output parameter variable>> = stringWrapper;
```

```
<<output parameter variable>> = (commonj.sdo.DataObject)<<input parameter variable>>;
```

```
ServiceManager serviceManager = new ServiceManager();

DataObject anyTypeValue = (DataObject)<<input parameter variable>>;
Object simpleValue = null;
Object complexValue = null;
com.ibm.websphere.bo.BOType boType = (com.ibm.websphere.bo.BOType)serviceManager.locateService("com/ibm/websphere/bo/BOType");
if (boType.isDataTypeWrapper(anyTypeValue))
	simpleValue = anyTypeValue.get("value");
else
	complexValue = anyTypeValue;
```

```
ServiceManager sm = ServiceManager.INSTANCE;
BOFactory bf = (BOFactory) sm.locateService("com/ibm/websphere/bo/BOFactory"); 				
com.ibm.websphere.bo.BOType boType = (com.ibm.websphere.bo.BOType)sm.locateService("com/ibm/websphere/bo/BOType");

Type objectType = boType.getType("http://www.w3.org/2001/XMLSchema", "string");
DataObject wrapper = bf.createDataTypeWrapper(objectType, new String("abc"));
<<output BO variable>>.set("anyTypeElement", wrapper);
```

```
List inputAnyAttributes = (List)<<input parameter variable>>;
// iterate through the list or pick the one you want
Property myProp = (Property)inputAnyAttributes.get(0);
			
Sequence seq = <<output BO variable>>.getSequence();
seq.add(myProp, "abc");
```

```
ServiceManager sm = ServiceManager.INSTANCE;
BOFactory bf = (BOFactory) sm.locateService("com/ibm/websphere/bo/BOFactory"); 
		
BOXSDHelper boXSDHelper = (BOXSDHelper) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOXSDHelper");
		
Property property = boXSDHelper.getGlobalProperty("http://anytest", "StringAnyAttr", false); // false indicates it's a global attribute
<<output BO variable>>.setString(property, "abc");
```

```
commonj.sdo.Sequence seq = <<input BO variable>>.getSequence();
com.ibm.websphere.bo.BOXSDHelper boXSDHelper = (BOXSDHelper) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOXSDHelper");

Property prop = helper.getGlobalProperty("http://www.ibm.com/bo/SubMapAnyAnyType","myany",true);

// Adding two Complex types to the any for list into the global property
DataObject Branch1 = boFactory.create(boTNS, "Branch");
Branch1.set("fName","wilshire");
seq.add(prop, Branch1);
DataObject Branch2 = boFactory.create(boTNS, "Branch");
Branch2.set("fName","poplar");
seq.add(prop, Branch2);
```

```
<<output parameter variable>> = (List)<<input parameter variable>>.getList.(0);
```

```
commonj.sdo.Sequence seq = <<input BO variable>>.getSequence();
com.ibm.websphere.bo.BOXSDHelper boXSDHelper = (BOXSDHelper) ServiceManager.INSTANCE.locateService("com/ibm/websphere/bo/BOXSDHelper");

Property prop = helper.getGlobalProperty("http://www.ibm.com/bo/SubMapAnyAnyType","myany",true);

// Adding two Complex types to the any for list into the global property
DataObject Branch1 = boFactory.create(boTNS, "Branch");
Branch1.set("fName","wilshire");
seq.add(prop, Branch1);
DataObject Branch2 = boFactory.create(boTNS, "Branch");
Branch2.set("fName","poplar");
seq.add(prop, Branch2);

List properties = <<input BO variable>>.getProperty(prop);

// use this list of properties as needed.
```

```
<<input BO variable>>;

List anyTypeList = <<input BO variable>>.getList("anAnyType");
        
DataObject Address1 = boFactory.create(boTNS, "Address");
Address1.set("address1", "hillsboro");
anyTypeList.add(Address1);

DataObject Address2 = boFactory.create(boTNS, "Address");
Address2.set("address1", "sandiego");
anyTypeList.add(Address2);
```

```
<<output parameter variable>> = (List)<<input parameter variable>>.getList.("anAnyType").get(0);
```

- The <any> element

The <any> element extends the XML document with elements not specified by the schema. The <any/> tag allows a complex type to have global elements set to it.  The <any> element makes extensible documents and allows documents to contain additional elements that are not declared in the main XML schema.
- The <anyType> element

The mapping of the <anyType> element is handled the same as any other complex type by the SDO APIs.  Complex types are limited to a single type (that is, Customer, Address, and so on) but <anyType> allows any data object, regardless of type, to be set in the <anyType> element.
- The <anySimpleType> element

From a mapping perspective, <anySimpleType> elements can be mapped in the same way as simple types.
- Submaps with <any> and <anyType> elements

It is possible to create submaps with the <any> and <anyType> types provided that these types contain complex types as the instance data. A runtime exception will be thrown if they contain non-complex types.
- Substitution group mappings

In XML 1.0, the name and content of an element had to correspond exactly to the element type referenced in the corresponding content model. Through substitution groups, XML schemas provide a more powerful model supporting substitution of one named element for another.