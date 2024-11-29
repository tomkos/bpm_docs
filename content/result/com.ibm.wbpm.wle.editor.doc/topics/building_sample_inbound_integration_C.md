# Creating an undercover agent for a BPD

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

The undercover agent tells IBM Business Automation Workflow what
service to run when the message event is received. The message can
be triggered by Business Automation Workflow itself
or by an external system as in this example.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application in the Designer view.
3. Click the plus sign next to Implementation and then select Undercover
Agent from the list.
4 In New Undercover Agent , enter thefollowing information and then click the Finish button.
    - Name: Type My UCA or something
similar for the name.
    - Schedule Type: Select On Event from
the drop-down list.
5. In the Details section, the queue for processing this undercover
agent is set to Async Queue by default. This setting is fine for the
sample integration. (To learn more about the queue options, see Undercover agents.)
6. In the Parameter Mapping section, you can see that the
undercover agent is automatically mapped to the someString variable
from the attached service, My UCA Handler.
7. Save your work.

## What to do next