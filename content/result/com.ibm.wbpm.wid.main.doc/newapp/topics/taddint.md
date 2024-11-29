<!-- image -->

# Adding interfaces

You can add interfaces to a component, an import, or an
export, and you can define how a component is invoked by other components.
Interfaces are also stored in a library to facilitate reuse.

## About this task

The Service Component Architecture (SCA) programming model
supports Web Service Definition Language (WSDL) and Java™ interfaces.
All the components support WSDL type interfaces. Only Java components, untyped components, and selectors
support Java type interfaces. If a component,
import, or export has more than one interface, all the interfaces
must be the same type.

Untyped components, Java components,
imports without binding, exports, and selectors can all have either
WSDL or Java interfaces. When you add interfaces
to nodes, you must specify the type of interface; that is, you have
a set of radio buttons for Show WSDL and Java, Show
WSDL, and Show Java options.

For
the other components that require a specific interface type, the options
to select WSDL or Java interfaces are not be
available.

The instructions in this topic assume that you have
a choice in selecting either a WSDL or Java interface.

## Procedure

To add an interface to a node before you do the wiring,
complete the following steps:

1. In the assembly editor, click the node so that it is selected
on the canvas.
2. Click the Add Interface icon  that
appears above the node. The Add Interface window
opens.
3. The Add Interface window shows interfaces
in the module and dependent libraries and projects. The list of interfaces
is displayed in the Matching interfaces container.
To see Java interfaces, select the Show
Java or the Show WSDL and Java option.
4 To find an interface, start to type the name of the interfacein the Filter field until you see the name of the interface in theMatching interfaces container. If the interface you want to use doesnot exist, complete the following steps:
    1. Click the New button.
If you have selected Show WSDL and Java,
a message asks which type of interface you want to create. Select
the type you want and click OK.
    2. In the Create New Interface wizard, specify a module
or library where the new interface is to be added and provide a name
for the interface. Depending whether the interface is a Java or WSDL interface, you may need to specify
different information; use the Tab key to focus on the field or button
and press the F1 key (Ctrl+F1 for Linux®)
to get additional help to complete the information in the wizard.
    3. Click Finish to create the new
interface. In the Java interface that opens, you
can add Java code to complete the interface definition.A WSDL interface
is created without any operations. The interface editor opens for
the new interface. Use it to add operations to the interface.
5. In the Add Interface window, select
the interface in the Matching interfaces container.
The fully qualified file that has the interface is shown in the Qualifier container.
If there is more than one interface with the same name, make sure
that you select the right file in the Qualifier container.
6. Click OK to finish adding the interface
to the node.

## Add the interface as you add the wire

You
can add wires by using the wire in the palette and then drag the wire
handle from the source node, or by using the Advanced wiring window
box. As you add a wire from a source to a target, you must decide
if you want to add a matching interface or reference, or both. When
you click OK, the interface is created on the
target node. See "Wiring nodes" for more information on the wiring
actions.

The interface icon, ,
on the node, indicates that it has one or more interfaces.