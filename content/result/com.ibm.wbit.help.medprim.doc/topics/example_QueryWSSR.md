# Example: Querying WSRR

## Context

## Requirements

## Java imports

```
import com.ibm.wsspi.sibx.mediation.wsrr.client.ServiceRegistryProxy;
import com.ibm.wsspi.sibx.mediation.wsrr.client.ServiceRegistryProxyFactory;
import com.ibm.wsspi.sibx.mediation.wsrr.client.data.ServiceRegistryDataGraphList;
import com.ibm.wsspi.sibx.mediation.wsrr.client.exception.ServiceRegistryProxyException;
import com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.types.DataGraphType;
import com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.BaseObject;
import com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.WSDLPort;
import com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.WSDLService;
import java.util.Iterator;
```

## Code sample

```
.
.
String endpointAddress = null;

// Get the factory and then get the default instance of a ServiceRegistryProxy. Can also use getServiceRegistryProxy("RegistryName")
ServiceRegistryProxy srProxy = ServiceRegistryProxyFactory.getInstance().getDefaultServiceRegistryProxy();

try
{
	// Set up the WSRR XPath query
	String query = "/WSRR/WSDLService/ports[binding(.)/portType(.)[@name = 'AccountManagement' and 
        @namespace='http://www.example.org/AccountManagement/']]";
	
	// Run the query & get the results
	ServiceRegistryDataGraphList list = srProxy.query(query, -1, false);
	
	// Iterate through the results
	Iterator<DataGraphType> resultsIterator = list.getDataGraphs().iterator();
  while(resultsIterator.hasNext() && endpointAddress == null)
	{
		DataGraphType dgt = resultsIterator.next();
		BaseObject[] baseObjects = dgt.getWSRR().getArtefacts();

		// Find the SOAP Address 
		for(int i=0; i<baseObjects.length; i++)
		{
			BaseObject bo = baseObjects[i];
			if(bo instanceof WSDLService)
			{
				WSDLPort[] ports = ((WSDLService)bo).getPorts();
				// Look for the SOAP Address in the first port				
				endpointAddress = ports[0].getSOAPAddress().getLocation();
				break;			
			}
		}
	}
}
catch(ServiceRegistryProxyException e)
{
	e.printStackTrace();
}

System.out.println(endpointAddress);

// If we have successfully retrieved an endpoint from WSRR, set it into the SMO
if(endpointAddress != null)
{
	smo.setString("headers/SMOHeader/Target/address", endpointAddress);	
}
.
.
```