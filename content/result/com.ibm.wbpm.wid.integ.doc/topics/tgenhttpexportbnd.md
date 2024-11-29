<!-- image -->

# Generating an HTTP export binding

## Before you begin

## About this task

If you intend to use the predefined
HTTP bytes data binding then you must use the following schema and
data handler. Under Predefined Resources in
the Dependencies editor, select Native Body schema for
Native Body DataHandler. Save your work and close the
dependencies editor.

If you intend to use the predefined HTTP
bytes data binding with a static service gateway then you must add
the service gateway interface and schema files. To add this interface
and schema files to your module, open the dependencies editor. Under Predefined
Resources, select Service gateway interface
and schema files. Save your work and close the dependencies
editor.

## Procedure

1. Open the assembly editor. Under Inbound Exports,
select HTTP and drag it to the assembly editor.
Select an interface or create one. Alternately, from
the palette under Components, select an export
and drag it on to the canvas. An export with no implementation and
no interface is created. Right-click the export, select Add Interface from
the menu and add an interface describing your interaction with a client.
Generate the HTTP binding by selecting the export and from the menu
selecting Generate Binding > HTTP Binding.
2 The Configure HTTP Export Service windowbox opens. In the End-point configuration section,enter the context path. By default, it will be the module of yourexport. The context path is a relative URL address where the applicationproject, <project name>web, is the default context root. Inthe Default data format field, select how thedata will be serialized between the business object and the JMS messagewith a binding. To change the default, click Select besidethe field to launch the Data Transformation Configuration window.Your selections are as follows: In the Function selector section,select the function selector configuration you want to use. A functionselector selects an operation to invoke on your component at run time.Clicking Select beside the Functionselector field, launches the Function SelectorConfiguration window and provides the following selections: In the next section, if you want to use the default moduleto module fault handling, which is a SOAP transport, select it. Click OK .The HTTP binding is created and shown in the properties view whenthe Binding tab is selected. Sub tabs under the binding tabprovide binding information details, which are discussed in the nextsteps.

In the End-point configuration section,
enter the context path. By default, it will be the module of your
export. The context path is a relative URL address where the application
project, <project name>web, is the default context root.

In
the Default data format field, select how the
data will be serialized between the business object and the JMS message
with a binding. To change the default, click Select beside
the field to launch the Data Transformation Configuration window.
Your selections are as follows:

    - Use a data format transformation in the binding registry. This
list includes the Prepackaged HTTP data format transformations. Selecting Show
the deprecated data format transformations adds previous
transformations that have been deprecated.
    - Use a custom data format transformation you have created in your
workspace
    - Create a new Creating a data format transformation resource configuration.

In the Function selector section,
select the function selector configuration you want to use. A function
selector selects an operation to invoke on your component at run time.
Clicking Select beside the Function
selector field, launches the Function Selector
Configuration window and provides the following selections:

    - Use an existing function selector (default)
lists the function selector configurations available. This list includes
the Prepackaged HTTP function selectors.
    - Use a custom function selector that you have created in your workspace.
    - Create a new Creating a function selector resource configuration.

In the next section, if you want to use the default module
to module fault handling, which is a SOAP transport, select it.

Click OK.
The HTTP binding is created and shown in the properties view when
the Binding tab is selected. Sub tabs under the binding tab
provide binding information details, which are discussed in the next
steps.

3. In the Properties view, selecting
the Binding tab displays the service level
configuration properties, which can be edited. The context path, function
selector configuration and data binding configuration are shown. A
description of the binding may be added.
4. Advanced configuration has the same
tabs as described in the next step - HTTP Headers and HTTP Method
Settings - but sets the values in these containers at the service
level; that is, for the entire service. Method binding properties
take precedence over these ones.
5. Selecting Method bindings and the Generic tab
displays the method level properties that can be edited. The properties
list the context path and the native method, which will correspond
to the operation name of the interface of the export. There is a field
for a method binding description. Note that these properties only
apply to the method level and changing them will only affect the method
level, not the entire service. All method binding properties except
the context path will be appended to the binding level context path
to create a URL pointing to a specific method. All method level binding
properties override the binding level properties. The Data
Serialization tab lets you change the input and output
data binding configuration.
Selecting the HTTP Headers tab
lets you choose the transport and content encoding. Defaults are provided,
but you can select different types of compression for the content
and use chunking for an alternate transfer method. There are a range
of media types and character sets that are displayed in drop-down
lists. The HTTP 1.1 specification discusses these header fields in detail. 
The HTTP
Method Settings tab displays the HTTP methods available.
GET is the default for a two-way operation and POST is the default
for a one-way operation. The HTTP methods selectable are: DELETE,
GET, HEAD, OPTIONS, POST, PUT, TRACE. These methods may be set as
pingable and also contain a status code. 200, meaning the request
sent by the client was successful, is the default status code.
6 Selecting the Faults configuration tablets you configure the business fault data format for the faults inthe interface. The configuration of faults is optional. The configurationcan apply to all operations, a specific operation or a specific fault. If fault configuration is new to you, see Handling faults in bindings foran overview. Click Select beside Businessfault data format . Your selections are as follows:

If fault configuration is new to you, see Handling faults in bindings for
an overview.

- Use a data format transformation in the binding registry. This
list includes the Prepackaged HTTP data format transformations.
- Use a custom data format transformation you have created in your
workspace
- Create a new Creating a data format transformation resource configuration .
7. The Propagation tab lets you select
two types of context propagation. Context propagation takes information
associated with a runtime or an application and passes it along with
requests that are the result of interactions with that run time or
application. The default is to use runtime context propagation. See Propagation.
8. The Summary tab displays the method
that will be invoked on the export. The method name defaults to the
operation name of the export interface. The endpoint URL address,
which is the complete URL for the method, is formed from the application
project, <project name>web, interface name and operation name.
When the URL specified is invoked, a method with the given name is
invoked.

## Related concepts

- HTTP binding overview
- Uses of the HTTP binding
- HTTP data bindings

## Related tasks

- Generating an HTTP import binding

## Related reference

- Example of the HTTP binding
- Limitations of the HTTP binding