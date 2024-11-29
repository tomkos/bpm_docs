<!-- image -->

# Publishing and exporting artifacts from the server environment
for web services client applications

## About this task

- Web Service Definition Language (WSDL) files describing the web
service endpoint, the port types and operations that make up the Business
Process Choreographer web services API (always required for the web service proxy generation).
- XML Schema Definition (XSD) files containing definitions of data
types referenced by services in the Business Process Choreographer
WSDL files (always required for the web service proxy generation).
- Your own WSDL and XSD files describing interfaces and data types
for your BPEL processes or human tasks running on the process server.
These additional files are only required if your client application
needs to interact directly with your BPEL processes or human tasks
through the web services APIs. They are not necessary if your client
application is only going to invoke operations that can be fulfilled
by Business Process Choreographer without direct interaction with
your process or task instances, such as issuing queries.
- Web Service Policy (WS-Policy) files describing the quality of
service attributes for the web services API. You can export these
files as a basis for creating client-side web service policies. 
WS-Security 
The request message must contain either a UserName token or an
LPTA token.
WS-Transaction 
The request message can contain a WS-AtomicTransaction context.
If this context is present, the request is processed in the transaction
scope of the caller.

After these artifacts are published, you need to copy
them to your client programming environment, where they are used to
generate a web service proxy and helper
classes.

- Publishing Business Process Choreographer WSDL files

A Web Service Definition Language (WSDL) file contains a detailed description of all the operations available with a web services API. Separate WSDL files are available for the Business Flow Manager and Human Task Manager web services APIs. These files are used to generate a web service proxy for your application.
- Exporting WSDL and XSD files for BPEL process and human task web services applications

BPEL processes and human tasks have well-defined interfaces that allow them to be accessed externally as web services. You need to export the WSDL interface definitions and the XML Schema data type definitions to your client programming environment.