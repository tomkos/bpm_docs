<!-- image -->

# Creating and wiring components

You can build applications by assembling the SCA components.
Components form the individual elements of the applications that are
in your process. The following tasks describe how you can add and
wire components together.

- Business services: Top-down development

When using the top-down development approach to build an assembly diagram, you define the components for your application and then implement them.
- Business services: Bottom-up development

When using the Bottom-up development approach to build a module assembly, you will implement your business logic first and then wire the artifacts together in the assembly diagram.
- Assembly editor

The IBM Integration Designer's assembly editor lets you build applications by assembling the Service Component Architecture (SCA) components.
- Components

You can build applications by assembling the SCA components.
- Wires

You can use a wire to connect components into an integrated application. The target of a wire must support the interface or interfaces that the source specifies.
- Creating components

Use the assembly editor to create Service Component Architecture (SCA) components, called components in most of the documentation. Components are business services that operate on business data and refer to an implementation. They can also contain partner references and interfaces.
- Renaming components

If you want to rename a component in the assembly editor, you can choose between simply renaming the component without renaming its implementation or renaming both the component and its implementation. You might want to rename components to keep the names of the component and implementation in synchronization.
- Deleting components

If you choose to delete a component in the assembly editor and a component implementation exists for the component, you can delete the associated component implementation.
- Adding interfaces

You can add interfaces to a component, an import, or an export, and you can define how a component is invoked by other components. Interfaces are also stored in a library to facilitate reuse.
- Adding partner references

The partner reference of a component or a stand-alone references node specifies the interface that is used to invoke another service.
- Wiring nodes in the assembly diagram

An assembly diagram can contain components (including selectors), imports, exports, and stand-alone references. Some of them have interfaces, some have references, and some have both. You use wires to assemble these nodes into an integrated application that is deployed to the runtime environment.
- Adding more than one wire to a partner reference

To add more than one wire to a partner reference, you must change the multiplicity setting for the reference to 0..n.

## Related concepts

- Workspaces
- Creating modules and libraries

## Related tasks

- Organizing projects using integration solutions
- Working with implementations
- Adding notes
- Setting assembly editor preferences
- Finding errors in the assembly diagram

## Related information

- Assembling services: Customer enquiry example