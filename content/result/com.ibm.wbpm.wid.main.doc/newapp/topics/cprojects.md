<!-- image -->

# Business integration projects

The first act in developing an application is to set up
one or more projects to hold your resources. A project is an organized
collection of folders or packages, and it is the largest structural
unit in your workspace.

A project is an organized collection of folders or packages. Projects
are used for building, version management, sharing, and organizing
resources related to a single work effort. The projects that you will
work with most in IBM® Integration
Designer are
modules, libraries, and mediation modules.

- Modules provide the business services for your application,
which are modeled as Service Component Architecture (SCA) components
wired together in a module assembly. Modules are the basic units of
deployment to the IBM Workflow
Server runtime
environment.
- Libraries offer a place to store resources that will be
shared by more than one module. Libraries are associated with modules
through dependencies.
- Mediation modules provide mediation service applications,
which intercept and modify messages that are passed between existing
services (providers) and clients (requesters) that will use those
services. Mediation modules can be deployed on the IBM Workflow
Server.

Component test projects provide a way that you can automate
the running of test cases. You can deploy and run component test projects
on IBM Workflow
Server.
They contain component test suites and test cases for testing components
in business integration modules. A succession of wizards help you
define the suites and cases.

You can bring Java™ projects into
your application. In some cases, you might choose to do bottom-up
development by designing Java resources
and then importing them into your IBM Integration
Designer application.
If you have Java code that will be used in a
business integration module or mediation module, create a Java project for the code and add a dependency
on the Java project from the module that will be using
the Java code. See the topic "Bottom-up development"
and "Using Java projects with modules" under
related topics for more information.

- Modules

A module is a project that is used for development, version management, organizing business service resources, and deploying to the  IBM Business Automation Workflow. In fact, a module is the basic unit of deployment to this runtime environment.
- Mediation modules

A mediation module is a WebSphere® Business Integration project that is used for development, version management, organizing resources, and deployment of mediation flows to the IBM Workflow Server.
- Modules and libraries dependencies

When developing and deploying integration applications, you might need to declare dependencies for your modules, mediation modules, and libraries. Use the dependency editor to manage these dependencies.
- Predefined resources

You can use predefined resources to save time when building your BPEL process.
- Namespaces

A namespace is a logical container in which all the names are unique; that is, a name can appear in multiple namespaces but cannot appear twice in the same namespace.
- Versions

Versioning provides the ability for the runtime environment to identify snapshots in the lifecycle of a solution or service and to be able to concurrently run multiple snapshots at the same time.