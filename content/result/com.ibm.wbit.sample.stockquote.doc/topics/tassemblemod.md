<!-- image -->

# Assemble the mediation module

## About this task

<!-- image -->

## Procedure

1. In the Business Integration view, expand the StockQuote module.
2. To open the assembly editor, double-click Assembly Diagram.
The assembly editor opens showing the StockQuote mediation
flow component.
3. Select the StockQuote mediation flow component and hover
over it.  The select Add Interface > StockQuoteService
Interface.
4. Right-click the StockQuote mediation flow component, and
select Generate Export > Web Service Binding.
5. In the Configure Web Service Export wizard, select the
SOAP 1.1/JMS option, and then click Finish.
6. Right-click StockQuoteServiceExport1,
and then select Refactor > Rename.  You need
to save the StockQuote Assembly diagram.  Change the name to StockQuoteService
in the Rename Artifact window.
7. Locate the generated WSDL port, StockQuoteService\_StockQuoteServiceJms
Port under the resource library's Web Service Ports category.
8. In the Resources library's Interfaces category select DelayedServicePort and
drag it onto the assembly editor canvas. In the Configure
Web Service Import  window, select Import with
Web Service Binding and click OK.
9. Select the import and use refactoring to rename it to DelayedService.
Click the Binding tab in the Properties view to see the binding information.
10. Drag the RealtimeServicePort artifact
onto the assembly editor canvas, and then select Import
with Web Service Binding.
11. Select the import and use refactoring to rename the import
to RealtimeService.
12. Click StockQuote. This is the mediation
flow component that was created with the mediation module. Use refactoring
to rename it to StockQuote\_MediationFlow
13. Create a wire from source StockQuote\_MediationFlow to
target RealtimeService, and click OK.
A matching reference, RealtimeServicePortTypePartner,
is created on the source and the wire is created.
14. Create a wire from source StockQuote\_MediationFlow to
target DelayedService, and click OK.
A matching reference, DelayedServicePortTypePartner,
is created on the source and the wire is created.
15. Generate the implementation for StockQuote\_MediationFlow.
In the assembly editor, select the component, and then right-click
and select Generate Implementation. Select
the StockQuote folder, and click OK. The mediation
flow editor opens, showing the source interface and target references.
16. Save the assembly diagram. Expand the
StockQuote assembly under the module in the Business Integration view
to see the artifacts created.