<!-- image -->

# Module deployment properties

Any changes that you directly make to module deployment properties
in deployment descriptor files are typically overwritten when the
deploy code is next regenerated.

However, you can use the module deployment editor to specify and
retain changes to module deployment properties. The module deployment
editor saves your changes to a deployment side file, which is used
to automatically update the module deployment properties in the deployment
descriptor files whenever the deploy code is regenerated or the module
is installed on the server.

- Change URLs for web service exports
- Create and assign security roles for web service exports
- Bind security roles (including roles that are defined in assembly
diagrams)
- Edit WS-Security properties for JAX-RPC exports and imports
- Add JAX-RPC handlers for web service imports and exports
- Add resource references

- When a JAX-RPC web services SCA binding is used in your SCA module,
it triggers an EJB module that is created dynamically at deployment
time to contain the web service and its settings.
- You can get the information about the generated EJB module by
using the administrative console to view the modules for the application.
Look up the related artifacts there or use the AdminApp.View command.
Fore more information, see Commands for the AdminApp object using
wsadmin scripting in the WebSphere Application Server information
center.
- If you have set properties on the SCA module's deployment descriptor
that are related to the JAX-RPC web services SCA bindings, they will
be transferred to the generated EJB module. For example, see the settings
used in Implementing authentication.
- The values can be modified by accessing the web services subsections
of the EJB module in the administrative console or by using the adminApp.edit
command with one of the options like -WebServicesClientBindPortInfo.
For more information, see Configuring web service client port information using
wsadmin scripting in the WebSphere Application Server documentation.
- The EJB module is not created when JAX-WS bindings are used. JAX-WS
bindings are the default web services SCA binding type for IBM® Business Automation Workflow.