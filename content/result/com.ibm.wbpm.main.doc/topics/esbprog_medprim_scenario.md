<!-- image -->

# Example scenarios

The scenario addresses the business need of a financial services company that provides an
interactive web-based stock market service to its customers.

The company wants to differentiate itself from its competition by offering tiered levels of
service. The company's goal is to offer delayed stock quotes to their standard customers and
real-time quotes to their gold customers, that is, customers who pay a fee.

The service requester provides a query containing a stock symbol and customer ID to the mediation
primitive, which processes the query. The customer's subscription level is determined, and depending
on the level of subscription, the query is routed to the appropriate service provider. The quote
that is returned from the service provider is then returned to the client application. The following
areas look at the ways in which the query can be processed by different mediation primitives.

## Message filter mediation primitive

To facilitate the basic request, the company can use the Message Filter mediation primitive
within their mediation flow component to selectively route messages that meet a certain criteria,
through different paths of a flow, using XPath expressions.

Figure 1. Message filter mediation primitive

<!-- image -->

Figure 1 shows how the gold output, is associated
with the real-time service provider, to offer real-time stock quotes to all gold customers. The
default output wire is associated with the delayed service provider, to give delayed stock quotes to
all standard customers. The contents of the input message are compared with each XPath expression in
turn, and depending on which condition is met, a message can be sent from the associated output
terminal.

```
<body>
	<getStockQuote>
		<companyID>IBM</companyID>
		<customerType>GOLD</customerType>
		<person xsi:type="Customer">
			<customerID>013652</customerID>
			<customerName>Joe Bloggs</customerName>
			<customerAddress>123 One Street</customerAddress>
		</person>
	</getStockQuote>
</body>
```

```
/body/getStockQuote/customerType=='GOLD'
```

## Type Filter mediation primitive

The company want to extend the functionality of their mediation flow component, by giving
employees the same real-time quotes that the gold customers receive.

To facilitate this request, the company use the Type Filter mediation primitive within their
mediation flow component. The primitive uses XPath expressions that can route messages down
different paths of a flow, based on their business object type. The Type Filter mediation primitive
always sends a message from the first matching output terminal.

Figure 2. Type Filter mediation primitive

<!-- image -->

Figure 2 shows that the message that is sent from the
Message Filter default output wire to the Type Filter mediation primitive. If the business object of
type employee is found; the message is sent along the employee output wire to the real-time service
provider. For any other business object the message is sent along the default output wire to the
delayed service provider.

```
<body>
	<getStockQuote>
		<companyID>IBM</companyID>
		<customerType>STANDARD</customerType>
		<person xsi:type="Employee">
			<employeeID>013690</employeeID>
			<employeeName>Jack Bloggs</employeeName>
			<employeeAddress>123 Two Street</employeeAddress>
		</person>
	</getStockQuote>
</body>
```

```
XPath: /body/getStockQuote/person
Business object type: Employee
```

## Flow Order mediation primitive

The company must log all requests that go to the real-time stock service provider.

To facilitate this request the company use the Flow Order mediation primitive. With this
primitive, the company can order the output of the messages.

Figure 3. Flow Order mediation primitive

<!-- image -->

The log must be carried out before the messages are sent to the real-time service provider
through the callout. The log service is a one-way operation. Figure 3 shows that the message that is output from both the
Message Filter and the Type Filter mediation primitives is sent to the Flow Order mediation
primitive. The output that is sent includes information of all gold member customers and employees
that have requested real-time stock quotes. This mediation primitive will send a message to the
Service Invoke Log, before sending a message to the callout.

## Custom mediation primitive

The company have introduced a silver level of subscription. Silver members will receive real-time
stock quotes between the hours of 9:00am and 12:00pm. Outside these hours, silver members receive
delayed stock quotes.

Figure 4. Custom mediation primitive

<!-- image -->

```
String customerType = smo.getString("/body/getStockQuote/customerType");
 if(customerType.equals("GOLD") || (customerType.equals("SILVER") && 
 Calendar.getInstance().get(Calendar.HOUR\_OF\_DAY)<12 && 
 Calendar.getInstance().get(Calendar.HOUR\_OF\_DAY)>8))
 {
 	// Fire realtime service output service
 	realTimeTerminal.fire(smo);
 }
 else
 {
	 delayedTerminal.fire(smo);
 }
```