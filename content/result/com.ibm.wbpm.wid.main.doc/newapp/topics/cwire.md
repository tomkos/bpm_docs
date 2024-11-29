<!-- image -->

# Wires

You can use a wire to connect components into an integrated
application. The target of a wire must support the interface or interfaces
that the source specifies.

There are two types of wires. The first type of wire comes from
a partner reference (the source) that is defined for a component or
stand-alone references node and goes to a component or import (the
target). In this case, the wire identifies the component or import
(target) that is accessed when the source component uses that partner
reference. By default, a partner reference contains only one wire
leading from it unless the partner reference's multiplicity property
is changed to 0...n.

The second type of wire comes from an export (the source) and goes
to a component or import (the target). In this case, the wire identifies
the (target) component that provides the service. An export can have
only one wire leading out of it.

You can wire components together in the assembly editor by moving
the mouse pointer over the source component or partner reference to
display the handle and then dragging the handle to connect to the
target. The following illustration shows a component with the handle
displayed for wiring:

The following illustration shows a partner reference with the handle
displayed for wiring:

You can also use the editor's wire action to automatically wire
components together. To learn about the wiring action, see "Creating
and wiring components."