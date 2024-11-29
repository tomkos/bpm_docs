<!-- image -->

# Generating an HTTP import binding

## Before you begin

## About this task

If you intend to use the predefined
HTTP bytes data binding then you must use the following schema and
data handler. Under Predefined Resources in
the Dependencies editor, select Native Body schema for
Native Body DataHandler. Save your work and close the
dependencies editor.

If you intend to use the predefined HTTP
bytes data binding with a static service gateway then you must also
add the service gateway interface and schema files. To add this interface
and schema files to your module, open the dependencies editor. Under Predefined
Resources, select Service gateway interface
and schema files. Save your work and close the dependencies
editor.

## Procedure

1. Open the assembly editor. Under Outbound Imports,
select HTTP and drag it to the assembly editor.
Select an interface or create one. Alternately, from
the palette under Components, select an import
and drag it on to the canvas. An import with no implementation and
no interface is created. Right-click the import, select Add Interface from
the menu and add an interface describing your interaction with a client.
Generate the HTTP binding by selecting the import and from the menu
selecting Generate Binding > HTTP Binding.
2 The Configure HTTP Import Service windowbox opens. In the End-point configuration section,enter the Uniform Resource Locator (URL) your binding will requestdata from. In the Default data format field,select how the data will be serialized between the business objectand the HTTP message with a binding. To change the default, click Select besidethe field to launch the Data Transformation Configuration window.Your selections are as follows: In the next section, if you want to use the TargetFunctionNamemessage header property to be used with module to module communication,select it. If you want to use the default module to module fault handling,which is a SOAP transport, select it. Click OK . The HTTPbinding is created and shown in the properties view when the Binding tabis selected. Sub tabs under the binding tab provide binding informationdetails, which are discussed in the next steps. The HTTP bindingis complete as is with some qualifications:

In the End-point configuration section,
enter the Uniform Resource Locator (URL) your binding will request
data from.

In the Default data format field,
select how the data will be serialized between the business object
and the HTTP message with a binding. To change the default, click Select beside
the field to launch the Data Transformation Configuration window.
Your selections are as follows:

    - Use a data format transformation in the binding registry. This
list includes the Prepackaged HTTP data format transformations. Selecting Show
the deprecated data format transformations adds previous
transformations that have been deprecated.
    - Use a custom data format transformation you have created in your
workspace
    - Create a new Creating a data format transformation resource configuration.

In the next section, if you want to use the TargetFunctionName
message header property to be used with module to module communication,
select it. If you want to use the default module to module fault handling,
which is a SOAP transport, select it.

Click OK. The HTTP
binding is created and shown in the properties view when the Binding tab
is selected. Sub tabs under the binding tab provide binding information
details, which are discussed in the next steps.

    - The interface has only a single operation or, if it has more than
one operation, they all use the same URL address.
    - The target service is not using the Secure Sockets Layer (SSL)
and does not require basic authentication.
    - The request and, if necessary, response does not need to use a
proxy.
    - The target service does not need any special headers to be set
up.
    - The target service can be called with the default HTTP method
preselected by the handler based on the set of assumptions derived
from the interface structure.
3. In the Properties view, selecting
the Binding tab displays the service level
configuration properties, which can be edited as discussed previously.
The endpoint URL and data binding configuration are shown. Note that
the URL at the method binding level will override this URL. The
HTTP version and HTTP method, GET by default in a two-way operation
and POST in a one-way operation, are shown. The HTTP methods available
are: DELETE, GET, HEAD, OPTIONS, POST, PUT, TRACE. A description of
the binding may be added.
4. Advanced configuration has the same
tabs as described in the next step - HTTP Headers, HTTP Proxy, Security
and Performance - but sets the values in these containers at the service
level; that is, for the entire service. Method binding properties
take precedence over these ones.
5 Selecting Method bindings and the Generic tabdisplays the method level properties that can be edited. The propertieslist the endpoint URL, HTTP method and version and provide a fieldfor a method binding description. These properties only apply to themethod level and changing them will only affect the method level,not the entire service. All method level binding properties overridethe binding level properties. In the next section,if you want to use the TargetFunctionName message header propertyto be used with module to module communication, select it. If youwant to use the default module to module fault handling, which isa SOAP transport, select it. The Data Serialization tablets you change the input and output data binding configuration. Selecting the HTTP Headers tab lets you choose the transport and contentencoding. Defaults are provided, but you can select different types of compression for the contentand use chunking for an alternate transfer method. There are a range of media types and charactersets that are displayed in drop-down lists. The HTTP 1.1 specification discusses these header fields in detail. To send the Content-Type without a character set, such asContent-Type : application/json instead of Content-Type :application/json;charset=UTF-8 , clear the choice and add the keyword<UNSET> for the character set. The TargetFunctionName header value isdisplayed. This value corresponds to the operation that should be invoked on the application that isbeing called by the import. Proxy servers service the requests of clients. Ifyou want to use a proxy server, the HTTP Proxy tabpresents fields for the host name, port and security attributes. The Security tablets you add a Secure Sockets Layer (SSL) authentication alias anda basic authentication alias. These aliases need to be configuredon the server manually to work as they are not created on the deploymentof your service. Configure these properties: The Performance tablets you set a timeout value and number of retries value to minimizelengthy delays at run time.

