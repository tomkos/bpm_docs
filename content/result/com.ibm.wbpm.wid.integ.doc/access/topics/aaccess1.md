<!-- image -->

# Calling services

You can use an import to access functions that are
not a part the module that you are assembling. An export is a published interface from a component or import to offer its
service to the outside world, for example, as a web service. Stand-alone references allow a Java™ program to start SCA components or imports.

## Business objects and interfaces
for imports and exports

If you plan to use imports and
exports in assembly diagrams, it is a good practice to put the business
objects and interfaces that are used by the import and exports into
a library so that they can be shared. Then, add a dependency on the
library to all of the modules that use these common resources. Avoid
copying the same business objects and interfaces into different modules
to use them.

- Imports

You can use an import to access functions that are not a part of the module that you are assembling.
- Exports

An export is a published interface from a component or import that offers its service to the outside world, for example, as a web service.
- Stand-alone references

You can use Stand-alone references in a Java program to invoke SCA components or imports.
- Export and import binding overview

An export lets you make services in an integration module available to external clients, and an import makes it possible for your SCA components in an integration module to call external services. The binding associated with the export or import specifies the relationship between protocol messages and business objects. It also specifies the way that operations and faults are selected.
- Binding types

You use protocol-specific bindings with imports and exports to specify the means of transporting data into or out of a module.
- Export and import binding configuration

One of the key aspects of export and import bindings is data format transformation, which indicates how data is mapped (deserialized) from a native wire format to a business object or how it is mapped (serialized) from a business object to a native wire format. For bindings associated with exports, you can also specify a function selector to indicate which operation should be performed on the data. For bindings associated with exports or imports, you can indicate how faults that occur during processing should be handled.
- Interoperability between SCA modules and Open SCA services

The IBM® WebSphere® Application Server V7.0 Feature Pack for Service Component Architecture (SCA) provides a simple, yet powerful programming model for constructing applications based on the Open SCA specifications. The SCA modules of IBM Integration Designer use import and export bindings to interoperate with Open SCA services developed in a Rational® Application Developer environment and hosted by the WebSphere Application Server Feature Pack for Service Component Architecture.
- Version-aware bindings

Process applications can contain SCA modules that include import and export bindings. When you co-deploy applications, the binding for each version of the application must be unique. Some bindings are automatically updated during deployment to ensure the uniqueness between versions. In other cases, you have to update the binding after deployment to ensure its uniqueness.
- Bindings

Imports and exports require binding information. Binding information specifies the means of transporting the data from the modules.
- SCA bindings

Service Component Architecture (SCA) bindings are used for SCA invocations between modules running in the same runtime cell. This binding is simple to configure and provides seamless integration between modules.
- Web service bindings

You can use a web service binding to invoke existing web services and expose functionality within the module as a web service. A web service binding offers a way to enable an import or export for remote calls, or for a data request.
- Creating exports

You can create an export for a component so that its business service can be used by other modules.
- Creating imports

You can create an import to use an existing service that is not part of the module that you are assembling.
- Deleting exports and imports

You can delete an export or import in the assembly editor, along with any resources that directly support the export or import binding.
- Invoking a service from another module

Mediation modules and business integration modules have interfaces in their exports. You can invoke any type of module from any other type of module.
- Generating SCA bindings

The Service Component Architecture (SCA) binding is simple to configure and provides seamless integration between modules. You can generate SCA bindings automatically in the assembly editor.
- Importing the ServiceGateway interface and schema

A service gateway has a single generic export and a single generic gateway interface. The generic gateway interface named ServiceGateway, along with schema files, is provided for you. You can import the predefined service gateway resources into your module or library.
- WSDL import and export files

Web Services Description Language (WSDL) files are commonly shared among users working on service-oriented architecture (SOA) projects. You can import and export WSDL files with options to make the WSDL files interoperable with different vendors, and reusable within your workspace.
- Changing an external service without interruption

When you design a system or develop modules, it is sometimes helpful to place an intermediary module between a module and an external service that it invokes. You can use this approach only if you use SCA bindings.