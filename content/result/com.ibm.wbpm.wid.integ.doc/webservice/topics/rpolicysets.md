<!-- image -->

# Policy sets

A policy set is a collection of policy types, each of which provides a quality of service. These
types have been configured and can be associated with a web service provider or consumer.

- Associate a policy set with imports and exports. Only the SOAP1.2/HTTP and the SOAP1.1/HTTP
transport protocols support policy sets. Note: A policy set can't be associated with the
SOAP1.1/HTTP using JAX-RPC transport protocol.
- Have the same policy set on the service requester as on the service provider.
- If you create multiple web service imports that share the same WSDL in one SCA module, use the
same policy set and bindings for each of the imports.
- On an import, have the same policy set on the import binding as on the service provider it is
calling.
- On an export, have the same policy set on the export binding as on the client.

To find the policy set properties and how to set them on the web services binding, complete the
following steps:

1. Select your import or export and then select the Properties view.
2. Click the Policy Sets tab.
3. No policy set is specified by default. To select a policy set for your operations, make your
selection from the drop-down list of the Default policy set field. A
description is shown for each policy set.You can find the complete list of available policy sets
including a description of each one by selecting Window > Preferences and selecting Service Policies from the list of
preferences.
4. Select a binding from the Binding list. The binding is used to configure
how the server implements the default policy set.
5. Save the configuration.

You can export policy sets from a WebSphere server as discussed in Exporting policy sets using the administrative console. To import a policy set into IBM® Integration
Designer, select File > Import. Then select Web services > WebSphere Policy Sets. Click
Next, browse to the policy set file, and then click
Finish to import the policy set.

For more information about policy sets, see WebSphere Application
Server Web Services Guide. If security is important for your application, this book also
contains a section called on secure conversation that you should read.