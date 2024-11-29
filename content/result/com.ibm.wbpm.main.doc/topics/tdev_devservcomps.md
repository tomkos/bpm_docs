<!-- image -->

# Developing service components

## Before you begin

## About this task

## Procedure

1. Define the data object to move data between the caller and the service component.

The data object and its type is part of the interface between the callers and the service
component.
2. Define an interface that the callers will use to reference the service component.

This interface definition names the service component and lists any methods available within the
service component.
3. Generate the class that implements calling the service.
4. Develop the implementation of the generated class.
5. Save the component interfaces and implementations in files with a .java extension.
6. Package the service module and necessary resources in a JAR file.

See Deploying a module to a production server in this documentation for a description
of steps 6 through 8.
7. Run the serviceDeploy command to create an installable EAR file containing
the application.
8. Install the application on the server node.
9. Optional: 
Configure the wires between the callers and the corresponding service component, if calling a
service component in another service module.

The Administering section of this documentation describes configuring the wires.

## Examples of developing components

```
public interface CustomerInfo {
	public Customer getCustomerInfo(String customerID);
}
```

```
public class CustomerInfoImpl implements CustomerInfo {
	public Customer getCustomerInfo(String customerID) {
		Customer cust = new Customer();

		cust.setCustNo(customerID);
		cust.setFirstName("Victor");
		cust.setLastName("Hugo");
		cust.setSymbol("IBM");
		cust.setNumShares(100);
		cust.setPostalCode(10589);
		cust.setErrorMsg("");

		return cust;
	}
}
```

```
public class StockQuoteImpl implements StockQuote {
	
	public float getQuote(String symbol) {

	    return 100.0f;
	}
}
```

## What to do next