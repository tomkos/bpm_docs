# Creating a caller service

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

The next step in completing this sample inbound
integration is to create an Integration service to call the UCA to
send the event when the inbound web service (that you create in the
following section) is called.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Create an Integration service and name it Inbound
WS Handler or something similar. (If you need detailed instructions,
see Building an Integration service.)
4. Drag an Invoke UCA component from the palette, name it My
UCA and place it between the Start Event and End Event in
the service diagram.
5. Use the Sequence Flow tool to connect the service components
on the diagram.
6. Click the Invoke UCA component in the diagram.
7. Click the Variables tab, and then
click the Add Input button to add the someString variable
as an input variable.
8. Save the changes.
9. Select the Implementation option in the properties.
10. Click the Select button next to
the Attached Undercover Agent field and pick the Undercover Agent
that you created in the preceding procedure, My UCA.
11. Select the Data Mapping option in the properties.
The Input Mapping is automatically set to the someString variable
from the UCA.
12. In the field next to the variable, type tw.local.someString.
This sets the input value of the UCA to the local value of the someString variable,
which enables you to test the implementation in the Inspector as instructed
in Testing the integration.
The value is used in the business process definition correlation
mapping that is created in the initial task. Note: The someString variable
is available only if you create the attached service as instructed
in Creating an attached service and
the UCA as instructed in Creating an undercover agent before performing
the steps in this procedure.
13. Save your work.