# Using message end events

## About this task

## Procedure

1. Open a process and drag a message end event from the palette onto the
diagram.
2. In the Event Properties section, click Select next to
Attached message UCA to select an existing undercover agent. 
To create an undercover agent, click New. See Undercover agents.
Undercover agents must have a schedule type of On Event to function as a
message trigger. Plus, the service attached to the selected undercover agent must have one or more
input variables so that it can pass and correlate information from the event.

Note: Ensure that the sender and receiver of the message both use the same undercover agent. For
example, if the receiver of the message is an message intermediate event in another process, then
select the same undercover agent for both the sending message end event and the receiving
intermediate event in the other process.
3. Click the Data Mapping option in the properties.
4. In the Input section, click the variable selector icon on the right side of each field to
map each undercover agent output variable to a local variable in the BPD. Click the
Use default check box if you want to use a default value from the attached
undercover agent for a particular variable. When you enable this check box, the variable selector
icon is disabled.