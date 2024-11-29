<!-- image -->

# Modules

A module is a project that is used for development,
version management, organizing business service resources, and deploying
to the  IBM® Business Automation
Workflow.
In fact, a module is the basic unit of deployment to this runtime
environment.

There are two kinds of modules - business modules and mediation
modules. Both types of modules be deployed to the IBM Workflow
Server.
(See "Mediation modules" for information about that kind of module.)
Modules can include processes, human tasks, mediation flows, state
machines, business rules, and Java™ services.
You can add dependent libraries, Java projects,
and Java 2 Platform Enterprise Edition projects to a module and choose
to deploy them with the module.

The module provides the business services, which are modeled as
Service Components Architecture (SCA) components wired together in
a module assembly. This module can contain all the resources that
are used in the service, but these resources are private and can only
be used within the module. To reuse the logic in a module from
other modules, you can export a component's interfaces. For information
about exports, components, and interfaces, see the related concepts
listed at the end of this topic.

The module assembly contains a diagram (referred to as the assembly
diagram) of the integrated business application, consisting of
components and the wires that connect them. You use the assembly editor
to visually compose the integrated application by using elements that
you drag from the palette or from the tree in the Business Integration
view.

The implementations of components that are used in a module's assembly
reside within the module. Components belonging to other modules can
be used through imports. Components in different modules can be wired
together by publishing the services as exports that have their interfaces,
and then dragging the exports into the required assembly diagram to
create imports.

Modules can export interfaces, but they cannot share resources.
Resources that are to be shared must be stored in a library.

## Java 2 Platform Enterprise Edition staging projects

- MyAppApp
- MyAppWeb

If
the Java 2 Platform Enterprise Edition staging projects are manually
deleted for a module, then all staging projects may not be recreated
after saving an editor (for example, the assembly editor). This problem
only arises when auto-build is turned on. Only artifacts that have
changed will have their deployment code regenerated as the build incrementally
processes deltas. To solve this problem, perform a clean build.

Do
not modify the generated Java 2 Platform Enterprise Edition modules
or make changes to a web.xml file or an ejb-jar.xml file. When you
issue a Project > Clean command, the system will discard the former Java 2
Platform Enterprise Edition staging project and regenerate it. Any
changes you made to the former project will be lost. Also, direct
modifications to these modules can result in an invalid application.

1. Create your own web project and create JavaServer Pages scripting
for your HTML files in the web project.
2. In the Business Integration view, expand the business integration
module's folder and double-click Dependencies.
The module dependencies editor will open. (Do not change dependencies
except through the dependencies editor.)
3. In the Java 2 Platform Enterprise Edition section of that editor
view, click Add to add your module as the dependent
project. This action will pull your dependent project into the EAR.