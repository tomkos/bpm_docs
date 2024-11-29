<!-- image -->

# Creating a JNDI adapter reference for an application

## Before you begin

Because a stand-alone adapter must be set up to use the Java Naming and Directory Interface
(JNDI) defined adapter configuration, first install the stand-alone adapter to a cluster where you
want to deploy your applications with adapter bindings that use the JNDI resources.

## About this task

- If you are a developer, complete these steps at development time when you create an adapterimport or export:
    1. Set the following value in the configuration properties that are specified on the
Specify the Service Generation and Deployment Properties window. This value
enables the stand-alone adapter when you create an import or export. In the Deploy
connector project property list, select On server for use by multiple
applications.
    2. In the same window, check that the following value is set to use a JNDI resource lookup. From
the Connection properties list, select Use JNDI lookup name
configured on server.
    3. In the JNDI lookup name property field, specify the JNDI name that you
want to use. Use this same JNDI name when you create the related JNDI resource in the administrative
console.
- If you are an administrator, take these steps before application deployment:

1. In the Integrated Solutions console, go to the resource adapters section
and select Resources > Resource Adapters.
2. Change the scope to the application cluster and click the stand-alone adapter related to your
application's import or export binding.
3 For inbound adapter export bindings, create an activation specification. For outbound adapterimport bindings, create a connection factory.
    - For inbound adapter export bindings, select J2C activationspecifications . Then, select New to create an activationspecification based on the selected adapter. Add values for the following properties: After the activation specification is created, under AdditionalProperties you can modify the custom properties that relate to various inbound adapterexport binding configurations. These properties are adapter-specific. See your adapter'sdocumentation for details about the exact options.
        - Name: The display name
        - JNDI name: The JNDI name must match the name that is used for your
application export binding.
        - Message listener type: The type of listener
        - Security settings: The settings for your security
- For outbound adapter import bindings, select J2C connection factories .Then, select New to create a connection factory based on the selectedadapter. Add values for the following properties: After the connection factory is created, under Additional Properties youcan modify the custom properties that relate to various outbound adapter export bindingconfigurations. These properties are adapter-specific. See your adapter's documentation for detailsabout the exact options.
    - Name: The display name
    - JNDI name: The JNDI name must match the name that is used for your
application import binding.
    - Connection Factory interface: The managed connection factory
properties
    - Security settings: The settings for your security
    - Container-managed authentication: The authentication mechanism

## Results

A JNDI activation specification or connection factory is available for use with your adapter
bindings.