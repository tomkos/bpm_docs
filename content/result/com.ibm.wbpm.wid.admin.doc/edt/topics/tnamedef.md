<!-- image -->

# Renaming or refactoring event definition names

## About this task

## Procedure

1 If you want to rename an event definition, completethe following steps:
    1. In the event definition editor, insert your cursor in
the Name field of the event definition that
you want to rename.
    2. Type in the new name that you want to assign to the
event definition. Note: 
The event definition name
must be unique within the project scope. If you are creating the event
definition in a module, the project scope is the entire module plus
any dependent libraries. If you are creating the event definition
in a business monitoring project, the project scope is the project
references that are listed in the project properties. If the project
references contain a module, then the modules' dependent libraries
are also in the same project scope as the business monitoring project.
    3. Press Ctrl-S. If the underlying
event definition file only contains this one event definition, then
the event definition file name is automatically changed to reflect
the new name of the event definition.
2 If you want to refactor an event definition name,complete the following steps:

1. Press Ctrl-S to save your most current changes.
2. In the event definition editor, insert your cursor in
the Name field of the event definition that
you want to rename.
3. Right-click and select Refactor Event Definition
Name. The Rename Artifact window opens.
4. In the New Name field, type the
new name of the event definition. Note: 
The event
definition name must be unique within the project scope. If you are
creating the event definition in a module, the project scope is the
entire module plus any dependent libraries. If you are creating the
event definition in a business monitoring project, the project scope
is the project references that are listed in the project properties.
If the project references contain a module, then the modules' dependent
libraries are also in the same project scope as the business monitoring
project.
5. If you want your new event definition name to be refactored
in all other event definitions that reference your event definition,
ensure that Update references is selected.
6. If you want to change the name of the event definition
file to match the new name of your event definition, ensure that Update
the file name to match the new name is selected.
7. Click OK.