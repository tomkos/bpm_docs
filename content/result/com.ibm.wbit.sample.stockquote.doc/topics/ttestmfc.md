<!-- image -->

# Debug the mediation flow

## About this task

## Procedure

1. To add a breakpoint to a mediation primitive, right-click
the primitive node in the request or response flow canvas, and select Debug
> Add Breakpoint. 

Notice that a small blue icon is added to the top left corner
of the primitive, indicating that a breakpoint has been added to it.
2. Select a server, right-click and click it and select Restart
in Debug to restart the server in Debug mode. Note that
if the server is already started, you must stop and start the server
again in Debug mode.
3. When the server has started, open the Assembly Diagram
of the StockQuote mediation module. Then right-click the StockQuote\_MediationFlow
component and select Test Component.The Unit Test Environment opens.
4 In the Unit Test Environment you can select the modules,components, interfaces and operations that you want to test. For thissample, ensure the Detailed Properties are:
    1. Configuration: Default Module Test
    2. Module: StockQuote
    3. Component: StockQuote\_MediationFlow
    4. Interface: StockQuoteService
    5. Operation: getQuote
5. In the Initial request parameters table, you enter information
by double clicking the cell in the value column. Double-click the
value cell in the symbol row and enter AAA.
In the same manner, enter CustomerA for the customerID.
6. Next, click the Continue button . The Deployment Location window opens.
7. Select the server you started in Debug mode earlier and
click Finish. Enter the User ID and password
for your server. The default is admin/admin. When the flow reaches
a breakpoint, you are prompted to open the Debug perspective. Click Yes to
open the perspective.
8. You can view the values of message elements, paths taken
and breakpoints reached in this view. To continue the flow through
to the end or to the next breakpoint click the Resume button .