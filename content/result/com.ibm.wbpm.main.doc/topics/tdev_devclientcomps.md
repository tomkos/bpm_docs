<!-- image -->

# Invoking components

## Before you begin

## About this task

## Procedure

1. Determine the components required by the calling module.

Note the name of the interface within a component and the data type that interface requires.
2. Define a data object.

Although the input or return can be a Java™ class, a service data object is optimal.
3 Locate the component.
    1. Use the ServiceManager class to obtain the references available to the
calling module.
    2. Use the locateService() method to find the component.

Depending on the component, the interface can either be a Web Service Descriptor Language (WSDL)
port type or a Java interface.
4. Invoke the component synchronously.

You can either invoke the component through a Java interface or use the
invoke() method to dynamically invoke the component.
5. Process the return.

The component might generate an exception, so the client has to be able to process that
possibility.

## Example of invoking a component

```
ServiceManager serviceManager = new ServiceManager();
```

```
InputStream myReferences = new FileInputStream("MyReferences.references");
ServiceManager serviceManager = new ServiceManager(myReferences);
```

```
StockQuote stockQuote = (StockQuote)serviceManager.locateService("stockQuote");
```

```
Service stockQuote = (Service)serviceManager.locateService("stockQuote");
```

```
public class MyValueImpl implements MyValue {

	public float myValue throws MyValueException {
		
		ServiceManager serviceManager = new ServiceManager();

	    // variables
	        Customer customer = null;
	        float quote = 0;
	        float value = 0;

	    // invoke
	        CustomerInfo cInfo = 
						(CustomerInfo)serviceManager.locateService("customerInfo");
	        customer = cInfo.getCustomerInfo(customerID);

	    if (customer.getErrorMsg().equals("")) {

	        // invoke
	    		StockQuote sQuote = 
						(StockQuote)serviceManager.locateService("stockQuote");
	    		Ticket ticket =  sQuote.getQuote(customer.getSymbol());
				// … do something else …
	    		quote =  sQuote.getQuoteResponse(ticket, Service.WAIT);

	        // assign
	        	value = quote * customer.getNumShares();
	    } else {

	        // throw
	       	throw new MyValueException(customer.getErrorMsg()); 
	    }
	    // reply
	        return value;
	}
}
```

## What to do next