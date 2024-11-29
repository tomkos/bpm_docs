# Adding a Decision service to a process (deprecated)

## Before you begin

To perform
this task, you must be in the IBM Process
Designer desktop
editor, which is deprecated.

To create
services, you must have access to a process application or toolkit
in the Workflow Center repository.
Access to process applications and toolkits is controlled by users
who have administrative rights to the repository. For more information,
see Managing access to the Workflow Center repository.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a BPD.
3 Create a new Decision service.
    1. Click the plus sign next to Decisions to add a new Decision service.
    2. In the Create New window, click Decision Service.
    3. In the New Decision Service window,
enter a name for the new Decision service, then click Finish.
    4. Process Designer displays
the diagram of the service with the default Start Event and End Event
components.
4. Drag a rule component, such as a BAL Rule, JRules Decision
Service or Decision Table component, from the component palette to
the Decision service diagram.
5 Depending on which component or components you added tothe service diagram, follow the additional steps in the followingrelated topics to configure the components in the Decision service:

- Adding a BAL Rule component to a service
- Adding a JRules Decision Service component to a service
- Adding a Decision Table component to a service
6. If you do not want to automatically synchronize shared business objects that are inputs to this
service when the business object is changed in other instances, switch to
Overview and clear Automatically sync shared business
objects.

Important: Nested services inherit the synchronization behavior of the starting service.
In addition, if you have a service that runs custom logic and then explicitly saves your shared
business objects, always clear the automatic synchronization option. Otherwise, the shared business
object is automatically saved and the code in your service will not run.

## What to do next

You can now nest this Decision service in any other service
within your process application that requires this logic. Be sure
to adjust the input and output variables as required for each implementation.
See  Declaring and passing variables for more information.