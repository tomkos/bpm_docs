# Authoring tools

## Process Designer

Process Designer provides several user interfaces
where you can model, implement, and inspect business processes. You create and manage process
applications, toolkits, tracks, and snapshots in Workflow Center. You can create process models,
reports, and simple services in Process Designer. You
can run and debug processes in the Inspector.

Process Designer helps
you develop business processes. With an easy-to-use graphics-oriented
tool, you can create a sequence of actions that compose a business
process, and you can redraw that process over time as circumstances
change. If one or more activities require access to large back-end
systems or services that provide data for the business process, for
example to get information on customers, you can meet that need using Integration Designer. Using
a simple interface, an activity in Process Designer can
call a service created in Integration Designer. That
service can use mediation flows to transform, route, and enhance data
and adapters to get to many back-end systems in standard way. In short, Process Designer focuses
on the business process and Integration Designer focuses
on automated services to complement the business process.

Process applications that are developed in Process Designer can at any time be run on the Workflow Center server or saved to a snapshot and deployed on
the Workflow Server. The same is true of services
that are developed in Integration Designer and associated
with process applications.

<!-- image -->

## Integration Designer

Integration Designer provides editors and aids to help
developers create complex automated processes and services (such as SCA modules, mediations, and
BPEL processes). It is available as part of the Business Automation Workflow package or as a stand-alone toolset for other
uses.

IBM Integration
Designer is
a complete integration development environment for building integrated
applications. Integrated applications are not simple. They can call
applications on Enterprise Information Systems (EIS), involve business
processes across departments or enterprises, and invoke applications
locally or remotely written in various languages and running on various
operating systems. The components are created and assembled into other
integrated applications (that is, applications that are created from
a set of components) through visual editors. The visual editors present
a layer of abstraction between the components and their implementations.
A developer using the tools can assemble an integrated application
without detailed knowledge of the underlying implementation of each
component.

Integration Designer tools
are based on a service-oriented architecture. Components are services
and an integrated application that involves many components is also
a service. The services that are created comply to the leading, industry-wide
standards. BPEL processes, which also become components, are similarly
created with easy-to-use visual tools that comply to the industry-standard
Business Process Execution Language.

In Integration Designer, components
are assembled in modules. Imports and exports are used to share data
between modules. Artifacts placed in a library can be shared among
modules.

Modules and libraries can be associated with a process application for use with the Workflow Center and can be used as services by processes that
are created in Process Designer. In such cases, they
can also be deployed with the process application.

Alternatively, modules and libraries can be deployed directly to the test environment or to the
Workflow Server. You can also use mediation modules
to create mediation flows, which you can deploy to the Workflow Server.