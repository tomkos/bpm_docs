<!-- image -->

# Adding partner references

The partner reference of a component or a stand-alone
references node specifies the interface that is used to invoke another
service.

## About this task

The component implementation type determines the type
of interface that its partner references have. All components support
Web Service Definition Language (WSDL) interfaces in their partner
references. The Java™ component, the component that
does not have an implementation type, and the stand-alone references
can have either a WSDL or Java interface
in its partner reference. In this case, the Add Reference window
specifies the type of interface that you use for the partner reference.
You have a set of radio buttons for the Show WSDL and Java, Show
WSDL, and Show Java options. If
the Java interface is not supported for the partner
reference, the Add Reference window does not
show the options to select WSDL or Java interfaces.

When you work in the assembly
editor, you can add a partner reference to a node before you
wire it to a target, or you can add a partner reference during the
wiring.

## Procedure

To add a partner reference to a component or stand-alone
references node before you do the wiring, complete the following steps:

1. In the assembly editor, click the component or stand-alone
references so that it is selected on the canvas.
2. Click the Add Reference icon, ,
that appears above the component. The Add
Reference window is opened. 
The partner reference
specifies the interface that is used in the invocation of the other
component; the Add Reference window lets you
select the interface that will be used.
3. To see interfaces in the module and dependent libraries
and projects, see the Matching interfaces container. To
see Java interfaces, select the Show
Java or the Show WSDL and Java option.
4 To find an interface, type the name of the interface inthe Filter field until you see the name of the interface in the Matchinginterfaces container. If the interface you want to use does not exist,complete the following steps:
    1. Click the New button. Then select
the type of interface you want to create, and click OK.
    2. In the Create New Interface wizard,
specify the module or library to indicate where the new interface
is to be added and a name for the interface. Depending if the interface
is a Java or WSDL interface, you may need to specify
different information; use the Tab key to focus on the field or button
and press the F1 key (Ctrl+F1 for Linux®)
to get additional help to complete the information in the wizard.
    3. Click Finish to create the new
interface. In the Java interface that opens, you
can add Java code to complete the interface definition. You can add
the code or close the Java editor
and complete the coding later.A WSDL interface without any operations
is created. After the partner reference has been added to the stand-alone
references node or component, the interface editor opens. Use the
interface editor to add operations to the interface.
5. Now, you can proceed to finish adding the partner reference
to the node. In the Add Reference window, select
the interface in the Matching interfaces container.
The fully-qualified file that has the interface is shown in the Qualifier container.
If there is more than one interface with the same name, make sure
that you select the right file in the Qualifier container.
6. Select the interface and click OK to
finish the creation of the partner reference.

## Results

Every reference on the node is represented by a reference
icon,  on the right side of the component. By default,
a newly created reference has multiplicity setting of 1..1 which means
that it must have exactly one wire going to a target service. See
related tasks for more information on adding more than one wire to
a reference.

## Add the partner reference as you add the wire

You
can add wires by using the wire in the palette or dragging the wire
handle from the source node. As you add a wire from a component or
stand-alone references node to a target service (which is either a
component or import), you will be prompted if a matching partner reference
is to be added to the source node. If you answer OK,
the reference will be created on the source component or stand-alone
references.

Also, you can invoke the advanced
wiring window to do the wiring. Click the New Reference button
to add a new partner reference before you do the wiring. See "Wiring
nodes in the assembly editor" under related tasks for more information
on advanced wiring.