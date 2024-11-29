<!-- image -->

# Adding Java to the application

Modules are built using SCA components and WSDL interfaces. However,
you can also create Java components
with Java interfaces in your modules. You can drag
a Java class onto the assembly editor canvas as
a component.
You can also add a JAR file to a module or library. You can invoke
SCA components from Java applications
through the use of stand-alone references. You can use imports to
draw from stateless session Enterprise JavaBeans (EJBs),
modeled as an imported service. You can drag a stateless session bean
onto the canvas of the assembly editor to create an import. You can
double-click many Java objects in the Business Integration
view to open a Java source editor where you can
edit the code (but beware of editing generated code, because you may
cause build or deployment errors).

Topics in this section of the documentation provide additional
information about using Java with
SCA and WSDL artifacts.

- Opening the Java or Java 2 Platform Enterprise Edition perspective

The Business Integration view shows the navigation of Java and Java 2 Platform Enterprise Edition projects in their native form. However, you might occasionally need to see all the supporting views and their default layouts for Java projects. Use the Java or Java 2 Platform Enterprise Edition perspective for that function.
- Using a Java project with a module

If you need to develop Java code that will be used in a business integration module or mediation module, you should create a Java project for the code and add a dependency on the Java project from the module that will be using the Java code.
- Adding a Java Archive (JAR) file to a module

You can add a JAR file to a module, mediation module, or library by copying it from the file system into a project in the Business Integration view.
- Using Java in the assembly editor

Most of the time you deal with WSDL interfaces and references when working with components and imports in the assembly diagram. However, IBM Integration Designer supports some Java functions and provides some ways for you to use Java components with your WSDL components. Java components, components with no implementation, and stand-alone references can have Java or WSDL interfaces in their partner references.
- Understanding the SCA architecture to Java relationship

The environments for the Service Component Architecture (SCA) and Java are different. Understanding the map between them is the key to developing applications that use both environments.
- Invoking SCA components from JavaServer Pages

JavaServer Pages (JSP) files invoke Service Component Architecture (SCA) components using stand-alone references in the module assembly.