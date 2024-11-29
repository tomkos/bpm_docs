# Example: Accessing WebSphere eXtreme
Scale

## Context

## Requirements

## Java imports

```
import com.ibm.wsspi.sibx.mediation.wxs.client.ExtremeScaleProxyFactory;
import com.ibm.wsspi.sibx.mediation.wxs.client.ExtremeScaleProxy;
import com.ibm.websphere.objectgrid.ObjectMap;
import com.ibm.websphere.objectgrid.ObjectGrid;
import com.ibm.websphere.objectgrid.Session;
import com.ibm.wsspi.sibx.mediation.wxs.client.exception.ExtremeScaleProxyException;
import com.ibm.websphere.objectgrid.ObjectGridException;
import com.ibm.websphere.objectgrid.plugins.TransactionCallbackException;
import com.ibm.websphere.objectgrid.UndefinedMapException;
```

## Code sample

```
.
.
try {
	//Get the factory and then the default eXtreme Scale definition 
 	ExtremeScaleProxyFactory factory = ExtremeScaleProxyFactory.getInstance();
 
 	ExtremeScaleProxy proxy = factory.getDefaultExtremeScaleProxy();

	//Get ObjectGrid instance defined in proxy
	ObjectGrid oGrid = proxy.getObjectGrid();
	
	//Get the transactional session
	Session session = oGrid.getSession();
	
	//Get the ObjectMap to use for store and retrieve 
	ObjectMap map = session.getMap("Map2");

	//Store a value into the ObjectMap
 	map.put("custom"+smo.get("/body/operation1/input1"), "custom mediation SPI success");
 	
 	//Retrieve a value from another ObjectMap and populate the ServiceMessageObject
 	ObjectMap anotherMap = session.getMap("Map1");
 	
 	Object customer = anotherMap.get("customerX");
 	
 	if (customer != null) {
 		smo.set("/context/transient/customer", customer);
 	}
}
catch (ExtremeScaleProxyException e) {
	e.printStackTrace();
}
catch (UndefinedMapException e) {
	e.printStackTrace();
}
catch (TransactionCallbackException e) {
	e.printStackTrace();
}
catch (ObjectGridException e) {
	e.printStackTrace();
}

out.fire(smo);
.
.
```