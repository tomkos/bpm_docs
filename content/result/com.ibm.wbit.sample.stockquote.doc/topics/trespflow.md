<!-- image -->

# Build the response flow

## About this task

<!-- image -->

To build the response flow, complete the following steps:

## Procedure

1. Click the Response tab to view the
response flow.
2. Select an Mapping Transformation primitive
from the Transformation folder in the palette, drop it onto the response
flow canvas, and rename it DelayedToStockQuoteService.
3. Select another Mapping Transformation primitive,
drop it onto the response flow canvas, and rename it RealtimeToStockQuoteService.
4. Select a Message Element Setter primitive
from the Transformation folder, drop it onto the canvas, and rename
it SetQualityOfService.
5. Select a Fail primitive from the
Error Handling folder, drop it onto the canvas and rename it DelayedStockQuoteFail.
Add another Fail primitive to the canvas and
rename it RealtimeStockQuoteFail.
6. Before you proceed to wire the primitives, right click
the canvas and make sure that the Automatic Layout option
is on.
7 Wire the primitives: The wired response flow should look like this:
    - The output terminal of getQuote : DelayedServicePortTypePartner to
the input terminal of DelayedToStockQuoteService
    - The output terminal of getQuote : RealtimeServicePortTypePartner to
the input terminal of RealtimeToStockQuoteService
    - The output terminal of DelayedToStockQuoteService to
the input terminal of  SetQualityOfService
    - The output terminal of RealtimeToStockQuoteService to
the input terminal of  SetQualityOfService
    - The output terminal of SetQualityOfService to
the input terminal of getQuote : StockQuoteService
    - The fail terminal of getQuote : DelayedServicePortTypePartner to
the input terminal of DelayedStockQuoteFail
    - The fail terminal of getQuote : RealtimeServicePortTypePartner to
the input terminal of RealtimeStockQuoteFail

<!-- image -->

8 Set the properties for the XSLT primitive DelayedToStockQuoteService:

1. Select the DelayedToStockQuoteService primitive
in the response flow canvas and double-click it.
2. The New XML Mapping wizard opens. Click Next to
see the root, input, and output message types that will be mapped.
Accept the defaults and click Finish.
3. In the input object section (left side) of the map editor,
expand body. In the output object section (right
side), expand body > getQuoteResponse > response.
4. Click value on the left side and drag it to value on
the right side to wire them and create the mapping.
5. Save your changes and close the map editor.
The mapping file is displayed in the Details tab of the
Properties view.
9 Similarly, set the properties for the XSLT primitive RealtimeToStockQuoteService:

1. Select the RealtimeToStockQuoteService primitive
in the response flow canvas and double-click it.
2. The New XML Mapping wizard opens. Click Next  to
see the root, input, and output message types that will be mapped.
Accept the defaults and click Finish.
3. In the input object section (left side) of the map editor,
expand body. In the output object section (right
side), expand body > getQuoteResponse > response.
4. Click value on the left side and drag it to value on
the right side to wire them and create the mapping.
5. Save your changes and close the map editor.
The mapping file and associated XSL style sheet are displayed
in the Details tab of the Properties view.
10 Set the properties for the Message Element Setter primitiveSetQualityOfService:

1. Select the SetQualityOfService primitive
in the response flow canvas. Switch to the Details tab
in the Properties view.
2. Click Add... to start the Add/Edit
Properties wizard.
3. From the Action dropdown select Copy.
 For Target select Browse, which will start
the XPath Expression Builder.
4. In the Data Types Viewer, expand ServiceMessageObject
> body > getQuoteResponse > response : StockQuoteResponse,
and select qualityOfService. The XPath expression
is shown in the expression field. Click OK.
5. For the Source field select Browse.
In the Data Types Viewer, expand ServiceMessageObject >
context > correlation and select subscriptionLevel.
 The XPath expression is shown in the expression field. Click OK.
In the Add/Edit window, click Finish.The target,
type and value columns of the table are populated in the first row
as shown. To edit them later, select the row and click Edit...
11 For the two Fail primitives:

1. Right click DelayedStockQuoteFail and
select Show in Properties. Click Details and
in the Error message field enter Failed to call DelayedStockQuoteService.
2. For RealtimeStockQuoteFail enter Failed
to call RealtimeStockQuoteService in the Error message
field.
12. Save the flow by pressing Ctrl-S.