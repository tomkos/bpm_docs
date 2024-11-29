<!-- image -->

# Interoperability between SCA modules and Open SCA services

An SCA application invokes an Open SCA application by way of an
import binding. An SCA application receives a call from an Open SCA
application by way of an export binding. A list of supported bindings
is shown in Invoking services over interoperable bindings.

## Invoking Open SCA services from SCA modules

Figure 1. Component
in SCA module invoking Open SCA service

<!-- image -->

No special configuration is required to invoke an Open
SCA service.

1 To obtain the name of the target component and service from theOpen SCA composite, perform the following steps:
    1. Ensure that the Properties  tab is open
by clicking Window > Show
View > Properties.
    2. Open the composite editor by double-clicking the composite diagram
that contains the component and service. For example, for a component
named customer, the composite diagram is customer.composite\_diagram.
    3. Click the target component.
    4. In the Name field of the Properties tab,
note the name of the target component.
    5. Click the service icon associated with the component.
    6. In the Name field of the Properties tab,
note the name of the service.
2 To configure the IBM IntegrationDesigner importto connect it to the Open SCA service, perform the following steps:

1. In IBM Integration
Designer, navigate to the Properties tab of
the SCA import that you want to connect to the Open SCA service.
2. In the Module name field, enter the component
name from step 1.d.
3. In the Export name field, enter the service
name from step 1.f.
4. Save your work by pressing Ctrl+S.

## Invoking SCA modules from Open SCA services

Figure 2. Open SCA service invoking component in SCA module

<!-- image -->

To connect to an SCA component by way of an Open SCA
reference binding, you provide the module name and export name.

1 To obtain the name of the target module and export, perform thefollowing steps:
    1. In IBM Integration
Designer, open the module in the assembly editor by double-clicking
the module.
    2. Click the export.
    3. In the Name field of the Properties tab,
note the name of the export.
2 Configure the Open SCA reference that you want to connect to the IBM IntegrationDesigner moduleand export:

1. In  Rational Application
Developer, open the composite editor by double-clicking the composite
diagram that contains the component and service.
2. Click the reference icon of the component reference to display
the reference properties in the Properties tab.
3. Click the Binding tab on the left side
of the page.
4. Click Bindings and then click Add.
5. Select the SCA binding.
6. In the Uri field, enter the IBM Integration
Designer module
name, followed by a slash (/), followed by the export name
(which you determined in step 1.c).
7. Click OK.
8. Save your work by pressing Ctrl+S.

## Invoking services over interoperable
bindings

- SCA bindingIn IBM IntegrationDesigner , whenan SCA module invokes an Open SCA service by way of an SCA importbinding, the following invocation styles are supported: The SCA import interface and the OpenSCA service interface must use a web services interoperability (WS-I)compliant WSDL interface. Note that the SCA binding supportstransaction and security context propagation.
    - Asynchronous (one-way)
    - Synchronous (request/response)

The SCA import interface and the Open
SCA service interface must use a web services interoperability (WS-I)
compliant WSDL interface.

Note that the SCA binding supports
transaction and security context propagation.

- Web service (JAX-WS) binding with either theSOAP1.1/HTTP or SOAP1.2/HTTP protocol The SCAimport interface and the Open SCA service interface must use a webservices interoperability (WS-I) compliant WSDL interface. Inaddition, the following qualities of service are supported:

The SCA
import interface and the Open SCA service interface must use a web
services interoperability (WS-I) compliant WSDL interface.

In
addition, the following qualities of service are supported:

- Web Services Atomic Transaction
- Web Services Security
- EJB bindingA Java™ interface
is used to define the interaction between an SCA module and an Open
SCA service when the EJB binding is used. 
Note that the EJB
binding supports transaction and security context propagation.
- JMS bindings The SCA import interface and the Open SCA serviceinterface must use a web services interoperability (WS-I) compliantWSDL interface. The following JMS providers are supported:

The SCA import interface and the Open SCA service
interface must use a web services interoperability (WS-I) compliant
WSDL interface.

- WebSphere Platform
Messaging (JMS Binding)
- WebSphere MQ (MQ JMS
Binding)