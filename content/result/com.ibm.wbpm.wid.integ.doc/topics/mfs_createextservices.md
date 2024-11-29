<!-- image -->

# Creating a new external service from a conversational MFS application

## About this task

## Procedure

1. Select File > New > External Service.  The New External
Service window opens
2. Select IMS from the list of available
types.
3. In the Select an Adapter screen, select the version of
the IMS TM resource adapter for
your environment.
4. In the Select the Application Type screen, select IMS
MFS-based application.
5. Click Add and navigate to where
your MFS conversational application is and click Next.
6. Select the first discovered message input descriptor (MID)
object, or the first operation, and add it to the selected object.
In the next screen, you are asked to specify the configuration
properties for the selected operation.
7 Examine the auto-selected message output descriptor (MOD)object for the MID. Click Add to add any additionalMODs.
    1. Click Add if there are multiple
possible outputs.
    2. By default, the Generate business graph for
conversation option is selected. For conversational MFS
services, ensure that this option is selected. For non-conversational
MFS services, clear this check box.
    3. Optionally, modify the namespace for generated business
objects if a different namespace is preferred
    4. Click OK.
8. Repeat the same steps for the second MID, or the second
operation, until all operations are selected and generation properties
are configured.
9. Click Next when you are done selecting
and configuring all MODs.

In the subsequent screens, you are asked to specify the
service generation and deployment properties.

1. Select Other under the Deployment
Properties section. The security property is configured by using the IBM® Process
Server administrative
console, through the connection factory later.
2. Clear the Join the global transaction option
for the component to run in a new global transaction. Important: By default, global transaction assumes two-phase
commit. Because two-phase commit is not supported by MFS, always clear
this option.
3. For the connection settings field, select Use predefined
connection properties.
4. For JNDI lookup name, specify the JNDI name to match the
JNDI name on the IBM Process
Server (for
connections to IMS).
5. Click Next. The Specify the Location
Properties page opens.
6 In the Specify the Location Properties page: A default value for the name of the service is specified.This value is the name for the generated import component.
    1. Click New to create a module
to contain the generated service.
    2. Specify a module name and click Next.
    3. Select the business object parsing mode and click Finish.
You are back to the Specify the Location Properties page.
7. Click Finish.

## Results

- Generated services

MFS SOA support generates business objects and corresponding business graphs from the MFS source file. Both are XML schema definition (XSD) files. Each complex type in the XSD file corresponds to a business object.
- Examining the files in Java EE view

You can examine the data bindings, XSD files, and import files from the Java™ EE view.