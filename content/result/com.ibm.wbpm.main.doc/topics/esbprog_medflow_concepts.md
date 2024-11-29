<!-- image -->

# Mediation policy concepts

## Promoted properties

Mediation flow primitives have properties that can be set at build time using IBM® Integration
Designer to determine the behavior of the mediation primitive when a message
flows through it. Many of these mediation flow properties can be promoted, which means
they are then visible in the IBM Business Automation Workflow administrative console so that their
values can be reconfigured. Using mediation policy you can determine the values of these promoted
properties dynamically, depending upon the message context, without the need for user interaction.
When a property is promoted, it is assigned to a Property Group: a logical
collection of related properties. A policy document can then be used to specify the
values for the properties in a Property Group. Each promoted property is assigned an
Alias and can have an Alias Value, which becomes the
default value for that property if it is not overridden at run time.

## Dynamic property context

The dynamic property context is an area of the Service Message Object (SMO) that
contains a list of properties and their values. Each mediation primitive with promoted properties
uses the dynamic property context to determine the property value, and if the value is not present
in the dynamic property context the static value of the promoted property is used.

## Policy Resolution mediation primitive

The Policy Resolution mediation primitive is used in a mediation flow to initiate mediation
policy control over downstream mediation primitives. The Policy Resolution mediation primitive
determines which policies should be applied, and writes these policies into the Dynamic Property
Context area of the SMO, in the form of a list of names and values. The Property Context is then
queried by downstream mediation primitives. Any promoted property that matches a name in the Dynamic
Property Context is updated with the corresponding value.

## Gate conditions

Mediation policies can be defined as applying to a message only under certain conditions, known
as gate conditions.

If a gate condition is true for a given message, then the policy
applies; otherwise it is ignored. Gate conditions for mediation policies are based on the values of
message elements. Each gate condition identifies the message element (using an XPath expression) and
compares the element with a fixed value. For example, a gate condition might check whether a
transfer amount value is greater than 10000.

## Mediation policy documents

A mediation policy document holds information about the gate conditions and promoted
property values that must be applied by a Policy Resolution mediation primitive. The policy
domain (which is called a Promoted Property Group in IBM Business Automation Workflow) can contain several policy assertions (each of which is
a Promoted Property Alias in IBM Business Automation Workflow). Each policy assertion can have a
policy assertion value (the Promoted Property Alias value in IBM Business Automation Workflow).

## Mediation policy scopes

- Module. The policy applies to all of the messages being processed by the mediation module.
- Service. The policy applies to a specific target service.
- Endpoint. The policy applies to a specific target service endpoint address.
- Operation. The policy applies to a specific operation in the service interface.

## WebSphere Service Registry and Repository (WSRR)

Mediation Policy Documents are held in WSRR, a separate product that is based on WebSphere® Application
Server. WSRR can act as a repository for service endpoints and can be used to
govern how services are used. IBM Business Automation Workflow has various mediation primitives
that can access data in WSRR. IBM Business Automation Workflow specifically uses the Policy
Resolution mediation primitive to query WSRR for matching policy documents and to set promoted
property values of downstream mediation primitives. Mediation Policy Documents are stored in WSRR as
.xml files in WS-Policy format. The default mediation policy document is
created when you load the Mediation module into WSRR, by generating a .ear file
from the mediation flow module and then loading that .ear file into WSRR. When
the .ear file is loaded, new policy documents can be created in WSRR and
attached to it to add new policies with associated Gate Conditions.

## Policy resolution

1. Policies with gate conditions
2. Policies without gate conditions
3. Promoted properties set in the administrative console

Policies with the same precedence are merged unless they conflict in some way. For example, when
two gate conditions evaluate to true but the policies associated with
the conditions attempt to set a property to two different values. In this situation a policy error
occurs, and the policyError terminal of the Policy Resolution mediation
primitive is fired.

## Business Space

Business Space is a browser-based Web 2.0 WebSphere
application that presents content relating to particular aspects of a business in
spaces. A space consists of a set of pages relating to a particular business function.
Each page is populated by widgets: user interface components that, when combined,
provide the required business function. Business Space has a set of predefined spaces and a set of
supplied widgets. You can create your own spaces and pages and drag the supplied widgets onto pages
to create your own business environments.

## Mediation Policy widgets

BusinessSpace installed on a IBM Business Automation Workflow
server provides several pre-defined spaces, each containing several pages. Each page is
used to manage a different aspect of IBM Business Automation Workflow.

The Solution Administration space has a Module Administration page for
managing modules. The Module Administration page contains a Module Browser widget and the Module
Administration widget. You can use the Module Administration page to manage mediation policies for
modules.

The Service Administration space has a Service Administration page. This
page can help you manage mediation policies for target services. The page contains two widgets: a
Service Browser widget and a Mediation Policy Administration widget. See the Applying policies using Business Space scenario for an example of how these
widgets are applied.

- Mediation policy widgets

When using Business Space you can use these widgets to administer mediation policy.