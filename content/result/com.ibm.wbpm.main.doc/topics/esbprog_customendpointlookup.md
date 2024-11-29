<!-- image -->

# Custom Endpoint Lookup mediation primitive

## Example scenario

The fictional company My Airways has registered some WSDL-defined service providers in a WSRR
registry, and want to retrieve the service endpoint URL that is based on a user property, which is
determined from the SMO at run time. My Airways use a Custom mediation primitive to retrieve the
service endpoint URL and set it in the SMO, so the service providers are called dynamically.

- It sends an XPath query to the WSRR registry to look up the provider service WSDL information.
- It processes the results returned from WSRR, retrieving the service endpoint URL.
- It sets the service endpoint URL into the SMOHeader Target address field. The URL is used when
an import with a Web Services binding is called, and the Callout node has been configured to use a
dynamic endpoint.

```
String endpointAddress = null;

// Get the factory and then get the default instance of a ServiceRegistryProxy. 
Can also use getServiceRegistryProxy("RegistryName")
com.ibm.wsspi.sibx.mediation.wsrr.client.ServiceRegistryProxy srProxy = 
com.ibm.wsspi.sibx.mediation.wsrr.client.ServiceRegistryProxyFactory.getInstance().
getDefaultServiceRegistryProxy();

try
{
		 // Set up the WSRR XPath query - this query looks for WSDL Ports that 
				have the PortType name 'MyAirwaysAccount'and the required customerType user property
		 // and the PortType namespace 'http://www.MyAirways.com/AccountManagement/'
			String customerType = smo.getString("/body/bookFlight/customerType");
		 	String query = "/WSRR/WSDLService/ports[binding(.)/portType(.)
			[@name = 'MyAirwaysAccount' "+
			 		 "and @namespace='http://www.MyAirways.com/AccountManagement/'
					  and @customerType ='" + customerType + "']]";
		 
		 // Run the query & get the results
		com.ibm.wsspi.sibx.mediation.wsrr.client.data.
		ServiceRegistryDataGraphList list = srProxy.query(query, -1, false);
		 
		 // Iterate through the results
		 Iterator<DataGraphType>  resultsIterator = list.getDataGraphs().iterator();
		 while(resultsIterator.hasNext() && endpointAddress == null)
		 {
		 		DataGraphType dgt = resultsIterator.next();
		 		BaseObject[] baseObjects = dgt.getWSRR().getArtefacts();

				com.ibm.ws.management.discovery.EndpointAddress endpointAddress = null;

		 		// Find the SOAP Address  		 		 
				for(int i=0; i<baseObjects.length; i++)
				{
		 		 		 BaseObject bo = baseObjects[i];
		 		 		 if(bo instanceof com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.WSDLService)
		 		 		 {
		 		 		 		com.ibm.wsspi.sibx.mediation.wsrr.client.jaxrpc.WSDLPort[] ports = ((com.ibm.
								  wsspi.sibx.mediation.wsrr.client.jaxrpc.WSDLService)bo).getPorts();
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
```