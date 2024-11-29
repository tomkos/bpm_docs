<!-- image -->

# Data handler

In your SOA implementation, business data can flow between service providers and service
requesters over a variety of protocols (HTTP, JMS, MQ, and so on), in a variety of data formats such
as comma separated value, delimited, fixed width, COBOL and so on. Different protocols can have the
same mechanisms for carrying the business data in their respective protocol envelope. For example, a
HTTP message can encode its data using a comma delimited format, which can also be used in a JMS
message.

To allow imports and exports to process these multiple data formats, data handlers are used to
translate request and response data. SCA modules handle data as business objects. Data handlers need
to convert message data to and from business objects. Data Handlers can optionally contain
configurations such as codepage information for further flexibility. They can also be defined at
different levels of granularity allowing specific data handling.

- XMLDataHandler for handling XML formats
- Delimited for delimited formats including comma separated values
- FixedWidth
- JSON
- SOAP
- Serialized Java Object
- JAXB for conversion to Java Beans
- Handled by WTX for delegating data transformation to WebSphere
Transformation Extender
- MQ Adapter language data binding generator
- JMS Adapter language data binding generator
- Service Gateway for using business objects that leave the message data
unparsed

An API is provided for custom data handlers to be written. These are implemented with a Java
class that implements the commonj.connector.runtime.DataHandler interface.