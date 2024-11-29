<!-- image -->

# Prepackaged MQ data format transformations

The following MQ data format transformations are available in the
product.

Note that the data format transformations you see listed when you
make a selection are filtered by the ones available in that context.
For example, you would find wrapped text if you had an operation with
an input or output variable with a JMSTextBody type.

If you intend to use the standard JMS message class with a body
type containing the message then you must use the business objects
provided for these body types. To create these business objects, a
predefined resource is available. To add this predefined resource,
expand your module and then double-click Dependencies.
The Dependencies editor opens. Expand Predefined Resources and
select Native Body Schema for Native Body DataHandler.
Save your work. You should also read Working with the simple JMS data bindings).

| Data format transformations       | Description                                                                                                                                                                                                                                                                                                                                                                                                   | Simple type supported?   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| Delimited                         | This data format transformation serializes the business object to and from a delimited format in the message sent and received from the MQ client. This data format transformation must be configured. See Delimited format.                                                                                                                                                                                  | No                       |
| Fixed width                       | This data format transformation serializes the business object to and from a fixed width format in the message sent and received from the MQ client. This data format transformation must be configured. See Fixed width format.                                                                                                                                                                              | No                       |
| Handled by WTX                    | The data format transformation is delegated to the WebSphere® Transformation Extender (WTX). The WTX map name is derived by the data handler. See WTX data handler.                                                                                                                                                                                                                                           | No                       |
| Handled by WTX Invoker            | The data format transformation is delegated to the WebSphere Transformation Extender (WTX). The WTX map name is supplied by the user.                                                                                                                                                                                                                                                                         | No                       |
| JAXB-based Java™ code             | This data format transformation serializes Java code to a business object using the Java Architecture for XML Binding (JAXB) specification receiving a message and deserializes a business object to Java code using the JAXB specification when sending a message.                                                                                                                                           | No                       |
| JSON                              | This data format transformation sends and receives a business object based on JavaScript Object Notation (JSON) from the MQ client. This data format transformation must be configured. See json.                                                                                                                                                                                                             | No                       |
| MQ CICS bridge                    | This data transformation sends and receives a business object based on the DFHCOMMAREA that CICS uses to transfer data between programs. See Creating a WebSphere MQ data binding for the WebSphere MQ CICS bridge.                                                                                                                                                                                           | No                       |
| MQ serialized business object XML | This data format transformation serializes a business object to an XML document and deserializes an XML document to a business object. Your wrapped data objects must be a complex type; they cannot be a simple type.                                                                                                                                                                                        | No                       |
| MQ serialized Java object         | This data format transformation serializes a business object to a Java object and deserializes a Java object to a business object.                                                                                                                                                                                                                                                                            | No                       |
| MQ unstructured binary message    | This data format transformation sets the incoming bytes into a business object property called "value" on the inbound message and gets the bytes from the business object property called "value" and sets it in the output stream on the outbound message. See MQ data bindings in IBM Integration Designer for some steps you will need to do to use this type of data format transformation.               | No                       |
| MQ unstructured text message      | This data format transformation sets the incoming text message into a business object property called "value" on the inbound message and gets the text message from the business object property called "value" and sets it in the output stream on the outbound message. See MQ data bindings in IBM Integration Designer for some steps you will need to do to use this type of data format transformation. | No                       |
| SOAP                              | The Simple Object Access Protocol (SOAP) data format transformation parses the body of a SOAP message into a business object when receiving a message. It serializes a business object and places it in the body of a SOAP message when sending a message.                                                                                                                                                    | Yes                      |
| XML                               | This data format transformation takes an XML data format as input and transforms it to a business object. It takes a business object output and transforms it to an XML data format. All character encoding sets (CCSIDs) are supported.                                                                                                                                                                      | Yes                      |
| UTF8XMLDataHandler                | This data format transformation parses UTF-8 encoded XML data into a business object when receiving a message. It serializes a business object into UTF-8 encoded XML data when sending a message.                                                                                                                                                                                                            | Yes                      |

If you want to create and use a new data transformation binding
resource, see Creating a data format transformation resource configuration .

## Related concepts

- Prepackaged MQ function selectors

## Related reference

- Overview of MQ data format transformations
- Data handlers
- Overview of the MQ function selectors
- Prepackaged JMS and MQ fault selectors