# Using a message (receiving) event to receive intermediate and boundary message events

## About this task

## Procedure

1. Open a process, then using the intermediate event icon's drop-down, drag a Message
(receiving) event component from the palette onto the diagram. It can be dragged to the
swimlane or attached to an activity.
When the event is attached to an activity, the event is known as a boundary event and it is
included in the outline of the activity.
2 If the intermediate message event is a boundary event, use the BoundaryEvent section to specify its behavior:
    1. If receiving the message signals completion of the activity, make sure that the
Interrupt Activity option is selected, which is the default setting.
Otherwise, clear the selection, so that the activity is not interrupted and completed when the
message is received.
    2. If Interrupt Activity is not selected, the
Repeatable option is available. If the boundary message event can be
triggered more than once, select the Repeatable option so that the attached
activity can receive multiple messages.
3 Complete the following actions in the Event Properties section. Important: The sender and receiver of the message must both use the same undercoveragent. For example, if the sender of the message is a message end event in another process, thenselect the same undercover agent for both the receiving intermediate event and the sending messageend event in the other process. Tip: Undercover agents must have a schedule type of On Event tofunction as a message trigger. Plus, the service that is attached to the selected undercover agentmust have one or more input variables so that it can pass and correlate information from theevent.

1. To select an existing undercover agent, click Select next to the
Attached Message UCA field.
2. To create an undercover agent, click New. See Undercover agents.
3. In the Condition text box, type a JavaScript expression if you want to
define conditions under which the message event is processed.

If you do specify a condition and the condition evaluates to true, the message is accepted and
processing continues. If the condition evaluates to false, processing stops. In most cases, special
message conditions are not necessary because you should implement each message event with a separate
undercover agent.
4. If you want the incoming message to be consumed after it is received by the message event,
enable Consume Message. Refer to the bulleted list in Modeling message events to learn more about message consumption.
5. To allow the message event to receive an incoming message that arrives before a process is at a
point where the event can accept the
message, select Durable
Subscription. The durable subscription causes the message to be stored until the message
event is reached. Only the most recently received message is stored. 

Tip: If you occasionally use inbound messages and undercover agents, consider using
durable subscription events.
When Durable Subscription is selected, incoming messages are persisted in
the database. The durable messages accumulate, even if you select the check box to make them
consumable. Periodically use the BPMDeleteDurableMessages command for deleting
durable subscription events.
4 Specify the correlation and output mapping.

1. On the Properties tab, click Data Mapping.
2. Open the Correlation and Output Mapping section.
3. Select the output variable that you want to use to for correlation. The value that is assigned
to it ensures that the parameter values of the runtime message are passed to the correct process
instance. The variable that is selected for correlation is identified by an assignment symbol
(). This correlation ensures that the parameter values of the runtime message are passed to
the correct process instance. 
 For undercover agents that are implemented using a complex variable rather than a service,
you can select the complex variable or the top-level child properties of the variable for mapping or
correlation.
4. Map each output variable to a local variable in the process. 
For each variable, click the variable selector icon to map each output variable to a local
variable in the process.
5. Click Save or Finish Editing.