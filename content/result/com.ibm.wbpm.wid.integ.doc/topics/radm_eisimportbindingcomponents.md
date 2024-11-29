<!-- image -->

# Key features of EIS bindings

## Imports

The role of the EIS import is to bridge the gap between SCA components and external EIS systems.
External applications can be treated as an EIS import. In this case, the EIS import sends data to
the external EIS and optionally receives data in response.

The EIS import provides SCA components with a uniform view of the applications external to the
module. This allows components to communicate with an external EIS, such as SAP, Siebel, or
PeopleSoft, using a consistent SCA model.

On the client side of the import, there is an interface, exposed by the EIS import application,
with one or more methods, each taking data objects as arguments and return values. On the
implementation side, there is a Common Client Interface (CCI) implemented by a resource adapter.

The runtime implementation of an EIS import connects the client-side interface and the CCI. The
import maps the invocation of the method on the interface to the invocation on the CCI.

Bindings are created at three levels: the interface binding, which then uses the contained method
bindings, which in turn use data bindings.

The interface binding relates the interface of the import to the connection to the EIS system
providing the application. This reflects the fact that the set of applications, represented by the
interface, is provided by the specific instance of the EIS and the connection provides access to
this instance. The binding element contains properties with enough information to create the
connection (these properties are part of the
javax.resource.spi.ManagedConnectionFactory instance).

The method binding associates the method with the specific interaction with the EIS system. For
JCA, the interaction is characterized by the set of properties of the
javax.resource.cci.InteractionSpec interface implementation. The interaction
element of the method binding contains these properties, along with the name of the class, thus
providing enough information to perform the interaction. The method binding uses data
bindings describing the mapping of the argument and result of the interface method to EIS
representation.

1. The method on the import interface is invoked using the SCA programming model.
2. The request, reaching the EIS import, contains the name of the method and its
arguments.
3. The import first creates an interface binding implementation; then, using data from the
import binding, it creates a ConnectionFactory and associates the two.
That is, the import calls setConnectionFactory on the interface binding.
4. The method binding implementation matching the invoked method is created.
5. The javax.resource.cci.InteractionSpec instance is created and populated;
then, data bindings are used to bind the method arguments to a format understood by the
resource adapter.
6. The CCI interface is used to perform the interaction.
7. When the call returns, the data binding is used to create the result of the invocation,
and the result is returned to the caller.

## Exports

The role of the EIS export is to bridge the gap between an SCA component and an external EIS.
External applications can be treated as an EIS export. In this case, the external application sends
its data in the form of periodic notifications. An EIS export can be thought of as a subscription
application listening to an external request from an EIS. The SCA component that uses the EIS export
views it as a local application.

The EIS export provides SCA components with a uniform view of the applications external to the
module. This allows components to communicate with an EIS, such as SAP, Siebel, or PeopleSoft, using
a consistent SCA model.

The export features a listener implementation receiving requests from the EIS. The listener
implements a resource adapter-specific listener interface. The export also contains a component
implementing interface, exposed to the EIS through the export.

The runtime implementation of an EIS export connects the listener with the component implementing
interface. The export maps the EIS request to the invocation of the appropriate operation on the
component. Bindings are created at three levels: a listener binding, which then uses a contained
native method binding, which in turn uses a data binding .

The listener binding relates the listener receiving requests with the component exposed through
the export. The export definition contains the name of the component; the runtime locates it and
forwards requests to it.

The native method binding associates the native method or the event type received by the listener
to the operation implemented by the component exposed by way of the export. There is no relationship
between the method invoked on the listener and the event type; all the events arrive through one or
more methods of the listener. The native method binding uses the function selector defined in the
export to extract the native method name from the inbound data and data bindings to bind
the data format of the EIS to a format understood by the component.

1. The EIS request triggers invocation of the method on the listener implementation.
2. The listener locates and invokes the export, passing to it all the invocation
arguments.
3. The  export creates the listener binding implementation.
4. The  export instantiates the function selector and sets it on the listener binding.
5. The export initializes native method bindings and adds them to the listener binding.
For each native method binding, the data bindings are also initialized.
6. The export invokes the listener binding.
7. The listener binding locates exported components and uses the function selector to retrieve the
native method name.
8. This name is used to locate the native method binding, which then invokes the target component.

The adapter interaction style allows for the EIS export binding to invoke the target component
either asynchronously (the default) or synchronously.

## Resource adapters

You develop an import or an export with the external service wizard and, in developing it,
include a resource adapter. The adapters that come with IBM® Integration
Designer used to access CICS, IMS, JD Edwards,
PeopleSoft, SAP and Siebel systems are intended for development and test purposes only. This means
you use them to develop and test your applications.

Once you deploy your application, you will need licensed runtime adapters to run your
application. However, when you build your service you can embed the adapter with your service. Your
adapter licensing might allow you to use the embedded adapter as the licensed runtime adapter. These
adapters are compliant with the Java EE Connector Architecture (JCA 1.5). JCA, an open standard, is
the Java EE standard for EIS connectivity. JCA provides a managed framework; that is, Quality of
Service (QoS) is provided by the application server, which offers lifecycle management and security
to transactions. They are also compliant with the Enterprise Metadata Discovery specification with
the exception of IBM CICS ECI Resource Adapter and IBM IMS Connector for Java.

The WebSphere Business Integration Adapters, an older set of adapters, are also supported by the
wizard.

## Java EE resources

The EIS module, an SCA module that follows the EIS module pattern, can be deployed to the Java EE
platform.

The deployment of the EIS module to the Java EE platform results in an application that is ready
to start, packaged as an EAR file and deployed to the server. All Java EE artifacts and resources
are created; the application is configured and ready to be run.