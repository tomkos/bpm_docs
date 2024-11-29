<!-- image -->

# Exception handling for synchronous invocation

<!-- image -->

Here is a sample client that invokes a Java™ component
declared with a Java interface. The interface has one method
declared as follows:

```
public interface StockQuote {
	float getQuote(String symbol) throws InvalidSymbolException;
}
```

The client code looks like this:

```
try {
	float quote = StockQuoteService.getQuote(symbol);
	} catch (InvalidSymbolException s) {
	System.out.println(This is business exception declared in the Java interface.);
	} catch (ServiceRuntimeException e) {
	System.out.println("Unchecked system exception detected");
}
```

In the scenario, the first exception InvalidSymbolException indicates that the request has
reached the service provider, which does not recognize the client input. The service provider then
throws a business exception stating that the symbol supplied is invalid. This business exception is
the only one declared by the method signature.

exceptions like InvalidSymbolException are only caught with clients using a reference.

In addition to the business exception declared, the client can receive system exceptions. For
example, if the stock exchange system runs into a problem, the service might fail to obtain the
quote with some unchecked exceptions. When such an exception is thrown by the service, a
ServiceRuntimeException is returned to the client, and the client might then want to determine the
underlying cause. The following code snippet shows how it can obtain this information:

```
try {
	float quote = StockQuoteService.getQuote(String symbol);
	} catch (ServiceRuntimeException e) {
	Throwable t = e.getCause();
	if (t instanceof RemoteException) {
	System.out.println("System ran into RemoteException. Details as follows: " + e.toString());
}
```