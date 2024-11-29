<!-- image -->

# Creating a BPEL process from a component

## Before you begin

## Procedure

1. In the assembly editor, click the component so that it
is selected. Only Process and Untyped components
support BPEL process implementations.
2 Right-click the selected component and select GenerateImplementation to create the implementation. If a newimplementation is generated then it will be opened for editing. Ifthere is no implementation type for the component, select Process togenerate a BPEL process for this component. If the componenthas more than one interface you will be prompted to select the maininterface for the process. Callers of the process will interact withit using this interface. If the selected interface has morethan one operation, the Select Starting Operations windowis displayed. Select all of the operations which can start the process.If there are operations which do not start the process you shouldleave the associated check boxes cleared. In this case, where someoperations are not selected the generated BPEL process will containerrors. These errors stem from these unimplemented operations. Toresolve the errors you must add one or more of the following to theprocess in order to implement the remaining operations: To use an existing implementation for the component, click SelectImplementation and select one of the listed implementations.Note that the listed implementations must be located within the samemodule. Implementations in other modules can be used in the moduleassembly by creating imports for the published services (exports). Note: The SelectImplementation action does not add or remove componentinterfaces or partner references so that it does not affect existingwires. However, after using this action, the component's existinginterfaces or references might not match what is required by the selectedprocess implementation. In this case, there will be errors in theassembly diagram. Try these actions to fix the errors: If interfaces or partner references have been replaced, youmay need to add interface maps to rewire.

If the component
has more than one interface you will be prompted to select the main
interface for the process. Callers of the process will interact with
it using this interface.

    - a Receive activity
    - a Receive Choice activity
    - event handlers.

To use an existing implementation for the component, click Select
Implementation and select one of the listed implementations.
Note that the listed implementations must be located within the same
module. Implementations in other modules can be used in the module
assembly by creating imports for the published services (exports).

    - Use the Synchronize Interfaces and References menu item on the
component to synchronize to or from the implementation.
    - Manually add the required interfaces and references to the component,
and remove or change the non-matching ones.
    - Drag the implementation onto the canvas (to create a new component)
and then rewire the assembly diagram so that the new component replaces
the unimplemented component. Be sure to also copy the name and qualifiers
you defined in the original component to the new one. You can now
safely delete the replaced component.

## What to do next