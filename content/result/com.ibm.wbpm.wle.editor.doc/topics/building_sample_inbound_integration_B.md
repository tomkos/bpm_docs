# Creating an attached service for a BPD

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

The undercover agent (UCA) that you attach to the
message event needs a service to pass the parameter values from the
runtime message to the BPD.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a BPD.
3. Create a General System service and name it My
UCA Handler or something similar. (If you need detailed instructions,
see Building a General System service.)
4. Use the Sequence Flow tool to connect the Start Event and
End Event components in the service diagram. Because this
service is used to simply pass values, you do not need to add any
service components to the diagram.
5. Click the Variables tab.
6. Click the Add Input button and replace Untitled in
the Name field with someString.
7. Leave the variable type for the input variable set to String.
8. Click the Add Output button and
replace Untitled in the Name field with someString.
9. Leave the variable type for the output variable set to String.
10. Save your work.