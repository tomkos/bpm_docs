# Using the event handler for FileNet Content
Manager

## Overview

The event handler is for IBM
FileNet Content Manager version
5.1 or higher.

## Supported events

The following table lists
all ECM events that are supported by Business Automation Workflow, and
the corresponding FileNet Content
Manager events.
Use the table to identify the FileNet Content
Manager events
that you need to subscribe to, and the names that are used in Process
Designer to identify the same events in Business Automation Workflow.

| ECM events supported by Business Automation Workflow (com.ibm.bpm.BPMEventType)   | Object types that the event can apply to   | Corresponding FileNet Content Manager events (com.filenet.api.events)   |
|-----------------------------------------------------------------------------------|--------------------------------------------|-------------------------------------------------------------------------|
| CheckedIn                                                                         | Document                                   | CheckinEvent                                                            |
| CheckedOut                                                                        | Document                                   | CheckoutEvent                                                           |
| CheckOutCancelled                                                                 | Document                                   | CancelCheckoutEvent                                                     |
| ClassChanged                                                                      | Folder or Document                         | ChangeClassEvent                                                        |
| ClassifyCompleted                                                                 | Document                                   | ClassifyCompleteEvent                                                   |
| Created                                                                           | Folder or Document                         | CreationEvent                                                           |
| Deleted                                                                           | Folder or Document                         | DeletionEvent                                                           |
| Filed                                                                             | Folder                                     | FileEvent                                                               |
| Frozen                                                                            | Document                                   | FreezeEvent                                                             |
| Locked                                                                            | Folder or Document                         | LockEvent                                                               |
| PublishCompleted                                                                  | Document                                   | PublishCompleteEvent                                                    |
| PublishRequested                                                                  | Document                                   | PublishRequestEvent                                                     |
| SecurityUpdated                                                                   | Folder or Document                         | UpdateSecurityEvent                                                     |
| StateChanged                                                                      | Document                                   | ChangeStateEvent                                                        |
| Unfiled                                                                           | Folder                                     | UnfileEvent                                                             |
| Unlocked                                                                          | Folder or Document                         | UnlockEvent                                                             |
| Updated                                                                           | Folder or Document                         | UpdateEvent                                                             |
| VersionDemoted                                                                    | Document                                   | DemoteVersionEvent                                                      |
| VersionPromoted                                                                   | Document                                   | PromoteVersionEvent                                                     |

## Define a process to consume the ECM events

## Copy the event handler to your FileNet Content
Manager server

- install\_root/BPM/EventHandlers/ECM/FileNet/filenet-bpm-event-handler-51.jar
- install\_root\BPM\EventHandlers\ECM\FileNet\filenet-bpm-event-handler-51.jar

## Creating the connection information
document

The connection information necessary for the ECM
event handler to connect to the Business Automation Workflow system
is stored as a document in the FileNet Content
Manager repository.
To create the connection information document, perform the following
steps:

1 On your FileNet ContentManager server,create a properties file. Tip: If you require multiplesubscriptions that notify different Business Automation Workflow serversof events, you need one properties file for each Business Automation Workflow server.Although you can give the properties file any name, it makes senseto include the name of the server in the name of the properties file,for example, bpmserver1.properties .
    - If you have a suitable J2C authentication alias defined on the
application server where FileNet Content
Manager is
running, you can define the connection properties file to use the
authentication alias. For example:bpm.server.authalias=scope/my\_authentication\_alias
bpm.server.uri=https\://bpm\_server\_name\:9443Where scope is
the scope of the authentication alias my\_authentication\_alias,
and bpm\_server\_name is the host name or IP address
of your Business Automation Workflow server,
for example, bpm1.example.com.
    - If you do not use an authentication alias, your server connection
properties file must specify a suitable Business Automation Workflow user
name and password. For example:bpm.server.username=bpm\_user
bpm.server.password=bpm\_user\_password
bpm.server.uri=https\://bpm\_server\_name\:9443Where bpm\_user is
a user ID that is authorized to access the Business Automation Workflow, bpm\_user\_password is
the password for the user ID, and bpm\_server\_name is
the host name or IP address of your Business Automation Workflow server,
for example, bpm1.example.com.
    - Business Automation Workflow by
default uses the context root /rest/bpm/wle/ for
its REST API. If you use a custom context root prefix, add this line
to your connection properties file:bpm.server.contextRoot=/myCustomContextRoot/rest/bpm/wle/
2 Store the properties file in the ECM system. You can store theproperties file in several ways. For example, you can use the IBM Administration Console forContent Platform Engine tostore the properties file by using the following actions:

1. Using a browser, log in to the Administration Console for Content Platform
Engine at
the URL http://filenet\_server\_host\_name:port/acce.
2. Select the object store where you want to store the configuration
file.
3. Expand the object store, then either add a folder or select a
suitable existing folder where you want to store the properties file.
4. Select New Document from the Actions drop-down
list of the folder.
5. Specify a Document title. You might want
to choose a name that identifies the BPM system that this connection
document is targeting. Then, click Next.
6. In the Content Elements section, click Add.
In the Add Content Element dialog, click Browse and
select the property file that you created. Click Add Content.
Click Next.
7. On the following pages (Object Properties, Document
Content and Version, Specify Settings for Retaining
Objects, and Advanced Features) you
can keep the default values. Click Next on
each page.
8. On the Summary page, click Finish.
9. The document is created. Click Open to
open it.
10. In the Properties tab, look for the ID
property and note the value. Select and copy it to a clipboard or
text file. You need it later when you create the event subscription.
11. In the Security tab, you might want to
make sure that the document can be read and modified only by administrators
to prevent all of your users from seeing these connection information.

