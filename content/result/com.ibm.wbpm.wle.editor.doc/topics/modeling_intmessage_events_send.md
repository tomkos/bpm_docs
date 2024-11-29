# Using intermediate message events and message end events to send messages

You can include an intermediate message event in your process when you want to model a
message event that is sent during execution of a process, or a message end event when you want to
send a message at an end of a path.

## Procedure

1. Open a process and drag an intermediate or end event from the palette onto the
diagram.
2. In the diagram, select the new event.
3. On the Properties tab, click
General. The default implementation for intermediate events that are
included in the process flow is Message. If you are creating a message end
event, select Message as the end event type.
4. If you are creating an intermediate message event, select Message
(sending) as the intermediate event type in the drop-down list. By default, all message
end events are sending message end events.
5 In the Event Properties section, complete oneof the following actions: Important: The sender and receiver of the message must both use the same undercoveragent. For example, if the sender of the message is a message end event in another process, thenselect the same undercover agent for both the receiving intermediate event and the sending messageend event in the other process. Tip: Undercover agents must have a schedule type of On Event tofunction as a message trigger. Plus, the service that is attached to the selected undercover agentmust have one or more input variables so that it can pass and correlate information from theevent.
    - To select an existing undercover agent, click Select next to the
Attached Message UCA field.
    - To create an undercover agent, click New. See Undercover agents.
6 If you created an end event, specify the input mapping.

1. On the Properties tab, click Data
Mapping.
2. Open the Input section.
3 Map each input variable to a local variable in the process. For each variable, select it then complete one of the following actions.
    - Click the variable selector icon to map each input variable to a local variable in the
process.
    - Enter a literal value or the name of a local variable.
    - To use the default value from the variable, click Use default. When you
enable this check box, the variable selector icon is disabled.