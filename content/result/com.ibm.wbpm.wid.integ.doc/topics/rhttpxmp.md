<!-- image -->

# Example of the HTTP binding

Creating and configuring HTTP import or HTTP export bindings is not as simple as using a web
browser to access data. The application demonstrates how HTTP bindings can be used to make the
application consumable by HTTP clients, how to consume an external HTTP XML service, and how to
integrate SCA application modules using HTTP. For each scenario, specific configuration points are
covered. Also shown, are how to create a custom mediation module and a custom data binding with an
HTTP binding.

## Scenarios shown in the example

The following
scenarios are shown in the example:

- Scenario 1: An SCA application is exposed through an HTTP GET
operation that returns a response message in XML format. The sample
application demonstrates how the HTTP export binding can use plain
XML or Atom feed format. In this case, a client running in the web
browser invokes the SCA application through the an HTTP URL that defines
the application's entry point. As a result, a business integration
application is exposed using the easy-to-use interface of the web
browser.
- Scenario 2: An SCA application is exposed through an HTTP POST
operation which accepts requests in the XML format as an input. This
scenario shows the use of Asynchronous JavaScript and XML (AJAX) as the front
end of an SCA application and is an example of a starting point for
those wishing to build a rich internet application utilizing the SCA
architecture.
- Scenario 3: An SCA application invokes an external service through
the HTTP GET operation. In this scenario, the service response format
is in XML. This scenario highlights how third party lightweight web
services using Atom (Atom is an XML-based file format used to syndicate
content such as blogs) and RSS feeds and services based on Representational
State Transfer (REST) can be integrated into an SCA application.
- Scenario 4: HTTP bindings are used as an integration point of
multiple SCA applications utilizing the HTTP infrastructure as a communication
mechanism. One SCA application is configured to invoke another SCA
application through HTTP export and import bindings.

## Description of the example

The goal of the
application is to expose an internal data source named Customers (an
XML file) to the web using Web 2.0 technologies: a Google map and
an Atom feed. To display the customers' locations in this file on
the map, a third party Representational State Transfer (REST) service,
geocoder.ca, is used, which returns the latitude and longitude of
any address in the United States and Canada.

Two SCA modules,
a library module and a client web application, are created in the
example. The library module contains a Web Service Description Language
(WSDL) interface and business objects. A CustomerLocations mediation
module is used to expose the SCA application through HTTP bindings.
The mediation module contains two HTTP export binding components (CustomerLocationsExportAsFeed
and CustomerLocationsExportAsXML), a custom mediation component (CustomerLocations)
that processes a URL query and forwards the request onward to another
SCA component, and an HTTP import binding component (GetCustomersWithLocationsHTTPImport)
that invokes the Customers module using HTTP.

The Customers
module consists of an HTTP import binding (GetCoordinates) used to
invoke the external REST service provided by geocoder.ca. It also
includes an HTTP export binding component (GetCustomersWithLocationExport)
invoked by the HTTP import binding component from the CustomerLocations
mediation module, a simple Java™ component
that loads an XML file and returns a list of Customers business objects.
The HTTP export binding (AddCustomerExport) is used by an external
application to add new Customers to the XML repository by using a
POST operation to send an XML file over HTTP. A Business Process Execution
Language (BPEL) component (GetCustomersWithLocations) ties the application
together by invoking the REST service for each customer retrieved
from the XML repository.

The HTTPExportToGoogleMap web project
contains an HTML page (customersMap.html) that is designed to create
a mashup that displays the customers' locations on the Google
map. It also allows the filtering of the Customers that get displayed
based on their type.

The application also contains
another HTML page (addCustomer.html) that allows a user to add new
customers to the data source by invoking an HTTP export binding component
through the HTTP POST operation.

## Related concepts

- HTTP binding overview
- Uses of the HTTP binding
- HTTP data bindings

## Related tasks

- Generating an HTTP import binding
- Generating an HTTP export binding

## Related reference

- Limitations of the HTTP binding