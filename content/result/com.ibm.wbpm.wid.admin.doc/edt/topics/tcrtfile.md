<!-- image -->

# Creating new event definitions

Using the New Event Definition wizard, you can create a
new event definition in a module, library, or business monitoring
project and then edit the event definition in the event definition
editor. Event definitions that have been created in the event definition
editor can be used to create custom event emitter activities in the
visual snippet editor.

## About this task

## Procedure

1. From the File menu, select New >
Other. The New wizard opens.
2. In the Wizards list, expand Business
Monitoring and select Event Definition.
3. Click Next. The New Event Definition
wizard opens.
4. Beside the Source folder field,
click Browse. The Folder Selection window
opens.
5. In the Folder Selection window, select the module,
library, or business monitoring project where you want to create the
new event definition.
6. Click OK.
7. In the Name field, type the name
that you want to give to the event definition. Note: 
The
event definition name must be unique within the project scope. If
you are creating the event definition in a module, the project scope
is the entire module plus any dependent libraries. If you are creating
the event definition in a business monitoring project, the project
scope is the project references that are listed in the project properties.
If the project references contain a module, then the modules' dependent
libraries are also in the same project scope as the business monitoring
project.
8. Click Finish. Depending on the perspective
that you are currently working in, the new event definition is created
in the Events folder or the Event
Definitions folder under the selected module, library,
or business monitoring project. The event definition editor automatically
opens to enable you to edit the new event definition.

## What to do next