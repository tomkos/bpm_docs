<!-- image -->

# Managing SCA modules, libraries, and staging modules in Integration Designer

## Before you begin

## About this task

## Procedure

- When working with a module that is being managed under
source control, make sure to check out the entire module from the
remote software configuration management (SCM) system. Never check
out an individual artifact, such as a single WSDL or XSD file, from
a module that is managed in source control.
- Although a module can be checked out by multiple users
simultaneously, only one person should ever have write-access to the
module at any one time if the system allows that restriction. Enforcing
such practices prevents merge conflicts. If you need to make changes
to a module and want to prevent other users from committing any changes,
lock the module for exclusive write-access. Any management system
you use will work best if there is good communication among developers.
- When using libraries, keep in mind that changing a shared
business object or WSDL may have unexpected side effects on other
modules or components that also use this library artifact.
- Always synchronize changes with the repository before blindly
adding code through commit or update actions. Although a full synchronization
is not strictly required before you commit or update artifacts, synchronizing
will not only provide you with a full list of changes, but might also
prevent you from inadvertently overwriting modified artifacts saved
by other users.
- If synchronization conflicts do occur, manually merge the
changes rather than relying on the text-based merge techniques that
are used in the Integration Developer merge tools. Although
text-based merging works well with Java™ code,
it is not as reliable for XML-based Integration Developer artifacts.
If you use the merge tools to combine two BPEL processes, you will
be merging raw XML code or plain text, which is contrary to the standard
GUI editors that exist for many Integration Developer artifacts.
- Use the Show Files option in the
Business Integration view to see a list of the backing files for a
component.
- Never change the derived flag in the artifact properties.
Integration Designer generates
background files when you build your project. These generated files
are automatically marked as derived when they are generated.
Derived files should not be placed in the source control management
system. In most cases, you should not change that derived marking.
If an authored artifact is changed to derived, Integration Designer will permanently
delete the file from the SCA module. This deletion occurs because
the builders assume that a derived file is a generated file. The program
assumes that generated files can only be created during deployment
or installation; therefore, this derived artifact must be present
by mistake, so the program deletes it from the workspace. This behavior
only exists for SCA modules; other modules, such as web or Java projects, can contain derived
artifacts that will not be removed during deployment.
- If you are using Rational ClearCase, do not change the
read-only flag on a file.  Note: Support for Rational® ClearCase® has
been deprecated.
- Usually, you do not need to manage staging modules in sourcecontrol, but there are exceptions described below.
    1. You need to manage the ModuleNameApp
staging module under version control in rare cases where the module
deployment editor lacks a feature that exists in the ModuleNameApp
Java EE deployment descriptor.
    2. In cases where you need to add custom web content, such
as web client interfaces, create a separate web project for that custom
dynamic web content. You should not add custom code to the ModuleName web
staging module.