<!-- image -->

# Libraries and JAR files overview

While developing a module, you might identify certain resources
or components that could be used by other modules. These artifacts
can be shared by using a library.

## What is a library?

- Interfaces or web services descriptors (files with a .wsdl extension)
- Business object XML schema definitions (files with an .xsd extension)
- Business object maps (files with a .map extension)
- Relationship and role definitions (files with a .rel and .rol
extension)

At deployment time, these Integration Designer libraries
are transformed into utility JAR files in the applications to be run.

When
a module needs an artifact, the server locates the artifact from the
EAR class path and loads the artifact, if it is not already loaded,
into memory. Figure 1 shows how an application
contains components and related libraries.

Figure 1. Relationships among module, component,
and library

<!-- image -->

## What are JAR, RAR, and WAR files?

There
are a number of files that can contain components of a module. These
files are fully described in the Java™ Platform, Enterprise Edition specification.
Details about JAR files can be found in the JAR specification.

In IBM® Business Automation Workflow, a
JAR file also contains an application, which is the assembled version
of the module with all the supporting references and interfaces to
any other service components used by the module. To completely install
the application, you need this JAR file, any other dependent JAR,
web services archive (WAR), resource archive (RAR), staging libraries
(Enterprise JavaBeans) JAR files, and any other archives. You then
create an installable EAR file using the serviceDeploy command.

## Naming conventions for staging
modules

- myServiceApp
- myServiceWeb

## Considerations when using libraries

Using
libraries provides consistency of business objects and consistency
of processing amongst modules because each calling module has its
own copy of a specific component. To prevent inconsistencies and failures
it is important to make sure that changes to components and business
objects used by calling modules are coordinated with all of the calling
modules. Update the calling modules by:

1. Copying the module and the latest copy of the libraries to the
production server
2. Rebuilding the installable EAR file using the serviceDeploy command
3. Stopping the running application containing the calling module
and reinstalling it
4. Restarting the application containing the calling module