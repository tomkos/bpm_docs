<!-- image -->

# Limitations of binding resource configurations

## Class does not implement correct
interface message

- Implementation class cannot be found: This message usually means
that all of the required classes for the class are not on the classpath
of the project the implementation class is contained in. For example,
if the implementation comes as a binary format in a JAR file, compilation
errors will not show up in the IDE, but the classes needed to load
the implementation class cannot be found.
- The class does not implement the data binding, data handler or
function selector interface: This message usually means that the classpath
for the tools and the classpath for the user project have the same
JAR file or classes on the classpath, but they are from two physically
different JAR files. For example, the module has the IBM® Workflow
Server stub
and the user project has the commonj.connector.jar explicitly on the
classpath.

- Place your code in a Java EE utility project that has the same
target runtime as the module targeted for the resource configuration.
Set the utility project as a dependency on the module.
- Place your code in the same module targeted for the resource configuration.

If you have a JAR file containing your classes, you can
create a utility project by following these steps:

1. From the menu, select File > Import > General >
File System. The Import window opens.
2. In the From directory field, enter the JAR file location.
In the Into folder field, enter the module location.
3. Click Finish. A message asks if you want
to create a project and set it as a dependency on the module. Click Yes.
4. A utility project is created with the correct classpath.

Alternately, if you are developing your classes in the IDE,
you can either create your classes in the same module or create a
Java EE utility project that specifies the same target runtime as
the module. Then you should set the utility project as a dependency
on the IBM Integration
Designer module.

## Configurations with non-configurable data bindings

In
some cases, non-configurable data bindings may be used within the
context of a configuration. In these cases, the normal sequence of
pages in a wizard may differ.