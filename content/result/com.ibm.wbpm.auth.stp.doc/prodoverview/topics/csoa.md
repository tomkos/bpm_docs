<!-- image -->

# Service-oriented architecture

The goal of service-oriented architecture is to separate business
integration logic from implementation so that an integration developer
can focus on assembling an integrated application rather than on the
implementation details. To achieve that end, service components that
contain the implementation of individual services required by business
processes are created. The result is an architecture of three layers
(business integration logic, service components, and implementation)
as shown in the following diagram:

<!-- image -->

Because the service components contain the implementation, they
can be assembled graphically by the integration developer without
the knowledge of implementation details. Service components also provide
the option of letting the integration developer, or someone who works
for the integration developer, add the implementation later. Components
are assembled together visually. In other words, you are not exposed
to the code within the components. In the business logic level shown
in the diagram that follows, the components are assembled independently
of their implementation. The service oriented architecture, then,
lets you focus on solving your business problems by using and reusing
components rather than diverting your attention to the technology
that is implementing the services you are using.

<!-- image -->

Key benefits of service-oriented architecture

- Consolidating business logic and business data. Components used
by various groups in a corporation or even shared among a set of corporations
can be used by everyone as the components comply to industry standards
like the Web Services Descriptive Language (WSDL) and the Business
Process Execution Language (BPEL), which are independent of platform
and vendor. Data is consistently represented in the same way, allowing
data to be shared among components of a service-oriented architecture
application.
- Leveraging applications and systems that already exist. When you
place applications and systems inside WSDL code, they become universally
available to any application developer in the enterprise developing
a current application.

- Components are loosely coupled. A component accessing another
component does not require knowledge of the data structures, the calls
to other components, transaction management, and so on in that other
component.
- Components are configurable. Looking at a service oriented architecture
application such as the previous diagram is similar to looking at
a configuration diagram. Components can be added, deleted, and configured
in different ways to create new applications.
- Components are interoperable. Any one component can interoperate
with another component including components created by different vendors'
development environments.
- Components are location independent.

Together, these design principles create a flexible architecture
able to adapt to and thrive on rapidly changing business conditions.

## Related concepts

- Service Component Architecture (SCA)
- Deployment options for IBM Integration Designer
- The runtime environments for IBM Integration Designer
- Task flows

## Related reference

- Keyboard shortcuts for the workbench, Java development tools, and the Debug perspective

## Related information

- Team development in Business Automation Workflow