<!-- image -->

# Import resources

## About this task

To build this sample, you need the DelayedStockQuote and
RealtimeStockQuote sample web services. These are supplied for you
and represent existing web services you want to call, that take a
string stock symbol and return the value of the stock as a float.
The services are implemented using a mediation module with two simple
mediation components that are exported with a web service export binding.

## Procedure

To import the ready-made StockQuoteProvider web service
implementation to your workspace, complete the following steps:

1. Open IBM Integration Designer and select a new workspace.
2. On the Getting Started - IBM Integration Designer page,
select the IBM Integration Designer samples gallery link under Samples
and Tutorials.  The Samples and Tutorials page opens.
3. Under the Stock Quote sample, click Import. You are presented with two options for import.
4. Select Starter artifacts and click OK. You should now see two projects named Resources and StockQuoteProvider
in your Business Integration view.  The Resources library has the
following business objects, interfaces and web service definitions. The StockQuoteService interface is used to connect your web client to the mediation module.
 The StockQuoteService interface has a getQuote operation to send the request for a stock quote.
The data that is sent and received by the getQuote operation will be contained in business objects. The operation will
send the request data as a business object named StockQuoteRequest that contains the fields symbol and customerID. The operation will receive the response data as business object
named StockQuoteResponse that contains the
fields value and qualityOfService.  The request
message is routed based on the value of the subscription level. This
value needs to be passed with the message from one primitive to another.
 The SubscriptionInformation business object
will contain a subscriptionLevel field. You
need to set the value of the subscription level when you build the
request flow.
5. Close the Getting Started page by clicking on the X in
its tab. Also close the Samples and Tutorials page.