<!-- image -->

# Viewing and updating EJB import bindings

## Before you begin

## About this task

You can modify only the JNDI name property. All other properties for an
EJB binding import are read-only.

| EJB scenario                                                                                        | JNDI configuration information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IBM® Business Automation Workflow in a different Java™ EE module                                    | Set the JNDI name in the EJB import binding to match the global namespace. Also, confirm that the JNDI name specified in the EJB import binding matches what is specified in the Java EE module bindings file. Note: The JNDI name for local invocations, which apply only to the EJB 3.0 programming model, take the form ejblocal: followed by the fully qualified class name of the local interface.You can find more information in the JNDI name topic.                                                                               |
| Remote IBM Business Automation Workflow or WebSphere Application Server                             | Create a namespace binding (of EJB binding type) using the IBM Business Automation Workflow administrative console. To create the namespace binding, click Environment > Naming > Namespace.  The name specified in the namespace field for the namespace binding should match the JNDI name specified in the EJB import binding configuration.                                                                                                                                                                                            |
| Remote Java EE server (other than IBM Business Automation Workflow or WebSphere Application Server) | Create a namespace binding using the IBM Business Automation Workflow administrative console.  If the Java EE server provides a COSNaming interface, create a namespace binding of type CORBA. If the Java EE server does not provide a COSNaming interface, create a namespace binding of the indirect type.  To create the namespace binding, click Environment > Naming > Namespace.  The name specified in the namespace field for the namespace binding should match the JNDI name specified in the EJB import binding configuration. |

To view or configure EJB import properties using the IBM Business Automation Workflow administrative console, complete the
following steps:

## Procedure

1. Select the module
that contains the binding by navigating to Applications > SCA Modules and clicking the
module name.
2 Selectthe binding by performing the following steps:
    1. In the Module components section,
expand Imports.
    2. Expand the import, and then
expand Binding.
    3. Click the binding to view
information about its properties.
3. Optional: 
Change the JNDI name.
4. Save your changes to the master configuration.

## Results

To ensure
that the changes you made remain with the module across deployments,
use IBM Integration Designer to make the changes in the source code
for the module.