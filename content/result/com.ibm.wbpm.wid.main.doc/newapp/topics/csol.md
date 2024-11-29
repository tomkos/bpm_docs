<!-- image -->

# Creating modules and libraries

When you build integrated business solutions with IBM® Integration
Designer,
you will create modules, mediation modules, and libraries to contain
the resources and code.

Integration Designer provides
you with the tools to easily compose a business solution that integrates
applications, processes, and data across multiple systems and business
organizations. You can use Service Components Architecture (SCA) components
to build solutions that are wired together to form modules or mediation
modules. You can then deploy the solutions to the IBM Workflow
Server.

You
can use the simple organization of resources in IBM Integration
Designer to
quickly build and test integrated business solutions without worrying
about the details of the generated artifacts. You can create a module
or a mediation module and immediately start to create business integration
applications, including resources such as business objects and interfaces.
Generated code is automatically placed in default locations. The supporting
artifacts that do not have to be manipulated when creating the applications,
are hidden in the views.

## Public and private artifacts

Artifacts in
a library are public. Artifacts in a module are private. When you
are designing an application, think about logical function and visibility
as you organize artifacts. For example, place related data types that
are used by various pieces of a system into a library. Other modules
can then reuse this library. You only need to create and maintain
one copy of each artifact when you use this method. Likewise, you
should group related business logic features of the application into
modules. When you make an application a component, it is easier to
change and maintain the application. It is also easier to add new
features.

- Partitioning libraries and modules

When you put artifacts in libraries, you can share those artifacts with modules. The method that you use to package the libraries and their contents can affect maintenance and scalability.
- Business integration projects

The first act in developing an application is to set up one or more projects to hold your resources. A project is an organized collection of folders or packages, and it is the largest structural unit in your workspace.
- Creating new projects

The first step in developing an application is to set up one or more projects.
- Creating a module

You can use a module in a business integration project to develop and organize resources, and deploy them to IBM Integration Designer.
- Creating mediation modules

A mediation module is a business integration project that is used for development, version management, organizing resources, and deployment to the runtime environment. It contains flows that intercept and modify messages between service consumers (exports) and service providers (imports). Mediation modules can be deployed to the IBM Business Automation Workflow.
- Creating libraries

A library is an IBM Integration Designer project that is used for the development, version management, and organization of shared resources.  Only a subset of the artifact types can be created and stored in a library.
- Creating shared libraries

In IBM Integration Designer, you can share your Java™ binaries, XML schemas, and WSDL definitions by using shared libraries (by-reference) for your Service Component Architecture (SCA) modules and libraries.
- Versioned modules and libraries

You can create versioned modules and libraries to use on a server at run time.
- Comparing business objects in modules and libraries

You can compare modules and libraries to see the differences in the business objects. You can view, but not edit, the comparison file.
- Configuring the business object parsing mode of modules and libraries

The method by which XML data is parsed at run time on IBM Workflow Server is governed by the business object parsing mode.
- Adding dependencies

You can add dependencies on libraries, Java™ projects, and Java 2 Platform Enterprise Edition projects.

## Related concepts

- Workspaces

## Related tasks

- Organizing projects using integration solutions
- Creating and wiring components
- Working with implementations
- Adding notes
- Setting assembly editor preferences
- Finding errors in the assembly diagram

## Related information

- Assembling services: Customer enquiry example