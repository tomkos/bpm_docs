<!-- image -->

# Module

- Service components, that hold the business function within a module. A service component
configures a service implementation. The service component name inside a module is unique. A service
component can have an arbitrary display name, that is more useful to a user. It is not necessary for
each module to have a service component, but there is no limit to the number of service components
per module.
- Imports, that are calls to services external to the module. It is not necessary for each module
to have an import, but there is no limit to the number of imports per module. Imports are detailed
later on in the chapter.
- Exports, that are used to expose components to callers that are external to the module. It is
not necessary for each module to have an export, but there is no limit to the number of exports per
module. Exports are detailed later on in the chapter.
- Interfaces, which can be associated with one or more components. The interfaces associated with
a service component show the business operations associated with the component.
- Stand-alone references or reference applications that are not defined as SCA components (for
example, JavaServer Pages). These applications can then interact with SCA components. There can be
only one stand-alone reference per module.
- Other elements, for example WSDL files, Java™ classes, XSD
files.

Figure 1. Structure of a module

<!-- image -->

Figure 1 shows an example module, which contains two
service components, each containing an implementation. An export reveals Service Component A's
capabilities to external service consumers. A stand-alone reference shows the component's
capabilities to other non-SCA artifacts included within the deployment artifact such as JavaServer
Pages (JSP). Service Component A may require the capabilities of two other services. One implemented
by Service Component B, and one included using an SCA import. All exports, imports and components
have interfaces that describe the inputs and outputs of these elements. References are used on
service components and stand-alone references to declare the additional capabilities they require to
function. Wiring is used between all the elements to represent their relationships.