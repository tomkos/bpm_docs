# Subscribing to document and folder events

## About this task

- Create an event subscription
- Add an attached service and a Content undercover agent (UCA)
- Add a content event to a process
- Test the new components

To perform these activities, complete the following procedure:

## Procedure

1 Create an event subscription by completing the followingsteps:
    1. Open a process application in the Process Designer.
    2. In the library, click the plus (+) icon beside Events and then select
Event Subscription. The New Event Subscription wizard opens.
    3. In the Name field, specify a
name for the new event subscription.
    4. Click Finish. The new event subscription is displayed in the library
under Events and the event subscription opens in the Event Subscription
editor.
    5 In theECM Server drop-down list, select one of the following server types toassociate with the event subscription: If you want to select the name of an ECM server but no ECM servers are available for selection,you can add a server in the Process App Settings editor by selecting the Use the ProcessApplication Settings editor to add a server link and then clicking theServers tab. After adding the server, Click Save or Finish Editing . Switch to the event subscriptioneditor again and select the server from the ECM Server drop-down list. Formore information, see Adding an Enterprise Content Management server .
        - BPM content store
        - BPM document store. See Working with BPM documents.
        - The name of an ECM server

If you want to select the name of an ECM server but no ECM servers are available for selection,
you can add a server in the Process App Settings editor by selecting the Use the Process
Application Settings editor to add a server link and then clicking the
Servers tab. After adding the server, Click Save or Finish Editing. Switch to the event subscription
editor again and select the server from the ECM Server drop-down list. For
more information, see Adding an Enterprise Content Management server.

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
9. In the Event Type drop-down list, accept the default
Created event type for your ECM server or select a different event type. (If
the drop-down list is disabled, the server is probably unavailable.) For more information about the
available event types, see Content event types.
10 By default, event subscriptions are exposed to all users. This means that when anyuser performs an action that corresponds to the event type that is specified in the EventType drop-down list (such as creating a document), a document event or a folder eventwill be fired. If you selected the Business Automation Workflow document store in theECM Servers drop-down list, you cannot change the default behavior of eventsubscriptions being exposed to all users. If you selected the name of an ECM server in theECM Servers drop-down list, you can specify that you only want events to befired for designated users who are named in an existing team. This is accomplished byclicking Select in the Exposing area and then choosingthe name of the team. Alternatively, you can create a new team for designated users bycompleting the following steps:
    1. In the Exposing area, click New. The New
Team wizard opens.
    2. In the Name field, type a name for the new team.
    3. Click Finish. The Team page opens.
    4. In the Team page, define the team by following the instructions in the
topic Creating a team.
11. Click Save or Finish Editing.
2 Add an attached service and a Content UCA by completingthe following steps:

1. In the Attached Service area, click New. The New
Service Flow wizard opens.
2. In the Name field, accept the default name or type a different name for
your new service flow.
3. If you want to create a service that directly invokes the content UCA without first querying
the ECM server for additional information, select Create a service that directly invokes
a content UCA. However, if you want to create a service that queries the ECM server for
additional information before determining whether a UCA should be invoked, select Create
a service that queries the ECM server before invoking a Content UCA.
4 Click Finish . The new service opens in the service editor. The service flow is already fully implemented and is modeled based on the option that youselected. Create a service that directly invokes a content UCA The service flow consists of the following elements: Create a service that queries the ECM server before invoking a Content UCA The service flow consists of the following elements: Complete the service flow according to your scenario.
    - A start event and an end event.
    - A send message event with an attached content UCA.
    - A variable called contentEvent with a business object called ECMContentEvent as its type.
    - A start event and an end event
    - A content integration task that has error handling logic. The content integration task is
configured for the ECM server and event type that are defined in the event subscription.
    - A send message event with an attached content UCA.
    - A variable called contentEvent with a business object called ECMContentEvent as its type and a
variable called documentInfo with a business object called ECMDocument as its type.
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
Details section, change None to ECM
Content. The event in the diagram changes to display a Content marker icon.
7. Beside the Attached Content UCA area in the Event
Properties section, click Select and then select the UCA that was
automatically created when you created the attached service. It has the same name as the service.
(Additional information about creating a Content UCA is found in the topic Creating and configuring an undercover agent for a content event.)
8. In the canvas, ensure that the Content event is selected, then click the
Properties tab and click Data Mapping. The Data
Mapping panel opens.
9. Click the variable selector icon on the right side of each field to map each UCA output
variable to a local variable in the process.
10. If you are working with an intermediate event, select the variable that you want to use to
correlate the event with the process instance. The variable selected for correlation is identified
by an assignment symbol. This correlation ensures that the parameter values of the runtime message
are passed to the correct process instance.
11. Click Save or Finish Editing.
4 Test the new components by completing the following steps:

1. Switch to your event subscription in the event subscription
editor.
2. Click Test Subscription. Test
Event Subscription opens, which contains fields that are
populated with the selections that you made in the Event Subscription
editor. The selections represent the data that will be returned from
the ECM server.
3. In the Object field, accept the
default object or select a different object on the ECM server.
4. Click Test.  If the event subscription is defined correctly, a simulated incoming ECM event is triggered
and the following message is displayed: An inbound ECM event has been successfully
simulated for the event subscription.
The attached service, content UCA, and
start or intermediate event are subsequently invoked, which leads to either a response from an
existing process instance or the creation of a new process instance. You can view process instances
in the Inspector view of Process Designer.