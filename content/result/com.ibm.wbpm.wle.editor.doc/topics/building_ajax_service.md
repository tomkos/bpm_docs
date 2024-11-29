# Building an Ajax service in the desktop Process Designer
(deprecated)

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

To create
services, you must have access to a process application or toolkit
in the Workflow Center repository.
Access to process applications and toolkits is controlled by users
who have administrative rights to the repository. For more information,
see Managing access to the Workflow Center repository.

## About this task

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Click the plus sign (+) next to User Interface,
and then click Ajax Service.
4. Specify a name for the service and click Finish.
IBM Process
Designer displays the
diagram of the service with the default Start Event and End Event components.
5. To protect your Ajax service against unauthorized callers, in the
Overview tab, under Settings, select Secure
service against unauthorized access. 
At run time, the caller's authorization is checked. If
the caller is not authorized to access the service, the call is rejected.
6. Add variables that the service will use as input or output.
You can also add private variables. See Declaring variables for a process or service for information.
7. Add components to the service diagram and then set up the
sequence flow. For more information about components, see Service components in Process Designer.
8. Configure the components in the sequence flow. For
example, if you are using a Server Script component,
add a script in the implementation properties.
9. Save changes. The Ajax service is available
for use in coach views. Attention: You cannot
automatically synchronize shared business objects for Ajax services.
The Automatically Sync Shared Business Objects setting
is always disabled

## Example