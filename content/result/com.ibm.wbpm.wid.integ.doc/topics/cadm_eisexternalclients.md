<!-- image -->

# External clients with EIS bindings

An external client, for example a web portal or an EIS, needs to
send a message to an SCA module in the server or needs to be invoked
by a component from within the server.

The client invokes the EIS import as with any other application,
using either the Dynamic Invocation Interface (DII) or Java™ interface.

1. The external client creates an instance of the ServiceManager and
looks up the EIS import using its reference name. The result of the
lookup is a service interface implementation.
2. The client creates an input argument, a generic data object, created
dynamically using the data object schema. This step is done using
the Service Data Object DataFactory interface implementation.
3. The external client invokes the EIS and obtains the required results.

1. The client creates an instance of the ServiceManager and
looks up the EIS import using its reference name. The result of the
lookup is a Java interface of the EIS import.
2. The client creates an input argument and a typed data object.
3. The client invokes EIS and obtains the required results.

The EIS export interface defines the interface of the exported
SCA component that is available to the external EIS applications.
This interface can be thought of as the interface that an external
application (such as SAP or PeopleSoft) will invoke through the implementation
of the EIS export application runtime.

The export uses EISExportBinding to bind exported
services to the external EIS application. It allows you to subscribe
an application contained in your SCA module to listen for EIS service
requests. The EIS export binding specifies the mapping between the
definition of inbound events as it is understood by the resource adapter
(using Java EE Connector Architecture interfaces) and the invocation
of SCA operations.

The EISExportBinding requires external EIS services
to be based on Java EE Connector Architecture 1.5 inbound contracts.
The EISExportBinding requires that a data handler
or data binding be specified either at the binding level or the method
level.