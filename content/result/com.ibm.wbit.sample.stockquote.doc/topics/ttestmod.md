<!-- image -->

# Test the mediation flow

## Before you begin

## About this task

1 In the Servers view, right click the server you will be deployingto, and select Properties. Select WebSphere Application Server. Check the value of the HTTP port. If the port is differentfrom 9080 you have to make sure that the Stock Quote application looksfor the web service on the correct port. This will affect the imports.To change the port:

<!-- image -->

    1. Open the Assembly Diagram of the Stock Quote module.
    2. Select the DelayedService import and in the Properties view, click Binding.
    3. The Address text box will contain something similar to http://localhost:9080/StockQuoteProviderWeb/sca/DelayedServicePortTypeExport1.
    4. "Overwrite "9080" with the value of the HTTP port displayed from
the Server Properties.
    5. Follow the previous steps for the RealtimeService import and then
save your module.
2. To add the StockQuoteApp project and the StockQuoteProviderApp project to the server,
right-click the server, select Add and remove project, and then click
Add All. Click Finish and wait for the server to
finish publishing.
3. Open the Assembly Diagram of the StockQuote mediation module.
Then right-click the StockQuote\_MediationFlow component and select Test
Component. The Events page of the integrated test client
opens.
4 In the Events page, you can select the modules, components, interfacesand operations that you want to test. For this sample, ensure theDetailed Properties are:

- Configuration: Default Module Test
- Module: StockQuote
- Component: StockQuote\_MediationFlow
- Interface: StockQuoteService
- Operation: getQuote
5. In the Initial request parameters table, you enter information
by double clicking the cell in the value column. Double-click the
value cell in the symbol row and enter AAA.
In the same manner, enter CustomerA for the customerID.
6. Next, select the Continue button  to invoke the getQuote operation. The Deployment Location
window opens.
7. Select a server and click Finish. Enter
the user ID and password for your server. The default is admin/admin.You
will see the resulting values for qualityOfService and value in the
return parameters.
8 If the application does not run successfully, try the following actions:

- If you see a service runtime exception, check that the web service application is started. In
the Servers view, select the server, right click and select Run Administration
Console and log in. In the list of running applications under Applications >
Enterprise Applications, check the status of the SQSample application and start the
application if necessary.
- If you see an error indicating that the module StockQuote cannot be found, make sure the
StockQuoteApp application and StockQuoteProviderApp application are running, by following the
previous instructions.