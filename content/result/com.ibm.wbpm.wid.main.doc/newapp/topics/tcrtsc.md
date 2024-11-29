<!-- image -->

# Creating components

Use the assembly editor to create Service Component Architecture
(SCA) components, called components in most of the documentation.
Components are business services that operate on business data and
refer to an implementation. They can also contain partner references
and interfaces.

## About this task

## Procedure

- Select a component from the palette and drop it onto the
canvas.  Use the untyped component (or component with
no implementation type) in the palette when you want to create a new
component but do not know which type of implementation you want to
use for it. Later, you can specify the implementation type and generate
its implementation. However, you cannot use untyped components in
mediation modules.
The Java™ component in the palette will be implemented as a Java class. It supports both WSDL type interfaces and Java type interfaces. Java components and stand-alone references are
the only component types that support Java type interfaces.
Other components include process, human task,
and state machine. For more information on each type of component,
see the topics about implementations.
- Drag an interface (from the same module or from a dependent
library) onto the canvas.  When you are prompted to specify
the type of object to create, select an implementation or Untyped Component. Later, you can change the implementation
type and generate the implementation.
- Drag an implementation such as a human task from the same
module onto the canvas.