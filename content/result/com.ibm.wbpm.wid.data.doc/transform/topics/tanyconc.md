<!-- image -->

# Mapping a concrete type to <any> target element

## About this task

```
// The specific type of variable Any\_Customer is commonj.sdo.DataObject

// Variable AnyElemAny\_xsd:any0 is represented as AnyElemAny\_xsd$cany0
   ServiceManager serviceManager = new ServiceManager();
	Bofactory bofactory = (BOFactory)serviceManager.locateService("com/ibm/websphere/bo/BOFactory");

	BOXSDHelper xsdHelper = (BOXSDHelper)serviceManager.locateService("com/ibm/websphere/bo" );
// Move the Customer Complex Type to the xsd:any Output
// The global property globalElement3 corresponds to the Customer
// Complex Type. Use this same global property to set the target
	Property anyProp = Any.getInstanceProperty("globalElement3");
	DataObject Customer = (DataObject)Any.get("Customer");
	AnyElemAny.set(anyProp, Customer);
```