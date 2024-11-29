<!-- image -->

# Creating an implementation for a component

The component's implementation provides the business logic
for the service.

## About this task

There is no exclamation mark on the component when
its implementation exists. The following CustomerQuery component has
an existing business process implementation:

## Procedure

1. In the assembly editor, click the component so that it
is selected.
2 Right-click the component and select GenerateImplementation to create the implementation. If a newimplementation is generated then it will be opened for editing. Ifthere is no implementation type for the component, you have to selecta type for this action. To use an existing implementationfor the component, click Select Implementation andselect one of the listed implementations. Note that the listed implementationsare located within the same module. Implementations in other modulescan be used in the module assembly by creating imports for the publishedservices (exports). Note: The Select implementation actiondoes not add or remove component interfaces or partner referencesso that it does not affect existing wires. However, after using thisaction, the component's existing interfaces or references might not matchwhat is required by the selected implementation. In this case, therewill be errors in the assembly diagram. Try these actions to fix theerrors: If interfaces or partner references have been replaced, you mayneed to add interface maps to rewire.

To use an existing implementation
for the component, click Select Implementation and
select one of the listed implementations. Note that the listed implementations
are located within the same module. Implementations in other modules
can be used in the module assembly by creating imports for the published
services (exports).

    - Use the Synchronize Interfaces and References menu
item on the component to synchronize to or from the implementation.
See "Synchronizing the interfaces and references between components
and implementations" in the related links at the end of this topic.
    - Manually add the required interfaces and references to the component,
and remove or change the non-matching ones.
    - Drag the implementation onto the canvas (to create a new component)
and then rewire the assembly diagram so that the new component replaces
the unimplemented component. Be sure to also copy the name and qualifiers
you defined in the original component to the new one. Afterward, you
can safely delete the replaced component.

## Related tasks

- Opening an implementation
- Replacing an implementation
- Changing the implementation type of a component

## Related information

- Synchronizing the interfaces and references between components and implementations