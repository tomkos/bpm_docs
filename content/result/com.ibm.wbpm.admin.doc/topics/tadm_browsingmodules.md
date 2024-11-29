<!-- image -->

# Browsing and administering modules

## Before you begin

- If you are using a deployment environment, ensure the deployment manager is running before you
use the widget. In addition, the node agents must be running in order to see module status in the
widget.
- If you have turned on security in your business space, make sure you are using both
administrative security and application security.
- If you are using Microsoft Internet Explorer as your browser, configure it to display new
versions of pages instead of cached versions. See Caching problem in
default configuration of Microsoft Internet Explorer for more information.

Required security role for this task: When administrative security is enabled, you must be
logged in with an administrative role (Administrator, Configurator, Operator, Monitor,
AdminsecurityManager, Deployer, or icsadmins) to view and administer modules.

## About this task

For each module in the cell, you can see a list of artifacts associated with it in the Module
Browser widget, including service exports, service imports, properties, policies, and service
control points. If you are using IBM® Workflow
Server,
you can also see BPEL processes, human tasks, business rules, business state machines, business
calendars and security roles for the module.

The related Module Administration widget displays a graphical representation of module service
exports and service imports and provides administrative access to module artifacts.

To browse for a module and examine its details, perform the following steps.

## Procedure

1. Log in to your business space and open the page that contains the Module Browser and Module
Administration widgets.
The Module Browser widget lists all of the modules currently deployed to the
cell.
2 Optional: If you want to display only a subset of modules, complete the following steps.
    1. From the menu on the widget toolbar, click Edit Settings.
    2. Select Show selected modules, and click Add.
    3. In the Select Modules to Add window, select the names of modules that you want to show in the
Module Browser widget.
In the Search modules text box, you can type the first few letters of
the name of a module, and the list of modules in the window is refreshed with only the modules that
begin with those letters.
    4. After selecting all modules that you want to show in the Module Browser widget, click
Add.
The Module Browser widget displays the specific modules you selected.
3. Browse the list of modules to locate the one you want to see in detail.
4 Click the arrow next to the module name to expand the tree view. The widget displays the following information about the module:

- Service imports and service exports in the module
- Whether properties and policies have been defined for the module
- Business rule groups defined in the module
- BPEL processes defined in the module
- Business state machines defined in the module
- Human tasks defined in the module
- Business calendars defined in the module
- Security roles defined for the module (available only when administrative
security and application security are enabled)
- Service control points defined for the module
5 To see additional details about module artifacts, perform one of the following actions. Option Description To view service imports and service exports You can also click the name of an individual import or export in Module Browser to display itshigh-level binding endpoint details in the Module Administration widget. To view or administer module policies To view a BPEL process template, human task, or business state machine To view or administer module properties To view or administer business rule groups To view or administer a security role To view or administer a business calendar To view all of the service control points for a module and display details for a servicecontrol point To view all of the service control points for a module: To display details for a service control point:

| Option                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| To view service imports and service exports                                                            | Click the name of the module to display a diagram of all of its service imports and service exports in the Module Administration widget. Click any service import or export in the diagram to display more information.  You can also click the name of an individual import or export in Module Browser to display its high-level binding endpoint details in the Module Administration widget.                                                                                                                                                                                                                |
| To view or administer module policies                                                                  | Click the Module Policies section of the browser tree to view the policy attachments defined for the module in the Module Administration widget. Optionally, create new policy attachments and click Save.                                                                                                                                                                                                                                                                                                                                                                                                      |
| To view a BPEL process template, human task, or business state machine                                 | Do one of the following: Expand the Processes section of the browser tree to list all BPEL processes in the module, then click the process name. Expand the Human Tasks section of the browser tree to list all tasks in the module, then click the task name. Expand the State Machines section of the browser tree to list all business state machines in the module, then click the state machine name.   View the artifact details in the Module Administration widget and, optionally, click the link to open Business Process Choreographer Explorer in a new browser window and administer the artifact. |
| To view or administer module properties                                                                | Click the Module Properties section of the browser tree to list all promoted properties defined for the module in the Module Administration widget. Optionally, modify property values and click Save.                                                                                                                                                                                                                                                                                                                                                                                                          |
| To view or administer business rule groups                                                             | Expand the Rule Groups section of the browser tree to list all business rule groups. Click the name of the rule group to display its details in the Module Administration widget. Click the link in the Module Administration widget to open the business process rules manager.                                                                                                                                                                                                                                                                                                                                |
| To view or administer a security role                                                                  | Expand the Security Roles section of the browser tree to list all security roles. Click the name of the security role to display its details in the Module Administration widget.Note: You must have BPMAdmin or BPMRoleManager authority to assign or modify roles.                                                                                                                                                                                                                                                                                                                                            |
| To view or administer a business calendar                                                              | Expand the Business Calendar section of the browser tree to list all calendars. Click the name of the business calendar to display its details in the Module Administration widget.Note: You must have appropriate Reader, Writer, or Owner permissions for the calendar.                                                                                                                                                                                                                                                                                                                                       |
| To view all of the service control points for a module and display details for a service control point | To view all of the service control points for a module: Expand the Service Control Points section of the browser tree to list all service control points. Click Service Control Points to display all service control points in the Module Administration widget.   To display details for a service control point:  Expand the Service Control Points section of the browser tree to list all service control points.  Click the name of a service control point to display its details in the Module Administration widget.                                                                                   |