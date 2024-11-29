<!-- image -->

# Build the request flow

## About this task

<!-- image -->

To build the request flow, complete the following steps:

## Procedure

1. When the mediation flow opens, you will see a tip explaining
how to invoke a service. Since you have already added a callout to
the target service using the Service Integration template, you can
close the tip.
2. Click the Tracing palette category to expand the group.
3. Click the Trace primitive and drop
it onto the request flow canvas, and rename the primitive Trace.
4. Select a Mapping primitive from
the Transformation folder in the palette, drop it onto the request
flow canvas, and name it Lookup.
5. Select a Message Filter primitive
from the Routing folder, drop it onto the request flow canvas, and
name it Filter.
6. Select a Mapping primitive from
the Transformation folder, drop it onto the request flow canvas, and
name it TransformToDelayed.
7. Select another Mapping primitive,
drop it onto the request flow canvas, and name it TransformToRealtime.
8. Select a Message Element Setter primitive
from the Transformation folder, drop it onto the request flow canvas,
and name it SetCustomerType.
9. Before you proceed to wire the primitives, right click
the canvas and make sure that the Automatic Layout option
is on.
10 In the request flow canvas, wire the primitives: The wired request flow should look like this:
    - The output terminal of getQuote : StockQuoteService to
the input terminal of Trace
    - The output terminal of Trace to the
input terminal of Lookup
    - The output terminal of Lookup to the
input terminal of Filter
    - The default terminal of Filter to the
input terminal of SetCustomerType
    - The match1 terminal of Filter to the
input terminal of TransformToRealtime
    - The output terminal of SetCustomerType to
the input terminal of  TransformToDelayed
    - The output terminal of TransformToRealtime to
the input terminal of getQuote : RealtimeServicePortTypePartner
    - Select Filter.  In the Properties view, select the Terminal
tab.  Right-click the Output terminal and select Add output
terminal. In the New Dynamic Terminal window,
take the defaults of Terminal type match and change the Terminal name delayedTime.
Select OK.
    - Wire the delayedTime output terminal
of Filter to the input terminal of TransformToDelayed.

<!-- image -->

11. You will now add the business object that was created earlier
to the correlation context of the input node getQuote :
StockQuoteService. This enables the property subscriptionLevel to
persist in the message flow. Click getQuote : StockQuoteService input
node and switch to the Details tab in the Properties view. In the Correlation
context field, click Browse. Select
SubscriptionInformation under matching data types, and click OK.
The URI, {http://Resources}SubscriptionInformation, now appears in Correlation
context .
12 Click Trace in the request flowcanvas to see the primitive's properties in the Properties view. Clickthe Details tab to view the properties. Send the trace output to theServer Logs view. Ensure that these properties are set: Table 1. Trace properties Property Value Description Destination Local Server Log Outputs messages to the Server Logs view. Message {0}, {1}, {2}, {3}, {4}, {5} Includes the following information in theoutput: Root path / The scope of the message and SMO to be insertedinto the trace message at insert {4}.

| Property    | Value                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Destination | Local Server Log             | Outputs messages to the Server Logs view.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Message     | {0}, {1}, {2}, {3}, {4}, {5} | Includes the following information in the output: {0} - the time stamps when the Trace primitive was invoked.   {1}  - the message ID from the SMO.   {2}  - the name of the Trace mediation primitive instance that generated the trace message.   {3} - t name of the module, containing the Trace mediation primitive instance, that generated the trace message.   {4}  - the part of the SMO, as specified by the Root property XPath.   {5} - the version of the SMO. |
| Root path   | /                            | The scope of the message and SMO to be inserted into the trace message at insert {4}.                                                                                                                                                                                                                                                                                                                                                                                       |

<!-- image -->

13. Select Lookup in the request flow canvas, hover over it
and select . Select the
out message and set its type to StockQuoteService:getQuote:getQuoteRequestMsg.
14 Double-click Lookup . In the NewXML Map wizard click Next . Make sure the MessageRoot is "/" and then click Finish .

<!-- image -->

1. In the map, wire the source body getQuote to
the target body getQuote.
2. Fully expand the source getQuote.
 On the target, expand context > correlation.  Wire the source customerID to
the target subscriptionLevel.  Change the transform
to the Lookup transform.  In the Lookup engine
field, select Comma Separated Value File Lookup.
 For CSV file, browse and select CustomerType.csv from the Resources
library.  Click Save and then close the map.
15 Click Filter in the request flowcanvas. Select the Terminal view:

1. Click match1 in the Output terminal list.
The properties of the match1 terminal appear on the right.
2. In the Terminal name field, change the name to realtime.
16. By default, the message is sent to the TransformToDelayed
primitive. You need to set the pattern for mapping to TransformToRealtime.
Select the Details tab. In the Filter table, click Add... and
enter the following values: 
Table 2. Filter table
properties

Column
Value

Pattern
/context/correlation/subscriptionLevel = 'premium'

Terminal name
realtime

Pattern
/context/correlation/subscriptionLevel = 'regular'

Terminal name
delayedTime
17 A promoted property can be changed by an administratorat run time. The pattern property can be changed at run time to changethe quality of service. To promote the pattern property:

1. Click the Promotable properties tab.
2. Click the promoted check box of the realtime [Pattern]
property.
3. Click the alias Filter.realtime. Type PREMIUM\_SERVICE to
rename the alias.

<!-- image -->

18. Select SetCustomerType.  In the
Properties view Details tab, select Add. Set
the value regular into the correlation subscriptionLevel and
then click Save.
19 Set the properties for the Mapping primitive TransformToDelayed :

1. Select the TransformToDelayed primitive
in the request flow canvas and double-click it.
2. Click Next  to see the
root, input, and output message types that will be mapped. Click Finish to
accept the defaults. This launches the map editor.
3. On the left side, the Input object side, expand body
> getQuote > request. In the Output object side, the right
side, expand body. Click symbol on the left
side and drag it to symbol on the right side to wire them together
and create the mapping.
4. Save your changes and close the map editor.
The mapping file is displayed in the Details tab of the
Properties view.
20 Similarly, set the properties for the Mapping primitive TransformToRealtime :

1. Select the TransformToRealtime primitive
in the request flow canvas and double-click it.
2. The New XML Mapping wizard opens. Click Next  to
see the root, input, and output message types that will be mapped.
Click Finish to accept the defaults. This action
opens the map editor.
3. On the left side, expand body > getQuote
> request. On the right side, expand body.
Click symbol on the left side and drag it to symbol on
the right side to create the mapping.
4. Save your changes and close the map editor.
The mapping file is displayed in the Details tab of the
Properties view.
21. Save the request flow.