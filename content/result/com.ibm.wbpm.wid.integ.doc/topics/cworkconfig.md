<!-- image -->

# Working with data handlers, faults and registries

Whereas a binding class provided as-is might be thought of as a
class with hard-coded values, a binding resource configuration allows
you to customize a binding yourself for your particular needs. Moreover,
a binding resource configuration you create can often be reused by
another type of binding. For example, you might create a binding resource
configuration to work with a Flat Files adapter that might be suitable
for a service with a JMS binding.

Binding resource configurations can be created for data bindings,
data handlers and function selectors, each of which has a section
explaining their creation and how these binding resource configurations
work together to bring flexibility and reuse to your services. These
sections are followed by a look at the registry where these configurations
are contained.

- Data handlers

Data handlers are reusable transformation logic independent of a specific transport protocol like JMS or HTTP. They can be invoked from data bindings and Java™ components.
- Creating a custom data handler

A custom data handler is useful when the data formats requiring transformation are unique and the prepackaged data handlers are not sufficient for your needs.
- Handling faults in bindings

A fault or error that occurs at run time needs to be handled in some way by an application.
- Resource configurations for imports and exports

Resource configurations can be used with imports and exports to provide reusable configurations for your services. In this section, you are shown how to create these resource configurations with the tools in IBM Integration Designer.
- Binding registry preferences page

The binding registry preferences page is a list of registered bindings available in IBM Integration Designer.
- Application Specific Information (ASI) registry preferences page

 The application specific information (ASI) registry preferences page is a registered list for your ASI schemas created by IBM Integration Designer generations or by yourself.