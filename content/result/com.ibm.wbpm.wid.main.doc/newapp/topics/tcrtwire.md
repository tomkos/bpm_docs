<!-- image -->

# Wiring nodes in the assembly diagram

An assembly diagram can contain components (including selectors),
imports, exports, and stand-alone references. Some of them have interfaces,
some have references, and some have both. You use wires to assemble
these nodes into an integrated application that is deployed to the
runtime environment.

## About this task

There are two types of wires. The first type of wire comes
from a partner reference (the source) that is defined for a component
or stand-alone references node and goes to a component or import (the
target). In this case, the wire identifies the component or import
(target) that the source component accesses when it uses that partner
reference. By default, a partner reference uses only one wire leading
from it unless the partner reference's multiplicity property is changed
to 0...n.

The target of a wire must support the interface or
interfaces that the source specifies. If the partner reference on
a source cannot find a matching interface on the target, you can add
a new interface on the target to create a mediation flow. Also, a
WSDL partner reference cannot be wired directly to a Java™ interface. For WSDL and Java interfaces and partner references wiring
information, see the "WSDL and Java interfaces
and references" topic under related concepts.

The second type
of wire comes from an export (the source) and goes to a component
or import (the target). In this case, the wire identifies the target
component that provides the service. An export can have only one wire
leading out of it.

Wiring components and stand-alone references

After
you open the module assembly with the assembly editor, select one
of the following three methods to wire two nodes together:

## Procedure

To wire a node in the assembly diagram, complete the
steps in one of the following three methods:

1 Using the wiring handle
    1. If you have added the wiring reference to the source
node (for example, a component), move the mouse pointer over the partner
reference. An orange box with a handle appears around the reference,
as shown in the following illustration:  
You can see reference information in the window that
appears. Drag the handle to the target node. If a matching interface
is not available on the target, you must create a matching interface.
You can also generate a mediation flow for the wire. Make a selection
and click OK.
    2. If the reference for the wiring is not been added
to the source node, move the mouse pointer over the source node. An
orange box with a handle appears around the node:  
Drag the handle to the target node. When you select
the source node when you are creating a wire, instead of its partner
reference, you create a new partner reference on the source.
2 Using the Wire palette

1. On the palette, click Wire.
2. To add a wire for a partner reference, click a partner
reference on the source. Always click the source first, then the target.
If you want to ignore existing partner references on the source
and you want to create and wire a new partner reference on the source,
click the source node instead of a partner reference.
3. Click the target node. If a matching interface is not
available on the target, create a matching interface or a mediation
flow for the wire. Make a selection and click OK.
4. If the source selection is a node (rather than a reference)
and the target node does not have an interface, you must find an existing
interface definition to use for the wiring.
3 Using the Wire action The wire actionswork only on existing unwired partner references and interfaces onthe selected node.

The wire actions
work only on existing unwired partner references and interfaces on
the selected node.

1 Right-click a source node and select one of these actions: If you selected the partner reference of the node wheninvoking the Wire (Advanced) action, the AdvancedWiring window displays only the target nodes.
    - Wire References to NewTo create new target components
or imports and wire them to the unwired partner references on the
selected source, click Wire References to New. 
If
you selected a partner reference of a source instead of selecting
the node, the new target is created only for the selected reference.
    - Wire to ExistingTo complete the wiring for unwired interfaces
and references on the selected node, click Wire to Existing.
This action completes the wiring for unwired interfaces and references
on the selected node. If you selected a node and launched the Wire
to Existing action, matching interfaces and the references
of existing nodes in the assembly diagram are located, and the wiring
of all available partner references and interfaces on the selected
node is completed. If several sources or targets are possible, select
the appropriate sources or target in the Advanced Wiring window.
If
you selected a partner reference or the interface and launched the
action, the wiring is completed only for the selected partner reference
or interface.
    - Wire (Advanced) To complete the wiring of available partnerreferences, click Wire (Advanced) . This actioncompletes only the wiring of available partner references. If youselected a node and right-click to select Wire (Advanced) ,the following Advanced Wiring window opens: By default, the Onlyshow targets with matching interface types check box isselected. This means that the right container lists only the interfacesthat match the selected partner reference. The left containertree shows the node with its available (unwired) partner references.Select one of partner references in the references tree for wiring.If this container does not show any references, it means that thereare no partner references on the node or that all the references havebeen wired and none are available for wiring. When the Onlyshow targets with matching interface types check box isnot checked or if there are no available references to wire, click NewReference to create a new partner reference and wire it.The new partner reference is created in the assembly diagram onlyif it is used in the Advanced Wiring window. Thecontent of the right container changes depending on what is selectedin the left container. You can click New to create anew node for the wiring. Click OK tocomplete the wiring.

To complete the wiring of available partner
references, click Wire (Advanced). This action
completes only the wiring of available partner references. If you
selected a node and right-click to select Wire (Advanced),
the following Advanced Wiring window opens:

By default, the Only
show targets with matching interface types check box is
selected. This means that the right container lists only the interfaces
that match the selected partner reference.

The left container
tree shows the node with its available (unwired) partner references.
Select one of partner references in the references tree for wiring.
If this container does not show any references, it means that there
are no partner references on the node or that all the references have
been wired and none are available for wiring.

When the Only
show targets with matching interface types check box is
not checked or if there are no available references to wire, click New
Reference to create a new partner reference and wire it.
The new partner reference is created in the assembly diagram only
if it is used in the Advanced Wiring window.

        - If the Only show targets with matching interface types check
box is selected, the right container lists only the interfaces that
match the selected partner reference in the left container.  If no
nodes appear in the right container, it means that there are no nodes
that have matching interface types for the selected partner reference,
or that there are no other nodes in the wiring diagram.You have
the option of clicking the New button to create
a new component or import for the wiring. The new node appears in
the right container for your selection. The new node is created only
if it is used in the Advanced Wiring window box.
        - If the Only show targets with matching interface types check
box is not selected, the right container lists all the nodes
in the wiring diagram. You can select any node and if there is no
matching interface on the target node, you can add a new interface
on the target. Sometimes, you are also given the option to create
a mediation flow.

You can click New to create a
new node for the wiring.

Click OK to
complete the wiring.

If you selected the partner reference of the node when
invoking the Wire (Advanced) action, the Advanced
Wiring window displays only the target nodes.

## Results

To delete unwanted wires, select the wire in the assembly
diagram and press the Delete key.