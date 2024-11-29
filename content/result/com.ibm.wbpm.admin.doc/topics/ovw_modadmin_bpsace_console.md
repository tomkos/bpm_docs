<!-- image -->

# Administering service modules with the administrative console or widgets

## Module administration with the administrative console

- List all of the associated service modules deployed to IBM® Workflow
Server, including mediation modules
- See the applications associated with each module, and determine if those applications are
running
- List details for a service module, including module properties
- List details about the application used to deploy a service module
- Start or stop a service module
- Modify service module properties
- Work with imports and exports for a service module

For specific information on these tasks, refer to the online help in the administrative
console.

## Module administration with widgets

Use one or more of the administration widgets in a business space to browse deployed modules in a
cell, view detailed information about each module, and edit module artifacts. These artifacts can
include module properties, business rule groups, security roles, business calendars, and service
control points.

For example, the Module Browser widget has a graphical view that visually represents the services
exposed and invoked by a module with appropriate contextual information about each. Detailed
information about the module is also available and includes the module version, cell identifier
(used to uniquely identify a versioned module in a cell), and endpoints. The graphical view provides
overall module status and highlights any existing configuration problems.

The Module Browser widget is used with other administration widgets. It enables you to list the
names of any properties and policies defined for the module. In addition, if you are using IBM Workflow
Server, it lists the business rules, BPEL
processes, business state machines, human tasks, business calendars, and security roles defined for
the module. Select an artifact from the list in this widget to perform any necessary administration
tasks in related widgets.

- What services are consumed in or exposed by a module?
- Is the module wiring correct, and are the correct versions of modules deployed?
- Are all service exports and service imports bound to existing modules?
- What is the status of a module? Is it running, or stopped?
- Are there any failed events in the module?
- What properties does the module expose?
- What mediation policies are associated with the module?
- What BPEL processes and human tasks are used in a module?
- What security roles are used in a module?
- What business calendars are used in a module?
- What business state machines are defined for a module?
- What business rules are used in a module?

For detailed task information, refer to the online help provided with each widget.