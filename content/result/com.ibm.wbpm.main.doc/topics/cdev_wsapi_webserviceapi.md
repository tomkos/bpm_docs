# Business Automation Workflow web
service APIs programming guide (deprecated)

Because the web API abstracts the actual technology used in Business Automation Workflow, you
can write external client applications using different technologies
such as Microsoft .NET or Java. You can use a number of toolkits depending
on the technology you are using, such as the Axis
WSDL-to-Java tool, to help you generate classes based on the
WSDL description.

- Query process instances and tasks
- Manage process instances
- Manage and synchronize tasks
- Search business data
- Manage external activities

## Compatibility considerations

The Business Automation Workflow web API
complies with the WS-I Basic Profile 1.0 standard for web service
interoperability. Complete interoperability and other guarantees for
the web API are outlined at the beginning of the WSDL.

In some
cases, you can implement versions of web service operations that are
different from the version of Workflow Server. For
complete compatibility information, see the WSDL file.

All clients
created using the web API must include a ClientInfo header object
that identifies the client to Workflow Server. This
header passes time zone and other compatibility information to Workflow Server, as
described in the WSDL.

- Web API and external implementations (deprecated)

Business Automation Workflow includes a sample external implementation that illustrates how to use Business Automation Workflow web API operations when developing a custom application to enable process participants to complete a particular step within a process instance.
- Passing and retrieving variables (deprecated)

You can pass variables to the web API by mapping Business Automation Workflow simple variable types to XML data.