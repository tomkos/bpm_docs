<!-- image -->

# Working with modules in the administration widgets

A graphical view visually represents the services exposed and invoked by a module with
appropriate contextual information about each. Detailed information about the module is also
available and includes the module version, cell identifier (used to uniquely identify a versioned
module in a cell), and endpoints. The graphical view provides overall module status and highlights
any existing configuration problems.

The Module Browser widget is used with other administration widgets. It enables you to list the
names of any properties and policies defined for the module. In addition, if you are using IBM® Workflow
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

- Browsing and administering modules

Use the administration widgets to view and administer all deployed SCA modules in a cell.
- Administering mediation policies for modules

Use the Mediation Policy Administration widget to work with mediation policies associated with modules. Using mediation policies you can dynamically control service interactions, using contextual information.
- Managing timetables in Business Calendar Manager

You can use the Business Calendar Manager widget in a business space to view, edit, and modify timetables that define the available time for your business application, and you can set the appropriate role-based access for the timetables.