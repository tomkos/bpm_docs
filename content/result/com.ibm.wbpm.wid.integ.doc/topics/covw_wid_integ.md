<!-- image -->

# Developing services with adapters

Integrating applications on Enterprise Information Systems (EIS)
with those developed locally is a key feature of IBM® Integration
Designer.
Examples of EIS systems include Enterprise Resource Planning (ERP)
systems, mainframe transaction processing systems, and database systems.
In the diagram that follows, we see some developed imports and exports
at work. A stock purchase service, StockPurchase, accesses an import,
CustomerCredit, to check on a customer's credit before purchasing
some stock for him or her. The import, created by the external service
wizard, represents an application on a CICS® server.
From the stock purchase service's perspective, the CustomerCredit
import is a local service.

Similarly, the stock purchase service is periodically notified
of stock price changes by an export, StockPrice, which the stock purchase
service interacts with as a local service. The export, created by
the external service wizard, represents an application on a PeopleSoft
server.  Another way of looking at an export is to think of it as
a subscription service listening to an external request from an EIS
system. Since imports and exports behave as local services, there
is no special management of them that you have to do. In both cases,
appropriate resource adapters and binding information provide the
means of interaction between the imports and exports and the applications
on the EIS systems.

<!-- image -->

- Using adapters in IBM Integration Designer
- Imports and exports
- Enterprise Metadata Discovery specification
- Resource adapters
- Bindings
- Messaging bindings and EIS bindings
- Business objects from data structures
- How the wizards and editors support J2C and messaging bindings
- Modules for EIS imports and exports

## Using adapters in IBM Integration
Designer

Resource
adapters in IBM Integration
Designer are
used within the context of an import or an export. You develop an
import or an export with the external service wizard and, in developing
it, include the resource adapter. An EIS import, which lets your application
invoke a service on an EIS system, or an EIS export, which lets an
application on an EIS system invoke a service developed in IBM Integration
Designer,
are created with a particular resource adapter. For example, you would
create an import with the JD Edwards adapter to invoke a service on
the JD Edwards system.

The information on creating imports
and exports with the external service wizard and an associated adapter
is contained in this section.

## Imports and exports

Finding
an application or data on an EIS system and creating an import or
export based on it follows the same pattern using the same wizard.
The external service wizard is the tool you use to find an application
on an EIS system and then generate the code for the import or export
to represent it. You can start the wizard by selecting it from the
business integration perspective menu using File > New >
External Service. You can also select the adapter you
want from the assembly editor palette, for example, the FTP adapter,
and drag it onto the canvas, which will also launch the wizard.

Once
launched, you select the adapter you will work with from a list. The
list displays the available adapters. You continue by configuring
the import or export, which means specifying the RAR file of the adapter,
logon information, where the server is located and so on. The wizard
searches the EIS system, returns the information on the applications
at the EIS system, and through some additional pages guides you through
the creation of the import and export.

The reference point of
the initiation of the transaction is what separates an import from
an export. With an import, the transaction is initiated when
your application is invoking a program on the EIS system. At run time,
this is known as an outbound call. With an export, the
transaction is initiated by the external EIS system. In other words,
the application on the EIS system is the one initiating the transaction.
At run time, this is known as an inbound call. Another way
of looking at an export in the context of EIS systems is to think
of it as a subscription service listening to an external request from
an EIS system. Exports can only be created for EIS systems that support
initiating external function calls. CICS and IMS systems, for example, do not
support initiating external function calls and hence export components
cannot be created for them.

Imports and exports are created
in a module and represent a Service Component Architecture abstraction
of the Java EE Connector Architecture (J2C) invocation models (CCI
API for outbound and MDB EJB + CCI Message Listener for inbound).
EIS imports and exports cannot be paired to represent the loosely-coupled
model similar to a JMS binding where the messaging provider acts as
a intermediary and decouples import from export. If this function
were supported for an EIS binding, you would be able to drag-and-drop
an export in the assembly editor to another module to create an import.

In
addition to generating imports and exports, the wizard also generates
business objects representing data structures on the EIS systems.

## Enterprise Metadata Discovery specification

