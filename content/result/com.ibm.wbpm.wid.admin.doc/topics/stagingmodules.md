<!-- image -->

# Modules and staging modules in Integration Designer

Every IBM® Integration
Designer application
consists of an SCA module and an optional set of service library dependencies.
The SCA module contains the core artifacts that are needed to deploy
and run the application. Core artifacts might include business objects,
interfaces, maps, and BPEL processes, and other objects. When the
application is deployed and installed, Java™ code
is generated based on core artifact logic.

Artifacts that are created in Integration Designer are said
to be authored. If you create a new WSDL interface or business object,
you are also creating, behind the scenes, a corresponding .wsdl or
.xsd file in the workspace. In some cases, a single artifact type
consists of multiple files. For example, when you create a new BPEL
process, a few authored files including the .bpel, .bpelex, and Artifacts.wsdl
file are created in the workspace. Each of these files is authored,
since they are all necessary in order for the module to build successfully.

After a module is built, Integration Designer generates Java code for the authored artifacts
during the deployment process. Generated artifacts are usually Java classes based on the logic
defined in the authored BPM artifacts. Some of the generated deployment
code is in the module or library; some is in a separate staging project.
When working with the Process Center, no generated artifacts, neither
files nor entire projects, are placed in the repository.

## Staging modules

Every SCA module also contains
a set of generated staging modules. Since the staging modules define
the Java EE dependencies and optional web content, they generally
do not need to be modified by the user. Since the staging modules
do not contain authored BPM logic, they are not visible in the Business
Integration perspective, but they can be viewed in the Java EE or
Resource perspective.

- HelloWorldApp
- HelloWorldWeb

In general, only the SCA module and dependent libraries
need to be managed in source control. Staging modules appear in the
workspace after the SCA module is built. Because of this timing, staging
modules do not need to be managed within the source management control
system as long as they contain no custom content or changes to the
Java EE deployment descriptor.

In general, it is not advisable
to add authored content to a staging module. If you add authored content
to a staging module or make custom Java EE deployment changes, then
the affected staging modules will also need to be managed in source
control so that these changes can be preserved. If you add custom
content to the web staging module, such as HTML or JSP pages, the ModuleName web
module will need to be managed in the remote source control repository.
To avoid confusion, consider creating a separate web module for any
custom web content, rather than rely on the ModuleName web
staging module.

Non-derived files that are
inside a folder marked as derived assume the properties of the parent
folder; therefore, those files become derived.

An artifact's
derivation properties should never be changed. If you change an authored
artifact to "derived", the Integration Designer builders
treat the files as generated and delete them from the workspace.