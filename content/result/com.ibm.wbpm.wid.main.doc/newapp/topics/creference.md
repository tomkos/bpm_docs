<!-- image -->

# Partner references

A partner reference is required when one component
uses another component; it is defined on the component that wants
to use another component. The partner reference (sometimes referred
to as a reference) specifies the interface that is used in
the invocation of the other component. The partner reference also
contains wires that specify the target components that can be used.

Assembling the components for the application involves creating
partner references, interfaces, and the wiring of components in the
module assembly. The result is an assembly diagram that represents
the modeled solution.

In the assembly editor, the component's partner references are
represented by small blocks on the right side of the component. The
block contains the number of wires that are allowed in the partner
reference; the numbers are either 1..1 or 0..n to indicate
one wire or 0 to n number of wires. adding wires explains
how to add several wires. The following image shows a CustomerQuery
component that has partner references:

If there are many partner references for your component, you can
collapse them. Select the partner reference on the component and right-click
to invoke the Collapse References  and Expand
References actions to collapse and expand them. As shown
here, the CustomerQuery component's partner references have been collapsed: