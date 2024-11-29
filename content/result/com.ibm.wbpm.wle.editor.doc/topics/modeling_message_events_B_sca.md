<!-- image -->

# Using an SCA service with intermediate and boundary message events to receive
messages

## About this task

## Procedure

1. Open a process and drag a Message (receiving) Event component from the palette onto the
diagram. It can be dragged to the swimlane or attached to an activity.
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
3 To use an SCA service with an intermediate message event, complete the following actions on theImplementation tab:

1. In the Intermediate Event Type select SCA
Service.
2. For Message Object Type, click Select to select a
business object (BO) type, click New to define a new BO type, or leave it to
be set automatically when you select a service definition.
 The business object type that you select determines the output parameters of the intermediate
message event. The message object type must be a complex type.
3 For Service Identifier , a default value is provided, based on the nameof the event, as shown in the process diagram. If you want, you can either specify a different service identifier name, or select one fromthe drop-down list of services that match the selected message object type. If you enter a name, itis restricted to using the NMToken character set. Tip: If you specify the sameSCA identifier for multiple message events, the service interface can trigger multiple events in theprocess instance. However, each incoming message is received by only one of the events. Which eventreceives the message, or whether it is stored for future delivery, depends on whether a correlatingprocess instance is found, and if so, which compatible message events are in the waiting state. Fordetails of the semantics, see Using Service Component Architecture to interact with processes . Important: It ispossible to define unintentionally the same service identifier on multiple events. For example, ifdifferent events have identical names (which is shown as an error on the General tab), or ifdifferent service identifiers map onto identical NMToken strings. If such a naming clash happens,you can break the unintended polymorphism by renaming the duplicate event names and then clickX (delete) to restore the default service identifiername.
    - If you selected an existing service definition and the message object type was not set, the
message object type is updated to match the service definition.
    - The service identifier is used with the process name to generate a unique SCA service for this
event point. The generated service interface name is displayed.
    - If you selected an existing service definition, the associated events are added to the list of
events that the definition includes.
    - If
you specify the same SCA identifier for multiple message events, any changes to the service
identifier or message object type affect all the events that provide the service. Making such
changes can break data mappings for the events.
    - To restore the default value, click the X (delete) icon.
4 Specify the correlation and output mapping.

1. On the Data Mapping tab, open the Correlation and Output
Mapping section.
2. Select the output variable that you want to use to for correlation. The value that is assigned
to it ensures that the parameter values of the runtime message are passed to the correct process
instance. The variable that is selected for correlation is identified by an assignment symbol
(). This correlation ensures that the parameter values of the runtime message are passed to
the correct process instance. 
You must select a variable that is marked as a process instance identifier that ensures that
the message is passed to the correct process instance based on the value of that variable.
3. Map each output variable to a local variable in the process. 
For each variable, click the variable selector icon to map each output variable to a local
variable in the process.
5. Click Save or Finish Editing.