The Enterprise Metadata Discovery specification is
a joint specification from IBM and
BEA. It has been influenced by the rapid acceptance of service-oriented
architecture as the means of inter-application communication. To realize
the benefits of a service-oriented architecture, it is critical to
have easy interoperability with EIS systems. This specification introduces
a new metadata discovery and import model for adapters and the enterprise
application integration (EAI) tools framework. The model allows adapters
to easily plug into an integration framework and improves the usability
of adapters within the framework. Any adapter that complies with this
specification can plug into any EAI tools framework that also supports
this specification. Any EAI tools framework that supports this specification
can use any adapter that implements this specification. Tools that
support Enterprise Metadata Discovery specification have become the
standard way to implement Java EE Connector Architecture (J2C)-based
applications.

The external service wizard supports the specification.
The wizard browses the metadata information of an EIS system in a
process called discovery. Then the artifacts that are of interest
to you are imported into a service description. The service description
contains all the information required to generate an implementation
of the service. It, in turn, can be deployed to an application server.
In addition to generating a service, you may be able to edit the configuration
of the adapter or service after it has been created and configured.
The tools in IBM Integration
Designer that
perform this editing function, the assembly editor and the business
object editor, are demonstrated in the task help.

The IBM WebSphere® Adapters listed in the resource
adapters section comply with the specification, with the exception
of IBM CICS ECI Resource Adapter 7.1.0.2 and IBM IMS Connector
for Java™ 9.1.0.2. The specification
defines a common API that adapters use to expose services and business
objects to tools for the generation of Java EE Connector Architecture
(J2C)-based applications.

This specification means there is
a single tool environment to support development of applications accessing
multiple EIS systems using multiple adapters. For you it means that
developing services using the external service discovery wizard will
consistently follow a similar development pattern regardless of the
EIS system you access. The specification leverages the metadata capabilities
found on many EIS systems, which provide descriptive information about
the services available from the EIS system. Simply put, the specification
provides a standard way for tools to access EIS systems using a variety
of resource adapters.

## Resource adapters

Resource
adapters, usually referred to as adapters, provide a mechanism that
allows for the integration of an existing EIS infrastructure with
the IBM Workflow
Server.
They provide a service-oriented approach to EIS integration. Adapters
offer a consistent framework for access to back-end systems and their
applications.

Selecting an adapter is the first choice you make
when you use the external service wizard. The adapters that come with IBM Integration
Designer used
to access CICS, IMS, JD Edwards, PeopleSoft, SAP and Siebel systems
are intended for development and test purposes only. This means you
use them to develop and test your applications. Once you deploy your
application, you will need licensed runtime adapters to run your application.
However, when you build your service you can embed the adapter with
your service. Your adapter licensing may allow you to use the embedded
adapter as the licensed runtime adapter.

IBM WebSphere Adapters
- These adapters are compliant to the Java Connector Architecture (J2C
1.5). J2C is an open standard. J2C is the Java EE standard
for EIS connectivity. J2C provides a managed framework; that is Quality
of Service (QoS) is provided by the application server, which offers
lifecycle management and security to transactions. They are also compliant
to the Enterprise Metadata Discovery specification discussed previously
with the exception of IBM CICS ECI Resource Adapter and IBM IMS Connector
for Java.

The following IBM WebSphere Adapters are supported in IBM Integration
Designer:

- IBM CICS ECI Resource Adapter version
- IBM IMS TM Resource Adapter version
- IBM WOLA Resource Adapter version
- IBM WebSphere Adapter for Email version
- IBM WebSphere Adapter for FTP version
- IBM WebSphere Adapter for Flat Files version
- IBM WebSphere Adapter for IBM i version
- IBM WebSphere Adapter for JDBC version
- IBM WebSphere Adapter for JD Edwards EnterpriseOne
version
- IBM WebSphere Adapter for Lotus Domino
- IBM WebSphere Adapter for Oracle E-Business
Suite version
- IBM WebSphere Adapter for PeopleSoft Enterprise
version
- IBM WebSphere Adapter for SAP Software version
- IBM WebSphere Adapter for Siebel Business
Applications Version

All adapters that were installed with the product and their
version numbers can be found in this path: <installRoot>\ResourceAdapters.
They can also be found in the product by selecting from the menu File > New > External
Service. The New External Service wizard
shows the adapters available. Selecting one and beginning to install
an adapter shows the version number of that adapter.

Check
the documentation that comes with these adapters for details such
as their availability on platforms such as Linux®.

There are also an older set of
adapters supported by the wizard called the WebSphere Business Integration Adapters
(see Using WebSphere Business Integration Adapters).

## Bindings

Binding information
determines how a service connects to and interacts with an application.
Bindings are also a critical part of imports and exports. Bindings
determine specifically how the imports and exports interact with clients
outside the module where the imports and exports reside. Bindings
specify the message format and protocol details for a particular interface.

