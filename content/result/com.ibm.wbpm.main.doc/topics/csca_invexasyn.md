<!-- image -->

# Exception handling for asynchronous invocation

In IBM® Business Automation Workflow, there is always an
asynchronous counterpart of the synchronous interface.

Here is an example of an asynchronous interface:

```
public interface StockQuoteAsync {
public Ticket getQuoteAsync(String arg0);
public Ticket getQuoteAsyncWithCallback(String arg0);
public float getQuoteResponse(Ticket ticket, long timeout) throws InvalidSymbolException;
}
```

Here is the client code for a call using the invocation pattern for deferred response:

```
Ticket ticket = stockQuote.getQuoteAsync(symbol);
try {
	quote = stockQuote.getQuoteResponse(ticket, Service.WAIT);
	} catch (InvalidSymbolException s) {
	System.out.println(This is business exception declared in the interface.);
	} catch (ServiceRuntimeException e) {
	System.out.println("Unchecked system exception detected");
}
```

Like a synchronous invocation, InvalidSymbolException indicates that the request has reached the
service provider, which has thrown a business exception stating that the symbol is invalid. This
business exception is the only one declared by the interface. exceptions like InvalidSymbolException
are caught only with clients using a reference.

In addition to the business exception declared, the client can receive system exceptions such as
connection error that happens while sending the message. The client cannot receive system exceptions
that happen in the service thread (the thread on the service side of the asynchronous invocation).
According to the SCA asynchronous programming model, runtime exceptions that occur at the target
component are not returned to the source component.

## Exception case on asynchronous exception handling

There is one exception to the SCA asynchronous programming model rule that runtime exceptions
that occur at the target component are not returned to the source component. If the source component
is a Business Process component or Staff Process, system exceptions that occur in the target service
component are returned to the caller. This capability lets business process designers model and
catch system exceptions, and run error logic if a BPEL client returns a system exception.