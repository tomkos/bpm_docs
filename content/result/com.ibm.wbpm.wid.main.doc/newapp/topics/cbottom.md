<!-- image -->

# Business services: Bottom-up development

When using the Bottom-up development approach to build
a module assembly, you will implement your business logic first and
then wire the artifacts together in the assembly diagram.

For this type of development, SCA implementations (such
as business processes, state machines, and so forth) that provide
the required services (business logic) for your application are available.
These implementations know the interfaces of their partner references
and they have been coded to provide the right input data and expect
the required output data. Now, you want to assemble all the services
using Service Components Architecture (SCA) to resolve the references
and handle the calls from one service to the other. There are no new
implementations being created in the bottom-up development scenario.

## Bottom-up StockPortfolio sample

To illustrate
the concepts covered in this topic, we will use a simple example of
the assembly of a stock portfolio application from three existing
services. There is a CustomerQuery business process which accepts
a customer ID and returns the customer's portfolio information. It
uses two other services to retrieve the requested information.

The
following picture shows this application:

These three existing implementations
provide the SCA services:

- CustomerQuery business process retrieves the portfolio
information for a customer and invokes the other two services
- CustomerInfo state machine accesses the customer's account
information
- StockQuote business process finds out the current stock
price

For the bottom-up scenario, let us assume that there are
two modules containing the implementations for our sample:

- StockPortfolio module contains the CustomerQuery business
process and CustomerInfo state machine.
- Quote module contains the StockQuote business process.

We will assemble the application in the StockPorfolio module.

## Bottom-up development steps

This topic provides
some general instructions on how you can use the assembly editor to
assemble the integrated application. Detailed step-by-step instructions
on how to use tools will not be covered but they are available from
the related information at the end of this topic.

Also, we
assume that interfaces and business objects that are required by both
modules are already made available, for example, by storing them in
a library and dependency on the library is set for both modules to
access the resources.

Here are the steps:

1. Create exports for services outside of the module
SCA
services from a module must be available as an export so that they
can be used in another module. Open the Quote assembly diagram. If
the assembly diagram is empty, drag the StockQuote implementation
into the assembly diagram to create a component. In the assembly diagram
select the StockQuote component and right-click to select Export and
the export is created. Select the binding that you want to use for
the communication, for example, SCA binding.
For bindings information,
see "Generating bindings for imports and exports" topic under related
tasks. 
Here is the StockQuote component with its export in
the Quote assembly diagram:

The StockQuote service can now be accessed via its
export.
2. Create the components in the assembly diagram
Open the
StockPortfolio module assembly. Drag the CustomerQuery process and
CustomerInfo state machine implementations into the assembly diagram.
The implementations are created as components with interfaces and
references, as shown in this assembly diagram:
3. Create imports for services in other modules
From the
Business Integration view, find the export for StockQuote component
(StockQuoteExport) under the Quote module assembly. Drag it into the
StockPortfolio assembly diagram and an import is created. Select the
import with web service binding and you have the following diagram:

Rename the Import1 to StockQuoteImport
to make it easy to identify.
4. Wire the artifacts
Now, we can wire all
the artifacts in the assembly diagram. Select CustomerQuery, right-click
and select Wire to Existing and the wiring
is completed for the diagram, as shown here: 

In bottom-up development,
where the components already have interfaces and references defined,
the Wire to Existing action is a quick way
to do the wiring. See "Adding and wiring components" under related
tasks for more information on the different ways to do wiring.

We have finished using the bottom-up approach to build the
required application. If a component in the assembly diagram has to
be used outside of the module, then create an export for the component's
interface.