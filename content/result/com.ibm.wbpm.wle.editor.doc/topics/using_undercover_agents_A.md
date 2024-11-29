# Creating and configuring an undercover agent for a message event

## Procedure

To create and configure an undercover agent for a message
event, perform the following tasks:

1. Open the designer.
2. To launch the New Undercover Agent, click the plus
(+) icon beside Events and then select
Undercover Agent. The New Undercover Agent wizard
opens.
3 In the New Undercover Agent window, enter the followinginformation:
    - Name: Type a name for the new undercover
agent.
    - Schedule Type: Select On Event from
the drop-down list.
    - Click Finish.
4. In the Common section, you can type a description of the
undercover agent in the Documentation text
box.
5. In the Scheduler section, you can see the type of schedule
for the current undercover agent in the Schedule Type field.
6. Beside the Event Marker area, accept
the default event marker Message. If you want,
you can later click Select and then select Content.
(The Content selection is used to work with
content events that originate from ECM servers. The Message selection
is used to work with message events that originate from business process
definitions, JMS listeners, or web services that you have created.)
7. Under Details, click the drop-down list next to Queue
Name to select the queue that you want from the following
options:                    
Table 1. Available
queue options

Option
Description

Async Queue
Allows Event Manager jobs to run at the same
time.

SYNC\_QUEUE\_1
Forces one job to finish and starts the next job even if the previous task
fails. By default, three synchronous queues are available.

SYNC\_QUEUE\_2
Forces one job to finish and starts the next job even if the previous task
fails. By default, three synchronous queues are available.

SYNC\_QUEUE\_3
Forces one job to finish and starts the next job even if the previous task
fails. By default, three synchronous queues are available.

Note: For more information about Event Manager jobs, monitoring those
jobs, and creating and maintaining Event Manager execution queues, see Maintaining and monitoring IBM Business Automation Workflow Event Manager. When you install and run the process on a workflow server
in a test or production environment, the queue that you select must exist in that environment in
order for the undercover agent to run.
8. Beside Implementation, accept the default selection
Variable or select Service. Use a variable
implementation to pass events directly from the undercover agent to the process. By comparison, use
a service implementation to process information about events by adding business logic or
decisions.
9. If you selected Variable, the default
variable type NameValuePair is already selected.
However, you can click Select to choose a different
existing variable type or you can click New to
create variable type.
10. If you selected Service, the default
attached service Default BPD Event is already
selected. However, you can click Select to
choose a different existing service or you can click New to
create a service.
11. Ensure that the Enabled check box
is selected. Note: If this check box is not selected, the
Event Manager does not run the undercover agent when the message is
received or sent. (The Event Manager monitor might show that the Event
Manager has run the undercover agent, but if this check box is not
selected, the execution does not occur.)
12. In the Parameter Mapping section, select the Use
Default check box if you want to use the default value
of the input variable in the attached service. If the input variable
of the attached service does not have a default value, this check
box is disabled. Type a value in the text box if you
want to map a constant value to the input variable of the attached
service. For example, you might use a constant for testing purposes.
In most cases, the required values are included in the
incoming message event and no action is required here.
13. In the Event section, a unique default ID is provided in the Event
Message field. This ID represents the event message for processing.

If you are posting a message to the Event Manager from an external system, the ID in this field
is the event name that you need to include in the XML message. See Posting a message to IBM Business Automation Workflow Event Manager for more information about the message structure.
If you are using a web service to enable an external application to call into your process app
, you should not alter this ID. The product
seamlessly uses this ID if you create an inbound integration as described in
Building a sample inbound integration.
14. Open the process that includes the message event to which you want to attach the
undercover agent. For example, if you want a particular process to start when a new customer record
is created in an external system, you can associate the start event in the process with an
undercover agent that handles that incoming event. 
Note: Ensure that the sender and receiver of a message both use the same undercover agent. For
example, if the sender of a message is a message end event in another process, then select the same
undercover agent for both the receiving start event and the sending message end event in the other
process.
Tip: If you occasionally use inbound messages, consider using durable subscription
events. Durable subscriptions are Java Message Service (JMS) subscriptions that persist and store
subscribed messages even when the client is not connected. The durable messages accumulate, even if
you select the check box to make them consumable. Periodically use the BPMDeleteDurableMessages command or the DELETE
/std/bpm/durable\_messages method in the Operational Rest API to
delete durable subscription events.
15. Click the message event in the process to select it.
16. Click the General tab option in
the properties.
17. In the Event Properties section, click Select next to
Attached message UCA and pick the undercover agent created in the previous
steps.
18. Click Save or Finish Editing.
19. In the undercover agent editor, you can click Run Now if you want
to test and monitor the undercover agent as described in Maintaining and monitoring IBM Business Automation Workflow Event Manager.