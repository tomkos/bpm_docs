# Attaching the undercover agent to the message event

## Before you begin

To perform
this task, you must be in the IBM® Process
Designer desktop
editor, which is deprecated.

## About this task

After you create the UCA, you should go back to
the message event in the BPD and attach the UCA as described in the
following steps.

## Procedure

1. Open the desktop Process Designer (deprecated).
2. Open a process application that contains a BPD with a message
event.
3. Open the BPD that includes the message event.
4. Click the message event in the BPD to select it.
5. Click the Implementation option in the properties.
6. In the Message Trigger section, click the Select button
next to the Attached UCA field and pick My UCA that
you created in the preceding steps.
7. Ensure that the Consume Message and Durable
Subscription check boxes are enabled. (For more information
about these options, see Modeling message events.)
Tip: If you occasionally use inbound messages, consider
using durable subscription events. Durable subscriptions are Java
Message Service (JMS) subscriptions that persist and store subscribed
messages even when the client is not connected. The durable messages
accumulate, even if you select the check box to make them consumable.
Periodically use the BPMDeleteDurableMessages 
command for deleting durable subscription events.
8. Click the Data Mapping option in the properties.
Notice that the Output correlation key is automatically
set to the someString variable from the UCA. The
variable is used as a correlation parameter, which allows you to correlate
an event recipient with a particular key. Note: When an event occurs,
that event must be matched against the correct instance of the process
for which the event is destined. The ability to match the event against
the correct instance is called correlation. You must specify one variable
in the message event that has a value that matches the value of the
incoming event's UCA payload (the correlation value). If there is
such a match, the message is received. If not, the message is not
received, and the event continues to wait.
9. In the field next to the variable, type tw.system.process.instanceId.
This sets the value of the someString variable to
the ID of the running instance, which allows you to test the implementation
in the Inspector. In this example, you are creating
a UCA that uses the current process instance ID as the correlation
parameter. For example, if you have a process application with the
instance ID of 50 and another process application with the instance
ID of 100, if you invoke the UCA passing an ID of 50, only the first
process application receives the event.
10. Save your work.