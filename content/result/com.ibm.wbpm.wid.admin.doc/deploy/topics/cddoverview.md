<!-- image -->

# Module deployment properties

Using the module deployment editor, you can accomplish numerous
tasks relating to module deployment properties, such as:

- Changing URLs for web service exports
- Creating and assigning security roles for web service exports
- Binding security roles (including roles that are defined in assembly
diagrams)
- Editing WS-Security properties for JAX-RPC exports and imports
- Adding JAX-RPC handlers for web service exports
- Adding JAX-RPC handlers for web service imports
- Adding resource references

Editing module deployment properties is a task that is best suited
to advanced users of IBM Integration
Designer. This is especially true of module deployment properties that relate
to web services security, which requires a solid understanding of
the OASIS Web Services Security (WS-Security) specification.

To work with the module deployment editor, you should be familiar
with the Rational® Application
Developer tools that are used to manage properties in the deployment
descriptor files, such as the web services editor and the EJB deployment
descriptor editor. However, you can successfully use the module deployment
editor with only a basic understanding of modules and web services
exports and imports.

When you use the module deployment editor to change the deployment
properties for a module, your changes are saved to an XML deployment
side file named ibm-deploy.scaj2ee that resides
directly under your module in the Physical Resources view of the Business
Integration perspective. The side file automatically updates the module
deployment properties in the deployment descriptor files whenever
your deploy code is regenerated during a build or when your module
is installed on the server. This ensures that your changes are retained
even though the deploy code is periodically regenerated.

Although the module deployment editor documentation provides basic
information on using the editor to manage module deployment properties,
detailed information on managing web services and their deployment
properties is found in the IBM redbook WebSphere Version 6 Web
Services Handbook - Development and Deployment (SG246461), which
is available at the following IBM Redbooks site: http://www.redbooks.ibm.com