<!-- image -->

# Disassociating a module or library from a process application
or toolkit

## About this task

## Procedure

To disassociate a module or library from a process application
or toolkit, complete the following steps:

1 To disassociate a module or library:
    1. If you are connected to the Process Center, right-click
the module or library you want to disassociate from a process application
or toolkit. From the menu, click Disassociate from Process
Center. A message warns that the module or library will
be disassociated from the Workflow Center,
where other people might have been using it.
    2. If you are disconnected from the Process Center, right-click
the module or library you want to disassociate from a process application
or toolkit. From the menu, click Disassociate.
A message warns that the module or library will be disassociated from
the process application or toolkit only in your workspace. Your modules
and libraries will still be in the Process Center.
2. Check if there are other modules and libraries with a dependency
on the module or library that is being disassociated. Disassociate
those modules and libraries also and remove their dependency. If the
module or library is refactored and is still needed by these other
modules and libraries, associate them again with the refactored module
or library and add the dependencies back.
3. Click Yes to continue or No to
leave the module or library in its present state.

## Results

- Connected to the Process Center - When you disassociate a module
or library while you are connected to the Process Center, it is removed
 in the Process Center and your workspace from the process application
or toolkit it was associated to. The module or library that was disassociated
remains in your workspace, outside of the process application or toolkit,
in the Business Integration  view.
- Disconnected form the Process Center - When you disassociate a
module or library while you are disconnected from the Process Center,
it is removed only in your workspace from the process application
or toolkit it was associated to. The module or library that was disassociated
remains in your workspace, outside of the process application or toolkit,
in the Business Integration  view. You cannot
reassociate the same module to the process application or toolkit
it was disassociated from.

## What to do next

## Related tasks

- Switching between simple and advanced mode