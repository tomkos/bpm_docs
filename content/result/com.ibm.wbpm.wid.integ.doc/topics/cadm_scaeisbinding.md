<!-- image -->

# EIS bindings

Your SCA components might require that data be transferred to or
from an external EIS. When you create an SCA module requiring such
connectivity, you will include (in addition to your SCA component)
an import or export with an EIS binding for communication with a specific
external EIS.

Resource adapters in IBM Integration Designer are used within the
context of an import or an export. You develop an import or an export
with the external service wizard and, in developing it, include the
resource adapter. An EIS import, which lets your application invoke
a service on an EIS system, or an EIS export, which lets an application
on an EIS system invoke a service developed in IBM Integration Designer,
are created with a resource adapter. For example, you would create
an import with the JD Edwards adapter to invoke a service on the JD
Edwards system.

When you use the external service wizard, the EIS binding information
is created for you. You can also use another tool, the assembly editor,
to add or modify binding information. See the Adapters for more information.

After the SCA module containing the EIS binding is deployed to
the server, you can use the administrative console to view information
about the binding or to configure the binding.

- EIS bindings overview

The EIS (enterprise information system) binding, when used with a JCA resource adapter, lets you access services on an enterprise information system or make your services available to the EIS.
- Key features of EIS bindings

An EIS import is a Service Component Architecture (SCA) import that allows components in the SCA module to use EIS applications defined outside the SCA module. An EIS import is used to transfer data from the SCA component to an external EIS; an EIS export is used to transfer data from an external EIS into the SCA module.
- JCA Interaction Spec and Connection Spec dynamic properties

The EIS binding can accept input for the InteractionSpec and ConnectionSpec specified by using a well-defined child data object that accompanies the payload. This allows for dynamic request-response interactions with a resource adapter through the InteractionSpec and component authentication through the ConnectionSpec.
- External clients with EIS bindings

The server can send messages to, or receive messages from, external clients using EIS bindings.