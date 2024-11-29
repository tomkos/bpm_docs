<!-- image -->

# Modules and libraries dependencies

When developing and deploying integration applications,
you might need to declare dependencies for your modules, mediation
modules, and libraries. Use the dependency editor to manage these
dependencies.

When you create a new module or mediation module, you can add a
dependency on a library during that process. You can also use the
dependency editor to add dependencies on libraries, Java™ projects,
and Java 2 Platform Enterprise Edition projects. You can also use
the dependency editor to create a dependency on libraries or  Java projects for a library.

## Dependency on libraries

If a module or mediation
module needs to use resources from a library or if a library needs
to use resources from another library, you have to open the module
or library with the dependency editor and add a dependency on the
required library. Business objects and interfaces are examples of
the resources that you would want to share.

Libraries must
be deployed along with the projects that depend on them so that the
resources they offer are available at run time. You can deploy a library
to the runtime environment in two ways. In most cases, it is best
to deploy a library with the modules that have dependencies on it.
In this case, a copy of the library is made for each module that uses
it. If you have a large library that is used by many modules, you
can save memory use by choosing to create a global library. You must
deploy global libraries independently, but they allow modules to share
their resources without the need to create copies. Choose whether
a library should be deployed with the module or as a global library
by selecting the required radio button under Sharing across
Runtime Environments in the dependency editor.

Java project dependency

For a module, mediation module, or library, if
you add a dependency on a Java project,
it is automatically added to the build path of the module or library.
By default, the dependent Java project
is deployed with the module and, in the case of a library, the dependent Java project is deployed when the library is
deployed with a module. You can choose not to deploy the dependent Java project with the module or library. For
example, if the server is separately deploying the Java project
as a global utility, you can add the Java project
as a dependent to your module for build purposes, and then select
not to deploy it with the module.

If you choose to deploy a
library without a module, you need to configure a WebSphere shared
library using the instructions found in technote 21322617.

Java 2 Platform
Enterprise Edition project dependency

You
can specify dependent Java 2 Platform Enterprise Edition projects
for a module or mediation module. The dependency could be for build
or deployment purposes or both. When a module is dependent on a Java
2 Platform Enterprise Edition project, you might want to deploy it
with the module, but you might not want the Java 2 Platform
Enterprise Edition project as a part of the classpath of the module
because there is no real Java build
path dependency on the Java 2 Platform Enterprise Edition project.
In this case, you can use the dependency editor to add the Java 2
Platform Enterprise Edition project to the module for deployment.
For example, if you have a human task client application for the human
task service that is available from a module, you might add the Java
2 Platform Enterprise Edition project that has the human task client
to the dependency list for the module and deploy it with the module
in that way.

Ordering

A module may have several
dependencies. If there is more than one dependency, the dependencies
are resolved one by one in a consistent sequence. The order in which
the dependencies will be resolved is shown under Ordering.
Usually, the sequence will not matter to you, but when it does, you
can view the sequence and rearrange it here.

Unresolved dependencies

A
module's unresolved dependencies are listed under Unresolved
Projects and you will be able to select and remove them
or take other appropriate actions to restore the missing projects.

Modules
and libraries limitation

When you have artifacts that have
the same name, you need to place them in different subfolders. For
example, if you have a BPEL process in module Mod1 with two dependent
Libraries, and both libraries have an interface named MyInterface,
the interface may not resolve correctly. The BPEL process selects
the first MyInterface it finds in its dependency order (which is configurable
in the module dependencies). To ensure the BPEL process is referencing
the correct interface, create each interface in different subfolders.

## Avoid changing dependencies without the editor

You
should avoid modifying module dependencies outside the dependency
editor.

- The Java Build Path would have the library
or project added to its build path.
- The Project References determines which
Java 2 Platform Enterprise Edition projects or utility JAR files are
to be included in the resulting EAR file for the module. If in the
dependency editor, the library or project is also selected to be Deployed
with the Module, then the Project References will
have the library or project selected so that it will be added to the
EAR file for deployment.

Use the dependency editor to manage project dependencies
for your modules and libraries instead of editing their properties.
There are important Java assumptions
set in the properties of modules and libraries, so you should not
modify the Java properties, for example, to
change their source and output folders.