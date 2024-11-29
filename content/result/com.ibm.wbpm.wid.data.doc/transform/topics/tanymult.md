<!-- image -->

# Mapping multiple <any> elements

## About this task

When setting more than one <any> element,
you must do it in relation to the occurrence of the <any> to
some other identifying element.  For retrieving the <any> element
data, the data object sequence will have to be used to determine which <any> tag
the data originated from in relation to some other identifying element
or attribute.

<!-- image -->

```
// Variable AnyElemAny is represented as AnyElemAny\_1
  	ServiceManager serviceManager = new ServiceManager();
 	Bofactory bofactory = (BOFactory)serviceManager.locateService("com/ibm/websphere/bo/BOFactory");

 	OXSDHelper xsdHelper = (BOXSDHelper)serviceManager.locateService("com/ibm/websphere/bo" );
	// retrieve the data from the source - Source BO has already been set with the properties
	// that are retrieved below
 	Property marker1Prop = AnyElemAny.getType().getProperty("marker1");
 	Property firstAnyProp = (Property)
 	AnyElemAny.getInstanceProperties().get(1);
 	Property secondAnyProp = (Property)
 	nyElemAny.getInstanceProperties().get(2);

// Another way of getting the data in addition to the above is as follows :

 	firstAnyProp = AnyElemAny.getInstanceProperty("globalElement1");
	Object firstAnyData = AnyElemAny.get(firstAnyProp);
	secondAnyProp = AnyElemAny.getInstanceProperty("globalElement2");
	Object secondAnyData = AnyElemAny.get(secondAnyProp);
	Object markerData = AnyElemAny.get(marker1Prop);

// Set the data on the target BO,
// retrieve the global property fields on the target and set using the data from the source
	Property prop1 = xsdHelper.getGlobalProperty("http://GlobalElems", "globalElement1", true);
	Property prop2 = xsdHelper.getGlobalProperty("http://GlobalElems", "globalElement2", true);
AnyElemAny\_1.set(prop1,firstAnyData);
AnyElemAny\_1.set("marker1",markerData);
AnyElemAny\_1.set(prop2,secondAnyData);
```