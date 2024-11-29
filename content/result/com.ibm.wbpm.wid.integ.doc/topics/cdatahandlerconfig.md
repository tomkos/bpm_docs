<!-- image -->

# Prepackaged data format handlers

The following data format handlers are available with the product.

If you intend to use the standard JMS message class with a body
type containing the message then you must use the business objects
provided for these body types. To create these business objects, a
predefined resource is available. To add this predefined resource,
expand your module and then double-click Dependencies.
The Dependencies editor opens. Expand Predefined Resources and
select Native Body Schema for Native Body DataHandler.
Save your work.

| Data format handler   | Description                                                                                                                                                                                                                                                                         | Simple type supported?   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| Atom feed format      | This data format handler should be used when you have serialized data in a format an Atom feed format as input into an export or need to generate serialized data in an Atom feed format for an import. It can be used with JMS, MQ JMS, generic JMS, MQ and HTTP bindings.         | No                       |
| Delimited format      | This data format handler should be used when you have serialized data in a format using a delimiter as input into an export or need to generate serialized data in a format using a delimiter for an import. It can be used with JMS, MQ JMS, generic JMS, MQ and HTTP bindings.    | No                       |
| Fixed width format    | This data format handler should be used when you have serialized data in a fixed width format as input into an export or need to generate serialized data in a fixed width format for an import. It can be used with JMS, MQ JMS, generic JMS, MQ and HTTP bindings.                | No                       |
| json                  | This data format handler should be used when you have serialized data in a JavaScript Object Notation (JSON) format as input into an export or need to generate serialized data in a JSON format for an import. It can be used with JMS, MQ JMS, generic JMS, MQ and HTTP bindings. | No                       |
| SOAP data handler     | The Simple Object Access Protocol (SOAP) data handler parses and serializes both SOAP messages and the header, as well as the SOAP fault details.                                                                                                                                   | Yes                      |
| WTX data handler      | This data format handler invokes WTX to do the transformation. This data handler needs a WTX map name which is provided by the WTX MapSelectionDataHandler.                                                                                                                         | No                       |
| WTX data handler      | This data format handler should be used if you are creating a configuration that makes use of the Email, FTP and Flat Files adapters.                                                                                                                                               | No                       |
| XML Data Handler      | This data format handler should be used when you have serialized XML data as input into your export (for inbound processing at run time) or need to generate serialized XML data for an import (for outbound processing at run time).                                               | Yes                      |