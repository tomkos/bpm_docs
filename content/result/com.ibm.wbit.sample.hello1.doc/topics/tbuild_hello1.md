<!-- image -->

# Build it yourself

You can use the many tools of IBM® Integration
Designer to build the sample yourself.

To build the sample, you will complete the following steps:

1. Import the existing web service into your workspace.
2. Create a library project.
3. Copy the web service WSDL file. This is a concrete WSDL file for the supplied web service that
describes its interface and its SOAP binding.
4. Create the new service interface. In the library you will create a new business object and new
interface.
5. Create a mediation module project that references the library.
6. Create an assembly with a mediation flow component. That component is exported with an SCA
binding, and has a reference that is fulfilled by a web service import.
7. Create the mediation flow implementation, which includes mapping the request parameters between
the exported and imported services and the returned result.

- Import the existing web service into your workspace

To build this sample, you need the HelloService sample web service. This is pre-supplied for you and represents an existing web service you want to call, which takes a string and returns "Hello string".
- Create a library project

In IBM Integration Designer, a library is a project where you can place files that are needed by more than one module. Because you need to eventually share your new service's interface and business object artifacts with the Hello World Part 2 sample, you need a library to hold them. Otherwise, you could create them directly into your module.
- Copy the web service file

One use for the new library is to contain the endpoint WSDL file for the supplied web service you want to invoke.
- Create the new service interface

Your service will concatenate three input strings; namely, a title, a first name, and a last name. To hold these fields you need to create a business object and then an interface that takes one of these business objects as input and returns the concatenated string "Hello title firstname lastname".
- Create a mediation module project that references the library

A mediation module is a project containing service integration logic that can be deployed to either IBM Workflow Server.
- Assemble the mediation module

Next, you create an export that allows other modules to call the mediation flow component, and create an import that invokes the HelloWorld service. Wire together the export, mediation flow, and import to produce a deployable module.
- Create the mediation flow implementation

Finally, it is time to create the implementation for the HelloWorldMediation component. This component is a mediation flow and was created for you when you created the mediation module, although you could also create one by dragging a mediation flow from the palette. Because of the type of the component, you will use the mediation flow editor to implement it.