In
the following diagram, we can see the variety of bindings available.
When you use the external service wizard, the EIS binding information
is created for you. You can also use another tool, the assembly editor,
to add or modify binding information. You will likely be interested
in using messaging bindings (JMS, MQ, MQ JMS or generic JMS) if the
loosely-coupled model is the basis of your application development.
In the task information, you are shown how to create messaging bindings.
Message consumers and message producers have paired messaging bindings:
one binding for an import and one binding for an export. An import
using one binding, for example, would send a message to a message
consumer such as WebSphere MQ;
an export using another binding would receive a message from a message
producer such as WebSphere MQ.

IBM web services bindings and HTTP
bindings can also by used with imports and exports. In the case of
an import, a stateless session Enterprise JavaBean (EJB) binding can
be used. If no binding is selected for an import or export, the default
binding is SCA for Service Component Architecture. It is used to import
from or export to another module created with the same architecture.

For
the imports and exports created by the external service wizard, Enterprise
Information Service (EIS) bindings that work with adapters are the
key ones.

<!-- image -->

## Messaging bindings and EIS bindings

We
have mentioned that the key bindings when it comes to EIS systems
are messaging bindings (JMS, MQ, MQ JMS and generic JMS) and EIS bindings.
There are some important differences in how these bindings are created
and when one is chosen over another. For example, messaging bindings
are used from a module to a module; that is, you can create an export
in a module with a JMS binding or you can create an import in a module
with a JMS binding. You cannot do this with an EIS binding. Since
messaging bindings are used for asynchronous communication, you can
also use a messaging binding as the binding between an external messaging
source and a component in a module.

EIS bindings are used from
an EIS system to an application or vice-versa. In the first case,
you would develop an export with an EIS binding. In the second case,
it would be an import binding. Essentially, EIS bindings are used
to access external EIS systems or for external EIS systems to access
applications developed in IBM Integration
Designer.
See How the wizards and editors support J2C and messaging bindings to see the particular
wizards and editors used by EIS and JMS for creation and editing purposes.

## Business objects from data structures

Another
wizard associated with the external service wizard is the external
data wizard. It is used to discover data structures in programs and
then generate business objects from them. This wizard can be helpful
when you want to create one or more business objects for your EIS
services and you have the EIS application code available locally on
your computer. The wizard can save you the time of hand-coding these
business objects.

The task information shows how to use the
external data service wizard to create a business object from a data
structure.

## How the wizards and editors support
J2C and messaging bindings

The wizards and editors are used
to support J2C and messaging bindings. In the task help, you are shown
specifically how to use these tools. The tools can be divided into
creating and editing as follows.

- The external service wizard discovers services and generates business
objects.
- The external data wizard generates business objects.
- When you expose a component, you can create a messaging binding
for it.

- The assembly editor edits the connection and interaction binding
information in the binding section of the properties view.
- The business object editor edits the type binding information
in the properties view.

## Modules for EIS imports and exports

Using
the external service and external data wizards results in artifacts
generated into a module. A module is similar to a project container.
There are two types of modules, a module called module for
service component architecture artifacts, and a mediation module,
which contains only one service component architecture artifact, a
mediation flow component. Both modules and mediation modules result
in applications tested and deployed to the IBM Workflow
Server.

When
and why would you use a service from an EIS import and export in a
mediation module? A mediation flow component in a mediation module
was designed to mediate, as its name implies, between services. The
mediation flow in the component is similar to the flow-like constructs
you would see in the assembly editor or process editor. The mediation
flow is done independent of the services themselves. Mediation has
several useful functions. You can use mediation when you need to transform
data from one service into an acceptable format for a subsequent service.
Logging is another useful function of a mediation, where messages
are logged before being sent to the next service. Routing lets you
route data from one service into an appropriate service determined
by the mediation flow. In these cases you could use mediation between
a service needing to access EIS systems and services that provide
access to EIS systems created by the external service wizard.

## Related concepts

- Pattern of accessing external services with adapters
- Simple adapter wizard
- Migrating applications using previous adapter levels

## Related tasks

- Configuring and using adapters
- Creating a business object from a source file

## Related reference

- J2C data bindings
- A closer look at business objects from data structures
- J2C imports and exports at run time
- Trade-offs when developing adapter imports and exports
- Considerations when using adapters
- Considerations when refactoring
- Contributing your own external service or data wizard plug-in
- Limitations for adapter imports and exports