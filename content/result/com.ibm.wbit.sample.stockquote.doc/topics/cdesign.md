<!-- image -->

# Mediation design

The mediation service that runs on the IBM® Workflow
Server is
contained in a single mediation module  called StockQuote.

The mediation module consists of: an export that provides an interface to enable the
service to be called, imports that provide interfaces to the external web service providers,
and a mediation flow component that defines the mediation implementation. The mediation
module, StockQuote, is built in the assembly editor, and the mediation flow component,
StockQuote\_MediationFlow, is created in the mediation flow editor. The following figure shows the
relationship between the interfaces and references in the assembly editor and the mediation flow
editor.

<!-- image -->

<!-- image -->

- StockQuoteService has a WSDL interface, called StockQuoteService, and uses SOAP/JMS web
service binding so that the servlet front end can connect to the mediation module by using JAX-RPC.
In this sample, you will create the StockQuoteService interface and generate the WSDL file.
- StockQuote\_MediationFlow contains the mediation flow. In this sample, you will create and
implement the StockQuote\_MediationFlow component.
- RealtimeService has a web service binding and an interface that matches the real-time
(premium) service.
- DelayedService has a web service binding and an interface that matches the delayed
(standard) service.

The following diagram shows the request flow that defines the mediation logic applied to the
message as it flows through the StockQuote\_MediationFlow component to the target service
providers.

<!-- image -->

1. The property subscriptionLevel is set in the correlation context of the message so that it will
be available later in the response flow.
2. The request message is output to the server log view using the Trace mediation primitive..
3. A Map mediation primitive named Lookup uses the customerID element in the
message body to determine whether the customer is entitled to the premium or standard service by
looking this information up in the supplied CustomerType.csv file. This information is added to the
subscriptionLevel property in the correlation context of the message, for use later.
4. The request is routed by a Message Filter called Filter, based on the subscriptionLevel
information in the correlation context, to either the real-time or delayed stock quote service. The
Filter's pattern property is promoted so that it can be changed at run time to redirect the stock
quote request to the delayed service if the premium service is unavailable.
5. If the customerID was not found in the CustomerType.csv file, then a default subscriptionLevel
is set in the SetCutomerType using a Message Element Setter.
6. The message is transformed on the way to either service by XSLT primitives TransformToDelayed
and TransformToRealtime so that it matches what the service expects.
7. The response from each service is passed through an XSLT mediation primitive
(DelayedToStockQuoteService & RealtimeToStockQuoteService) to match the format that is required
by StockQuoteService.

The diagram below shows the response flow that defines the mediation logic applied to the
returning message as it flows through the StockQuote\_MediationFlow component from the target service
provider to the client. A Message Element Setter is used to copy the value of subscriptionLevel from
the correlation context to the property qualityOfService in the message. The qualityOfService text
indicates "Premium" to a response that is returned from the real-time service, and "Standard" to a
response that is returned from the delayed service. The qualityOfService text is displayed in the
client to indicate the service provider that was used.

<!-- image -->

Lessons in this Module