## Creating the event action

1. In your object store, browse to the Event Actions that
are located under Events, Actions, Processes.
2. Click New.
3. Enter a Display name, for example, BPM
event action. Click Next.
4. On the Specify the Type of Event Action page,
enter the Java class handler com.ibm.bpm.integration.filenet.BPMEventHandler.
Enable the Configure code module check box.
Click Next.
5. On the Specify the Code Module page, enter
a Code Module title, for example, BPM event
handler code module. Click Browse and select
the filenet-bpm-event-handler-51.jar file. Click Next.
6. On the Summary page, click Finish.

## Creating a subscription

A subscription
in FileNet Content
Manager defines
which events on a certain object are to be handled by an event action.

- If you define event subscriptions in BPM, you need to create corresponding
subscriptions in FileNet Content
Manager using
the event mapping table from above.
- If you use Document Start events in processes, you need to create
a subscription for the Created event for the document class.
- If you use activity preconditions based on documents that are
added to a folder, you need to create a subscription for the Filed
event for the folder class.

If you have multiple BPM systems that you want to send
the event to, create subscriptions in FileNet Content
Manager for
each of them individually.

- Document
    - ClaimForm
    - Contract

In your BPM system, you have an event subscription defined
for the Document Created event on the base Document class that includes
subclasses. You also have another event subscription for the Document
Created event on the Contract class that does not include subclasses.
In this scenario, you only need one subscription in your FileNet Content
Manager system:
an event subscription on the Document class that includes subclasses
and that subscribes to the Created event. This subscription will send
all required events to the BPM system. If you created an extra subscription
on the Contract class that subscribes to the Created event, then both
subscriptions would be triggered if a Contract is created. Subsequently,
two events would be sent to the BPM system.

1. In your object store, browse to the Subscriptions that
are located under Events, Actions, Processes.
2. Click New.
3. Enter a Display name and optionally a Description.
You should specify a display name and description that clearly identifies
which BPM system is targeted, which events are handled for which Document
and Folder classes, and if the include subclasses flag is enabled.
This clarification allows you to keep track of which events are handled
by which BPM systems. This clarification also helps you prevent subscriptions
that cause the same event to be sent multiple times to one BPM system.
Click Next.
4. On the Select Classes page, select Document or Folder as Class
type. Select the Class that you
want to handle events. Click Next.
5. On the Specify the Subscription Behavior page,
keep all defaults and click Next.
6. On the Select the Triggers page, select the
events you want to handle. Click Next.
7. On the Select an Event Action page, select
the event action that you previously created. Click Next.
8. On the Specify Additional Options page, for
the Initial state, disable the Enable
this subscription check box. Enable the Include
subclasses check box according to your needs. Do not enable
the Run synchronously check box. Synchronous
events are sent to the BPM system even before the transaction is completed.
As a transactional context cannot be propagated using a REST API,
this may result in operations getting triggered in the BPM system
even if the content operation is subsequently rolled back. Click Next.
9. On the Summary page, click Finish.
10. The subscription is now created. Click Open to
open it.
11. On the Properties tab, look for the User
String property. Enter the document identifier from the
connection information document as a value. Optionally, look for the Is
Enabled property and change its value to True.
Click Save.

## Updating the event action code
module

To update the BPM event handler to use the latest
version of the filenet-bpm-event-handler-51.jar file,
you must update the code module and the event action to point to the
updated code module. Perform the following steps in the IBM Administration Console for
Content Platform Engine:

1. Open the code module. By default, the code modules are created
in the Code Modules folder in the root folder
of the object store. Alternatively, you can find the code module by
browsing to the Event Actions that are located
under Events, Actions, Processes. Open the BPM
event action, then look for the Code Module property
and click on its value to open the code module.
2. For the code module, perform the action Checkin,
checkout, cancel > Exclusive Checkout.... A reservation is created that is opened automatically.
3. For the reservation, perform the action Checkin,
checkout, cancel > Checkin....
4. In the Checkin dialog, click Add and
select the latest version of the filenet-bpm-event-handler-51.jar file.
Select Update all Action class instances that reference
earlier versions of this Code Module class.
5. Click Check In Major Version.

## Advanced configuration

Certain event handler
behavior can be controlled by using Java Virtual Machine (JVM) system
properties. To create or modify those properties, log in to the WebSphere
Integrated Solutions Console of your FileNet Content
Manager system.
Browse to Servers > Server
Types > WebSphere application servers. For each server belonging to the deployment target
the FileNet Content
Manager engine
application is deployed to, go to Java and
Process Management > Process definition > Java Virtual Machine > Custom Properties. Click New... to create new
entries, or click an existing entry to apply changes to it. After
you have made changes, save the configuration, synchronize the nodes,
and restart the servers.

| Property name                                              | Default value   | Description                                                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| com.ibm.bpm.integration.filenet.configurationExpiration    | 600000          | The time in milliseconds that the content of a connection information document is cached.                                                                                                                                                                                                                                                                |
| com.ibm.bpm.integration.filenet.sendCreatedEventOnCheckOut | true            | When you check out a document, FileNet Content Manager fires a Creation event for the new document version. This behavior might not be desired if the expectation is that the event happens only for the first version of a document. Set this value to false to cause the BPM event action to ignore document creation events for non-initial versions. |