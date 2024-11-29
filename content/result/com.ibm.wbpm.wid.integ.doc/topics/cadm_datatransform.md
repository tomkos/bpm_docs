<!-- image -->

# Data format transformation in imports and exports

- For export bindings, in which a client application sends requests
to and receives responses from an SCA component, you indicate the
format of the native data. Depending on the format, the system selects
the appropriate data handler or data binding to transform the native
data to a business object (which is used by the SCA component) and
conversely to transform the business object to native data
(which is the response to the client application).
- For import bindings, in which an SCA component sends requests
to and receives responses from a service outside the module, you indicate
the data format of the native data. Depending on the format, the system
selects the appropriate data handler or data binding to transform
the business object to native data and vice versa.

IBM Integration
Designer provides
a set of predefined data formats and corresponding data handlers or
data bindings that support the formats. You can also create
your own custom data handlers and register the data format for those
data handlers. For more information, see the Developing data handlers topic
in the IBM Integration
Designer information
center.

- Data handlers are protocol-neutral and transform
data from one format to another. In IBM Integration
Designer, data
handlers typically transform native data (such as XML, CSV, and COBOL)
to a business object and a business object to native data. Because
they are protocol-neutral, you can reuse the same data handler with
a variety of export and import bindings. For example, you
can use the same XML data handler with an HTTP export or import binding
or with a JMS export or import binding.
- Data bindings also transform native data to a business
object (and vice versa), but they are protocol-specific. For example,
an HTTP data binding can be used with an HTTP export or import binding only.
Unlike data handlers, an HTTP data binding cannot be reused with an
MQ export or import binding.Note:  Three
HTTP data bindings (HTTPStreamDataBindingSOAP, HTTPStreamDataBindingXML,
and HTTPServiceGatewayDataBinding) are deprecated as of IBM Integration
Designer Version
7.0. Use data handlers whenever possible.

As noted earlier, you can create custom data handlers, if
necessary. You can also create custom data bindings; however,
it is recommended that you create custom data handlers because they
can be used across multiple bindings.

- Data handlers

Data handlers are configured against export and import bindings to transform data from one format to another in a protocol-neutral fashion. Several data handlers are provided as part of the product, but you can also create your own data handler, if necessary. You can associate a data handler with an export or import binding at one of two levels: you can associate it with all operations in the interface of the export or import, or you can associate it with a specific operation for the request or response.
- Data bindings

Data bindings are configured against export and import bindings to transform data from one format to another. Data bindings are specific to a protocol. Several data bindings are provided as part of the product, but you can also create your own data binding, if necessary. You can associate a data binding with an export or import binding at one of two levels-you can associate it with all operations in the interface of the export or import, or you can associate it with a specific operation for the request or response.