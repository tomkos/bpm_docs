<!-- image -->

# Prepackaged HTTP data format transformations

The following HTTP data format transformations are in the product
and can be used with HTTP binding.

If you intend to use the predefined HTTP bytes data binding then
you must use the following schema and data handler. Under Predefined
Resources in the Dependencies editor, select Native
Body schema for Native Body DataHandler. Save your work
and close the Dependencies editor.

| Data format transformations   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Simple type support?   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| Delimited                     | This data binding serializes the business object to and from a delimited format in the message sent and received from the client. This data binding must be configured.                                                                                                                                                                                                                                                                                                 | No                     |
| Fixed width                   | This data binding serializes the business object to and from a fixed width format in the message sent and received from the client. This data binding must be configured.                                                                                                                                                                                                                                                                                               | No                     |
| Handled by WTX                | The data format transformation is delegated to the WebSphere® Transformation Extender (WTX). The WTX map name is derived by the data handler. See WTX data handler.                                                                                                                                                                                                                                                                                                     | No                     |
| Handled by WTX Invoker        | The data format transformation is delegated to the WebSphere Transformation Extender (WTX). The WTX map name is supplied by the user.                                                                                                                                                                                                                                                                                                                                   | No                     |
| JAXB-based JavaBean           | This data format transformation serializes JavaBeans to a business object using the Java™ Architecture for XML Binding (JAXB) specification receiving a message and deserializes a business object to a JavaBean using the JAXB specification when sending a message.                                                                                                                                                                                                   | No                     |
| JSON                          | This data format transformation sends and receives a business object based on JavaScript Object Notation (JSON) from the JMS client. This data format transformation must be configured. See json.                                                                                                                                                                                                                                                                      | No                     |
| SOAP                          | This data binding parses the body of a SOAP message into a business object in the case of an inbound message and serializes a business object to the body of a SOAP message in the case of an outbound message.                                                                                                                                                                                                                                                         | Yes                    |
| Wrapped bytes                 | This data binding sets the incoming bytes in a business object property called "value" on the inbound message and gets the bytes from the business object property called "value" and sets them in the HTTP output stream. Though still supported, a preferred method would be to use the data format transformations added when you select the Native Body schema for Native Body DataHandler in the Predefined Resources as stated in the introduction to this table. | No                     |
| Wrapped text                  | This data binding serializes the business object in a message in text for the client. Though still supported, a preferred method would be to use the data format transformations added when you select the Native Body schema for Native Body DataHandler in the Predefined Resources as stated in the introduction to this table.                                                                                                                                      | No                     |
| UTF8XMLDataHandler            | This data format transformation parses UTF-8 encoded XML data into a business object when receiving a message. It serializes a business object into UTF-8 encoded XML data when sending a message.                                                                                                                                                                                                                                                                      | Yes                    |

## Related concepts

- Overview of HTTP data bindings
- Overview of HTTP function selectors
- Prepackaged HTTP function selectors

## Related reference

- Data handlers
- Prepackaged HTTP fault selectors