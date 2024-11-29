# Subscribing to document and folder events using the desktop Process Designer (deprecated)

## About this task

- Create an event subscription
- Add an attached service and a Content undercover agent (UCA)
- Add a content event to a BPD
- Test the new components

To perform these activities, complete the following procedure:

## Procedure

1 Create an event subscription by completing the followingsteps:
    1. Open a process application in Process Designer.
    2. In the library area of the Designer page, click the plus (+) icon beside
Implementation and then select Event Subscription. The
New Event Subscription wizard opens.
    3. In the Name field, specify a
name for the new event subscription.
    4. Click Finish. The new event subscription is displayed in the
Implementation library list (under Event Subscription) and the event
subscription opens in the Event Subscription editor.
    5 In the ECM Server drop-down list,select one of the following server types to associate with the eventsubscription: If you want to select the name of an ECM server but no ECM servers are available for selection,you can add a server in the Process App Settings editor by selecting the Use the ProcessApplication Settings editor to add a server link and then clicking theServers tab. After adding the server, click Save andthen switch to the event subscription editor again and select the server from the ECMServer drop-down list. For more information, see Adding an Enterprise Content Management server .
        - BPM content store
        - BPM document store. See Working with BPM documents.
        - The name of an ECM server

If you want to select the name of an ECM server but no ECM servers are available for selection,
you can add a server in the Process App Settings editor by selecting the Use the Process
Application Settings editor to add a server link and then clicking the
Servers tab. After adding the server, click Save and
then switch to the event subscription editor again and select the server from the ECM
Server drop-down list. For more information, see Adding an Enterprise Content Management server.

6. If you selected the name of an ECM server in the ECM
Server drop-down list, select either the default Document event
class or the Folder event class in the Event
Class drop-down list.
7. If you selected the name of an ECM server in the ECM
Server drop-down list, select either the top-level default Document object
type or select a different object type in the Object Type drop-down
list. (If the drop-down list is disabled, the server is probably unavailable.)
8. If you selected the name of an ECM server in the ECM
Server drop-down list and you want to include all of the
subtypes of the selected object type, ensure that the Include
Subtypes check box is selected.
9. In the Event Type drop-down list,
accept the default Created event type for your
ECM server or select a different event type. (If the drop-down list
is disabled, the server is probably unavailable.) Information about
the available event types is found in the topic Content event types.
10 By default, event subscriptions are exposed to all users.This means that when any user performs an action that correspondsto the event type that is specified in the Event Type drop-downlist (such as creating a document), a document event or a folder eventwill be fired. If you selected the Business Automation Workflow documentstore in the ECM Servers drop-down list, youcannot change the default behavior of event subscriptions being exposedto all users. However, if you selected the name of an ECM server inthe ECM Servers drop-down list, you can specifythat you only want events to be fired for designated users who arenamed in an existing team. This is accomplished by clicking Select inthe Exposing area and then choosing the nameof the team. Alternatively, you can create a new team for designatedusers by completing the following steps:
    1. In the Exposing area, click New.
The New Team wizard opens.
    2. In the Name field, type a name for the
new team.
    3. Click Finish. The Team page
opens.
    4. In the Team page, define the team by following
the instructions in the topic Creating a team.
11. Click Save.
2 Add an attached service and a Content UCA by completingthe following steps:

1. In the Attached Service area, click New. The New
Service for Event Subscriptions wizard opens.
2. In the Name field, accept the default name or type a different name for
your new service.
3. If you want to create a general system service that will directly invoke the Content UCA
without first querying the ECM server for additional information, select Create a service
that directly invokes a UCA. However, if you want to create an integration
service that will first query the ECM server for additional information before determining
whether a UCA should be invoked, select Create a service that queries the ECM server
before invoking a Content UCA.
4. Click Finish. A new service flow and a new content UCA of the
same name are automatically created. The new service opens in the service editor.

If you chose to create a general system service, it is already fully implemented and consists of
a Start event, an End event, and an Invoke UCA step that will invoke the new Content UCA. However,
if you chose to create an integration service, it is partially implemented and it consists of
several components, such as an Integration step, a decision gateway step, and an Invoke UCA step to
invoke the Content UCA. The following figure shows an integration service as it might appear after
it has been fully implemented:

For both a general system service and an integration service, the signature of both the service
and the Content UCA includes an Input named contentEvent with a business object type of
ECMContentEvent.
5. If you chose to create an integration service, select
the decision gateway in the canvas and open the Properties tab
and the Implementation pane, then define the
decision conditions for the decision gateway. Other than perhaps renaming
the labels of the components, this is all that is required to complete
the implementation of the integration service.
6. Click Save.
3 Add a content event to a process by completing the following steps:

1. In the library area of the Designer page, click the plus (+) icon beside
Processes and then select Process. The New Process
wizard opens.
2. In the Name field, specify a name for the new process.
3. Click Finish. The new process is displayed in the Process library list
(under Process) and the process opens in the process editor.
4. In the canvas, select the existing Start event or select the
Start Event or Intermediate Event icon in the palette
and drag the event to the canvas.
5. Click the Properties tab and then click
Implementation. The Implementation panel opens.
6. In the Start Event Details or Intermediate Event
Details section, change None to Content.
The event in the diagram changes to display a Content marker icon.
7. Beside the Attached Content UCA area in the Content
Trigger section, click Select and then select the Content UCA
that was automatically created when you created the attached service. It has the same name as the
service. (Additional information about creating a Content UCA is found in the topic Creating and configuring an undercover agent for a content event.)
8. In the canvas, ensure that the Content event is selected, then click the
Properties tab and click Data Mapping. The Data
Mapping panel opens.
9. Click the variable selector icon on the right side of each field to map each undercover agent
output variable to a local variable in the process.
10. If you are working with an intermediate event, select the variable that you want to use to
correlate the event with the process instance. The variable selected for correlation is identified
by an assignment symbol. This correlation ensures that the parameter values of the runtime message
are passed to the correct process instance. (IBM® Business Automation Workflow only requires one variable mapping to
correlate the event.)
11. Click Save.
4 Test the new components by completing the following steps:

1. Switch to your event subscription in the event subscription
editor.
2. Click Save.
3. Click Test Subscription. Test
Event Subscription opens, which contains fields that are
populated with the selections that you made in the Event Subscription
editor. The selections represent the data that will be returned from
the ECM server.
4. In the Object field, accept the
default object or select a different object on the ECM server.
5. Click Test.  If the event subscription is defined correctly, a simulated incoming ECM event is triggered
and the following message is displayed: An inbound ECM event has been successfully
simulated for the event subscription.
The attached service, content UCA, and
start or intermediate event are subsequently invoked, which leads to either a response from an
existing process instance or the creation of a new process instance. You can view process instances
in the Inspector view of Process Designer.