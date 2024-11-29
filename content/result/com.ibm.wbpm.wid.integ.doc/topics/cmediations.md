<!-- image -->

# Mediation flows overview

Mediation modules can be deployed on the IBM® Workflow
Server .

In service-oriented architecture (SOA), services represent
business functions that can be reused and combined in an ad hoc manner
 to create responsive business systems. These services have loosely
coupled connections, rather than being connected directly to each
other.

- Transforming a message from one format to another so that the
receiving service can accept the message
- Conditionally routing a message to one or more target services
based on the contents of the message
- Augmenting a message by adding data from a data source

## Stock Quote example: building a mediation
flow

To illustrate a mediation flow, we will use
an example of a simple mediation flow that provides stock prices.
A client application provides a query containing a stock symbol and
customer ID to the mediation flow, which processes the query. The
customer's subscription level is determined, and depending on the
level of subscription, the query is routed to the appropriate service
provider. The quote that is returned from the service provider is
converted into the customer's preferred currency before it is returned
to the client application.

We are using a mediation
flow because we want to use different interfaces from two external
service providers, and expose a single interface to the client application.
We need to build the service quickly, with the ability to change the
application on demand, and without modeling a business process. We
also want the ability to change the service provider without disrupting
the service.

<!-- image -->

- Mediation modules

Mediation service applications are assembled and deployed as one or more mediation modules. Mediation modules are deployable units that contains mediation flows. They can be deployed on the IBM Business Automation Workflow or the IBM Process Server.
- Mediation flow components

A mediation flow component provides a mediation service implemented using mediation flows. A mediation flow component in the assembly editor has the following parts
- Mediation flows

A mediation flow consists of a sequence of processing steps that are run when an input message is received.
- Mediation primitives

Mediation flows consist of a sequence of mediation primitives, which define processing steps.
- Service message objects

A message is a communication sent from one application or service to another application or service. Messages in mediation flows are represented as service message objects (SMOs)
- XPath for mediation flows

The XPath standard is well-suited for creating simple data-driven expressions. Most mediation primitives have properties that are specified with an XPath expression. For example, the root property takes an XPath 1.0 expression that specifies the part of the message that is available to the primitive for processing.
- Message Transformation

When you are integrating services, you usually need to transform the data into a format that the receiving service can process. Typically, interfaces and operations of disparate services are not identical, and the message from the source needs to be transformed into a format that can be accepted by the target.