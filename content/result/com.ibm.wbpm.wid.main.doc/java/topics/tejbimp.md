<!-- image -->

# Creating EJB imports

You can use IBM® Integration
Designer to
create EJB imports that invoke remote EJBs.

## About this task

- Use the External Service Discovery wizard.
- Use the Outbound Imports drawer in the assembly editor.
- Drag an EJB session bean object on to the canvas of the assembly
editor.
- Drag an EJB session bean file on to the canvas of the assembly
editor.
- Drag an EJB local or remote interface on to the canvas of the
assembly editor.

- Creating EJB imports using the external service wizard

You can use the external service wizard in IBM Integration Designer to build an EJB import service. The external service wizard is a tool used to create services based on criteria that you provide. It then generates business objects, interfaces, and import files based on the services discovered. The EJB import is created based on an existing EJB implementation and the newly created import can then be deployed to IBM Workflow Server.
- Creating EJB imports using the assembly editor

You can create an EJB import within an assembly diagram using the IBM Integration Designer assembly editor.
- JNDI names

JNDI (Java Naming and Directory Interface) names are used to provide a usable name for a Java objects. IBM Integration Designer uses the JNDI name to determine the EJB programming model level and the type of invocation (local or remote). You may sometimes need to provide the JNDI name when creating EJB imports and the format of the JNDI name required in an interface depends on the type of invocation you are using.
- Configuring properties for EJB imports

The properties of an EJB import can be edited as required from the assembly editor using the Properties view.