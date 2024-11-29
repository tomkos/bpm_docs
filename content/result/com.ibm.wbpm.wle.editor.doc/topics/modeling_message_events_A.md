# Using start message events

## About this task

- When a message is received by a start message event (specifying that an incoming message is to
start a process at run time), a new instance of the process is created and a unique instance ID is
assigned to it.
- If you use multiple start message events in a single process, use a separate undercover agent
for each. If you use the same undercover agent for multiple start message events, multiple instances
of the process are initiated.

For example, you might want an employee on-boarding process to start when a record for
each new employee is created in your HR system. When the record is created, the system sends an
event to the workflow server, which captures the event and starts the follow-on steps for each new
employee such as setting up the necessary space and computer equipment, requesting and creating a
security badge.

## Procedure

1. Open a process or drill into an event subprocess, then drag a Message Start Event
component from the palette onto the diagram.
2 If the start event is part of an event subprocess, the StartEvent section shows the following options.
    1. If receiving and processing the message causes completion of the
parent process, make sure that the Interrupt Parent Process option is
selected, which is the default setting. When this option is selected, when the subprocess reaches
its end, the parent instance is completed. Otherwise, clear the selection so that the parent process
is not interrupted or completed when the message is received.
    2. If Interrupt Parent Process is not selected,
the Repeatable option is available. If the start message event can be
triggered more than once, select the Repeatable option so that the subprocess
can receive multiple messages.
3 To use UCA for triggering a start message event, complete the followingactions in the Event Properties section: Important: The sender and receiver of the message must both use the same undercoveragent. For example, if the sender of the message is a message end event in another process, thenselect the same undercover agent for both the receiving intermediate event and the sending messageend event in the other process. Tip: UCAs must have a schedule type of On Event to function as amessage trigger. Plus, the service that is attached to the selected undercover agent must have oneor more input variables so that it can pass and correlate information from the event.

1. To select an existing undercover agent, click Select next to
the Attached Message UCA field.
2. To create an undercover agent, click New. See Undercover agents.
3. In the Condition text box, type a JavaScript expression if you
want to define conditions under which the message event is processed. 
If you do specify a condition and the condition evaluates to true, the message is accepted and
processing continues. If the condition evaluates to false, processing stops. In most cases, special
message conditions are not necessary because you should implement each message event with a separate
undercover agent.
4. If you want the incoming message to be consumed after it is received by the message
event, enable Consume Message. Refer to the bulleted list in Modeling message events to learn more about message consumption.
5. The Durable Subscription check box is not available for start
message events, only for intermediate message events as described in the following
section.
4 To use an SCA service for triggering a start message event, change thestart event type to SCA Service and complete the following actions in theEvent Properties section:

<!-- image -->

1. For Message Object Type, click Select to
select a business object (BO) type, click New to define a new BO type, or
leave it to be set automatically when you select a service definition.  The business
object type that you select determines the output parameters of the start message event. The message
object type must be a complex type.
2 For Service Identifier , a default value is provided, based onthe name of the event, as shown in the process diagram. If you want, you can eitherspecify a different service identifier name, or select one from the drop-down list of services thatmatch the selected message object type. If you enter a name, it is restricted to using the NMTokencharacter set. Tip: If your process includes more than one start message, each one should use adifferent SCA service identifier. Otherwise, if multiple start message events specify the same SCAservice identifier, the start event that receives the start message is selected arbitrarily.If you specify the sameSCA identifier for multiple message events, the service interface can trigger multiple events in theprocess instance. However, each incoming message is received by only one of the events. Which eventreceives the message, or whether it is stored for future delivery, depends on whether a correlatingprocess instance is found, and if so, which compatible message events are in the waiting state. Fordetails of the semantics, see Using Service Component Architecture to interact with processes . Important: It ispossible to define unintentionally the same service identifier on multiple events. For example, ifdifferent events have identical names (which is shown as an error on the General tab), or ifdifferent service identifiers map onto identical NMToken strings. If such a naming clash happens,you can break the unintended polymorphism by renaming the duplicate event names and then clickX (delete) to restore the default service identifiername.
    - If you selected an existing service definition and the message object type was not set, the
message object type is updated to match the service definition.
    - The service identifier is used with the process name to generate a unique SCA service for this
event point. The generated service interface name is displayed.
    - If you selected an existing service definition, the associated events are added to the list of
events that the definition includes.
    - To restore the default value, click the X (delete) icon.
    - If
you specify the same SCA identifier for multiple message events, any changes to the service
identifier or message object type affect all the events that provide the service. Making such
changes can break data mappings for the events.

If you specify the same
SCA identifier for multiple message events, the service interface can trigger multiple events in the
process instance. However, each incoming message is received by only one of the events. Which event
receives the message, or whether it is stored for future delivery, depends on whether a correlating
process instance is found, and if so, which compatible message events are in the waiting state. For
details of the semantics, see Using Service Component Architecture to interact with processes.

5 Specify the correlation and output mapping. For example, if the start message event starts an instance of an on-boarding process when anemployee record is created in your HR system, you can map the employee information from theundercover agent to a local variable in the process. If your start message event is inside an event subprocess, you must select a variable to be usedfor correlating process instances. Correlation is used to identify the process instance that themessage is meant for. For example, an employee number might be used to uniquely identify an instance of an on-boardingprocess. Selecting this variable for correlation ensures that when the data related to a specificemployee number is passed to the event subprocess, the appropriate instance of the on-boardingprocess is found.

1. On the Properties tab, click Data
Mapping.
2. Open the Output Mapping section.
3. Map each output variable to a local variable in the process.  For each
variable, click the variable selector icon to map each output variable to be passed into a local
variable in the process.

For example, if the start message event starts an instance of an on-boarding process when an
employee record is created in your HR system, you can map the employee information from the
undercover agent to a local variable in the process.

If your start message event is inside an event subprocess, you must select a variable to be used
for correlating process instances. Correlation is used to identify the process instance that the
message is meant for.

For example, an employee number might be used to uniquely identify an instance of an on-boarding
process. Selecting this variable for correlation ensures that when the data related to a specific
employee number is passed to the event subprocess, the appropriate instance of the on-boarding
process is found.