In the next section,
if you want to use the TargetFunctionName message header property
to be used with module to module communication, select it. If you
want to use the default module to module fault handling, which is
a SOAP transport, select it.

The Data Serialization tab
lets you change the input and output data binding configuration.

Selecting the HTTP Headers tab lets you choose the transport and content
encoding. Defaults are provided, but you can select different types of compression for the content
and use chunking for an alternate transfer method. There are a range of media types and character
sets that are displayed in drop-down lists. The HTTP 1.1 specification discusses these header fields in detail. To send the Content-Type without a character set, such as
Content-Type : application/json instead of Content-Type :
application/json;charset=UTF-8, clear the choice and add the keyword
<UNSET> for the character set. The TargetFunctionName header value is
displayed. This value corresponds to the operation that should be invoked on the application that is
being called by the import.

Proxy servers service the requests of clients. If
you want to use a proxy server, the HTTP Proxy tab
presents fields for the host name, port and security attributes.

The Security tab
lets you add a Secure Sockets Layer (SSL) authentication alias and
a basic authentication alias. These aliases need to be configured
on the server manually to work as they are not created on the deployment
of your service.

- SSL Configuration name: Select one of the existing SSL configuration
settings which are defined in WAS admin console: SSL certificate and key management > SSL
configurations. By default, 'CellDefaultSSLSettings' is recommended.
- Basic Authentication Alias: The authentication alias defined in WAS admin
console: Global security > Java Authentication and
Authorization Service > J2C authentication data. You
need to specify the username and password to login remote http server.

The Performance tab
lets you set a timeout value and number of retries value to minimize
lengthy delays at run time.

6 Selecting the Faults configuration tablets you configure the faults specified on the operations in the interface.The configuration of faults is optional. The configuration can applyto all operations or a specific operation. If faultconfiguration is new to you, see Handling faults in bindings foran overview. Click Select beside Faultselector to configure a fault. Your selections are asfollows: Specifying a fault selector requires that you also specifythe data format for the fault. Click Select beside Businessfault data format . Your selections are as follows: Expanding Advanced , lets you alsospecify the data format for a runtime exception.

If fault
configuration is new to you, see Handling faults in bindings for
an overview.

Click Select beside Fault
selector to configure a fault. Your selections are as
follows:

- Use a fault selector in the binding registry. This list includes
the Prepackaged HTTP fault selectors.
- Use a custom fault selector you have created in your workspace
- Create a new Creating a fault selector resource configuration.

- Use a data format transformation in the binding registry. This
list includes the Prepackaged HTTP data format transformations.
- Use a custom data format transformation you have created in your
workspace
- Create a new Creating a data format transformation resource configuration .

Expanding Advanced, lets you also
specify the data format for a runtime exception.

7. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that run time or
application. The default is to use runtime context propagation. See Propagation.
8. The Summary page maps a method on
the interface to a URL address that the application will call when
the import is invoked with this method.

## Related concepts

- HTTP binding overview
- Uses of the HTTP binding
- HTTP data bindings

## Related tasks

- Generating an HTTP export binding

## Related reference

- Example of the HTTP binding
- Limitations of the HTTP binding