<!-- image -->

# Custom mediation and transformations

## Mediation primitives and transformations

For
MFS applications, you can use custom mediation under the transformation
grouping to set or get the convID and convEnded properties. This custom
mediation code is added by dragging a custom mediation object on to
the canvas, wiring it, and then adding the code in the Details tab.
In a request flow, the custom mediation is typically used to set the
convID in the message before it is sent to the service provider at
the end of the request flow. Business graphs are required for MFS
conversational applications in order to dynamically set and get the
useConvID, convID and convEnded conversational properties.   These
properties are set in the properties element of the business graphs.
 Because these are interactionSpec properties from the IMS TM resource adapter, the pattern for the
property name used when you set or get these properties is ISinteractionSpec\_property\_name.

In
a response flow, the custom mediation is typically used to get the
convID and convEnded properties before it is sent to the service requester
at the end of the response flow.

## Custom mediation code

```
// Retrieve the business graph data object
 1 commonj.sdo.DataObject body = smo.getDataObject("body");
// Modify the following data objects based on your application
commonj.sdo.DataObject IVTCBMI1\_obj = body.getDataObject("IVTCBMI1");
commonj.sdo.DataObject IVTCBMI1Input\_obj = IVTCBMI1\_obj.getDataObject("IVTCBMI1Input");

// Create the business graph's properties element
commonj.sdo.DataObject prop\_obj = IVTCBMI1Input\_obj.createDataObject("properties");
// Set userConvID to true
 2 prop\_obj.setBoolean("ISuseConvID",true);
out.fire(smo); // propagate the service message object to the primitive that is wired to the 'out' terminal
```

You
can determine the DataObject property names to use by examining the
service message object details for the primitive. When you move the
mouse pointer over the custom mediation node, an interface icon is
displayed. Click the interface icon, and the details of the object
is available in the Service Message Object Details section.

1. Business object instances are represented by the commonj.sdo.DataObject
interface. For more information about the commonj.sdo.DataObject classes
and SDO programming, see the samples on the business process management
samples and tutorials site at http://publib.boulder.ibm.com/bpcsamp/index.html.
2. The conversation ID is assigned by IMS when
the useConvID property is set to true. The EIS binding in the JCA
framework expects that the interactionSpec property names must begin
with the prefix IS, followed by the property name.

```
// Get ConvID and convEnded from the transient context
commonj.sdo.DataObject context\_obj = smo.getDataObject("context");
commonj.sdo.DataObject tran\_obj	= context\_obj.getDataObject("transient");
commonj.sdo.DataObject prop\_obj = tran\_obj.getDataObject("properties");
String conv\_id = prop\_obj.getString("ISconvID");
String convEnded = prop\_obj.getString("ISconvEnded");

// Set "convid" and "convEnded" into your business object
commonj.sdo.DataObject body\_obj = smo.getDataObject("body");
commonj.sdo.DataObject first\_iteration\_response\_obj	= body\_obj.getDataObject("FirstIterationResponse");
commonj.sdo.DataObject output1\_obj = first\_iteration\_response\_obj.getDataObject("output1");
output1\_obj.setString("convid", conv\_id);
output1\_obj.setString("convEnded", convEnded);
out.fire(smo); // propagate the service message object to the primitive that is wired to the 'out' terminal
```

See the MFS SOA support - Business process terminology topic for complete
steps on how to mediate a MFS conversational application.

## Transient context, correlation context, and shared
context

- Use transient context for general data storage within a request
or a response flow. Typically you store the business graph information
in transient context.
- Use correlation context for general data storage across the request
and the response flows. Use the correlation context to store the conversation
ID.
- Shared context is used for aggregations (array data). This object
is used to create different messages from a repeating element in the
input message or response message and do not apply to IMS MFS-based applications.